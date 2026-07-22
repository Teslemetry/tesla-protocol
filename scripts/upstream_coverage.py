#!/usr/bin/env python3
"""Descriptor-level upstream coverage gate.

Verifies, for every upstream-tracked proto directory, that upstream (subset)
ours holds at the descriptor level: every upstream message, field, enum and
enum value must exist in our tree with the same name, number and type. Our
extra symbols are allowed, but inside upstream-tracked files each one must
carry a TESLEMETRY-EXT marker (trailing comment or BEGIN/END fence).

Modes:
  --mode pinned  compare against the upstream commit pinned in upstream.json
                 (deterministic; used by PR CI; verifies file sha256 too)
  --mode head    compare against upstream main HEAD (used by the weekly
                 drift job; new gaps here are upstream additions, not PR bugs)

Requires grpcio-tools (bundled protoc) in the running interpreter.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

from google.protobuf import descriptor_pb2

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKER = "TESLEMETRY-EXT"
FENCE_BEGIN = f"{MARKER} BEGIN"
FENCE_END = f"{MARKER} END"


def run_protoc(include: Path, files: list[Path], out: Path, source_info: bool) -> None:
    args = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        f"-I{include}",
        f"--descriptor_set_out={out}",
    ]
    if source_info:
        args.append("--include_source_info")
    args += [str(f) for f in files]
    proc = subprocess.run(args, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"protoc failed:\n{proc.stderr}")


def load_descriptor_set(path: Path) -> descriptor_pb2.FileDescriptorSet:
    fds = descriptor_pb2.FileDescriptorSet()
    fds.ParseFromString(path.read_bytes())
    return fds


@dataclass
class Symbols:
    """Flattened symbol tables for one FileDescriptorSet."""

    messages: dict[str, str] = field(default_factory=dict)  # fqn -> file
    enums: dict[str, str] = field(default_factory=dict)  # fqn -> file
    fields: dict[str, dict] = field(default_factory=dict)  # fqn -> info
    enum_values: dict[str, dict] = field(default_factory=dict)  # fqn -> info
    # fqn -> 0-based line of the declaration, when source info present
    lines: dict[str, int] = field(default_factory=dict)
    # fqn -> 0-based (start_line, end_line) of the full declaration
    spans: dict[str, tuple] = field(default_factory=dict)


def index_file(fd: descriptor_pb2.FileDescriptorProto, syms: Symbols) -> None:
    spans = {}
    for loc in fd.source_code_info.location:
        end = loc.span[2] if len(loc.span) == 4 else loc.span[0]
        spans[tuple(loc.path)] = (loc.span[0], end)

    def note_line(path: tuple, fqn: str) -> None:
        if path in spans:
            syms.lines[fqn] = spans[path][0]
            syms.spans[fqn] = spans[path]

    prefix = f".{fd.package}" if fd.package else ""

    def walk_enum(enum, fqn: str, path: tuple) -> None:
        syms.enums[fqn] = fd.name
        note_line(path, fqn)
        for i, val in enumerate(enum.value):
            vfqn = f"{fqn}.{val.name}"
            syms.enum_values[vfqn] = {"number": val.number, "enum": fqn, "file": fd.name}
            note_line(path + (2, i), vfqn)

    def walk_message(msg, fqn: str, path: tuple) -> None:
        syms.messages[fqn] = fd.name
        note_line(path, fqn)
        for i, f in enumerate(msg.field):
            ffqn = f"{fqn}.{f.name}"
            oneof = (
                msg.oneof_decl[f.oneof_index].name if f.HasField("oneof_index") else None
            )
            syms.fields[ffqn] = {
                "number": f.number,
                "type": f.type,
                "type_name": f.type_name,
                "label": f.label,
                "oneof": oneof,
                "message": fqn,
                "file": fd.name,
            }
            note_line(path + (2, i), ffqn)
        for i, nested in enumerate(msg.nested_type):
            walk_message(nested, f"{fqn}.{nested.name}", path + (3, i))
        for i, enum in enumerate(msg.enum_type):
            walk_enum(enum, f"{fqn}.{enum.name}", path + (4, i))

    for i, msg in enumerate(fd.message_type):
        walk_message(msg, f"{prefix}.{msg.name}", (4, i))
    for i, enum in enumerate(fd.enum_type):
        walk_enum(enum, f"{prefix}.{enum.name}", (5, i))


def index_set(fds: descriptor_pb2.FileDescriptorSet) -> Symbols:
    syms = Symbols()
    for fd in fds.file:
        index_file(fd, syms)
    return syms


@dataclass
class Finding:
    severity: str  # "gap" | "rename" | "wire" | "unmarked"
    detail: str


def compare(upstream: Symbols, ours: Symbols) -> list[Finding]:
    findings: list[Finding] = []

    for fqn in upstream.messages:
        if fqn not in ours.messages:
            findings.append(Finding("gap", f"message `{fqn}` missing from ours"))
    for fqn in upstream.enums:
        if fqn not in ours.enums:
            findings.append(Finding("gap", f"enum `{fqn}` missing from ours"))

    ours_fields_by_number = {
        (info["message"], info["number"]): (fqn, info)
        for fqn, info in ours.fields.items()
    }
    for fqn, up in upstream.fields.items():
        if up["message"] not in ours.messages:
            continue  # already reported as a missing message
        mine = ours.fields.get(fqn)
        if mine is None:
            same_number = ours_fields_by_number.get((up["message"], up["number"]))
            if same_number:
                findings.append(
                    Finding(
                        "rename",
                        f"field `{fqn}` (number {up['number']}) is named "
                        f"`{same_number[0].rsplit('.', 1)[-1]}` in ours - upstream wins names",
                    )
                )
            else:
                findings.append(
                    Finding("gap", f"field `{fqn}` (number {up['number']}) missing from ours")
                )
        elif (
            mine["number"] != up["number"]
            or mine["type"] != up["type"]
            or mine["type_name"] != up["type_name"]
            or mine["label"] != up["label"]
        ):
            findings.append(
                Finding(
                    "wire",
                    f"field `{fqn}`: ours has number={mine['number']} type={mine['type']}"
                    f" label={mine['label']}, upstream has number={up['number']}"
                    f" type={up['type']} label={up['label']}",
                )
            )

    ours_values_by_number = {
        (info["enum"], info["number"]): fqn for fqn, info in ours.enum_values.items()
    }
    for fqn, up in upstream.enum_values.items():
        if up["enum"] not in ours.enums:
            continue
        mine = ours.enum_values.get(fqn)
        if mine is None:
            same_number = ours_values_by_number.get((up["enum"], up["number"]))
            if same_number:
                findings.append(
                    Finding(
                        "rename",
                        f"enum value `{fqn}` (number {up['number']}) is named "
                        f"`{same_number.rsplit('.', 1)[-1]}` in ours - upstream wins names",
                    )
                )
            else:
                findings.append(
                    Finding(
                        "gap", f"enum value `{fqn}` (number {up['number']}) missing from ours"
                    )
                )
        elif mine["number"] != up["number"]:
            findings.append(
                Finding(
                    "wire",
                    f"enum value `{fqn}`: ours={mine['number']} upstream={up['number']}",
                )
            )
    return findings


def marked_lines(proto_file: Path) -> set[int]:
    """0-based line numbers covered by a TESLEMETRY-EXT marker or fence."""
    covered: set[int] = set()
    fence_start = None
    for i, line in enumerate(proto_file.read_text().splitlines()):
        if FENCE_BEGIN in line:
            fence_start = i
        elif FENCE_END in line:
            if fence_start is not None:
                covered.update(range(fence_start, i + 1))
                fence_start = None
        elif MARKER in line:
            covered.add(i)
    return covered


def check_markers(
    upstream: Symbols, ours: Symbols, local_dir: Path, tracked_files: set[str],
    unmarked_dump: list | None = None,
) -> list[Finding]:
    findings: list[Finding] = []
    marker_cache: dict[str, set[int]] = {}

    def is_marked(fqn: str, file: str) -> bool:
        line = ours.lines.get(fqn)
        if line is None:
            return False
        if file not in marker_cache:
            marker_cache[file] = marked_lines(local_dir / file)
        if line in marker_cache[file]:
            return True
        # a symbol nested in a marked symbol is covered by its ancestor
        parent = fqn.rsplit(".", 1)[0]
        if parent and (
            parent in ours.messages or parent in ours.enums
        ):
            return is_marked(parent, file)
        return False

    ours_only = []
    for fqn, file in ours.messages.items():
        if fqn not in upstream.messages:
            ours_only.append((fqn, file, "message"))
    for fqn, file in ours.enums.items():
        if fqn not in upstream.enums:
            ours_only.append((fqn, file, "enum"))
    for fqn, info in ours.fields.items():
        if fqn not in upstream.fields and info["message"] in upstream.messages:
            ours_only.append((fqn, info["file"], "field"))
    for fqn, info in ours.enum_values.items():
        if fqn not in upstream.enum_values and info["enum"] in upstream.enums:
            ours_only.append((fqn, info["file"], "enum value"))

    marked = 0
    for fqn, file, kind in ours_only:
        if file not in tracked_files:
            continue  # whole-file Teslemetry source-of-record, exempt
        if is_marked(fqn, file):
            marked += 1
        else:
            findings.append(
                Finding(
                    "unmarked",
                    f"{kind} `{fqn}` ({file}) is not in upstream and has no "
                    f"{MARKER} marker",
                )
            )
            if unmarked_dump is not None:
                start, end = ours.spans.get(fqn, (None, None))
                unmarked_dump.append(
                    {"fqn": fqn, "kind": kind, "file": file,
                     "dir": str(local_dir.relative_to(REPO_ROOT)),
                     "line": start, "end": end}
                )
    print(f"  {len(ours_only)} ours-only symbols, {marked} marked, "
          f"{len(ours_only) - marked} unmarked-or-exempt")
    return findings


def fetch_upstream(name: str, cfg: dict, mode: str, cache: Path) -> tuple[Path, str]:
    """Download upstream protos; returns (dir, commit)."""
    commit = cfg["commit"]
    if mode == "head":
        url = f"https://api.github.com/repos/{cfg['repo']}/branches/main"
        with urllib.request.urlopen(url) as resp:
            commit = json.load(resp)["commit"]["sha"]
    dest = cache / name / commit
    if dest.exists() and any(dest.iterdir()):
        return dest, commit
    dest.mkdir(parents=True, exist_ok=True)
    if mode == "head":
        # enumerate the proto dir so brand-new upstream files are seen
        url = (
            f"https://api.github.com/repos/{cfg['repo']}/contents/"
            f"{cfg['pathPrefix']}?ref={commit}"
        )
        with urllib.request.urlopen(url) as resp:
            names = [
                f["name"] for f in json.load(resp) if f["name"].endswith(".proto")
            ]
    else:
        names = list(cfg["files"])
    for fname in names:
        url = (
            f"https://raw.githubusercontent.com/{cfg['repo']}/{commit}/"
            f"{cfg['pathPrefix']}/{fname}"
        )
        with urllib.request.urlopen(url) as resp:
            (dest / fname).write_bytes(resp.read())
    return dest, commit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=["pinned", "head"], default="pinned")
    parser.add_argument("--cache-dir", type=Path, default=None,
                        help="reuse/download upstream protos here (default: temp dir)")
    parser.add_argument("--report", type=Path, default=None,
                        help="write a markdown gap report to this path")
    parser.add_argument("--dump-unmarked", type=Path, default=None,
                        help="write unmarked-extension symbols as JSON (tooling aid)")
    args = parser.parse_args()

    pins = json.loads((REPO_ROOT / "upstream.json").read_text())
    cache = args.cache_dir or Path(tempfile.mkdtemp(prefix="upstream-coverage-"))
    tmp = Path(tempfile.mkdtemp(prefix="descriptors-"))

    all_findings: dict[str, list[Finding]] = {}
    heads: dict[str, str] = {}
    unmarked_dump: list = []
    for name, cfg in pins["upstreams"].items():
        print(f"== {name} ({args.mode})")
        upstream_dir, commit = fetch_upstream(name, cfg, args.mode, cache)
        heads[name] = commit
        if args.mode == "pinned":
            for fname, want in cfg["files"].items():
                got = hashlib.sha256((upstream_dir / fname).read_bytes()).hexdigest()
                if got != want:
                    sys.exit(
                        f"sha256 mismatch for {name}/{fname} at pinned commit "
                        f"{commit}: upstream.json says {want}, fetched {got}"
                    )

        local_dir = REPO_ROOT / cfg["localDir"]
        upstream_files = sorted(upstream_dir.glob("*.proto"))
        ours_files = sorted(local_dir.glob("*.proto"))

        missing_files = {f.name for f in upstream_files} - {f.name for f in ours_files}
        findings = [
            Finding("gap", f"file `{f}` exists upstream but not in {cfg['localDir']}/")
            for f in sorted(missing_files)
        ]

        up_out, ours_out = tmp / f"{name}-up.pb", tmp / f"{name}-ours.pb"
        run_protoc(upstream_dir, [f for f in upstream_files if f.name not in missing_files],
                   up_out, source_info=False)
        run_protoc(local_dir, ours_files, ours_out, source_info=True)
        upstream_syms = index_set(load_descriptor_set(up_out))
        ours_syms = index_set(load_descriptor_set(ours_out))

        findings += compare(upstream_syms, ours_syms)
        findings += check_markers(
            upstream_syms, ours_syms, local_dir, set(cfg["files"]), unmarked_dump
        )
        all_findings[name] = findings

    total = sum(len(v) for v in all_findings.values())
    lines = [f"# Upstream coverage report ({args.mode} mode)", ""]
    for name, findings in all_findings.items():
        pin = pins["upstreams"][name]
        lines.append(
            f"## {pin['repo']} @ [`{heads[name][:12]}`]"
            f"(https://github.com/{pin['repo']}/tree/{heads[name]})"
        )
        if not findings:
            lines.append("No findings - full coverage.")
        for f in sorted(findings, key=lambda f: f.severity):
            lines.append(f"- **{f.severity}**: {f.detail}")
        lines.append("")
    report = "\n".join(lines)
    print()
    print(report)
    if args.report:
        args.report.write_text(report)
    if args.dump_unmarked:
        args.dump_unmarked.write_text(json.dumps(unmarked_dump, indent=1))
    shutil.rmtree(tmp)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
