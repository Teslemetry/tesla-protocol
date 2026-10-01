---
"@teslemetry/tesla-protocol": patch
---

Add telemetry `Field` values `AccRail` (272), `PowerTransferStatus` (273), `AutomaticEmergencyBrakingState` (274), `RollingResistanceCoefficient` (275), `CruiseState` (276), `LifetimeDcChargeEnergyKwh` (277) and `VehicleMassKg` (278, Semi only), plus the `CruiseStateValue` and `PowerTransferStatusValue` enums carried in the `Value` oneof as `cruise_state_value` (56) and `power_transfer_status_value` (57).
