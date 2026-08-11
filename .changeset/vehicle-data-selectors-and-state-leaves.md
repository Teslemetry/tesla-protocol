---
"@teslemetry/tesla-protocol": minor
---

Model `CarServer.GetVehicleData`'s four reserved request selectors -
`getLegacyVehicleState` (5), `getVehicleConfig` (6), `getSohState` (12), and
`getVehicleDetailState` (13) - and add high-confidence leaf fields to
already-published vehicle-state messages: `SohState`'s test-phase and
test-end-mode wrappers, `SuspensionState`'s `allowed_levels`/`level_options`
(new `SuspensionLevelObj` in `common.proto`), and `VehicleImage`'s
`image_type`, based on our own observations and contributions from the
community.
