# Changesets

Every PR that changes `proto/` (or the published packages) adds a changeset:

```sh
pnpm changeset
```

Changesets tracks the npm package `@teslemetry/tesla-protocol` only; the
PyPI package `tesla-protocol` gets the identical version copied into its
`pyproject.toml` (and the Go module its `/vN` path suffix) by
`scripts/sync-versions.mjs` during `pnpm run version`, so one Version PR always
bumps and releases all three packages in lockstep; the Go module is published
by the `go/vX.Y.Z` tag the release workflow pushes.

Bump rules: wire-compatible additions = minor; renames of fields/enum values =
major (they break generated-code APIs); tag renumbering is forbidden (CI
`buf breaking` gate). Do not use changesets prerelease mode - `-next.N`
versions are not valid PEP 440.
