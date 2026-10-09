#!/usr/bin/env bash
# Regenerates ALL committed codegen output (TypeScript + Python) from proto/.
# Deterministic: pinned protoc (grpcio-tools), pinned ts-proto.
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

PROTOC="$VENV/bin/python -m grpc_tools.protoc"
TS_PLUGIN="$PWD/node_modules/.bin/protoc-gen-ts_proto"
TS_OPTS="emitDefaultValues=json-methods,importSuffix=.js"
TS_OUT=packages/typescript/src
PY_PKG=packages/python/tesla_protocol

GROUPS_LIST="command telemetry energy_device energy_command teslapower charging dashcam"

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
  rm -rf "$STAGE"
  : > "$PY_PKG/$group/__init__.py"
  for module in "$PY_PKG/$group"/*_pb2.py; do
    echo "from . import $(basename "$module" .py)"
  done > "$PY_PKG/$group/__init__.pyi"
done

echo "generate: OK"
