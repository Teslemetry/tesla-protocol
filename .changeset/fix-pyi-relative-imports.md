---
"@teslemetry/tesla-protocol": patch
---

Fix cross-file imports left unrewritten in generated `.pyi` stubs (`car_server_pb2.pyi`, `universal_message_pb2.pyi`, `vcsec_pb2.pyi`, `vehicle_pb2.pyi`, and three `energy_device` stubs). protoc's pyi generator aliases same-package imports differently than its `.py` generator (`_foo_pb2` vs `foo__pb2`), so protoletariat's import rewriter - which matches whole import statements including the alias - left the pyi side as a bare top-level `import foo_pb2 as _foo_pb2` instead of the package-relative form the `.py` sibling already got. Static type checkers (e.g. pyright) can't resolve those imports, breaking type information for any field typed through them. `scripts/generate.sh` now runs a small `scripts/fix_pyi_imports.py` pass after `protol` to patch the remaining bare pyi imports.
