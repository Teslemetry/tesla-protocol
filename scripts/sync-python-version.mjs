// Copies the changesets-managed npm package version into pyproject.toml so
// both packages always release in lockstep from the same Version PR commit.
// Runs as part of `pnpm run version` (changeset version && this script).
import { readFileSync, writeFileSync } from "node:fs";

const { version } = JSON.parse(
  readFileSync("packages/typescript/package.json", "utf8"),
);
// Changesets prerelease mode emits `-next.N`, which is not valid PEP 440.
// Policy: this repo does not use prerelease mode.
if (!/^\d+\.\d+\.\d+$/.test(version)) {
  throw new Error(`version ${version} is not plain X.Y.Z (PEP 440-safe)`);
}

const path = "packages/python/pyproject.toml";
const toml = readFileSync(path, "utf8");
const updated = toml.replace(/^version = ".*"$/m, `version = "${version}"`);
if (updated === toml && !toml.includes(`version = "${version}"`)) {
  throw new Error(`could not find version line in ${path}`);
}
writeFileSync(path, updated);
console.log(`pyproject.toml -> ${version}`);
