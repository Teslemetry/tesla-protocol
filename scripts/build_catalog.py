#!/usr/bin/env python3
"""Deterministic, descriptor-based protobuf surface catalog.

Compiles every publish group under `proto/` to a descriptor set (same
technique as `upstream_coverage.py`/`check_reply_coverage.py`) and walks it
into a sorted, machine-readable inventory: every group, file, package,
message, enum, field (number/type/label/oneof), reservation, import and
provenance class, plus each group's generated TypeScript/Python target.
Cross-checks that every file's provenance class is consistent between its
header banner and `PROVENANCE.md`, and that `buf.yaml`, `GROUPS_LIST` (in
generate.sh), and the README/PROVENANCE group tables all register the same
set of groups as actually exist under `proto/`.

Writes `catalog/catalog.json` (full inventory) and `catalog/SUMMARY.md`
(short human-readable digest). Run it, then `git diff --exit-code -- catalog/`
to detect drift - the same pattern `generate.sh` uses for codegen output.
Exits non-zero (before writing, with a stderr explanation) if group
registration is inconsistent or any file's provenance class can't be
resolved unambiguously.

Requires grpcio-tools (bundled protoc) in the running interpreter.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from google.protobuf import descriptor_pb2

REPO_ROOT = Path(__file__).resolve().parent.parent
PROTO_ROOT = REPO_ROOT / "proto"
CATALOG_DIR = REPO_ROOT / "catalog"
TS_ROOT = REPO_ROOT / "packages" / "typescript" / "src"
PY_ROOT = REPO_ROOT / "packages" / "python" / "tesla_protocol"

UPSTREAM_HEADER = "UPSTREAM-SOURCE:"
SOR_HEADER = "TESLEMETRY SOURCE-OF-RECORD"
VENDORED_HEADER = "Vendored from"

FieldType = descriptor_pb2.FieldDescriptorProto.Type
FieldLabel = descriptor_pb2.FieldDescriptorProto.Label


# ---------------------------------------------------------------------------
# Group discovery


def discover_groups() -> list[str]:
    """Ground truth: top-level proto/ directories that contain a .proto file."""
    groups = []
    for child in PROTO_ROOT.iterdir():
        if child.is_dir() and any(child.rglob("*.proto")):
            groups.append(child.name)
    return sorted(groups)


def compiled_top_level_files(group: str) -> list[Path]:
    """Files generate.sh actually passes to protoc: `proto/<group>/*.proto` (non-recursive)."""
    return sorted((PROTO_ROOT / group).glob("*.proto"))


def all_source_files(group: str) -> list[Path]:
    """Every .proto file under the group, including vendored imports in subdirectories."""
    return sorted((PROTO_ROOT / group).rglob("*.proto"))


# ---------------------------------------------------------------------------
# Registration cross-check: buf.yaml / GROUPS_LIST / README / PROVENANCE.md


def parse_buf_yaml_groups() -> list[str]:
    text = (REPO_ROOT / "buf.yaml").read_text()
    return sorted(re.findall(r"^\s*-\s*path:\s*proto/(\S+)\s*$", text, re.MULTILINE))


def parse_generate_sh_groups() -> list[str]:
    text = (REPO_ROOT / "scripts" / "generate.sh").read_text()
    m = re.search(r'^GROUPS_LIST="([^"]+)"', text, re.MULTILINE)
    if not m:
        sys.exit("could not find GROUPS_LIST= in scripts/generate.sh")
    return sorted(m.group(1).split())


def parse_readme_groups() -> list[str]:
    text = (REPO_ROOT / "README.md").read_text()
    m = re.search(r"## Layout\s*```(.*?)```", text, re.DOTALL)
    if not m:
        sys.exit("could not find a '## Layout' fenced block in README.md")
    return sorted(re.findall(r"^[├└]──\s*(\S+)/", m.group(1), re.MULTILINE))


def parse_provenance_md_rows() -> list[tuple[str, str]]:
    """Returns [(path_token, normalized_class), ...] from PROVENANCE.md's table."""
    text = (REPO_ROOT / "PROVENANCE.md").read_text()
    rows: list[tuple[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|") or "---" in line:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2 or cells[0] in ("Directory",):
            continue
        paths = re.findall(r"`(proto/[^`]+)`", cells[0])
        if not paths:
            continue
        if "upstream-tracked" in cells[1]:
            klass = "upstream-tracked"
        elif "Teslemetry source-of-record" in cells[1]:
            klass = "teslemetry-source-of-record"
        else:
            sys.exit(f"PROVENANCE.md: unrecognized provenance class {cells[1]!r} for {paths}")
        for p in paths:
            rows.append((p, klass))
    return rows


def parse_provenance_md_groups() -> list[str]:
    groups = set()
    for path, _klass in parse_provenance_md_rows():
        rel = path[len("proto/"):].rstrip("/")
        if not rel:
            continue
        groups.add(rel.split("/")[0])
    return sorted(groups)


def check_registration(groups_on_disk: list[str]) -> dict:
    sources = {
        "buf.yaml": parse_buf_yaml_groups(),
        "scripts/generate.sh GROUPS_LIST": parse_generate_sh_groups(),
        "README.md layout table": parse_readme_groups(),
        "PROVENANCE.md table": parse_provenance_md_groups(),
    }
    problems = []
    for source_name, groups in sources.items():
        if groups != groups_on_disk:
            problems.append(
                f"{source_name} lists {groups} but proto/ has {groups_on_disk}"
            )
    for group in groups_on_disk:
        ts_dir = TS_ROOT / group
        py_dir = PY_ROOT / group
        if not ts_dir.is_dir() or not any(ts_dir.iterdir()):
            problems.append(f"group {group!r} has no generated TypeScript output at {ts_dir}")
        if not py_dir.is_dir() or not any(py_dir.iterdir()):
            problems.append(f"group {group!r} has no generated Python output at {py_dir}")
    return {
        "consistent": not problems,
        "problems": problems,
        "groups_on_disk": groups_on_disk,
        **{f"groups_in_{k}": v for k, v in
           {"buf_yaml": sources["buf.yaml"],
            "generate_sh": sources["scripts/generate.sh GROUPS_LIST"],
            "readme": sources["README.md layout table"],
            "provenance_md": sources["PROVENANCE.md table"]}.items()},
    }


# ---------------------------------------------------------------------------
# Provenance classification per file


def header_class(text: str) -> str | None:
    head = "\n".join(text.splitlines()[:10])
    if UPSTREAM_HEADER in head:
        return "upstream-tracked"
    if SOR_HEADER in head:
        return "teslemetry-source-of-record"
    if VENDORED_HEADER in head:
        return "vendored-import"
    return None


def provenance_md_class(rel_path: str, rows: list[tuple[str, str]]) -> str | None:
    best: tuple[int, str] | None = None
    for path, klass in rows:
        if rel_path == path or rel_path.startswith(path):
            if best is None or len(path) > best[0]:
                best = (len(path), klass)
    return best[1] if best else None


def classify_file(proto_path: Path, provenance_rows: list[tuple[str, str]]) -> str:
    rel = proto_path.relative_to(REPO_ROOT).as_posix()
    header = header_class(proto_path.read_text())
    if header == "vendored-import":
        # Documented only in the file's own header, by design: it is an
        # imported dependency, not part of any published group's surface.
        return header
    table = provenance_md_class(rel, provenance_rows)
    if header and table and header != table:
        sys.exit(f"{rel}: header says {header!r} but PROVENANCE.md says {table!r}")
    klass = header or table
    if klass is None:
        sys.exit(f"{rel}: no provenance class found in its header or PROVENANCE.md")
    return klass


# ---------------------------------------------------------------------------
# Descriptor walking


def compile_descriptor_set(include_dir: Path, files: list[Path]) -> descriptor_pb2.FileDescriptorSet:
    out = Path(tempfile.mkstemp(suffix=".pb")[1])
    args = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"-I{include_dir}",
        f"--descriptor_set_out={out}",
        "--include_source_info",
    ] + [str(f) for f in files]
    proc = subprocess.run(args, capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"protoc failed for {include_dir}:\n{proc.stderr}")
    fds = descriptor_pb2.FileDescriptorSet()
    fds.ParseFromString(out.read_bytes())
    out.unlink()
    return fds


def run_protoc(group: str, files: list[Path]) -> descriptor_pb2.FileDescriptorSet:
    return compile_descriptor_set(PROTO_ROOT / group, files)


def walk_field(f: descriptor_pb2.FieldDescriptorProto, oneof_names: list[str]) -> dict:
    return {
        "number": f.number,
        "name": f.name,
        "type": FieldType.Name(f.type),
        "type_name": f.type_name or None,
        "label": FieldLabel.Name(f.label),
        "oneof": oneof_names[f.oneof_index] if f.HasField("oneof_index") else None,
    }


def walk_enum(enum: descriptor_pb2.EnumDescriptorProto, fqn: str) -> dict:
    return {
        "fqn": fqn,
        "name": enum.name,
        "values": [
            {"number": v.number, "name": v.name} for v in enum.value
        ],
        "reserved_ranges": sorted(
            [rr.start, rr.end - 1] for rr in enum.reserved_range
        ),
        "reserved_names": sorted(enum.reserved_name),
    }


def walk_message(msg: descriptor_pb2.DescriptorProto, fqn: str) -> dict:
    oneof_names = [o.name for o in msg.oneof_decl]
    return {
        "fqn": fqn,
        "name": msg.name,
        "fields": [walk_field(f, oneof_names) for f in msg.field],
        "oneofs": oneof_names,
        "reserved_ranges": sorted(
            [rr.start, rr.end - 1] for rr in msg.reserved_range
        ),
        "reserved_names": sorted(msg.reserved_name),
        "nested_messages": [
            walk_message(nested, f"{fqn}.{nested.name}") for nested in msg.nested_type
        ],
        "nested_enums": [
            walk_enum(nested, f"{fqn}.{nested.name}") for nested in msg.enum_type
        ],
    }


def count_messages(messages: list[dict]) -> int:
    return sum(1 + count_messages(m["nested_messages"]) for m in messages)


def count_nested_enums(messages: list[dict]) -> int:
    return sum(len(m["nested_enums"]) + count_nested_enums(m["nested_messages"]) for m in messages)


def count_fields(messages: list[dict]) -> int:
    return sum(len(m["fields"]) + count_fields(m["nested_messages"]) for m in messages)


def walk_file(fd: descriptor_pb2.FileDescriptorProto) -> dict:
    prefix = f".{fd.package}" if fd.package else ""
    messages = [walk_message(m, f"{prefix}.{m.name}") for m in fd.message_type]
    enums = [walk_enum(e, f"{prefix}.{e.name}") for e in fd.enum_type]
    return {
        "package": fd.package or None,
        "imports": sorted(fd.dependency),
        "messages": messages,
        "enums": enums,
    }


# ---------------------------------------------------------------------------
# Catalog assembly


def build_group(group: str, provenance_rows: list[tuple[str, str]]) -> dict:
    top_level = compiled_top_level_files(group)
    source_files = all_source_files(group)
    vendored_only = sorted(set(source_files) - set(top_level))

    fds = run_protoc(group, top_level)
    by_name = {fd.name: fd for fd in fds.file}

    files = []
    for path in top_level:
        name = path.name
        fd = by_name.get(name)
        if fd is None:
            sys.exit(f"protoc did not emit a descriptor for compiled input {path}")
        entry = walk_file(fd)
        entry.update({
            "path": path.relative_to(REPO_ROOT).as_posix(),
            "compiled_top_level_input": True,
            "provenance_class": classify_file(path, provenance_rows),
        })
        files.append(entry)

    for path in vendored_only:
        rel_name = path.relative_to(PROTO_ROOT / group).as_posix()
        files.append({
            "path": path.relative_to(REPO_ROOT).as_posix(),
            "compiled_top_level_input": False,
            "provenance_class": classify_file(path, provenance_rows),
            "package": None,
            "imports": [],
            "messages": [],
            "enums": [],
            "note": (
                f"vendored import dependency ({rel_name}); pulled in transitively, "
                "not compiled as a top-level input, excluded from group/global totals"
            ),
        })

    files.sort(key=lambda f: f["path"])

    total_messages = sum(count_messages(f["messages"]) for f in files)
    total_enums = sum(len(f["enums"]) + count_nested_enums(f["messages"]) for f in files)
    total_fields = sum(count_fields(f["messages"]) for f in files)

    classes = sorted({f["provenance_class"] for f in files})

    return {
        "name": group,
        "source_files": len(source_files),
        "compiled_top_level_inputs": len(top_level),
        "provenance_classes": classes,
        "generated_targets": {
            "typescript": (TS_ROOT / group).relative_to(REPO_ROOT).as_posix(),
            "python": (PY_ROOT / group).relative_to(REPO_ROOT).as_posix(),
        },
        "messages": total_messages,
        "enums": total_enums,
        "fields": total_fields,
        "files": files,
    }


def build_catalog() -> dict:
    groups_on_disk = discover_groups()
    registration = check_registration(groups_on_disk)
    if not registration["consistent"]:
        print("Group registration is inconsistent:", file=sys.stderr)
        for p in registration["problems"]:
            print(f"  - {p}", file=sys.stderr)
        sys.exit(1)

    provenance_rows = parse_provenance_md_rows()
    groups = [build_group(g, provenance_rows) for g in groups_on_disk]

    totals = {
        "source_files": sum(g["source_files"] for g in groups),
        "groups": len(groups),
        "messages": sum(g["messages"] for g in groups),
        "enums": sum(g["enums"] for g in groups),
        "fields": sum(g["fields"] for g in groups),
    }

    return {
        "schema_version": 1,
        "groups": groups,
        "totals": totals,
        "registration": registration,
    }


def render_summary_md(catalog: dict) -> str:
    t = catalog["totals"]
    lines = [
        "# Protobuf surface catalog",
        "",
        "Generated by `scripts/build_catalog.py` from `proto/`. Do not edit by hand;",
        "regenerate with `.venv/bin/python scripts/build_catalog.py` and commit the diff.",
        "See `catalog/catalog.json` for the full descriptor-based inventory.",
        "",
        f"**Totals:** {t['source_files']} source files, {t['groups']} groups, "
        f"{t['messages']} messages, {t['enums']} enums, {t['fields']} fields.",
        "",
        "| Group | Source files | Compiled top-level inputs | Messages | Enums | Fields | Provenance |",
        "|---|---:|---:|---:|---:|---:|---|",
    ]
    for g in catalog["groups"]:
        lines.append(
            f"| `{g['name']}` | {g['source_files']} | {g['compiled_top_level_inputs']} | "
            f"{g['messages']} | {g['enums']} | {g['fields']} | "
            f"{', '.join(g['provenance_classes'])} |"
        )
    lines.append("")

    vendored = [
        f for g in catalog["groups"] for f in g["files"] if not f["compiled_top_level_input"]
    ]
    if vendored:
        lines.append(
            "Vendored import dependencies (present under `proto/`, not passed to protoc "
            "as a top-level input, excluded from the totals above):"
        )
        for f in vendored:
            lines.append(f"- `{f['path']}` - {f['note']}")
        lines.append("")

    reg = catalog["registration"]
    lines.append(
        f"Group registration (`buf.yaml`, `scripts/generate.sh`, `README.md`, "
        f"`PROVENANCE.md`) is **{'consistent' if reg['consistent'] else 'INCONSISTENT'}** "
        f"with `proto/`: {', '.join(reg['groups_on_disk'])}."
    )
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    catalog = build_catalog()
    CATALOG_DIR.mkdir(exist_ok=True)
    (CATALOG_DIR / "catalog.json").write_text(json.dumps(catalog, indent=2, sort_keys=False) + "\n")
    (CATALOG_DIR / "SUMMARY.md").write_text(render_summary_md(catalog))
    t = catalog["totals"]
    print(
        f"catalog: {t['source_files']} source files, {t['groups']} groups, "
        f"{t['messages']} messages, {t['enums']} enums, {t['fields']} fields"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
