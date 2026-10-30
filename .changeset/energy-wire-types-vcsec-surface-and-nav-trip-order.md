---
"@teslemetry/tesla-protocol": major
---

Correct `energy_device` wire types, enum types, oneofs and names, add the WMSA, SM, energy telemetry and energy command envelope types, model a large part of the VCSEC surface, retype the navigation trip order, and reserve obsolete vehicle-data tags.

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

| Message | Field | Before | After |
|---|---|---|---|
| `AlertLog` | `data` (1) | `uint64` | `fixed64` |
| `AlertMatrix` | `data` (1) | `uint64` | `fixed64` |
| `GridComplianceStatus` | `qualifying_time_remaining_s` (2) | `google.protobuf.FloatValue` | `google.protobuf.UInt32Value` |
| `WCAPIGetConfigResponse` | `charge_schedule` (5) | `WCChargeScheduleConfig` | `WCChargeScheduleConfigStatus` |
| `ControllableDeviceProgram_Schedule` | `start` (1), `end` (2), `expiry` (3) | `google.protobuf.Timestamp` | `ControllableDeviceProgram_Schedule_Boundary` |

**Breaking: `WCLifetimeStats` is renumbered.** Its ten fields move from tags 3-12 to tags 1-10 in the same order (`uptime_s` = 1 through `charging_energy` = 10). Tags 1 and 2 are no longer reserved.

**Breaking: `int32` fields now have enum types.** The tags and the wire bytes are the same. Generated code uses the enum types, and JSON output shows enum names instead of numbers:

| Message | Field | New type |
|---|---|---|
| `TEGAPIRegisterResponse` | `failure` (1) | `RegistrationFailure` |
| `WCAPIRegisterCommercialResponse` | `failure` (1) | `RegistrationFailure` |
| `LocalAuthAPILoginRequest` | `participant` (1) | `LocalParticipant` |
| `NeurioCTConfig` | `location` (1) | `MeterCTLocation` |
| `SuperchargerAPIGetDcMetersCommissioningResponse` | `error` (2) | `DcMeterCommissioningError` |
| `CarServer.NavigationRequest` | `order` (2) | `RemoteNavTripOrder_E` |

**Breaking: the navigation trip order enum is replaced.** The three nested `RemoteNavTripOrder` enums (`REMOTE_NAV_TRIP_ORDER_UNKNOWN = 0`, `REPLACE = 1`, `PREPEND = 2`, `APPEND = 3`) in `NavigationSuperchargerRequest`, `NavigationGpsRequest` and `NavigationGpsDestinationRequest` are deleted. The new top-level `CarServer.RemoteNavTripOrder_E` has `RemoteNavTripOrderReplace = 0`, `RemoteNavTripOrderPrepend = 1` and `RemoteNavTripOrderAppend = 2`, and types `NavigationRequest.order`, `NavigationSuperchargerRequest.remote_nav_trip_order`, `NavigationGpsRequest.order` and `NavigationGpsDestinationRequest.order`. The numbers change: a sender that used 1 for replace must now send 0.

**Breaking: fields move into oneofs.** The tags and the wire bytes are the same. Generated code exposes them through the oneof:

| Message | Oneof |
|---|---|
| `AcceptedPackage` | `sideloading_method` |
| `CommonMessages` | `message` (now includes `error_response` = 1) |
| `FileStoreAPIFile` | `content` |
| `PVMeterInterface` | `meter_interface` |
| `WCMeterInterface` | `meter_interface` |
| `TEGAPIDispatchBatteryPowerRequest` | `command` |
| `TEGAPIEnsureCertificateRequest` | `certificate_type` |
| `WCDryContactConfig` | `control_behavior` |
| `WCLoadSharingConfig` | `network_limit` |
| `WCLoadSharingSettings` | `network_limit` |
| `DeviceInfo` | `device_sub_type` |

**Breaking: names change.** The tags and the wire bytes are the same:

| Symbol | Before | After |
|---|---|---|
| `BackupEvent` field 3 | `sheduling_info` | `scheduling_info` |
| `EcuFirmwareUpdateInProgress` field 1 | `default` | `node_progresses` |
| `EcuFirmwareUpdateResult` field 2 | `default` | `ecu_update_results` |
