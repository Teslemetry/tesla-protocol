#!/usr/bin/env bash
# Regenerates ALL committed codegen output (TypeScript + Python) from proto/.
# Deterministic: pinned protoc (grpcio-tools), pinned ts-proto, pinned protol.
# CI runs this and fails on `git diff --exit-code`.
set -euo pipefail
cd "$(dirname "$0")/.."

VENV=.venv
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
fi
"$VENV/bin/pip" install --quiet --requirement scripts/requirements.txt
"$VENV/bin/pip" install --quiet --no-deps protoletariat==3.3.10

if [ ! -x node_modules/.bin/protoc-gen-ts_proto ]; then
  echo "node_modules missing - run 'pnpm install' first" >&2
  exit 1
fi

PROTOC="$VENV/bin/python -m grpc_tools.protoc"
TS_PLUGIN="$PWD/node_modules/.bin/protoc-gen-ts_proto"
TS_OPTS="emitDefaultValues=json-methods,importSuffix=.js"
TS_OUT=packages/typescript/src
PY_PKG=packages/python/tesla_protocol

GROUPS_LIST="command telemetry energy_device energy_command teslapower"

rm -rf "$TS_OUT"
for group in $GROUPS_LIST; do
  mkdir -p "$TS_OUT/$group"
  $PROTOC \
    --plugin=protoc-gen-ts_proto="$TS_PLUGIN" \
    --ts_proto_opt="$TS_OPTS" \
    --proto_path="proto/$group" \
    --ts_proto_out="$TS_OUT/$group" \
    proto/"$group"/*.proto

  rm -rf "${PY_PKG:?}/$group"
  mkdir -p "$PY_PKG/$group"
  $PROTOC \
    --proto_path="proto/$group" \
    --python_out=pyi_out:"$PY_PKG/$group" \
    proto/"$group"/*.proto
  # google/rpc/status.proto is not generated locally; it resolves at runtime
  # through googleapis-common-protos, so its import must stay absolute.
  "$VENV/bin/protol" \
    --create-package --in-place \
    --python-out "$PY_PKG/$group" \
    --exclude-imports-glob 'google/rpc/*' \
    protoc --protoc-path="$PROTOC" \
    --proto-path="proto/$group" proto/"$group"/*.proto
  # protoletariat only recognizes protoc's "import x_pb2 as x__pb2" alias
  # convention; the pyi-stub generator emits "import x_pb2 as _x_pb2"
  # instead, so protoletariat silently skips rewriting .pyi cross-file
  # imports to relative form. Cover that convention here.
  "$VENV/bin/python" scripts/fix_pyi_relative_imports.py "$PY_PKG/$group"
done

echo "generate: OK"
