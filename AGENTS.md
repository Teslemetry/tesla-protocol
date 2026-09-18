# Project agent memory

Project-intrinsic agent knowledge: build, test, release, architecture and sharp-edge notes that should travel with the code. CI's gate list is `.github/workflows/ci.yml`; the contributor workflow is README "Contributing".

## Generated code

- `proto/` is the only hand-edited code; everything under `packages/typescript/src` and `packages/python/tesla_protocol/*/` is generated (`pnpm install && pnpm generate`). CI fails on any diff, so never edit generated files directly.
- Each `proto/<group>/` compiles as an isolated `--proto_path` root (`GROUPS_LIST` in `scripts/generate.sh`); there is no cross-group `import`. Structurally identical types therefore exist independently in several groups on purpose - e.g. `energy_device/signed_message.proto`'s signing envelope for the Powerwall local v1r endpoint mirrors `command`'s `UniversalMessage`/`Signatures`, and `SignatureType` is defined in both `vcsec.proto` and `signatures.proto`. Do not "de-duplicate" across groups.
- Adding a new proto directory means registering it in three places: the `buf.yaml` module list, `GROUPS_LIST`, and the README layout table. Package exports are wildcarded, so no per-group registration there.
- Sharp edge: protoletariat is installed with `pip --no-deps` (`scripts/generate.sh`) because it over-pins `protobuf<6` while only parsing descriptor sets; its `--exclude-imports-glob` patterns match dependency names WITHOUT the `.proto` suffix.

## Toolchain pins and the gencode stamp

The codegen toolchain is fully pinned (`scripts/requirements.txt`, ts-proto in root `package.json`); changing a pin changes generated output and is a coordinated, changeset-worthy change. The `grpcio-tools` pin is load-bearing beyond determinism - see `scripts/check_gencode_runtime.py` for the compatibility rule it enforces. What that implies here:

- The gencode stamp is a *minimum runtime requirement*, so RAISING it breaks every consumer below it. The stamp and the `protobuf>=…` floor in `pyproject.toml` move together, in one major-bump changeset, or not at all. One wheel serves every runtime; do NOT split the package by protoc version.
- Verified grpcio-tools -> gencode mapping (recheck by compiling a throwaway proto): 1.74.0-1.80.0 emit 6.31.1, 1.81.0-1.81.1 emit 6.33.5, 1.82.0+ emit 7.35.x; no release emits 6.32.x. The pin sits at 1.81.1/6.33.5 because protobuf supports only the newest minor of a major (https://protobuf.dev/support/version-support), making 6.33 the lowest supported 6.x. Moving to 1.82.0+ raises `VersionError` at import for every 6.x runtime, including Home Assistant's constraint - a deliberate drop of 6.x support, not a routine bump.
- Bumping the pin rewrites the stamp in all 38 `_pb2.py` files and the `protoc vX` header of every `.ts` file while leaving serialized descriptors byte-identical. A stamp-only diff is expected and wire-neutral; anything else in that diff deserves scrutiny.

## Upstream sync

- `upstream.json` pins the commit and per-file sha256 that `proto/command/` and `proto/telemetry/` are reconciled against. Run `scripts/upstream_coverage.py --mode pinned` before pushing proto changes; its module docstring documents the modes, the delta outcome classes and the upstream-wins/`Void {}` rule.
- Local additions inside upstream-tracked files must carry a `TESLEMETRY-EXT` marker (trailing comment or `BEGIN`/`END` fence). The fence parser is flat and non-nesting: a `BEGIN` inside an open fence overwrites the open start, so only the innermost pair ends up marked. Adding a message inside an existing fenced block needs no new fence - it inherits the block's coverage.
- `upstream-drift.yml` decides whether to reconcile from the delta's `reconcile_needed` field, NOT the exit code (which reflects schema coverage only): upstream re-publishing an already-local symbol changes pinned bytes without changing coverage.
- To pull in a not-yet-merged upstream change (an open PR against a branch owned by the upstream org, not a fork), pin `upstream.json` to that PR's head commit and file sha256 so `--mode pinned` passes - these are upstream fields, not `TESLEMETRY-EXT` extensions. When upstream merges with identical bytes, reconciliation is a no-op.

## Proto content rules

- `CarServer.Response.response_msg` (`proto/command/car_server.proto`): every field must be either modelled in the oneof or `reserved` with a reason comment; `scripts/check_reply_coverage.py` enforces this against `KNOWN_REPLY_FIELDS`. Before modelling a new reply field, check whether its payload type pulls in an app-only namespace - either model it or add it as a reserved entry.
- Un-reserving a field to model it trips buf's `RESERVED_MESSAGE_NO_DELETE` even though it is a wire-compatible addition; `buf.yaml` excepts that rule repo-wide.
- Tag renumbering is a hard `buf breaking` gate, not a guideline: it fires even with hard evidence a published tag is wrong, and reserving the number alone is not enough - `FIELD_NO_DELETE` also requires reserving the name, which then collides with reusing it at the corrected number. Never attempt an in-place renumber; it always needs a maintainer decision. The sanctioned fix, once approved, is to reserve the old number and name and add a differently-named field at the correct number - a breaking rename needing a major changeset. Live example: `NavigationSuperchargerRequest` keeps `"order"` reserved by name, with `id` at tag 1 and `remote_nav_trip_order` at tag 2.
- Several `energy_device` fields and `MessageEnvelope` payload tags reference types from sibling proto packages this repo does not publish; they stay unmodelled behind a short inline comment rather than being guessed at or vendored in.
- `proto/charging/` has no BLE or Fleet API wire path but is published anyway because it describes the vehicle-charging product domain: a narrow, deliberate exception, not precedent for publishing other app-only namespaces.

## Catalog and fixtures

- `scripts/build_catalog.py` regenerates `catalog/catalog.json` + `catalog/SUMMARY.md` from `proto/` and cross-checks group registration across `buf.yaml`/`GROUPS_LIST`/README; CI fails on any diff. Run it after any proto or group-registration change.
- `scripts/test_build_catalog.py::test_baseline_totals` asserts literal message/enum/field/file/group counts - deliberate drift detection, not a frozen spec. A proto change that shifts them fails CI once; update the asserted numbers in the same change.
- Cross-package wire confirmation lives in `fixtures/golden/*.json`: hex-encoded, language-neutral cases consumed by both `packages/typescript/test/*.test.ts` and `packages/python/tests/*.py`, asserting both encoders produce identical bytes and both decoders round-trip. Add a new fixture file per confirmed command rather than growing one file unboundedly.

## Release

- Changesets tracks the npm package only; `scripts/sync-python-version.mjs` copies the version into `pyproject.toml` during `pnpm run version`. Bump rules: `.changeset/README.md`. Never use changesets prerelease mode - `-next.N` is not valid PEP 440.
- Versions follow pragmatic versioning (BIGRELEASE.ANNOUNCE.INCREMENT, https://raw.githubusercontent.com/seveibar/pragmaticversioning/refs/heads/main/README.md), not strict semver: INCREMENT is the default for any ordinary contribution - don't deliberate over whether an addition "counts" as a feature. ANNOUNCE is for a substantial incompatible change or a user-visible feature set; BIGRELEASE for a marketed milestone.
- `publish.yml` calls `ci.yml` as a reusable workflow so the full suite runs against the exact SHA it publishes; both publish jobs depend on that gate - keep them wired to it if you touch the release path. Publish flow and interrupted-publish recovery (always re-run the failed job, never fix the registry by hand) are in README "Releases".
- The `production` GitHub environment's required reviewer and main-only branch policy are configured on the environment, not in-repo; inspect via `gh api repos/Teslemetry/tesla-protocol/environments/production`.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
