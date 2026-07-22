# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- `proto/` is the only hand-edited code; everything under `packages/typescript/src` and `packages/python/tesla_protocol/*/` is generated. Regenerate with `pnpm install && pnpm generate`; CI fails on any diff, so never edit generated files directly.
- Provenance rules (upstream-tracked vs Teslemetry source-of-record, `TESLEMETRY-EXT` markers, upstream-wins-names policy) live in `PROVENANCE.md`. The enforcement tool is `scripts/upstream_coverage.py`; run it in `--mode pinned` before pushing proto changes.
- Release model: Changesets tracks only the npm package; `scripts/sync-python-version.mjs` copies the version into `pyproject.toml` during `pnpm run version`. Bump rules are in `.changeset/README.md`. Never use changesets prerelease mode (breaks PEP 440).
- Sharp edge: protoletariat is installed with `pip --no-deps` (see `scripts/generate.sh`) because it over-pins `protobuf<6` while only parsing descriptor sets; its `--exclude-imports-glob` patterns match dependency names WITHOUT the `.proto` suffix.
- The codegen toolchain is fully pinned (`scripts/requirements.txt`, ts-proto in root `package.json`). Changing any pin changes generated output and is a coordinated, changeset-worthy change.
- `CarServer.Response.response_msg` (`proto/command/car_server.proto`) models the full server reply surface except fields 12, 17 and 19, which are `reserved` with a reason comment (12: `GetRateTariffResponse`, blocked on a namespace-publish decision - its only field is a `com.tesla.proto.energy.rate_tariff.v1` type, an app-only namespace; 17/19: `centerdisplay.server`/`webrtc_comms`, app-only namespaces, intentionally excluded). `scripts/check_reply_coverage.py` (run in CI) fails if any field in its known-field set is neither modelled in the oneof nor `reserved` with a comment - before adding a new reply oneof field, check whether its payload type pulls in an app-only namespace first, and either model it or add it to `KNOWN_REPLY_FIELDS` as a reserved entry.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
