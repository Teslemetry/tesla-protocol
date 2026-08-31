---
"@teslemetry/tesla-protocol": minor
---

Add `tesla.proto.energy_device.v1.SignatureType` and `Tag` to
`proto/energy_device/signed_message.proto`, alongside the `SignatureData` and
`RoutableMessage` messages that reference them. The signed transport wrapper shipped
without these two enums; `SignatureData`/`RoutableMessage` consumers need them to build
and interpret the signature block.

Wire-compatible addition: two new enums, nothing renamed or renumbered.
