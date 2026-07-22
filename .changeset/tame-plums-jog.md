---
"@teslemetry/tesla-protocol": patch
---

Fix generated Python `.pyi` type stubs to use relative cross-file imports, matching the runtime `.py` files. The codegen toolchain now post-processes stub imports that protoletariat's rewriter doesn't recognize (the pyi-stub generator uses a different import-alias convention than protoc's `.py` output), so strict-mode type checkers (pyright/mypy) can resolve cross-module references in downstream consumers.
