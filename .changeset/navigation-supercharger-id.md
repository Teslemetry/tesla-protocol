---
"@teslemetry/tesla-protocol": minor
---

Add `CarServer.NavigationSuperchargerRequest.id` (`int64`, tag 1), the supercharger
location the request navigates to - the same identifier `CarServer.Superchargers.id`
carries in a `GetNearbyChargingSites` reply. Tag 1 was previously reserved and unmodelled,
so a supercharger-nav command could only carry a trip order with no supercharger named.

Wire-compatible addition: nothing is renamed or renumbered, and `"order"` stays reserved.
Callers that want the vehicle to act on the request must set `id` alongside
`remoteNavTripOrder` (TypeScript) / `remote_nav_trip_order` (Python).
