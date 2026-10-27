---
"@teslemetry/tesla-protocol": patch
---

Update the `telemetry` Semi streaming fields 272-278 to the final upstream layout. Releases 3.0.2 to 4.0.0 carried a draft layout of these fields.

| `Field` tag | Before | After |
|---|---|---|
| 272 | `AccRail` | `AccessoryRail` |
| 273-275 | unchanged | unchanged |
| 276 | `CruiseState` | `LifetimeDcChargeEnergyKwh` |
| 277 | `LifetimeDcChargeEnergyKwh` | `SemiVehicleMassKg` |
| 278 | `VehicleMassKg` | - (deleted) |

- `CruiseStateValue` and `Value.cruise_state_value` (56) are deleted.
- `AutomaticEmergencyBrakingStateValue` (Unknown, Unavailable, Standby, Enabled, Standstill) and `Value.automatic_emergency_braking_state_value` (60) are added.
- `CarTypeSemiTruckV2` (7) and `CarTypeCybercab` (8), and `PowerTransferStatusValue`, are unchanged.

Code that used `AccRail`, `CruiseState`, `VehicleMassKg` or `CruiseStateValue` must move to the new names. Code that matched tags 276 or 277 by number now gets a different field.
