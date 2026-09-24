---
"@teslemetry/tesla-protocol": major
---

**Breaking corrections to published `command` content.**

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
