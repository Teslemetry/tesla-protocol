---
"@teslemetry/tesla-protocol": minor
---

Add a batch of wire-compatible schema additions to `car_server.proto`, `vehicle.proto`, and
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
