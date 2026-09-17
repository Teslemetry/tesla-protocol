---
"@teslemetry/tesla-protocol": minor
---

Model VCSEC's Bluetooth walk-up authentication challenge: `AuthenticationRequest`/`AuthenticationResponse` (wired into `FromVCSECMessage` field 3 and `UnsignedMessage` field 3) plus their `AuthenticationLevel_E`, `AuthenticationReason_E`, and `AuthenticationRejection_E` enums - field numbers and types confirmed against a live vehicle, enum values recovered from the app; several field names could not be recovered and are marked `// name unverified`.
