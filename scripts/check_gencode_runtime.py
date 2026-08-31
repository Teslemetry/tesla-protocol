#!/usr/bin/env python3
"""Import every committed *_pb2 module under the installed protobuf runtime.

Each generated module calls ValidateProtobufRuntimeVersion with the gencode
version stamped in by the protoc that produced it. protobuf's only rule is that
the runtime must not be OLDER than that stamp - there is no minimum-gencode
check, so 6.x gencode loads fine on a 7.x runtime. This gate makes that
concrete: CI runs it against both the oldest supported runtime and the newest
major, so bumping the grpcio-tools pin onto a newer protoc (which would raise
the gencode stamp and lock out older runtimes) fails here instead of in a
downstream install.
"""

import importlib
import pathlib
import sys

import google.protobuf

PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent / "packages/python/tesla_protocol"


def main() -> int:
    modules = sorted(PACKAGE_ROOT.rglob("*_pb2.py"))
    if not modules:
        print(f"no generated modules found under {PACKAGE_ROOT}", file=sys.stderr)
        return 1

    sys.path.insert(0, str(PACKAGE_ROOT.parent))

    failures = []
    for path in modules:
        name = ".".join(path.relative_to(PACKAGE_ROOT.parent).with_suffix("").parts)
        try:
            importlib.import_module(name)
        except Exception as exc:  # report every failure, not just the first
            failures.append(f"{name}: {type(exc).__name__}: {exc}")

    runtime = google.protobuf.__version__
    print(f"protobuf runtime {runtime}: imported {len(modules) - len(failures)}/{len(modules)} modules")
    for failure in failures:
        print(f"  FAIL {failure}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
