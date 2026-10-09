---
"@teslemetry/tesla-protocol": major
---

Correct `energy_device` `CommonAPIGetSystemInfoResponse` to the layout the gateway sends. Before this change, a real gateway reply failed to decode with `DecodeError`, because tag 2 is a plain string on the wire, not a `Din` message.

| Tag | Before | After |
|---|---|---|
| 2 | `Din din` | `string din` |
| 3 | `FirmwareVersion firmare_version` | `FirmwareVersion firmware_version` (spelling fixed) |
| 4 | `SystemUpdate system_update` | reserved (never sent) |
| 5 | `DeviceType device_type` | `SystemUpdate system_update` |
| 6 | - | `DeviceType device_type` |
| 7 | - | `ComplianceInformation compliance_information` |

Tags 8 and 9 carry bytes and stay unmodelled; one of them is `installed_firmware_signature`. Code that read `response.din.value` now reads `response.din`, and code that read `response.firmare_version` now reads `response.firmware_version`. A golden fixture (`fixtures/golden/get_system_info_response.json`) pins a recorded Powerwall 3 reply in both packages.
