---
"@teslemetry/tesla-protocol": patch
---

Add the `ManualPreconditioningAction` vehicle action (`VehicleAction` 731429) for starting and stopping battery preconditioning, the `ChargeState` fields `manual_precon_supported`, `manual_precon_allowed`, `manual_precon_status` and `ecosystem_charge_mode` with their `ManualPreconStatus` and `EcosystemChargeMode` enums, and energy device additions: the `AUTHORIZATION_ROLE_INSTALLER` and `AUTHORIZED_CLIENT_TYPE_INSTALLER_APP` enum values, BLE key pairing messages (`MessageEnvelope.ble`, `BLEMessages`, NFC/SPAKE2+/resume steps, `SPAKE2PlusProfile`), `EnergySiteNetDevice`/`EnergySiteNetRecentlyAddedDevice` device types, TEG delay-battery-mating messages and Ausgrid/Endeavour/Essential CSIP certificate types, Supercharger ECU firmware update trigger and `PayterPostStatus.is_connected`, and Wall Connector `discharging_energy` and smart-charging command response fields. All additions are UNCONFIRMED until seen on a live vehicle or device.
