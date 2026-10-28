---
"@teslemetry/tesla-protocol": major
---

Add keep-on accessory ports, the legacy vehicle configuration block, VCSEC information-request replies and energy-device registration and Supercharger messages, and correct placeholder and mis-guessed field names in `command`.

**Breaking: field names in `command` change.** The tags and the wire bytes are the same. The field names, the generated-code names and the JSON names change:

| Message | Tag | JSON name before | JSON name after |
|---|---|---|---|
| `Signatures.AES_GCM_Detached_Signature_Data` | 1 | `epoch` | `nonce` |
| `Signatures.AES_GCM_Detached_Signature_Data` | 4 | `nonce` | `tag` |
| `Signatures.AES_GCM_Detached_Signature_Data` | 5 | `tag` | `prefix` |
| `Signatures.SessionInfo` | 7 | `field7` | `flags` |
| `CarServer.PrepareMobileUploadAction` | 3 | `field3` | `apply` |
| `CarServer.DogModeLiveActivityData` | 3 | `field3` | `vin` |
| `CarServer.DogModeLiveActivityData` | 4 | `field4` | `timestamp` |
| `CarServer.DogModeLiveActivityData.DogModeImageData` | 2 | `encryptedImage` | `image` |
| `CarServer.SetPhoneSettingPreferencesAction` | 2 | `field2` | `language` |
| `CarServer.SohState.SohResult` | 3 | `field3` | `soh` |
| `CarServer.VehicleDataSubscriptionResponse` | 3 | `unknown` | `error` |
| `CarServer.VitalsSubscriptionResponse` | 2 | `unknown` | `error` |
| `CarServer.PseudonymSyncResponse` | 1 | `unknown` | `pseudonym` |
| `CarServer.NavigationRouteResponse` | 1 | `unknown` | `route` |
| `CarServer.RequestTeslaAuthCommand` | 2 | `unknown` | `scope` |
| `CarServer.Profile` | 1 | `unknown1` | `uuid` |
| `CarServer.Profile` | 2 | `unknown2` | `name` |
| `CarServer.KeyInfo` | 1 | `unknown1` | `name` |
| `CarServer.KeyInfo` | 2 | `unknown2` | `model` |

`SohState.SohResult.soh` also moves from the oneof `optional_field_3` to `optional_soh`.

`AES_GCM_Detached_Signature_Data` is more than a rename: code that set `epoch` and `nonce` by name put the nonce bytes at tag 4 and the epoch bytes at tag 1. Tag 1 is the nonce, tag 4 is the tag and tag 5 is the prefix.

**Added (wire-compatible):**

- `command`: `KeepOnAccessoryPortRequest`, `KeepOnAccessoryPortsState` (`VehicleData` 39), `GetVehicleData.getKeepOnAccessoryPortsState` (34), `VehicleDataSubscription.keep_on_accessory_ports_state_max_update_rate_ms` (31), `VehicleDataFields.keep_on_accessory_ports_state` (33), and the commands `VehicleAction.setKeepOnCabin12vPortAction` (721262) and `setKeepOnCabin48vPortAction` (721263).
- `command`: `VehicleAction.dropNominalSuccessResponses` (185), `CurrentVehicleState.halloween_mode` (71) and `trick_or_treat_mode` (72), `RKEAction_E` `RKE_ACTION_LEFT_STORAGE_OPEN` (33) and `RKE_ACTION_RIGHT_STORAGE_OPEN` (34), and `Domain` `DOMAIN_ENERGY_DEVICE_AUTHORIZED_COMMAND` (11).
- `command`: named alternatives for `AutoparkStyle`, `AutoparkVersion`, `AutoparkState`, `SpoilerState`, `SohState.SohTestPhase` and `SohState.SohTestEndMode`, and the legacy `VehicleState` fields 34, 37, 46 and 47.
- `command`: the legacy `VehicleConfig` configuration fields (car type, trim, badging, wheels, colors, seats, charge port, drive units, efficiency package, steering wheel, `rhd`, `plg`, `vin`) with their Void-oneof types, more `InteriorTrimType` and `ExteriorTrimType` alternatives, and the `GuiSettings` distance, temperature, charge-rate and range-display units.
- `command`: the VCSEC replies to the personalization, capabilities, key-status and active-key information requests (`FromVCSECMessage` 5, 19, 21, 22), `VehicleStatus.keyLocationStatus`, and the key-permission lists on `WhitelistEntryInfo` and `PermissionChange`.
- `energy_device`: `registration_api.proto` (`RegistrationMessages`, `MessageEnvelope` 18) and `supercharger_api.proto` (`SuperchargerMessages`, `MessageEnvelope` 17); the register and site-lookup payloads on `CommonMessages` 40-45 and on the TEG and Wall Connector register calls; `Participant.proxied_device`; `CommonAPIGetSystemInfoResponse.installed_firmware_signature` (8) and `offline_firmware_signature` (9); and new `UpdateStatus`, `WCThirdPartyVehicleMode` and `WCEvseNotReadyReason` values.

Fields not yet confirmed on a live vehicle carry an `UNCONFIRMED` comment.
