# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- `proto/` is the only hand-edited code; everything under `packages/typescript/src` and `packages/python/tesla_protocol/*/` is generated. Regenerate with `pnpm install && pnpm generate`; CI fails on any diff, so never edit generated files directly.
- Provenance rules (upstream-tracked vs Teslemetry source-of-record, `TESLEMETRY-EXT` markers, upstream-wins-names policy) live in `PROVENANCE.md`. The enforcement tool is `scripts/upstream_coverage.py`; run it in `--mode pinned` before pushing proto changes.
- Release model: Changesets tracks only the npm package; `scripts/sync-python-version.mjs` copies the version into `pyproject.toml` during `pnpm run version`. Bump rules are in `.changeset/README.md`. Never use changesets prerelease mode (breaks PEP 440).
- Sharp edge: protoletariat is installed with `pip --no-deps` (see `scripts/generate.sh`) because it over-pins `protobuf<6` while only parsing descriptor sets; its `--exclude-imports-glob` patterns match dependency names WITHOUT the `.proto` suffix.
- The codegen toolchain is fully pinned (`scripts/requirements.txt`, ts-proto in root `package.json`). Changing any pin changes generated output and is a coordinated, changeset-worthy change.
- `CarServer.Response.response_msg` (`proto/command/car_server.proto`) models the full server reply surface except fields 17 and 19, which are `reserved` with a reason comment (`centerdisplay.server`/`webrtc_comms` replies, app-only namespaces, intentionally excluded). Field 12 (`GetRateTariffResponse`) is modelled, mirroring the tariff document already declared for `SetRateTariffRequest` (tag 55). `scripts/check_reply_coverage.py` (run in CI) fails if any field in its known-field set is neither modelled in the oneof nor `reserved` with a comment - before adding a new reply oneof field, check whether its payload type pulls in an app-only namespace first, and either model it or add it to `KNOWN_REPLY_FIELDS` as a reserved entry.
- Un-reserving a field to model it (as field 12 above did) trips buf's `RESERVED_MESSAGE_NO_DELETE` breaking check even though it's a wire-compatible addition; `buf.yaml` excepts that rule repo-wide for this reason, so the same move for fields 17/19 later won't need a fresh exception.
- The committed `proto/command/` baseline already reflects one specific Tesla app build reconstructed via cross-version protobuf diffing (`app-4.58.6`, see `TESLEMETRY-EXT` markers). A later app-version-diff pass will find most candidate fields already modelled here - check the current `.proto` files for the exact field/tag before assuming it needs adding, and only model the genuine delta.
- `proto/charging/` is a documented exception to the "app-only namespaces are not published" policy (`PROVENANCE.md`): it has no BLE or Fleet API wire path today, but was published because it describes the vehicle-charging product domain. Any future app-only module wanting the same exception should be argued explicitly, not assumed from this precedent.
- Adding a wholly new proto directory (a source with no upstream) needs registering in three places: the `buf.yaml` module list, `GROUPS_LIST` in `scripts/generate.sh`, and the layout table + provenance table in `README.md`/`PROVENANCE.md`. TypeScript/Python package exports are wildcarded, so no per-group registration is needed there.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
