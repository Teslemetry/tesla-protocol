---
"@teslemetry/tesla-protocol": minor
---

Model the `Response.response_msg` field 12 reply payload, `GetRateTariffResponse`, mirroring the tariff document already declared for `SetRateTariffRequest` (VehicleAction tag 55) - based on our own observations and contributions from the community. Consumers decoding this reply previously saw only `{actionStatus}` and silently dropped the payload.
