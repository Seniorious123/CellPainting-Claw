#!/usr/bin/env bash
set -euo pipefail
cd /root/pipeline/cellpaint_pipeline_lib
exec /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline serve-mcp --transport streamable-http --host 127.0.0.1 --port 8768 --path /mcp
