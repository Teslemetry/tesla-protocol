#!/usr/bin/env python3
"""Rewrite bare cross-file imports left in protoc-generated .pyi stubs.

protoc's built-in pyi generator emits `import foo_pb2 as _foo_pb2` for a
same-package dependency, using a different alias convention than the regular
.py output (`from . import foo_pb2 as foo__pb2`). protoletariat's import
rewriter matches whole import statements including the alias, so it silently
leaves the pyi import unrewritten - the .py sibling ends up package-relative
while the .pyi stays a bare top-level import that doesn't resolve, breaking
static type checkers (e.g. pyright) for every downstream consumer.

Usage: fix_pyi_imports.py <generated-package-dir>
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_BARE_IMPORT = re.compile(r"^import (\w+_pb2) as (\w+)$", re.MULTILINE)


def fix_file(path: Path, sibling_names: set[str]) -> None:
    text = path.read_text()

    def repl(match: re.Match[str]) -> str:
        module, alias = match.group(1), match.group(2)
        if module not in sibling_names:
            return match.group(0)
        return f"from . import {module} as {alias}"

    new_text = _BARE_IMPORT.sub(repl, text)
    if new_text != text:
        path.write_text(new_text)


def main(directory: str) -> None:
    root = Path(directory)
    sibling_names = {p.stem for p in root.glob("*_pb2.py")}
    for pyi_file in root.glob("*_pb2.pyi"):
        fix_file(pyi_file, sibling_names)


if __name__ == "__main__":
    main(sys.argv[1])
