---
"@teslemetry/tesla-protocol": minor
---

Add 10 new streamable telemetry fields to `telemetry.Field`
(`vehicle_data.proto`): `GpsAccuracyMeters`, `LifetimeEnergyChargedKwh`,
`BrickSocMinPercent`, `NominalFullPackEnergyKwh`, `GradeEstimatePercent`,
`MaxSpeedToReachDestinationMph`, `SoftwareUpdateAvailable`,
`SoftwareUpdateInProgress`, `RemoteStartActive`, `SemiCruiseSpeedLimitMph`
(tags 260-269).

Wire-compatible: additive only, nothing renamed or renumbered.
