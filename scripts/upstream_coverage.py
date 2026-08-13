#!/usr/bin/env python3
"""Descriptor-level upstream coverage and reconcile-delta gate.

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

Every run also computes a reconcile delta: how the freshly-fetched upstream
proto bytes compare to the pinned per-file sha256, independent of whether
schema coverage still holds. This is what lets a reconcile advance even when
upstream re-publishes a symbol we already carry as a local extension - that
case leaves schema coverage at zero findings, but the pin is still stale.
Each tracked upstream is classified into zero or more of four outcome
classes: `coverage_gap` (upstream has something ours doesn't), `wire_conflict`
(name/number/type mismatch), `upstream_overlap` (a marked local extension
that now also exists upstream, unchanged), and `non_proto_commit_only`
(upstream HEAD moved but the tracked proto bytes did not). `--dump-delta`
writes this as JSON; the exit code continues to reflect schema coverage only
(coverage_gap/wire_conflict/unmarked extensions), matching prior behavior for
both CI modes - callers that need the reconcile signal read `reconcile_needed`
from the delta file instead.

Upstream wins: if upstream later publishes a symbol we already define under
a different name or number, upstream's version replaces ours - except a
field whose upstream type is an empty placeholder message (e.g. `Void {}`,
Tesla's own convention for an unassigned slot) never overrides a field we
already define concretely at that number; a void never replaces a concrete
definition.

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

TYPE_MESSAGE = descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE


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
    # fqns of messages with no fields (Tesla's placeholder/void convention)
    empty_messages: set[str] = field(default_factory=set)


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
        if not msg.field:
            syms.empty_messages.add(fqn)
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
    outcome_class: str  # "coverage_gap" | "wire_conflict" | "upstream_overlap" | "unmarked_extension"
    detail: str


def is_void(syms: Symbols, info: dict) -> bool:
    """True if a field's type is an empty placeholder message in `syms`."""
    return info["type"] == TYPE_MESSAGE and info["type_name"] in syms.empty_messages


def missing_files(upstream_files: list[Path], ours_files: list[Path]) -> set[str]:
    return {f.name for f in upstream_files} - {f.name for f in ours_files}


def diff_files(pinned: dict[str, str], observed: dict[str, str]) -> dict[str, list[str]]:
    """Compare freshly observed upstream per-file sha256 against the pin."""
    common = set(pinned) & set(observed)
    return {
        "added": sorted(set(observed) - set(pinned)),
        "removed": sorted(set(pinned) - set(observed)),
        "changed": sorted(n for n in common if pinned[n] != observed[n]),
        "unchanged": sorted(n for n in common if pinned[n] == observed[n]),
    }


def compare(upstream: Symbols, ours: Symbols) -> tuple[list[Finding], list[str]]:
    """Returns (findings, void_masked) - void_masked entries are informational
    only: an upstream field's slot is a placeholder type and a concrete local
    definition is kept instead of being overridden."""
    findings: list[Finding] = []
    void_masked: list[str] = []

    for fqn in upstream.messages:
        if fqn not in ours.messages:
            findings.append(Finding("coverage_gap", f"message `{fqn}` missing from ours"))
    for fqn in upstream.enums:
        if fqn not in ours.enums:
            findings.append(Finding("coverage_gap", f"enum `{fqn}` missing from ours"))

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
                same_fqn, same_info = same_number
                if is_void(upstream, up) and not is_void(ours, same_info):
                    void_masked.append(
                        f"field `{same_fqn}` (number {up['number']}): upstream field is a "
                        f"placeholder type here - local concrete definition kept"
                    )
                    continue
                findings.append(
                    Finding(
                        "wire_conflict",
                        f"field `{fqn}` (number {up['number']}) is named "
                        f"`{same_fqn.rsplit('.', 1)[-1]}` in ours - upstream wins names",
                    )
                )
            else:
                findings.append(
                    Finding("coverage_gap", f"field `{fqn}` (number {up['number']}) missing from ours")
                )
        elif (
            mine["number"] != up["number"]
            or mine["type"] != up["type"]
            or mine["type_name"] != up["type_name"]
            or mine["label"] != up["label"]
        ):
            if is_void(upstream, up) and not is_void(ours, mine):
                void_masked.append(
                    f"field `{fqn}`: upstream field is a placeholder type here - "
                    f"local concrete definition kept"
                )
                continue
            findings.append(
                Finding(
                    "wire_conflict",
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
                        "wire_conflict",
                        f"enum value `{fqn}` (number {up['number']}) is named "
                        f"`{same_number.rsplit('.', 1)[-1]}` in ours - upstream wins names",
                    )
                )
            else:
                findings.append(
                    Finding(
                        "coverage_gap",
                        f"enum value `{fqn}` (number {up['number']}) missing from ours",
                    )
                )
        elif mine["number"] != up["number"]:
            findings.append(
                Finding(
                    "wire_conflict",
                    f"enum value `{fqn}`: ours={mine['number']} upstream={up['number']}",
                )
            )
    return findings, void_masked


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


def is_marked(
    fqn: str, file: str, ours: Symbols, local_dir: Path, marker_cache: dict[str, set[int]]
) -> bool:
    line = ours.lines.get(fqn)
    if line is None:
        return False
    if file not in marker_cache:
        marker_cache[file] = marked_lines(local_dir / file)
    if line in marker_cache[file]:
        return True
    # a symbol nested in a marked symbol is covered by its ancestor
    parent = fqn.rsplit(".", 1)[0]
    if parent and (parent in ours.messages or parent in ours.enums):
        return is_marked(parent, file, ours, local_dir, marker_cache)
    return False


def check_markers(
    upstream: Symbols,
    ours: Symbols,
    local_dir: Path,
    tracked_files: set[str],
    marker_cache: dict[str, set[int]],
    unmarked_dump: list | None = None,
) -> list[Finding]:
    findings: list[Finding] = []

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
            continue  # whole file has no upstream counterpart, exempt
        if is_marked(fqn, file, ours, local_dir, marker_cache):
            marked += 1
        else:
            findings.append(
                Finding(
                    "unmarked_extension",
                    f"{kind} `{fqn}` ({file}) is not in upstream and has no {MARKER} marker",
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


def check_overlaps(
    upstream: Symbols,
    ours: Symbols,
    local_dir: Path,
    tracked_files: set[str],
    marker_cache: dict[str, set[int]],
) -> list[Finding]:
    """Marked local extensions that now also exist upstream, unchanged -
    candidates for dropping the marker since upstream now defines them
    natively. A wire-level mismatch is reported by compare() instead, not
    counted here."""
    findings: list[Finding] = []

    def emit(fqn: str, kind: str, detail: str) -> None:
        findings.append(Finding("upstream_overlap", f"{kind} `{fqn}`: {detail}"))

    for fqn, file in ours.messages.items():
        if file in tracked_files and fqn in upstream.messages:
            if is_marked(fqn, file, ours, local_dir, marker_cache):
                emit(fqn, "message", "also defined upstream now")
    for fqn, file in ours.enums.items():
        if file in tracked_files and fqn in upstream.enums:
            if is_marked(fqn, file, ours, local_dir, marker_cache):
                emit(fqn, "enum", "also defined upstream now")
    for fqn, info in ours.fields.items():
        if info["file"] not in tracked_files:
            continue
        up = upstream.fields.get(fqn)
        if up is None:
            continue
        if (up["number"], up["type"], up["type_name"], up["label"]) != (
            info["number"], info["type"], info["type_name"], info["label"]
        ):
            continue
        if is_marked(fqn, info["file"], ours, local_dir, marker_cache):
            emit(fqn, "field", f"also defined upstream now at number {up['number']}")
    for fqn, info in ours.enum_values.items():
        if info["file"] not in tracked_files:
            continue
        up = upstream.enum_values.get(fqn)
        if up is None or up["number"] != info["number"]:
            continue
        if is_marked(fqn, info["file"], ours, local_dir, marker_cache):
            emit(fqn, "enum value", f"also defined upstream now at number {up['number']}")
    return findings


def classify(
    findings: list[Finding], proto_bytes_changed: bool
) -> tuple[dict[str, list[str]], list[str], bool]:
    """Group findings by outcome_class and decide whether this upstream needs
    reconciling: either schema coverage is incomplete/conflicting, or the
    pinned bytes are simply stale (even if coverage still holds)."""
    by_class: dict[str, list[str]] = {}
    for f in findings:
        by_class.setdefault(f.outcome_class, []).append(f.detail)
    outcome_classes = [
        c for c in ("coverage_gap", "wire_conflict", "upstream_overlap") if by_class.get(c)
    ]
    reconcile_needed = proto_bytes_changed or bool(outcome_classes)
    return by_class, outcome_classes, reconcile_needed


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
    parser.add_argument("--dump-delta", type=Path, default=None,
                        help="write the upstream/pin/coverage reconcile delta as JSON")
    args = parser.parse_args()

    pins = json.loads((REPO_ROOT / "upstream.json").read_text())
    cache = args.cache_dir or Path(tempfile.mkdtemp(prefix="upstream-coverage-"))
    tmp = Path(tempfile.mkdtemp(prefix="descriptors-"))

    all_findings: dict[str, list[Finding]] = {}
    heads: dict[str, str] = {}
    unmarked_dump: list = []
    delta_upstreams: dict[str, dict] = {}
    schema_total = 0

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
            observed_files = dict(cfg["files"])
        else:
            observed_files = {
                f.name: hashlib.sha256(f.read_bytes()).hexdigest()
                for f in sorted(upstream_dir.glob("*.proto"))
            }

        file_diff = diff_files(cfg["files"], observed_files)
        proto_bytes_changed = bool(
            file_diff["added"] or file_diff["removed"] or file_diff["changed"]
        )
        commit_changed = commit != cfg["commit"]
        non_proto_commit_only = commit_changed and not proto_bytes_changed

        local_dir = REPO_ROOT / cfg["localDir"]
        upstream_files = sorted(upstream_dir.glob("*.proto"))
        ours_files = sorted(local_dir.glob("*.proto"))

        missing = missing_files(upstream_files, ours_files)
        findings = [
            Finding("coverage_gap", f"file `{f}` exists upstream but not in {cfg['localDir']}/")
            for f in sorted(missing)
        ]

        up_out, ours_out = tmp / f"{name}-up.pb", tmp / f"{name}-ours.pb"
        run_protoc(upstream_dir, [f for f in upstream_files if f.name not in missing],
                   up_out, source_info=False)
        run_protoc(local_dir, ours_files, ours_out, source_info=True)
        upstream_syms = index_set(load_descriptor_set(up_out))
        ours_syms = index_set(load_descriptor_set(ours_out))

        compare_findings, void_masked = compare(upstream_syms, ours_syms)
        findings += compare_findings

        marker_cache: dict[str, set[int]] = {}
        findings += check_markers(
            upstream_syms, ours_syms, local_dir, set(cfg["files"]), marker_cache, unmarked_dump
        )
        overlap_findings = check_overlaps(
            upstream_syms, ours_syms, local_dir, set(cfg["files"]), marker_cache
        )
        all_findings[name] = findings + overlap_findings
        schema_total += sum(
            1 for f in findings if f.outcome_class != "upstream_overlap"
        )

        by_class, outcome_classes, reconcile_needed = classify(
            findings + overlap_findings, proto_bytes_changed
        )
        if non_proto_commit_only:
            outcome_classes.append("non_proto_commit_only")

        delta_upstreams[name] = {
            "repo": cfg["repo"],
            "pinned_commit": cfg["commit"],
            "observed_commit": commit,
            "commit_changed": commit_changed,
            "files": file_diff,
            "proto_bytes_changed": proto_bytes_changed,
            "non_proto_commit_only": non_proto_commit_only,
            "outcome_classes": outcome_classes,
            "outcomes": {
                "coverage_gap": sorted(by_class.get("coverage_gap", [])),
                "wire_conflict": sorted(by_class.get("wire_conflict", [])),
                "upstream_overlap": sorted(by_class.get("upstream_overlap", [])),
            },
            "unmarked_extensions": sorted(by_class.get("unmarked_extension", [])),
            "void_masked": sorted(void_masked),
            "reconcile_needed": reconcile_needed,
        }

    lines = [f"# Upstream coverage report ({args.mode} mode)", ""]
    for name, findings in all_findings.items():
        pin = pins["upstreams"][name]
        d = delta_upstreams[name]
        lines.append(
            f"## {pin['repo']} @ [`{heads[name][:12]}`]"
            f"(https://github.com/{pin['repo']}/tree/{heads[name]})"
        )
        schema_findings = [f for f in findings if f.outcome_class != "upstream_overlap"]
        if not schema_findings:
            lines.append("No coverage findings.")
        for f in sorted(schema_findings, key=lambda f: f.outcome_class):
            lines.append(f"- **{f.outcome_class}**: {f.detail}")
        overlap = [f for f in findings if f.outcome_class == "upstream_overlap"]
        if overlap:
            lines.append("")
            lines.append("Upstream overlap candidates (local extension also now upstream):")
            for f in overlap:
                lines.append(f"- {f.detail}")
        if d["files"]["added"] or d["files"]["removed"] or d["files"]["changed"]:
            lines.append("")
            lines.append("File changes vs pinned hashes:")
            for kind in ("added", "removed", "changed"):
                for fname in d["files"][kind]:
                    lines.append(f"- {kind}: `{fname}`")
        if d["void_masked"]:
            lines.append("")
            lines.append("Upstream placeholder fields masked by an existing concrete local definition:")
            for m in d["void_masked"]:
                lines.append(f"- {m}")
        if d["non_proto_commit_only"]:
            lines.append("")
            lines.append(
                f"Upstream HEAD moved to `{heads[name][:12]}` with no change under "
                f"`{pin['pathPrefix']}` - nothing to reconcile."
            )
        lines.append("")
    report = "\n".join(lines)
    print()
    print(report)
    if args.report:
        args.report.write_text(report)
    if args.dump_unmarked:
        args.dump_unmarked.write_text(json.dumps(unmarked_dump, indent=1))
    if args.dump_delta:
        delta = {
            "schema_version": 1,
            "mode": args.mode,
            "upstreams": delta_upstreams,
            "reconcile_needed": any(v["reconcile_needed"] for v in delta_upstreams.values()),
        }
        args.dump_delta.write_text(json.dumps(delta, indent=2, sort_keys=True) + "\n")
    shutil.rmtree(tmp)
    return 1 if schema_total else 0


if __name__ == "__main__":
    sys.exit(main())
