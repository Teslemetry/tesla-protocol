---
"@teslemetry/tesla-protocol": minor
---

Type `ControlEventSchedulingInfo.priority` as a decimal string in TypeScript, so a `uint64` priority above `Number.MAX_SAFE_INTEGER` decodes without loss.

A max-backup event is scheduled at priority `2^64 - 1`. As a `number`, encoding that value threw `invalid uint64`, and decoding any `MessageEnvelope` that carried it threw `Value is larger than Number.MAX_SAFE_INTEGER`, which lost the whole `TEGAPIGetBackupEventsResponse`.

**Breaking (TypeScript only): `ControlEventSchedulingInfo.priority` is now `string`, not `number`.** Pass and read it as a decimal string, for example `"18446744073709551615"`. JSON output already used a string for this field. The wire bytes do not change, and the Python API is unchanged.

Added golden fixture `fixtures/golden/energy_v1r_envelopes.json`: the energy_device `MessageEnvelope` requests for the Powerwall local v1r endpoint, and a `get_backup_events` reply carrying priority `2^64 - 1`, checked by both the TypeScript and Python tests.
