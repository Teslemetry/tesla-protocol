---
"@teslemetry/tesla-protocol": minor
---

Add the remaining `Response.response_msg` reply payloads - `StreamMessage`, `VehicleDataSubscriptionResponse`, `VitalsSubscriptionResponse`, `PiiKeyResponse`, `PseudonymSyncResponse`, `NavigationRouteResponse`, `GetManagedChargingSitesResponse`, `AddManagedChargingSiteResponse`, `GetMessagesResponse`, `GetLocalProfilesResponse`, `KeysInfoResponse` and `BandwidthTestResponse` - based on our own observations and contributions from the community. Consumers decoding these replies previously saw only `{actionStatus}` and silently dropped the payload.
