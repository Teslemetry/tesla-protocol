---
"@teslemetry/tesla-protocol": major
---

Require protobuf >= 6.33.5, the lowest supported 6.x runtime.

Protobuf supports only the newest minor of a major - releasing a minor
immediately ends support for the previous one - so 6.31 and 6.32 stopped
receiving patches and 6.33 is the lowest supported 6.x line in 2026. The
codegen toolchain moves to grpcio-tools 1.81.1, which stamps gencode 6.33.5,
and the declared floor moves to match it.

**Breaking:** consumers on protobuf 6.32.x or older must upgrade. The gencode
stamp is a hard minimum - a runtime below it raises `VersionError` at import,
not a warning. Home Assistant is unaffected: it constrains `protobuf==6.33.6`.
The `<8` cap is unchanged, so protobuf 7.x consumers are unaffected too.

No wire-format change: the serialized descriptors are byte-identical, and the
golden fixtures pass unchanged in both languages. The regenerated output is the
version stamp in each `_pb2.py`, the `protoc` header comment in each `.ts` file,
and a `.pyi` stub widening where protoc now types optional scalar parameters as
`_Optional[bool]` rather than bare `bool`.
