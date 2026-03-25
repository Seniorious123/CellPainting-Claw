#!/usr/bin/env bash
set -euo pipefail
cd /root/pipeline/CellPainting-Claw/integrations/openclaw/docker
if [ -f ./.env ]; then
  echo "Using docker env file: $(pwd)/.env"
else
  echo "No local .env found. Copy .env.example to .env or export OPENCLAW_BASE_URL/OPENCLAW_API_KEY/OPENCLAW_PRIMARY_MODEL."
fi
exec docker compose up --build "$@"
