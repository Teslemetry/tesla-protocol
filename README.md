# tesla-protocol

Teslemetry-maintained protobuf definitions for Tesla's vehicle-command,
fleet-telemetry and energy device protocols - the single source of truth
behind two packages published in lockstep:

| Package | Registry | Install |
| --- | --- | --- |
| [`@teslemetry/tesla-protocol`](https://www.npmjs.com/package/@teslemetry/tesla-protocol) | npm | `npm install @teslemetry/tesla-protocol` |
| [`tesla-protocol`](https://pypi.org/project/tesla-protocol/) | PyPI | `pip install tesla-protocol` |

The command and telemetry protos **track Tesla's upstream repositories**
([`teslamotors/vehicle-command`](https://github.com/teslamotors/vehicle-command),
[`teslamotors/fleet-telemetry`](https://github.com/teslamotors/fleet-telemetry))
as the primary source, with Teslemetry extensions - from our own observations
and contributions from the community - layered on top and marked
`TESLEMETRY-EXT`. See
**[PROVENANCE.md](PROVENANCE.md)** for the exact boundary, the upstream pin
(`upstream.json`) and the CI gate that keeps coverage of upstream complete.

## Usage

TypeScript ([ts-proto](https://github.com/stephenh/ts-proto) output, ESM + CJS,
one subpath per proto module):

```ts
import { Action } from "@teslemetry/tesla-protocol/command/car_server";
import { Payload } from "@teslemetry/tesla-protocol/telemetry/vehicle_data";
```

Python (`_pb2` modules with `.pyi` stubs, `py.typed`):

```python
from tesla_protocol.command import car_server_pb2
from tesla_protocol.telemetry import vehicle_data_pb2
```

## Layout

```
proto/                  source of truth (the only hand-edited artifacts)
├── command/            vehicle-command protos + session.proto
├── telemetry/          fleet-telemetry protos (upstream verbatim)
├── energy_device/      TEG gateway local-API protos
├── energy_command/     energy command identifiers
├── teslapower/         Powerwall local-API proto
└── charging/           EV charge-session metering/billing ("STEM") protos
packages/typescript/    @teslemetry/tesla-protocol (generated, committed)
packages/python/        tesla-protocol (generated, committed)
```

## Contributing

1. Edit `proto/`, then regenerate both packages: `pnpm install && pnpm generate`
2. Add a changeset: `pnpm changeset` (see `.changeset/README.md` for bump rules)
3. Open a PR. CI enforces: committed codegen freshness, `buf lint`,
   `buf breaking`, and the upstream coverage gate.

Releases: merging a PR with changesets makes the release workflow open a
single Version PR that bumps `package.json` and `pyproject.toml` together;
merging that publishes both packages via OIDC trusted publishing (npm
provenance + PyPI attestations, no stored tokens).

## License

[Apache-2.0](LICENSE), matching the upstream Tesla repositories this project
redistributes - see [NOTICE](NOTICE).
