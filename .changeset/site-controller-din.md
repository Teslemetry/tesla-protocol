---
"@teslemetry/tesla-protocol": minor
---

Add `string din = 1;` to `SiteController` (`AddManagedChargingSiteRequest` -> `ManagedChargingSite` -> `ManagerType` -> `SiteController`): the message was previously empty, so every managed charging site added through this library omits the gateway DIN the vehicle uses to match its Powerwall.
