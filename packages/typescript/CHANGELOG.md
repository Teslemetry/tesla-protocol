# @teslemetry/tesla-protocol

## 0.3.0

### Minor Changes

- ef034d4: Add `GetChargeOnSolarFeatureResponse` to `Response.response_msg` (field 15) in `car_server.proto`, based on our own observations and contributions from the community. Consumers can now decode `enabled`, `lowerChargeLimit`, and `upperChargeLimit` from a Charge On Solar config read instead of only `{result: true}`.

## 0.2.0

### Minor Changes

- 2fa5928: Add `DetailedChargeStateCalibrating` to telemetry `DetailedChargeStateValue`, sourced from Tesla's public `vehicle-command` repository. Reserve the numbers for three expected-but-unconfirmed Powershare telemetry values (not yet observed, no generated members added for them).

## 0.1.2

### Patch Changes

- d65c4cd: Fix release workflow provenance configuration.

## 0.1.1

### Patch Changes

- d7b1d83: Clarify provenance wording in docs and proto comments. No wire format, symbol, or logic changes.
