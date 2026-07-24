# Provenance

For the vehicle-command and fleet-telemetry protos, **Teslemetry is a tracker,
not an author**: Tesla's public repositories are the source of truth for every
symbol they define. This repo carries that upstream base plus clearly marked
Teslemetry extensions, from our own observations and contributions from the
community. For the remaining
directories no public upstream exists and this repo is the source of record.

| Directory | Class | Primary source |
| --- | --- | --- |
| `proto/command/` (except `session.proto`) | upstream-tracked + extensions | [`teslamotors/vehicle-command`](https://github.com/teslamotors/vehicle-command) `pkg/protocol/protobuf/` |
| `proto/telemetry/` | upstream-tracked, verbatim except marked extensions | [`teslamotors/fleet-telemetry`](https://github.com/teslamotors/fleet-telemetry) `protos/` |
| `proto/command/session.proto` | Teslemetry source-of-record | no upstream (Teslemetry session persistence) |
| `proto/energy_device/`, `proto/energy_command/` | Teslemetry source-of-record | no upstream (TEG gateway local API, from our own observations and contributions from the community) |
| `proto/teslapower/` | Teslemetry source-of-record | no upstream (Powerwall local API, from our own observations and contributions from the community, credit @brianhealey) |
| `proto/charging/` | Teslemetry source-of-record | no upstream (EV charge-session energy metering / billing schema, from our own observations and contributions from the community) |

## How the boundary is kept visible

1. **Per-file headers.** Every upstream-tracked file begins with an
   `UPSTREAM-SOURCE` / `UPSTREAM-PATH` / `UPSTREAM-COMMIT` header; files with
   no upstream carry a `TESLEMETRY SOURCE-OF-RECORD` banner instead.
2. **`TESLEMETRY-EXT` markers.** Inside upstream-tracked files, every message,
   field, enum or enum value that is NOT in upstream is marked: contiguous
   additions sit inside a `TESLEMETRY-EXT BEGIN … TESLEMETRY-EXT END` fence,
   single fields and enum values get a trailing `// TESLEMETRY-EXT (<source>)`
   comment. The marker grammar is machine-checked (below).
3. **`upstream.json`.** Pins the exact upstream commit (and per-file sha256)
   this repo is reconciled against. Only the upstream-drift workflow's
   reconcile PRs move it.

## The coverage gate

`scripts/upstream_coverage.py` compiles both sides to descriptor sets and
enforces, symbol by symbol, that **upstream ⊆ ours**:

- On every PR (`--mode pinned`, against the `upstream.json` commit): a missing
  upstream symbol, a rename/wire conflict, or an ours-only symbol without a
  `TESLEMETRY-EXT` marker fails CI.
- Weekly (`--mode head`, against upstream main): new upstream additions open
  an `upstream-drift` issue and a draft reconcile PR that advances the pin;
  that PR's own CI then lists exactly what must be merged.

The gate never requires deleting an extension - ours-only symbols are only
policed for marker presence.

## Standing policies

- **Upstream wins names.** If Tesla later publishes a symbol we already
  defined under a different name or number, upstream's version replaces ours; the
  rename is a **major** changeset (it breaks generated-code APIs).
- Wire-compatible additions = minor; field/enum renames = major; tag
  renumbering = forbidden (`buf breaking` gate).
- Tesla's internal app-only schema namespaces are deliberately NOT published
  here; only consumer-needed command/telemetry/energy surfaces are. `proto/charging/`
  is a deliberate, narrow exception: it models the vehicle-charging product
  domain even though no BLE or Fleet API surface exposes it as protobuf today
  (the public Fleet API charging endpoints return JSON), because the schema
  itself is a genuine, self-contained description of Tesla's charge-session
  metering/billing data.
