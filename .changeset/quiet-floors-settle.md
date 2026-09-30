---
"@teslemetry/tesla-protocol": patch
---

Restore protobuf 6.32.0 support in the Python package.

The Python package now declares `protobuf>=6.32.0,<8` again and its gencode is
stamped 6.31.1 instead of 6.33.5. The stamp is a hard minimum - a runtime below
it raises `VersionError` at import - and the current Home Assistant stable
release constrains `protobuf==6.32.0`, so the 6.33.5 floor made the package
uninstallable there. The codegen toolchain moves to grpcio-tools 1.80.0, the
newest release that stamps 6.31.1. protobuf 7.x remains supported by the same
wheel.

No wire-format change: the serialized descriptors are byte-identical and the
golden fixtures pass unchanged in both languages. The regenerated output is the
version stamp in each `_pb2.py`, `.pyi` stubs where this protoc types `bool`
constructor parameters as bare `bool` rather than `_Optional[bool]`, and, in the
TypeScript package, comments only: the `protoc` header of each `.ts` file and
the doc comment on the bundled `google.protobuf.Timestamp`.
