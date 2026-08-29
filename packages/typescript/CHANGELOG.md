# @teslemetry/tesla-protocol

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
