// Copies the changesets-managed npm package version into pyproject.toml and
// the Go module path so all three packages always release in lockstep from the
// same Version PR commit. Runs as part of `pnpm run version` (changeset version
// && this script).
import { readFileSync, readdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

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

// Go puts the major version in the module path (/vN from v2 on), so a major
// bump rewrites it in go.mod and every generated import - the same result
// scripts/generate.sh produces, keeping the Version PR's codegen fresh.
const major = Number(version.split(".")[0]);
const base = "github.com/Teslemetry/tesla-protocol/go";
const target = major >= 2 ? `${base}/v${major}` : base;
const goMod = readFileSync("go/go.mod", "utf8");
const current = goMod.match(/^module (\S+)$/m)?.[1];
if (!current) {
  throw new Error("could not find module line in go/go.mod");
}
if (current !== target) {
  const escaped = current.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const pattern = new RegExp(`${escaped}(?=[/"\\s]|$)`, "gm");
  const files = readdirSync("go", { recursive: true })
    .filter((f) => f === "go.mod" || f.endsWith(".go"))
    .map((f) => join("go", f));
  for (const file of files) {
    const text = readFileSync(file, "utf8");
    const next = text.replace(pattern, target);
    if (next !== text) writeFileSync(file, next);
  }
}
console.log(`go/go.mod -> ${target}`);
