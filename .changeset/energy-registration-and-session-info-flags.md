---
"@teslemetry/tesla-protocol": minor
---

Add energy-device registration types and the `Signatures.SessionInfoFlags` enum. `energy_device` gains the `MarketType`, `RegistrationFailure`, `SiteRegistrationStatus` and `BranchCircuitDeviceType` enums; the `TEGDeviceType` values `TULIP`, `DYNAMO` and `SMC_SUPERCHARGER`, the `iPMDeviceType` value `MEGACHARGER` and the `RegistrationDeviceType` value `OPTIMUS_CHARGER`; the fields `RegistrationRequest.market_type`, `RegistrationRequest.potential_site_uuid` and `DeviceDetail.teg_device_type`; and the messages `DeviceInfo`, `AssetSiteDetailsRequest`, `AssetSiteUuidOfDeviceRequest`, `CustomerRegistrationInfo`, `DeactivateDeviceResponse`, `SiteInfo`, `RegistrationRequestWithPartDetails` and `WCCommercialRegistrationRequestWithPartDetails`. `command` gains `Signatures.SessionInfoFlags`, which names the bit positions in `SessionInfo.flags`. All additions are wire-compatible.
