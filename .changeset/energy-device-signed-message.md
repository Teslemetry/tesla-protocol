---
"@teslemetry/tesla-protocol": minor
---

Add `tesla.proto.energy_device.v1.Message`, the RSA-signed transport wrapper for the
Powerwall local v1r endpoint: `Destination`, `KeyIdentity`, `RsaSignatureData`,
`SignatureData`, `RoutableMessage`, `Tail`, and the outer `Message`, in a new
`proto/energy_device/signed_message.proto`. `RoutableMessage.protobuf_message_as_bytes`
carries the domain routing envelope (`MessageEnvelope`, already in `transport.proto`) as
opaque bytes, so this only adds the signing layer - none of the domain schema is
duplicated.

Wire-compatible addition: brand-new file, nothing renamed or renumbered.
