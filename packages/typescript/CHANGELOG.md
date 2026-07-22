# @teslemetry/tesla-protocol

## 0.5.0

### Minor Changes

- a3d8ee5: Model the `Response.response_msg` field 12 reply payload, `GetRateTariffResponse`, mirroring the tariff document already declared for `SetRateTariffRequest` (VehicleAction tag 55) - based on our own observations and contributions from the community. Consumers decoding this reply previously saw only `{actionStatus}` and silently dropped the payload.

### Patch Changes

- ac30f3d: Fix cross-file imports left unrewritten in generated `.pyi` stubs (`car_server_pb2.pyi`, `universal_message_pb2.pyi`, `vcsec_pb2.pyi`, `vehicle_pb2.pyi`, and three `energy_device` stubs). protoc's pyi generator aliases same-package imports differently than its `.py` generator (`_foo_pb2` vs `foo__pb2`), so protoletariat's import rewriter - which matches whole import statements including the alias - left the pyi side as a bare top-level `import foo_pb2 as _foo_pb2` instead of the package-relative form the `.py` sibling already got. Static type checkers (e.g. pyright) can't resolve those imports, breaking type information for any field typed through them. `scripts/generate.sh` now runs a small `scripts/fix_pyi_imports.py` pass after `protol` to patch the remaining bare pyi imports.

## 0.4.0

### Minor Changes

- 31a7151: Add `BuckleStatusSNA` (value 4) to `BuckleStatus` in `vehicle_data.proto`, based on our own observations and contributions from the community. Consumers can now distinguish a signal-not-available buckle state from `Unknown`.
- 45cbf6b: Add the remaining `Response.response_msg` reply payloads - `StreamMessage`, `VehicleDataSubscriptionResponse`, `VitalsSubscriptionResponse`, `PiiKeyResponse`, `PseudonymSyncResponse`, `NavigationRouteResponse`, `GetManagedChargingSitesResponse`, `AddManagedChargingSiteResponse`, `GetMessagesResponse`, `GetLocalProfilesResponse`, `KeysInfoResponse` and `BandwidthTestResponse` - based on our own observations and contributions from the community. Consumers decoding these replies previously saw only `{actionStatus}` and silently dropped the payload.

### Patch Changes

- b6ce3b2: Mark `Response.response_msg` fields 12, 17 and 19 as `reserved` with a reason (deferred namespace-publish decision; app-only `centerdisplay.server` / `webrtc_comms` payloads). No wire changes - this documents fields that were already absent from the oneof.

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
