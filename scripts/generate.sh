#!/usr/bin/env bash
# Regenerates ALL committed codegen output (TypeScript + Python + Go) from proto/.
# Deterministic: pinned protoc (grpcio-tools), pinned ts-proto, and
# protoc-gen-go pinned by the google.golang.org/protobuf version in go/go.mod.
# CI runs this and fails on `git diff --exit-code`.
set -euo pipefail
export LC_ALL=C # stable glob order for the generated __init__.pyi
cd "$(dirname "$0")/.."

VENV=.venv
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
fi
"$VENV/bin/pip" install --quiet --requirement scripts/requirements.txt

if [ ! -x node_modules/.bin/protoc-gen-ts_proto ]; then
  echo "node_modules missing - run 'pnpm install' first" >&2
  exit 1
fi

if ! command -v go >/dev/null; then
  echo "go missing - install the Go toolchain (see go/go.mod)" >&2
  exit 1
fi

PROTOC="$VENV/bin/python -m grpc_tools.protoc"
TS_PLUGIN="$PWD/node_modules/.bin/protoc-gen-ts_proto"
TS_OPTS="emitDefaultValues=json-methods,importSuffix=.js,useJsTypeOverride=true"
TS_OUT=packages/typescript/src
PY_PKG=packages/python/tesla_protocol
GO_OUT=go

# Go requires a /vN module path suffix from major version 2 on, so the module
# path follows the shared package version (sync-versions.mjs rewrites it
# on a major bump). protoc-gen-go is built from the protobuf runtime version
# go.mod requires, so the generator and runtime are always the same release.
GO_MAJOR="$(node -p 'require("./packages/typescript/package.json").version.split(".")[0]')"
GO_MODULE=github.com/Teslemetry/tesla-protocol/go
if [ "$GO_MAJOR" -ge 2 ]; then GO_MODULE="$GO_MODULE/v$GO_MAJOR"; fi
sed -i "s#^module .*#module $GO_MODULE#" "$GO_OUT/go.mod"
GO_BIN="$(mktemp -d)"
go -C "$GO_OUT" build -o "$GO_BIN/protoc-gen-go" google.golang.org/protobuf/cmd/protoc-gen-go

GROUPS_LIST="command telemetry energy_device teslapower charging dashcam"

rm -rf "$TS_OUT"
for group in $GROUPS_LIST; do
  mkdir -p "$TS_OUT/$group"
  $PROTOC \
    --plugin=protoc-gen-ts_proto="$TS_PLUGIN" \
    --ts_proto_opt="$TS_OPTS" \
    --proto_path="proto/$group" \
    --ts_proto_out="$TS_OUT/$group" \
    proto/"$group"/*.proto

  # Python compiles from a staged copy namespaced under tesla_protocol/ (file
  # names and packages), so the modules never collide in the process-wide
  # descriptor pool with another library's copy of Tesla's protos. protoc then
  # emits absolute `from tesla_protocol.<group> import ...` imports itself.
  # google/rpc/status.proto keeps its canonical name and resolves at runtime
  # through googleapis-common-protos, so it is not generated locally.
  STAGE="$(mktemp -d)"
  "$VENV/bin/python" scripts/namespace_protos.py "proto/$group" "$STAGE"
  rm -rf "${PY_PKG:?}/$group"
  $PROTOC \
    --proto_path="$STAGE" \
    --python_out=pyi_out:"$(dirname "$PY_PKG")" \
    "$STAGE/tesla_protocol/$group"/*.proto

  # Go compiles from the same staged copy for the same reason: Go's global
  # registry panics on a duplicate file or symbol name. Each group is one Go
  # package, except command: its proto packages reuse type names (VCSEC and
  # Signatures both define SignatureType), so it gets one Go package per proto
  # package, laid out like vehicle-command's (command/carserver, command/vcsec,
  # ...). The M flags override upstream's go_package options without editing
  # proto/.
  rm -rf "${GO_OUT:?}/$group"
  GO_OPTS=(--go_opt=module="$GO_MODULE")
  for proto in "$STAGE/tesla_protocol/$group"/*.proto; do
    go_pkg="$group"
    if [ "$group" = command ]; then
      go_pkg="$(sed -n 's/^package tesla_protocol\.\([A-Za-z]*\);.*/\1/p' "$proto" | tr '[:upper:]' '[:lower:]')"
      go_pkg="command/${go_pkg:?no package in $proto}"
    fi
    GO_OPTS+=(--go_opt=M"tesla_protocol/$group/$(basename "$proto")=$GO_MODULE/$go_pkg;$(basename "$go_pkg")")
  done
  $PROTOC \
    --plugin=protoc-gen-go="$GO_BIN/protoc-gen-go" \
    --proto_path="$STAGE" \
    --go_out="$GO_OUT" \
    "${GO_OPTS[@]}" \
    "$STAGE/tesla_protocol/$group"/*.proto
  rm -rf "$STAGE"
  : > "$PY_PKG/$group/__init__.py"
  for module in "$PY_PKG/$group"/*_pb2.py; do
    echo "from . import $(basename "$module" .py)"
  done > "$PY_PKG/$group/__init__.pyi"
done
rm -rf "$GO_BIN"

echo "generate: OK"
