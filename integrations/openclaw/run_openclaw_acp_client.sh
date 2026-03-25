#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OPENCLAW_BIN="${OPENCLAW_BIN:-$(command -v openclaw || true)}"

if [ -z "$OPENCLAW_BIN" ]; then
  echo "openclaw is not installed." >&2
  echo "Run ./install_openclaw_cli.sh first." >&2
  exit 1
fi

export OPENCLAW_HOME="${OPENCLAW_HOME:-$SCRIPT_DIR/state}"
export OPENCLAW_CONFIG_PATH="${OPENCLAW_CONFIG_PATH:-$SCRIPT_DIR/openclaw.json}"

exec "$OPENCLAW_BIN" acp client "$@"
