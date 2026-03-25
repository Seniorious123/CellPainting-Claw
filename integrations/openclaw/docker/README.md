# Controlled OpenClaw Docker Runtime

This directory defines the Docker-first OpenClaw runtime for the Cell Painting pipeline.

## Goals

- keep OpenClaw inside a dedicated runtime boundary
- keep the validated Python stack in `lyx_env`
- avoid granting unnecessary host-level access
- preserve the stable library interfaces: CLI, Python API, and local MCP server
- avoid storing provider keys in repository-managed Docker config files

## Security Model

Current controls include:

- non-root runtime user
- dropped Linux capabilities
- `no-new-privileges`
- dedicated OpenClaw state storage
- mounted pipeline workspace instead of full host-home access
- browser and canvas tooling disabled in config
- elevated tooling disabled in config

OpenClaw still needs coding-style tools inside the container because it has to run the pipeline.

## Provider Configuration

This Docker track now uses the same env-driven provider pattern as the AutoDL track.

Provide these values through exported env vars or a local ignored `.env` file:

- `OPENCLAW_BASE_URL`
- `OPENCLAW_API_KEY`
- `OPENCLAW_PRIMARY_MODEL`
- optional: `OPENCLAW_FALLBACK_MODEL`
- optional: `OPENCLAW_PROVIDER_ID`
- optional: `OPENCLAW_PROVIDER_API`

Use the local template:

- `.env.example`

The runtime config is generated inside the mounted state volume at container start.

## Host Constraint on the Current Machine

On the current nested environment, Docker has to run in a reduced-capability mode.

That is why:

- `docker-compose.yml` uses `network_mode: host`
- the daemon may need restricted startup flags
- image pulls may still be limited by outbound network policy

## Files

- `Dockerfile`
- `entrypoint.sh`
- `openclaw.container.json`
- `.env.example`
- `project_config.docker.json`
- `docker-compose.yml`
- `start_docker_restricted.sh`
- `compose_up.sh`
- `compose_acp_client.sh`

## Expected Host Layout

The compose file mounts:

- host: `/root/pipeline`
- container: `/workspace/pipeline`

That keeps the validated backend directories available inside the runtime.

## Start Docker on This Machine

If the daemon is not already running:

```bash
cd /root/pipeline/cellpaint_pipeline_lib/integrations/openclaw/docker
./start_docker_restricted.sh
```

## Build and Run

```bash
cd /root/pipeline/cellpaint_pipeline_lib/integrations/openclaw/docker
cp .env.example .env
# edit .env
./compose_up.sh
```

This starts:

- OpenClaw gateway on `http://127.0.0.1:18789/`
- CellPaint MCP server on `http://127.0.0.1:8768/mcp`

## Terminal Chat

In a second shell:

```bash
cd /root/pipeline/cellpaint_pipeline_lib/integrations/openclaw/docker
./compose_acp_client.sh
```

For the current OpenClaw release, this wrapper launches the TUI path.

## Pipeline Config Inside the Container

Use this config path for direct CLI calls inside the runtime:

- `/opt/cellpaint_pipeline_lib/integrations/openclaw/docker/project_config.docker.json`

Example:

```bash
/opt/conda/envs/lyx_env/bin/python -m cellpaint_pipeline run-pipeline-skill \
  --config /opt/cellpaint_pipeline_lib/integrations/openclaw/docker/project_config.docker.json \
  --skill run-full-workflow
```

## Hardening Options

Future hardening options include:

- read-only mounts for more of the pipeline tree
- narrower OpenClaw tool allowlists
- shifting more execution behind MCP instead of raw shell tools
- separate library image and output-mount policy

## Host-Type Recommendation

- use this track on standard Linux hosts with Docker
- use `../autodl/` on AutoDL-like platforms
