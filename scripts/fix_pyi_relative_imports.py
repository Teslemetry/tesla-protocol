#!/usr/bin/env python3
"""Rewrite sibling-module imports in generated *_pb2.pyi stubs to relative form.

protoletariat's import rewriter matches protoc's `import x_pb2 as x__pb2`
alias convention, but the pyi-stub generator built into protoc's Python
codegen (`--python_out=pyi_out:...`) emits a different alias convention
(`import x_pb2 as _x_pb2`), so protoletariat silently leaves .pyi imports
untouched even though it rewrites the matching .py file. This script covers
that one alias convention protoletariat doesn't recognize.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_SIBLING_IMPORT = re.compile(r"^import (\w+_pb2) as (_\1)$", re.MULTILINE)


def fix_file(path: Path) -> bool:
    original = path.read_text()
    rewritten = _SIBLING_IMPORT.sub(r"from . import \1 as \2", original)
    if rewritten != original:
        path.write_text(rewritten)
        return True
    return False


def main(argv: list[str]) -> int:
    if not argv:
        print("usage: fix_pyi_relative_imports.py <dir> [...]", file=sys.stderr)
        return 1
    for directory in argv:
        for pyi_file in sorted(Path(directory).glob("*_pb2.pyi")):
            fix_file(pyi_file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
