#!/usr/bin/env python3
"""Stage one proto group under the tesla_protocol namespace for Python codegen.

Python protobuf keeps one default descriptor pool per process, keyed by proto
file name and fully-qualified symbol name. Compiled straight from proto/<group>,
the generated modules register bare file names (car_server.proto) and Tesla's
generic packages (CarServer, VCSEC, ...), so any other library that compiles
Tesla's protos into the same process collides with them at import time.

This copies proto/<group>/*.proto to <stage>/tesla_protocol/<group>/, prefixing
each `package` with `tesla_protocol.` and rewriting the group's own imports to
the staged path. protoc then registers e.g. tesla_protocol/command/car_server.proto
with package tesla_protocol.CarServer. Wire bytes are unchanged (they carry field
numbers, not names) except where a full type name is itself serialized, i.e.
google.protobuf.Any type URLs.

The checked-in protos stay byte-identical to upstream (see upstream.json); only
the Python output is namespaced. Files under google/ keep their canonical name
and package so they resolve to the runtime's well-known/googleapis definitions.

Usage: namespace_protos.py <proto-group-dir> <stage-dir>
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

NAMESPACE = "tesla_protocol"

_PACKAGE = re.compile(r"^(\s*package\s+)([\w.]+)(\s*;)", re.MULTILINE)
_IMPORT = re.compile(r'^(\s*import\s+(?:public\s+|weak\s+)?")([^"]+)(";)', re.MULTILINE)


def stage(group_dir: Path, stage_dir: Path) -> None:
    group = group_dir.name
    local = {p.relative_to(group_dir).as_posix() for p in group_dir.rglob("*.proto")}
    for rel in sorted(local):
        source = (group_dir / rel).read_text()
        if rel.startswith("google/"):
            target = stage_dir / rel
            text = source
        else:
            target = stage_dir / NAMESPACE / group / rel
            text, count = _PACKAGE.subn(lambda m: f"{m[1]}{NAMESPACE}.{m[2]}{m[3]}", source)
            if count != 1:
                raise SystemExit(f"{group_dir / rel}: expected one package statement, found {count}")

            def repl(m: re.Match[str]) -> str:
                path = m[2]
                if path in local and not path.startswith("google/"):
                    path = f"{NAMESPACE}/{group}/{path}"
                return f"{m[1]}{path}{m[3]}"

            text = _IMPORT.sub(repl, text)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)


def main(group_dir: str, stage_dir: str) -> None:
    out = Path(stage_dir)
    if out.exists():
        shutil.rmtree(out)
    stage(Path(group_dir), out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
