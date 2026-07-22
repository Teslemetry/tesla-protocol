# @teslemetry/tesla-protocol

TypeScript protobuf types for Tesla's vehicle-command, fleet-telemetry and
energy device protocols, generated with [ts-proto](https://github.com/stephenh/ts-proto).

```sh
npm install @teslemetry/tesla-protocol
```

Every proto module is a subpath export mirroring the `proto/` tree:

```ts
import { Action } from "@teslemetry/tesla-protocol/command/car_server";
import { Payload } from "@teslemetry/tesla-protocol/telemetry/vehicle_data";
```

See the [repository README](https://github.com/Teslemetry/tesla-protocol) for
provenance (which definitions track Tesla's upstream repos and which are
Teslemetry extensions from our own observations and contributions from the
community) and the release model.
