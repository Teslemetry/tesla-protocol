# @teslemetry/tesla-protocol

## 6.0.0

### Major Changes

- b9fbbd3: Add energy-device registration types and `Signatures.SessionInfoFlags`, give nine `energy_device` `int32` fields their enum types, make `PartnerInfo.site_relationship_type` repeated, and correct field and type names in `command` and `energy_device`.

  Added (wire- and JSON-compatible):

  - `energy_device` enums `MarketType`, `RegistrationFailure`, `SiteRegistrationStatus` and `BranchCircuitDeviceType`.
  - Enum values `TEGDeviceType` 11 `TULIP`, 12 `DYNAMO` and 13 `SMC_SUPERCHARGER`, `IPMDeviceType` 3 `MEGACHARGER` and `RegistrationDeviceType` 7 `OPTIMUS_CHARGER`.
  - Fields `RegistrationRequest.market_type` (12), `RegistrationRequest.potential_site_uuid` (13) and `DeviceDetail.teg_device_type` (4).
  - Messages `DeviceInfo`, `AssetSiteDetailsRequest`, `AssetSiteUuidOfDeviceRequest`, `CustomerRegistrationInfo`, `DeactivateDeviceResponse`, `SiteInfo`, `RegistrationRequestWithPartDetails` and `WCCommercialRegistrationRequestWithPartDetails`.
  - `command` enum `Signatures.SessionInfoFlags`, which names the bit positions in `SessionInfo.flags`.

  **Breaking: `int32` fields now have enum types.** The tags and the wire bytes are the same. Generated code uses the enum types, and JSON output shows enum names instead of numbers:

  | Message                                               | Field                    | New type                       |
  | ----------------------------------------------------- | ------------------------ | ------------------------------ |
  | `CommonAPIRegisterResponse`                           | `failure` (1)            | `RegistrationFailure`          |
  | `RegistrationAPIRegisterResponse`                     | `failure` (1)            | `RegistrationFailure`          |
  | `CommercialChargingDeviceProperties`                  | `power_type` (9)         | `PowerType`                    |
  | `CommercialChargingDeviceProperties`                  | `connector_type` (10)    | `ConnectorType`                |
  | `SystemUpdate`                                        | `handshake_result` (1)   | `UpdateHandshakeResult`        |
  | `SystemUpdate`                                        | `update_status` (2)      | `UpdateStatus`                 |
  | `SystemUpdate`                                        | `last_update_result` (8) | `LastUpdateResult`             |
  | `CommonAPIConfigureWifiWithEncryptedPasswordResponse` | `result` (3)             | `WifiConfigureResult`          |
  | `CommonAPIGetCellularInfoResponse`                    | `supported_profiles` (2) | `repeated CellularProfileType` |

  **Breaking: `PartnerInfo.site_relationship_type` (2) is now `repeated RegistrationSiteRelationshipType`.** The wire tag is the same. Generated code and JSON now use a list.

  **Breaking: names change.** The tags and the wire bytes are the same:

  | Symbol                              | Before                         | After                             | JSON name changes |
  | ----------------------------------- | ------------------------------ | --------------------------------- | ----------------- |
  | `Errors.NominalError` field 8       | `keyNotFoundContext`           | `keyNotFound`, in `oneof context` | yes               |
  | `Errors.KeyNotFoundContext` field 1 | `public_key`                   | `publicKey`, in `oneof key`       | no                |
  | `Errors.KeyNotFoundContext` field 2 | `handle`                       | `slot`, in `oneof key`            | yes               |
  | `VCSEC.VehicleStatus` field 6       | `uiDesire`                     | `UIDesire`                        | yes               |
  | `energy_device` enum                | `iPMDeviceType`                | `IPMDeviceType`                   | no                |
  | `EncryptedMessage` field 2          | `cipher_text`                  | `ciphertext`                      | yes               |
  | `GridComplianceStatus` field 2      | `qualifiying_time_remaining_s` | `qualifying_time_remaining_s`     | yes               |
  | `WifiNetwork` field 2               | `rssiValue`                    | `rssi_value`                      | no                |
  | `WifiNetwork` field 4               | `securityType`                 | `security_type`                   | no                |

- 2c45a2f: Correct `energy_device` wire types, enum types, oneofs and names, add the WMSA, SM, energy telemetry and energy command envelope types, model a large part of the VCSEC surface, retype the navigation trip order, and reserve obsolete vehicle-data tags.

  Added (wire- and JSON-compatible):

  - `energy_device` files `wmsa_api.proto` and `sm_api.proto` (20 messages, 3 enums), with `MessageEnvelope.wmsa` (13) and `MessageEnvelope.sm` (14) added as deprecated fields.
  - `energy_device` file `energy_telemetry.proto` (package `tesla.proto.energy_telemetry.v1`): `LogRecord`, `Signal`, `MP2LogRecord`, `DeviceTelemetryRecord` and `DeviceAlertRecord`.
  - `energy_device` file `energy_command.proto` (package `tesla.proto.energy.command.v1`): `EnergyDeviceMessage`, `ServerMessages` and `DeviceResponseTimeout`.
  - `energy_device` enums `TEGRegistrationFailure`, `DcMeterCommissioningError` and `MeterCTLocation`.
  - `command` VCSEC: 59 messages, 41 enums and 39 new oneof alternatives on `UnsignedMessage`, `FromVCSECMessage` and `WhitelistOperation`, plus `SignedMessage` fields 1, 4, 5 and 6 and `ToVCSECMessage.unsignedMessage` (2).
  - `command`: 155 tags reserved in `ChargeState`, `ClimateState`, `VehicleConfig`, `ClosuresState`, `LocationState`, `SoftwareUpdateState`, `SpeedLimitMode`, `DriveState`, `GuiSettings`, `VehicleState` and other messages, for fields that are obsolete.

  **Breaking: the `energy_command` group is removed.** `IdentifierType` moves from `proto/energy_command/identifier_type.proto` to `proto/energy_device/identifier_type.proto`. Its package (`tesla.proto.energy.command.v1`) does not change. Import it from `@teslemetry/tesla-protocol/energy_device/identifier_type` and `tesla_protocol.energy_device.identifier_type_pb2`.

  **Breaking: `LocalParticipant` moves from `transport.proto` to `local_auth_api.proto`.** The package and values do not change. Import it from `energy_device/local_auth_api` and `local_auth_api_pb2`.

  **Breaking: wire types change.** The old types did not match what devices send:

  | Message                              | Field                                | Before                       | After                                         |
  | ------------------------------------ | ------------------------------------ | ---------------------------- | --------------------------------------------- |
  | `AlertLog`                           | `data` (1)                           | `uint64`                     | `fixed64`                                     |
  | `AlertMatrix`                        | `data` (1)                           | `uint64`                     | `fixed64`                                     |
  | `GridComplianceStatus`               | `qualifying_time_remaining_s` (2)    | `google.protobuf.FloatValue` | `google.protobuf.UInt32Value`                 |
  | `WCAPIGetConfigResponse`             | `charge_schedule` (5)                | `WCChargeScheduleConfig`     | `WCChargeScheduleConfigStatus`                |
  | `ControllableDeviceProgram_Schedule` | `start` (1), `end` (2), `expiry` (3) | `google.protobuf.Timestamp`  | `ControllableDeviceProgram_Schedule_Boundary` |

  **Breaking: `WCLifetimeStats` is renumbered.** Its ten fields move from tags 3-12 to tags 1-10 in the same order (`uptime_s` = 1 through `charging_energy` = 10). Tags 1 and 2 are no longer reserved.

  **Breaking: `int32` fields now have enum types.** The tags and the wire bytes are the same. Generated code uses the enum types, and JSON output shows enum names instead of numbers:

  | Message                                           | Field             | New type                    |
  | ------------------------------------------------- | ----------------- | --------------------------- |
  | `TEGAPIRegisterResponse`                          | `failure` (1)     | `RegistrationFailure`       |
  | `WCAPIRegisterCommercialResponse`                 | `failure` (1)     | `RegistrationFailure`       |
  | `LocalAuthAPILoginRequest`                        | `participant` (1) | `LocalParticipant`          |
  | `NeurioCTConfig`                                  | `location` (1)    | `MeterCTLocation`           |
  | `SuperchargerAPIGetDcMetersCommissioningResponse` | `error` (2)       | `DcMeterCommissioningError` |
  | `CarServer.NavigationRequest`                     | `order` (2)       | `RemoteNavTripOrder_E`      |

  **Breaking: the navigation trip order enum is replaced.** The three nested `RemoteNavTripOrder` enums (`REMOTE_NAV_TRIP_ORDER_UNKNOWN = 0`, `REPLACE = 1`, `PREPEND = 2`, `APPEND = 3`) in `NavigationSuperchargerRequest`, `NavigationGpsRequest` and `NavigationGpsDestinationRequest` are deleted. The new top-level `CarServer.RemoteNavTripOrder_E` has `RemoteNavTripOrderReplace = 0`, `RemoteNavTripOrderPrepend = 1` and `RemoteNavTripOrderAppend = 2`, and types `NavigationRequest.order`, `NavigationSuperchargerRequest.remote_nav_trip_order`, `NavigationGpsRequest.order` and `NavigationGpsDestinationRequest.order`. The numbers change: a sender that used 1 for replace must now send 0.

  **Breaking: fields move into oneofs.** The tags and the wire bytes are the same. Generated code exposes them through the oneof:

  | Message                             | Oneof                                         |
  | ----------------------------------- | --------------------------------------------- |
  | `AcceptedPackage`                   | `sideloading_method`                          |
  | `CommonMessages`                    | `message` (now includes `error_response` = 1) |
  | `FileStoreAPIFile`                  | `content`                                     |
  | `PVMeterInterface`                  | `meter_interface`                             |
  | `WCMeterInterface`                  | `meter_interface`                             |
  | `TEGAPIDispatchBatteryPowerRequest` | `command`                                     |
  | `TEGAPIEnsureCertificateRequest`    | `certificate_type`                            |
  | `WCDryContactConfig`                | `control_behavior`                            |
  | `WCLoadSharingConfig`               | `network_limit`                               |
  | `WCLoadSharingSettings`             | `network_limit`                               |
  | `DeviceInfo`                        | `device_sub_type`                             |

  **Breaking: names change.** The tags and the wire bytes are the same:

  | Symbol                                | Before           | After                |
  | ------------------------------------- | ---------------- | -------------------- |
  | `BackupEvent` field 3                 | `sheduling_info` | `scheduling_info`    |
  | `EcuFirmwareUpdateInProgress` field 1 | `default`        | `node_progresses`    |
  | `EcuFirmwareUpdateResult` field 2     | `default`        | `ecu_update_results` |

## 5.0.0

### Major Changes

- d036d95: Add keep-on accessory ports, the legacy vehicle configuration block, VCSEC information-request replies and energy-device registration and Supercharger messages, and correct placeholder and mis-guessed field names in `command`.

  **Breaking: field names in `command` change.** The tags and the wire bytes are the same. The field names, the generated-code names and the JSON names change:

  | Message                                              | Tag | JSON name before | JSON name after |
  | ---------------------------------------------------- | --- | ---------------- | --------------- |
  | `Signatures.AES_GCM_Detached_Signature_Data`         | 1   | `epoch`          | `nonce`         |
  | `Signatures.AES_GCM_Detached_Signature_Data`         | 4   | `nonce`          | `tag`           |
  | `Signatures.AES_GCM_Detached_Signature_Data`         | 5   | `tag`            | `prefix`        |
  | `Signatures.SessionInfo`                             | 7   | `field7`         | `flags`         |
  | `CarServer.PrepareMobileUploadAction`                | 3   | `field3`         | `apply`         |
  | `CarServer.DogModeLiveActivityData`                  | 3   | `field3`         | `vin`           |
  | `CarServer.DogModeLiveActivityData`                  | 4   | `field4`         | `timestamp`     |
  | `CarServer.DogModeLiveActivityData.DogModeImageData` | 2   | `encryptedImage` | `image`         |
  | `CarServer.SetPhoneSettingPreferencesAction`         | 2   | `field2`         | `language`      |
  | `CarServer.SohState.SohResult`                       | 3   | `field3`         | `soh`           |
  | `CarServer.VehicleDataSubscriptionResponse`          | 3   | `unknown`        | `error`         |
  | `CarServer.VitalsSubscriptionResponse`               | 2   | `unknown`        | `error`         |
  | `CarServer.PseudonymSyncResponse`                    | 1   | `unknown`        | `pseudonym`     |
  | `CarServer.NavigationRouteResponse`                  | 1   | `unknown`        | `route`         |
  | `CarServer.RequestTeslaAuthCommand`                  | 2   | `unknown`        | `scope`         |
  | `CarServer.Profile`                                  | 1   | `unknown1`       | `uuid`          |
  | `CarServer.Profile`                                  | 2   | `unknown2`       | `name`          |
  | `CarServer.KeyInfo`                                  | 1   | `unknown1`       | `name`          |
  | `CarServer.KeyInfo`                                  | 2   | `unknown2`       | `model`         |

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

## 4.0.1

### Patch Changes

- 0479682: Update the `telemetry` Semi streaming fields 272-278 to the final upstream layout. Releases 3.0.2 to 4.0.0 carried a draft layout of these fields.

  | `Field` tag | Before                      | After                       |
  | ----------- | --------------------------- | --------------------------- |
  | 272         | `AccRail`                   | `AccessoryRail`             |
  | 273-275     | unchanged                   | unchanged                   |
  | 276         | `CruiseState`               | `LifetimeDcChargeEnergyKwh` |
  | 277         | `LifetimeDcChargeEnergyKwh` | `SemiVehicleMassKg`         |
  | 278         | `VehicleMassKg`             | - (deleted)                 |

  - `CruiseStateValue` and `Value.cruise_state_value` (56) are deleted.
  - `AutomaticEmergencyBrakingStateValue` (Unknown, Unavailable, Standby, Enabled, Standstill) and `Value.automatic_emergency_braking_state_value` (60) are added.
  - `CarTypeSemiTruckV2` (7) and `CarTypeCybercab` (8), and `PowerTransferStatusValue`, are unchanged.

  Code that used `AccRail`, `CruiseState`, `VehicleMassKg` or `CruiseStateValue` must move to the new names. Code that matched tags 276 or 277 by number now gets a different field.

## 4.0.0

### Major Changes

- 2870ee5: Correct `energy_device` `CommonAPIGetSystemInfoResponse` to the layout the gateway sends. Before this change, a real gateway reply failed to decode with `DecodeError`, because tag 2 is a plain string on the wire, not a `Din` message.

  | Tag | Before                            | After                                               |
  | --- | --------------------------------- | --------------------------------------------------- |
  | 2   | `Din din`                         | `string din`                                        |
  | 3   | `FirmwareVersion firmare_version` | `FirmwareVersion firmware_version` (spelling fixed) |
  | 4   | `SystemUpdate system_update`      | reserved (never sent)                               |
  | 5   | `DeviceType device_type`          | `SystemUpdate system_update`                        |
  | 6   | -                                 | `DeviceType device_type`                            |
  | 7   | -                                 | `ComplianceInformation compliance_information`      |

  Tags 8 and 9 carry bytes and stay unmodelled; one of them is `installed_firmware_signature`. Code that read `response.din.value` now reads `response.din`, and code that read `response.firmare_version` now reads `response.firmware_version`. A golden fixture (`fixtures/golden/get_system_info_response.json`) pins a recorded Powerwall 3 reply in both packages.

- ebc7866: Register every Python module under a `tesla_protocol` namespace in the protobuf descriptor pool. Each file is now registered as `tesla_protocol/<group>/<file>.proto` (for example `tesla_protocol/command/car_server.proto`) and each package as `tesla_protocol.<package>` (for example `tesla_protocol.CarServer`). Before this change, the bare file names and Tesla's generic package names (`CarServer`, `VCSEC`, `UniversalMessage`, ...) clashed with any other library that loads Tesla's protos into the same Python process: the import failed with `TypeError: Couldn't build proto file into descriptor pool`.

  Python import paths do not change (`from tesla_protocol.command import car_server_pb2` still works), and the encoded bytes of every message do not change, except where a full type name is itself serialized: a `google.protobuf.Any` packed in Python now carries a `tesla_protocol.`-prefixed `type_url`. Code that uses descriptor full names does change: `DESCRIPTOR.full_name`, `descriptor_pool.FindMessageTypeByName("CarServer.Action")` and `google.protobuf.Any` type URLs now carry the `tesla_protocol.` prefix. The only `Any` field is `teslapower.Status.details`. The generated imports between modules are now absolute (`from tesla_protocol.command import ...`).

  The TypeScript package is unchanged. It has no global descriptor registry, so it keeps upstream's package names; its major version moves only because the two packages release in lockstep.

## 3.0.2

### Patch Changes

- 8ba1eda: Add telemetry `Field` values `AccRail` (272), `PowerTransferStatus` (273), `AutomaticEmergencyBrakingState` (274), `RollingResistanceCoefficient` (275), `CruiseState` (276), `LifetimeDcChargeEnergyKwh` (277) and `VehicleMassKg` (278, Semi only), plus the `CruiseStateValue` and `PowerTransferStatusValue` enums carried in the `Value` oneof as `cruise_state_value` (56) and `power_transfer_status_value` (57).

## 3.0.1

### Patch Changes

- 29640b7: Add `CarTypeSemiTruckV2` (7) and `CarTypeCybercab` (8) to the telemetry `CarTypeValue` enum.

## 3.0.0

### Major Changes

- 0522dc0: **Breaking corrections to published `command` content.**

  - **Command enum numbering.** Four request enums carried an extra `*_UNKNOWN = 0` value, which
    shifted every real value up by one. `*_UNKNOWN` is removed and the values now start at 0:

    - `SetOutletsOnOffAction.OutletRequest`: `OFF = 0`, `CABIN_AND_BED = 1`, `CABIN = 2`
    - `SetPowerFeedOnOffAction.PowerFeedRequest`: `OFF = 0`, `FEED_1 = 1`, `FEED_2 = 2`,
      `FEED_1_AND_FEED_2 = 3`
    - `SetPowershareFeatureAction.PowershareFeatureRequest`: `OFF = 0`, `ON = 1`
    - `SetPowershareRequestAction.PowershareRequest`: `OFF = 0`, `ON = 1`

    Callers that use the symbolic names pick up the new numbers when they rebuild against this
    release. Callers that hard-code numbers, or reference a removed `*_UNKNOWN` value, must update.
    The new values are not yet confirmed on a live vehicle.

  - **`VehicleData.vehicle_state = 18` is now decoded.** The opaque `bytes unknown = 18` becomes
    `CurrentVehicleState vehicle_state = 18`. This covers 65 fields, including `feature_bitmask`,
    inlet heater, wiper service, photobooth, remote sketchpad, the Dog Mode live-activity key,
    car wrap, FSD stats, and deck lights/hazards. The wire format is unchanged: both are
    length-delimited. The generated field is renamed from `unknown` to `vehicleState` (TypeScript)
    / `vehicle_state` (Python), and its type changes from bytes to a message. The new helper
    messages are `DashcamUtils`, `AutoparkStyle`, `AutoparkVersion`, `AutoparkState` and
    `SpoilerState`. Tags 53 and 70 are varint placeholders (`field_53`, `field_70`) whose names
    and types are not yet known. Fields seen on a live vehicle are marked confirmed; the rest are
    marked unconfirmed until they are.
  - **Six misplaced fields are removed from `VehicleState`** (the legacy surface at
    `VehicleData.legacy_vehicle_state = 6`):

    - `deck_lights_on`, `hazards_on` and `deck_lights_allowed` (67-69) now live on
      `CurrentVehicleState` 67-69.
    - `autopilot_base`, `autopilot_override_state` and `autopilot_override_expire_time`
      (196-198) are already on `VehicleConfig` 196-198.

    Their tags and names are reserved on `VehicleState`.

### Minor Changes

- a7cfd24: Wire-compatible additions to the command protocol. Every new field is marked `UNCONFIRMED` (not yet confirmed on a live vehicle), and placeholder names are marked "name not recovered".

  - `VehicleAction`: wire the existing `PrepareMobileUploadAction` (177), `PutMobileUploadChunkAction` (178) and `DisplayStateAction` (180) messages, and add `SetUpkeepUsernameAction` (147), `DrivingSetCruiseSpeedLimitAction` (694177) and `SetDeckLightAction` (698038). Fill in `PrepareMobileUploadAction` tag 3, `MediaPlayAction.media_playback_status`, `SetPhoneSettingPreferencesAction` tag 2, the remaining `DestinationCharging` fields and `DogModeLiveActivityData` tags 2-4, and reserve `Action` tags 6-8.
  - Add the `MobileAppFeature` enum (the capability bits a vehicle advertises, with how to test them against the vehicle-state feature bitmask), `VehicleConfig.wheel_caps_on` (200), the `VehicleDataFields` enum that `EncryptedData.field_number` holds, the PII vehicle-data fields `VehicleData.encrypted_data` (11), `pii_key_responses` (900) and `wrapped_key` (901), and `SohState.SohResult` tag 3.
  - Signed transport: add the `ECDSA`, `PRESENT_KEY`, `AES_GCM_TOKEN`, `ECDSA_PERSONALIZED`, `AES_GCM_DETACHED` and `CERTIFICATE_ECDSA` signature types with their `Present_Key_Signature_Data`, `AES_GCM_Detached_Signature_Data` and `Certificate_ECDSA_Signature_Data` payloads on `SignatureData`, `TAG_COMMAND_PREFIX`, `KeyIdentity.identified_key` with the `IdentifiedKey` enum, `SESSION_INFO_STATUS_INVALID_HANDLE`, `SessionInfo` tag 7, `SessionInfoRequest` tags 3-4, the message-framing and zlib `Flags`, `RoutableMessage.message_frame` (`MessageFrame`), `MESSAGEFAULT_ERROR_COMMAND_REQUIRES_PHYSICAL_PROXIMITY`, four more key `Role`s, the `KEY_NOT_FOUND`/`NOT_SUPPORTED` generic errors with `NominalError.keyNotFoundContext`, and three more VCSEC `SignatureType` values.
  - Complete the rate-tariff document behind `SetRateTariffRequest` and its embedded `Tariff`: `code`, `name`, `utility`, `currency`, `daily_charges` (new `DailyCharge`), `monthly_charges`, `monthly_minimum_bill`, `demand_charges`, `daily_demand_charges`, `energy_charges`, `max_applicable_demand` and `min_applicable_demand` (tags 1-12). Add `GetRateTariffResponse.tariff_document` (1) alongside the existing tags 13-14.

## 2.2.0

### Minor Changes

- 6d37a11: Add `string din = 1;` to `SiteController` (`AddManagedChargingSiteRequest` -> `ManagedChargingSite` -> `ManagerType` -> `SiteController`): the message was previously empty, so every managed charging site added through this library omits the gateway DIN the vehicle uses to match its Powerwall.

## 2.1.0

### Minor Changes

- 4a370c5: Model VCSEC's Bluetooth walk-up authentication challenge: `AuthenticationRequest`/`AuthenticationResponse` (wired into `FromVCSECMessage` field 3 and `UnsignedMessage` field 3) plus their `AuthenticationLevel_E`, `AuthenticationReason_E`, and `AuthenticationRejection_E` enums - field numbers and types confirmed against a live vehicle, enum values recovered from the app; several field names could not be recovered and are marked `// name unverified`.

## 2.0.0

### Major Changes

- bdcba9a: Require protobuf >= 6.33.5, the lowest supported 6.x runtime.

  Protobuf supports only the newest minor of a major - releasing a minor
  immediately ends support for the previous one - so 6.31 and 6.32 stopped
  receiving patches and 6.33 is the lowest supported 6.x line in 2026. The
  codegen toolchain moves to grpcio-tools 1.81.1, which stamps gencode 6.33.5,
  and the declared floor moves to match it.

  **Breaking:** consumers on protobuf 6.32.x or older must upgrade. The gencode
  stamp is a hard minimum - a runtime below it raises `VersionError` at import,
  not a warning. Home Assistant is unaffected: it constrains `protobuf==6.33.6`.
  The `<8` cap is unchanged, so protobuf 7.x consumers are unaffected too.

  No wire-format change: the serialized descriptors are byte-identical, and the
  golden fixtures pass unchanged in both languages. The regenerated output is the
  version stamp in each `_pb2.py`, the `protoc` header comment in each `.ts` file,
  and a `.pyi` stub widening where protoc now types optional scalar parameters as
  `_Optional[bool]` rather than bare `bool`.

## 1.4.0

### Minor Changes

- 792fed0: Support protobuf 7.x in the Python package.

  The published gencode is stamped 6.31.1, and protobuf's only compatibility rule
  is that the runtime must not be older than the gencode stamp - Python gencode
  back to 3.20 is supported through at least 8.x. The `protobuf<7` cap was
  therefore the only thing keeping 7.x users out, not any real incompatibility, so
  it moves to `<8` (matching the cap `googleapis-common-protos` already declares).
  One wheel now serves both 6.x consumers such as Home Assistant, which constrains
  `protobuf==6.33.6`, and 7.x consumers.

  CI gains a `python-runtime` matrix that imports every generated module and runs
  the golden fixture suite against the declared floor (6.32.0), Home Assistant's
  pin (6.33.6), and the newest major (7.x). No generated code or wire format
  changed.

## 1.3.1

### Patch Changes

- 2828d5f: Add `tesla.proto.energy_device.v1.SignatureType` and `Tag` to
  `proto/energy_device/signed_message.proto`, alongside the `SignatureData` and
  `RoutableMessage` messages that reference them. The signed transport wrapper published in
  1.3.0 shipped incomplete: `SignatureData`/`RoutableMessage` already referenced these enums,
  so a consumer of that release had no way to actually build or interpret a signature block.
  This completes it.

  Wire-compatible addition: two new enums, nothing renamed or renumbered.

## 1.3.0

### Minor Changes

- a61d4c6: Add `tesla.proto.energy_device.v1.Message`, the RSA-signed transport wrapper for the
  Powerwall local v1r endpoint: `Destination`, `KeyIdentity`, `RsaSignatureData`,
  `SignatureData`, `RoutableMessage`, `Tail`, and the outer `Message`, in a new
  `proto/energy_device/signed_message.proto`. `RoutableMessage.protobuf_message_as_bytes`
  carries the domain routing envelope (`MessageEnvelope`, already in `transport.proto`) as
  opaque bytes, so this only adds the signing layer - none of the domain schema is
  duplicated.

  Wire-compatible addition: brand-new file, nothing renamed or renumbered.

## 1.2.0

### Minor Changes

- fb7d9b3: Add a batch of wire-compatible schema additions to `car_server.proto`, `vehicle.proto`, and
  `vcsec.proto`:

  - `CarServer.DogModeLiveActivityData` and its nested `DisabledReason` enum: a live Dog Mode
    status push (disabled reason, cabin temperature, fault state, temperature unit, battery level).
  - A chunked mobile-upload pipeline: `MobileImageUploadParams`, `MobileUploadParams`,
    `PrepareMobileUploadAction`/`PrepareMobileUploadResponse`,
    `PutMobileUploadChunkAction`/`PutMobileUploadChunkResponse`, with the two response types wired
    into `CarServer.Response.response_msg` at tags 31 and 32.
  - Center-display brightness as a subscribable vehicle-data field: `CarServer.DisplayState`
    (`vehicle.proto`), `DisplayStateAction`, `GetDisplayState`, plus the corresponding
    `VehicleData.display_state`, `VehicleDataAck.display_state_timestamp`,
    `VehicleDataSubscription.display_state_max_update_rate_ms`, and
    `GetVehicleData.getDisplayState` wiring.
  - `VCSEC.RKEAction_E.RKE_ACTION_UNLOCK_UNRESTRICTED_CLOSURES`.
  - Single-field additions: `ChargeState.PowershareType.PowershareTypePowerwall`,
    `ClosuresState.cruise_speed_limit_mph`, `VehicleState.deck_lights_allowed`,
    `VehicleConfig.supports_dynamic_environments`, `VehicleDetailState.is_fsd_v14_or_above`.

  Wire-compatible: nothing is renamed or renumbered, and every new field/message carries a
  `TESLEMETRY-EXT` marker.

- 5eedaa9: Add 10 new streamable telemetry fields to `telemetry.Field`
  (`vehicle_data.proto`): `GpsAccuracyMeters`, `LifetimeEnergyChargedKwh`,
  `BrickSocMinPercent`, `NominalFullPackEnergyKwh`, `GradeEstimatePercent`,
  `MaxSpeedToReachDestinationMph`, `SoftwareUpdateAvailable`,
  `SoftwareUpdateInProgress`, `RemoteStartActive`, `SemiCruiseSpeedLimitMph`
  (tags 260-269).

  Wire-compatible: additive only, nothing renamed or renumbered.

## 1.1.0

### Minor Changes

- f1535e2: Add `CarServer.NavigationSuperchargerRequest.id` (`int64`, tag 1), the supercharger
  location the request navigates to - the same identifier `CarServer.Superchargers.id`
  carries in a `GetNearbyChargingSites` reply. Tag 1 was previously reserved and unmodelled,
  so a supercharger-nav command could only carry a trip order with no supercharger named.

  Wire-compatible addition: nothing is renamed or renumbered, and `"order"` stays reserved.
  Callers that want the vehicle to act on the request must set `id` alongside
  `remoteNavTripOrder` (TypeScript) / `remote_nav_trip_order` (Python).

## 1.0.0

### Major Changes

- 7dec33b: **Wire-format break:** `CarServer.NavigationSuperchargerRequest.order` was published at
  tag 1 as `int32`. Live-vehicle and recovered-schema evidence both show tag 1 actually
  carries an unrelated value and the trip-order enum lives at tag 2. Tag 1 is now
  `reserved`; the field is renamed to `remote_nav_trip_order` (a new
  `RemoteNavTripOrder` enum, matching the sibling `NavigationRequest` /
  `NavigationGpsRequest` / `NavigationGpsDestinationRequest` messages) and moved to tag 2.

  Any consumer building a supercharger-nav command with the old `order` field was sending
  a malformed request that the vehicle silently ignored. Callers must switch to
  `remoteNavTripOrder` (TypeScript) / `remote_nav_trip_order` (Python).

### Minor Changes

- 1df2336: Model `CarServer.GetVehicleData`'s four reserved request selectors -
  `getLegacyVehicleState` (5), `getVehicleConfig` (6), `getSohState` (12), and
  `getVehicleDetailState` (13) - and add leaf fields to already-published
  vehicle-state messages: `SohState`'s test-phase and test-end-mode wrappers,
  `SuspensionState`'s `allowed_levels`/`level_options` (new
  `SuspensionLevelObj` in `common.proto`), and `VehicleImage`'s `image_type`.

## 0.6.0

### Minor Changes

- b755065: Add a new `charging` module modelling `com.tesla.proto.charging.v1`, the EV charge-session energy metering and per-session billing schema (`Energy`, `StemInfo`, `StemEventInfo`, `ChargeSessionTimeSeries`, `StemUi`, `StemBilling`).
- 505c980: Model field-level definitions for the `energy_device.v1` local-Powerwall/Wall-Connector/PV-inverter API - Wall Connector (`WCAPI`), TEG/Powerwall (`TEGAPI`, controllable-device-program scheduling, OCPP/CSMS config), PV inverter (`PVIAPI`, new `pvi_api.proto`), CT metering (`NeurioMeterAPI`, new `neurio_meter_api.proto`), local login (`LocalAuthAPI`, new `local_auth_api.proto`), site device pairing (`EnergySiteNetAPI`, `IntraSiteAPI`, new `intra_site_api.proto`), on-gateway file storage (`FileStoreAPI`, new `filestore_api.proto`), and the GraphQL-over-protobuf sub-channel (`GraphQLAPI`, new `graphql_api.proto`) - completing each service's request/response bodies and its `*Messages` oneof envelope.
- 15b0027: Model the remaining autonomy/autopilot surface and vehicle lighting fields: `UniversalMessage.Domain.DOMAIN_AUTOPILOT`, VCSEC's `AutonomyCommand` (wrapping the `PullOverCommand` trigger, wired into `UnsignedMessage` field 66), and `VehicleState.deck_lights_on` / `hazards_on`.
- a777637: Model `DashcamSei.SeiMetadata`, the per-frame vehicle telemetry (speed, gear, steering, GPS, heading, linear acceleration, autopilot state, blinkers, brake) carried in the SEI payload embedded in TeslaCam/Sentry/live-camera video.
- 82f65ef: Add `VehicleData.unknown` (field 18), an opaque `bytes` payload observed on live `vehicleDataSubscription` pushes but not yet decoded.

### Patch Changes

- cf9d721: Regenerate `packages/typescript/src/charging/charging.ts` from `proto/charging/charging.proto` to drop a stale comment block that was removed from the proto source but never re-synced into the generated output.

## 0.5.0

### Minor Changes

- a3d8ee5: Model the `Response.response_msg` field 12 reply payload, `GetRateTariffResponse`, mirroring the tariff document already declared for `SetRateTariffRequest` (VehicleAction tag 55). Consumers decoding this reply previously saw only `{actionStatus}` and silently dropped the payload.

### Patch Changes

- ac30f3d: Fix cross-file imports left unrewritten in generated `.pyi` stubs (`car_server_pb2.pyi`, `universal_message_pb2.pyi`, `vcsec_pb2.pyi`, `vehicle_pb2.pyi`, and three `energy_device` stubs). protoc's pyi generator aliases same-package imports differently than its `.py` generator (`_foo_pb2` vs `foo__pb2`), so protoletariat's import rewriter - which matches whole import statements including the alias - left the pyi side as a bare top-level `import foo_pb2 as _foo_pb2` instead of the package-relative form the `.py` sibling already got. Static type checkers (e.g. pyright) can't resolve those imports, breaking type information for any field typed through them. `scripts/generate.sh` now runs a small `scripts/fix_pyi_imports.py` pass after `protol` to patch the remaining bare pyi imports.

## 0.4.0

### Minor Changes

- 31a7151: Add `BuckleStatusSNA` (value 4) to `BuckleStatus` in `vehicle_data.proto`. Consumers can now distinguish a signal-not-available buckle state from `Unknown`.
- 45cbf6b: Add the remaining `Response.response_msg` reply payloads - `StreamMessage`, `VehicleDataSubscriptionResponse`, `VitalsSubscriptionResponse`, `PiiKeyResponse`, `PseudonymSyncResponse`, `NavigationRouteResponse`, `GetManagedChargingSitesResponse`, `AddManagedChargingSiteResponse`, `GetMessagesResponse`, `GetLocalProfilesResponse`, `KeysInfoResponse` and `BandwidthTestResponse`. Consumers decoding these replies previously saw only `{actionStatus}` and silently dropped the payload.

### Patch Changes

- b6ce3b2: Mark `Response.response_msg` fields 12, 17 and 19 as `reserved` with a reason (deferred namespace-publish decision; app-only `centerdisplay.server` / `webrtc_comms` payloads). No wire changes - this documents fields that were already absent from the oneof.

## 0.3.0

### Minor Changes

- ef034d4: Add `GetChargeOnSolarFeatureResponse` to `Response.response_msg` (field 15) in `car_server.proto`. Consumers can now decode `enabled`, `lowerChargeLimit`, and `upperChargeLimit` from a Charge On Solar config read instead of only `{result: true}`.

## 0.2.0

### Minor Changes

- 2fa5928: Add `DetailedChargeStateCalibrating` to telemetry `DetailedChargeStateValue`, sourced from Tesla's public `vehicle-command` repository. Reserve the numbers for three expected-but-unconfirmed Powershare telemetry values (not yet observed, no generated members added for them).

## 0.1.2

### Patch Changes

- d65c4cd: Fix release workflow npm publish attestation configuration.

## 0.1.1

### Patch Changes

- d7b1d83: Clarify wording in docs and proto comments. No wire format, symbol, or logic changes.
