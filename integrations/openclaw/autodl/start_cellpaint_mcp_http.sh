#!/usr/bin/env bash
set -euo pipefail

ROOT="/root/pipeline/cellpaint_pipeline_lib"
PYTHON_BIN="/root/miniconda3/envs/lyx_env/bin/python"
HOST="${CELLPAINT_MCP_HOST:-127.0.0.1}"
PORT="${CELLPAINT_MCP_PORT:-8768}"
PATH_MOUNT="${CELLPAINT_MCP_PATH:-/mcp}"
LOG_DIR="${CELLPAINT_OPENCLAW_LOG_DIR:-$ROOT/integrations/openclaw/autodl/state/logs}"
LOG_FILE="${CELLPAINT_MCP_LOG:-$LOG_DIR/cellpaint_mcp_http.log}"

mkdir -p "$LOG_DIR"

cd "$ROOT"
exec "$PYTHON_BIN" -m cellpaint_pipeline serve-mcp \
  --transport streamable-http \
  --host "$HOST" \
  --port "$PORT" \
  --path "$PATH_MOUNT" \
  >>"$LOG_FILE" 2>&1
