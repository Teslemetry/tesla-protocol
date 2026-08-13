# tesla-protocol

Teslemetry-maintained protobuf definitions for Tesla's vehicle-command,
fleet-telemetry and energy device protocols - the single source of truth
behind two packages published in lockstep:

| Package | Registry | Install |
| --- | --- | --- |
| [`@teslemetry/tesla-protocol`](https://www.npmjs.com/package/@teslemetry/tesla-protocol) | npm | `npm install @teslemetry/tesla-protocol` |
| [`tesla-protocol`](https://pypi.org/project/tesla-protocol/) | PyPI | `pip install tesla-protocol` |

The command and telemetry protos track Tesla's public repositories
([`teslamotors/vehicle-command`](https://github.com/teslamotors/vehicle-command),
[`teslamotors/fleet-telemetry`](https://github.com/teslamotors/fleet-telemetry)).
`upstream.json` pins the exact commit this repo is reconciled against, and
`scripts/upstream_coverage.py` is the CI gate that keeps coverage complete.

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
├── charging/           EV charge-session metering/billing ("STEM") protos
└── dashcam/            TeslaCam/Sentry video SEI metadata proto
packages/typescript/    @teslemetry/tesla-protocol (generated, committed)
packages/python/        tesla-protocol (generated, committed)
```

## Contributing

1. Edit `proto/`, then regenerate both packages: `pnpm install && pnpm generate`
2. Regenerate the surface catalog: `.venv/bin/python scripts/build_catalog.py`
   (see `catalog/SUMMARY.md` for the current inventory; full detail in
   `catalog/catalog.json`)
3. Add a changeset: `pnpm changeset` (see `.changeset/README.md` for bump rules)
4. Open a PR. CI enforces: committed codegen freshness, `buf lint`,
   `buf breaking`, the upstream coverage gate, and catalog freshness/group-registration
   consistency.

Releases: merging a PR with changesets makes the release workflow open a
single Version PR that bumps `package.json` and `pyproject.toml` together;
merging that publishes both packages via OIDC trusted publishing (npm and
PyPI attestations, no stored tokens).

Both publish jobs run under the `production` GitHub environment, which gates
on a required reviewer approving the exact SHA that the `ci` job (reused from
`ci.yml`) has already validated - approval cannot happen before that check is
green because both jobs declare `needs: ci`/`needs: [ci, release]`. GitHub
only asks for approval once per workflow run even though two jobs reference
`production`.

If a publish run is interrupted (cancelled, runner failure, transient
network error), re-running the failed job(s) from the Actions UI is the
recovery path - no manual registry cleanup is needed:

- **npm leg**: `changeset publish` checks the npm registry before publishing
  each package, so re-running `release` after a partial or already-completed
  npm publish is a no-op for versions that already landed. Re-running before
  the Version PR is merged just updates that PR in place.
- **PyPI leg**: `pypa/gh-action-pypi-publish` runs with `skip-existing: true`,
  so re-running `publish-pypi` after a version already uploaded skips it
  instead of failing on a duplicate-file error.

## License

[Apache-2.0](LICENSE), matching the upstream Tesla repositories this project
redistributes - see [NOTICE](NOTICE).
