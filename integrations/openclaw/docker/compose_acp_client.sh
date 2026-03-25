#!/usr/bin/env bash
set -euo pipefail
cd /root/pipeline/cellpaint_pipeline_lib/integrations/openclaw/docker
exec docker compose exec cellpaint-openclaw /opt/cellpaint_pipeline_lib/integrations/openclaw/docker/entrypoint.sh tui "$@"
