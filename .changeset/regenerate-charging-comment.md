---
"@teslemetry/tesla-protocol": patch
---

Regenerate `packages/typescript/src/charging/charging.ts` from `proto/charging/charging.proto` to drop a stale source-of-record comment block that was removed from the proto source but never re-synced into the generated output.
