---
"@teslemetry/tesla-protocol": minor
---

Model the remaining autonomy/autopilot surface and vehicle lighting fields observed in the current app: `UniversalMessage.Domain.DOMAIN_AUTOPILOT`, VCSEC's `AutonomyCommand` (wrapping the `PullOverCommand` trigger, wired into `UnsignedMessage` field 66), and `VehicleState.deck_lights_on` / `hazards_on` - based on our own observations and contributions from the community.
