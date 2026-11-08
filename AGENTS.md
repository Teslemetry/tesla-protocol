# Project agent memory

Project-intrinsic agent knowledge: build, test, release, architecture and sharp-edge notes that should travel with the code. CI's gate list is `.github/workflows/ci.yml`; the contributor workflow is README "Contributing".

## Generated code

- `proto/` is the only hand-edited code; everything under `packages/typescript/src`, `packages/python/tesla_protocol/*/` and `go/*/` is generated (`pnpm install && pnpm generate`). CI fails on any diff, so never edit generated files directly.
- Run every repo Python script and test with `.venv/bin/python`, never system `python3` (it has no protobuf). `.venv` does not exist until `pnpm install && pnpm generate` has run in the checkout. Run buf as `pnpm exec buf`.
- Each `proto/<group>/` compiles as an isolated `--proto_path` root (`GROUPS_LIST` in `scripts/generate.sh`); there is no cross-group `import`. Structurally identical types therefore exist independently in several groups on purpose - e.g. `energy_device/signed_message.proto`'s signing envelope for the Powerwall local v1r endpoint mirrors `command`'s `UniversalMessage`/`Signatures`, and `SignatureType` is defined in both `vcsec.proto` and `signatures.proto`. Do not "de-duplicate" across groups.
- Adding a new proto directory means registering it in three places: the `buf.yaml` module list, `GROUPS_LIST`, and the README layout table. Package exports are wildcarded, so no per-group registration there.
- Python and Go output are compiled from a staged copy (`scripts/namespace_protos.py`) that registers every file as `tesla_protocol/<group>/<file>.proto` and every package as `tesla_protocol.<package>`, so they never collide in Python's descriptor pool or Go's global registry with another library's copy of Tesla's protos. `proto/` and the TypeScript output keep upstream's names; the Python and Go descriptor full names (e.g. `tesla_protocol.CarServer.Action`) intentionally differ from the `.proto` sources.
- Go packages are set by `M` flags in `scripts/generate.sh`, never by editing `go_package` in `proto/`: one package per group, except `command`, which is one package per proto package (its packages reuse type names). The module path carries the major version (`go/vN`), so a major bump rewrites every generated import; `scripts/sync-versions.mjs` does that in the Version PR.

## Toolchain pins and the gencode stamp

The codegen toolchain is fully pinned (`scripts/requirements.txt`, ts-proto in root `package.json`, protoc-gen-go via the `google.golang.org/protobuf` version in `go/go.mod`); changing a pin changes generated output and is a coordinated, changeset-worthy change. The `grpcio-tools` pin is load-bearing beyond determinism - see `scripts/check_gencode_runtime.py` for the compatibility rule it enforces. What that implies here:

- The gencode stamp is a *minimum runtime requirement*, so RAISING it breaks every consumer below it. The stamp and the `protobuf>=…` floor in `pyproject.toml` move together, in one major-bump changeset, or not at all. One wheel serves every runtime; do NOT split the package by protoc version.
- Verified grpcio-tools -> gencode mapping (recheck by compiling a throwaway proto): 1.74.0-1.80.0 emit 6.31.1, 1.81.0-1.81.1 emit 6.33.5, 1.82.0+ emit 7.35.x; no release emits 6.32.x. The pin sits at 1.81.1/6.33.5 because protobuf supports only the newest minor of a major (https://protobuf.dev/support/version-support), making 6.33 the lowest supported 6.x. Moving to 1.82.0+ raises `VersionError` at import for every 6.x runtime - a deliberate drop of 6.x support, not a routine bump.
- Bumping the pin rewrites the stamp in every `_pb2.py` file and the `protoc vX` header of every `.ts` and `.pb.go` file while leaving serialized descriptors byte-identical. A stamp-only diff is expected and wire-neutral; anything else in that diff deserves scrutiny.

## Upstream sync

- `upstream.json` pins the commit and per-file sha256 that `proto/command/` and `proto/telemetry/` are reconciled against. Run `scripts/upstream_coverage.py --mode pinned` before pushing proto changes; its module docstring documents the modes, the delta outcome classes and the upstream-wins/`Void {}` rule.
- Local additions inside upstream-tracked files must carry a `TESLEMETRY-EXT` marker (trailing comment or `BEGIN`/`END` fence). The fence parser is flat and non-nesting: a `BEGIN` inside an open fence overwrites the open start, so only the innermost pair ends up marked. Adding a message inside an existing fenced block needs no new fence - it inherits the block's coverage.
- `upstream-drift.yml` decides whether to reconcile from the delta's `reconcile_needed` field, NOT the exit code (which reflects schema coverage only): upstream re-publishing an already-local symbol changes pinned bytes without changing coverage.
- To pull in a not-yet-merged upstream change, pin `upstream.json` to that PR's head commit and file sha256 so `--mode pinned` passes - these are upstream fields, not `TESLEMETRY-EXT` extensions. This works for a PR from a fork too: the upstream repo's raw URL serves the fork's head commit. When upstream merges with identical bytes, reconciliation is a no-op. While the pin sits on a PR head, the weekly `upstream-drift.yml` PR moves it back to upstream main and drops that PR's symbols; never push a fix to its `upstream-reconcile` branch, which every run force-pushes.

## Proto content rules

- `CarServer.Response.response_msg` (`proto/command/car_server.proto`): every field must be either modelled in the oneof or `reserved` with a reason comment; `scripts/check_reply_coverage.py` enforces this against `KNOWN_REPLY_FIELDS`. Before modelling a new reply field, check whether its payload type pulls in an app-only namespace - either model it or add it as a reserved entry.
- Un-reserving a field to model it trips buf's `RESERVED_MESSAGE_NO_DELETE` even though it is a wire-compatible addition; `buf.yaml` excepts that rule repo-wide.
- `buf breaking` (`WIRE_JSON`) fails every rename, renumber, retype and oneof move, even a wire-correct fix with hard evidence that a published tag or type is wrong. Never make one without a maintainer decision. Once one is approved, the release that carries it adds a temporary `breaking.ignore_only` block to `buf.yaml` that names only the rules that fired and only the files they fired on (buf scopes an ignore by file, not by field), merged with any block already there. Delete that block in the first PR after the release is published. For a single field, the other option is to reserve the old number and name and add a differently-named field at the correct number: `NavigationSuperchargerRequest` keeps `"order"` reserved by name, with `id` at tag 1 and `remote_nav_trip_order` at tag 2.
- A symbol not yet seen on a live vehicle carries `UNCONFIRMED: not yet confirmed on a live vehicle`, plus `name not recovered` when its name is a placeholder (e.g. `field_3`); drop the marker once wire-confirmed. Published text (protos, changesets, PR bodies, docs) never narrates where a schema came from.
- `CarServer.VehicleState` is upstream's name for the legacy vehicle-state surface (`VehicleData` 6); the current surface at `VehicleData` 18 is `CurrentVehicleState`. Never rename `VehicleState` (upstream owns the name; the coverage gate would fail permanently). The two share many field names at different tags, so add a field only to the message whose tag layout it belongs to.
- Several `energy_device` fields and `MessageEnvelope` payload tags reference types from sibling proto packages this repo does not publish; they stay unmodelled behind a short inline comment rather than being guessed at or vendored in.
- `proto/charging/` has no BLE or Fleet API wire path but is published anyway because it describes the vehicle-charging product domain: a narrow, deliberate exception, not precedent for publishing other app-only namespaces.

## Catalog and fixtures

- `scripts/build_catalog.py` regenerates `catalog/catalog.json` + `catalog/SUMMARY.md` from `proto/` and cross-checks group registration across `buf.yaml`/`GROUPS_LIST`/README; CI fails on any diff. Run it after any proto or group-registration change.
- `scripts/test_build_catalog.py::test_baseline_totals` asserts literal message/enum/field/file/group counts - deliberate drift detection, not a frozen spec. A proto change that shifts them fails CI once; update the asserted numbers in the same change.
- Cross-package wire confirmation lives in `fixtures/golden/*.json`: hex-encoded, language-neutral cases consumed by `packages/typescript/test/*.test.ts`, `packages/python/tests/*.py` and `go/golden_test.go`, asserting every encoder produces identical bytes and every decoder round-trips. Add a new fixture file per confirmed command rather than growing one file unboundedly.

## Release

- Changesets tracks the npm package only; `scripts/sync-versions.mjs` copies the version into `pyproject.toml` and the Go module path during `pnpm run version`, and `publish.yml` tags `go/vX.Y.Z` on the release SHA (Go modules publish by tag). Bump rules: `.changeset/README.md`. Never use changesets prerelease mode - `-next.N` is not valid PEP 440.
- Versions follow pragmatic versioning (BIGRELEASE.ANNOUNCE.INCREMENT, https://raw.githubusercontent.com/seveibar/pragmaticversioning/refs/heads/main/README.md), not strict semver: INCREMENT is the default for any ordinary contribution - don't deliberate over whether an addition "counts" as a feature. ANNOUNCE is for a substantial incompatible change or a user-visible feature set; BIGRELEASE for a marketed milestone.
- The publish flow, its `ci.yml` gate and interrupted-publish recovery (always re-run the failed job, never fix the registry by hand) are in README "Releases".
- The `production` GitHub environment's required reviewer and main-only branch policy are configured on the environment, not in-repo; inspect via `gh api repos/Teslemetry/tesla-protocol/environments/production`.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
