---
"@teslemetry/tesla-protocol": minor
---

Add `BuckleStatusSNA` (value 4) to `BuckleStatus` in `vehicle_data.proto`, based on our own observations and contributions from the community. Consumers can now distinguish a signal-not-available buckle state from `Unknown`.
