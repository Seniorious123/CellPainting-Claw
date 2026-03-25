#!/usr/bin/env bash
set -euo pipefail
cd /root/pipeline/CellPainting-Claw/integrations/openclaw/docker
exec docker compose exec cellpaint-openclaw /opt/CellPainting-Claw/integrations/openclaw/docker/entrypoint.sh tui "$@"
