---
"@teslemetry/tesla-protocol": major
---

**Wire-format break:** `CarServer.NavigationSuperchargerRequest.order` was published at
tag 1 as `int32`. Live-vehicle and recovered-schema evidence both show tag 1 actually
carries an unrelated value and the trip-order enum lives at tag 2. Tag 1 is now
`reserved`; the field is renamed to `remote_nav_trip_order` (a new
`RemoteNavTripOrder` enum, matching the sibling `NavigationRequest` /
`NavigationGpsRequest` / `NavigationGpsDestinationRequest` messages) and moved to tag 2.

Any consumer building a supercharger-nav command with the old `order` field was sending
a malformed request that the vehicle silently ignored. Callers must switch to
`remoteNavTripOrder` (TypeScript) / `remote_nav_trip_order` (Python).
