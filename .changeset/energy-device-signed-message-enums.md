---
"@teslemetry/tesla-protocol": patch
---

Add `tesla.proto.energy_device.v1.SignatureType` and `Tag` to
`proto/energy_device/signed_message.proto`, alongside the `SignatureData` and
`RoutableMessage` messages that reference them. The signed transport wrapper published in
1.3.0 shipped incomplete: `SignatureData`/`RoutableMessage` already referenced these enums,
so a consumer of that release had no way to actually build or interpret a signature block.
This completes it.

Wire-compatible addition: two new enums, nothing renamed or renumbered.
