---
"@teslemetry/tesla-protocol": major
---

Add energy-device registration types and `Signatures.SessionInfoFlags`, give nine `energy_device` `int32` fields their enum types, make `PartnerInfo.site_relationship_type` repeated, and correct field and type names in `command` and `energy_device`.

Added (wire- and JSON-compatible):

- `energy_device` enums `MarketType`, `RegistrationFailure`, `SiteRegistrationStatus` and `BranchCircuitDeviceType`.
- Enum values `TEGDeviceType` 11 `TULIP`, 12 `DYNAMO` and 13 `SMC_SUPERCHARGER`, `IPMDeviceType` 3 `MEGACHARGER` and `RegistrationDeviceType` 7 `OPTIMUS_CHARGER`.
- Fields `RegistrationRequest.market_type` (12), `RegistrationRequest.potential_site_uuid` (13) and `DeviceDetail.teg_device_type` (4).
- Messages `DeviceInfo`, `AssetSiteDetailsRequest`, `AssetSiteUuidOfDeviceRequest`, `CustomerRegistrationInfo`, `DeactivateDeviceResponse`, `SiteInfo`, `RegistrationRequestWithPartDetails` and `WCCommercialRegistrationRequestWithPartDetails`.
- `command` enum `Signatures.SessionInfoFlags`, which names the bit positions in `SessionInfo.flags`.

**Breaking: `int32` fields now have enum types.** The tags and the wire bytes are the same. Generated code uses the enum types, and JSON output shows enum names instead of numbers:

| Message | Field | New type |
|---|---|---|
| `CommonAPIRegisterResponse` | `failure` (1) | `RegistrationFailure` |
| `RegistrationAPIRegisterResponse` | `failure` (1) | `RegistrationFailure` |
| `CommercialChargingDeviceProperties` | `power_type` (9) | `PowerType` |
| `CommercialChargingDeviceProperties` | `connector_type` (10) | `ConnectorType` |
| `SystemUpdate` | `handshake_result` (1) | `UpdateHandshakeResult` |
| `SystemUpdate` | `update_status` (2) | `UpdateStatus` |
| `SystemUpdate` | `last_update_result` (8) | `LastUpdateResult` |
| `CommonAPIConfigureWifiWithEncryptedPasswordResponse` | `result` (3) | `WifiConfigureResult` |
| `CommonAPIGetCellularInfoResponse` | `supported_profiles` (2) | `repeated CellularProfileType` |

**Breaking: `PartnerInfo.site_relationship_type` (2) is now `repeated RegistrationSiteRelationshipType`.** The wire tag is the same. Generated code and JSON now use a list.

**Breaking: names change.** The tags and the wire bytes are the same:

| Symbol | Before | After | JSON name changes |
|---|---|---|---|
| `Errors.NominalError` field 8 | `keyNotFoundContext` | `keyNotFound`, in `oneof context` | yes |
| `Errors.KeyNotFoundContext` field 1 | `public_key` | `publicKey`, in `oneof key` | no |
| `Errors.KeyNotFoundContext` field 2 | `handle` | `slot`, in `oneof key` | yes |
| `VCSEC.VehicleStatus` field 6 | `uiDesire` | `UIDesire` | yes |
| `energy_device` enum | `iPMDeviceType` | `IPMDeviceType` | no |
| `EncryptedMessage` field 2 | `cipher_text` | `ciphertext` | yes |
| `GridComplianceStatus` field 2 | `qualifiying_time_remaining_s` | `qualifying_time_remaining_s` | yes |
| `WifiNetwork` field 2 | `rssiValue` | `rssi_value` | no |
| `WifiNetwork` field 4 | `securityType` | `security_type` | no |
