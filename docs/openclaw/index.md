# OpenClaw

This section documents the OpenClaw integration surface for CellPainting-Claw.

OpenClaw is an optional natural-language front end for the same workflow library. It does not replace the core pipeline implementation.

## Role in the Stack

The relationship between the components is:

1. `cellpainting-claw` provides the canonical workflow library and CLI
2. `cellpainting-claw serve-mcp` exposes that library as MCP tools
3. OpenClaw connects to that MCP surface and provides an agent-driven interface
4. the agent can then trigger the same workflow capabilities through natural-language requests

In practical terms, OpenClaw sits on top of the library. It is not a separate backend.

## When To Use OpenClaw

Use OpenClaw when you want:

- natural-language task execution
- an agent-facing interface for the workflow
- MCP-based integration with a controlled runtime

Use the Python API or the main CLI when you want:

- the most explicit and reproducible interface
- shell scripts, notebooks, or direct library calls
- easier debugging of configuration and workflow errors

## What OpenClaw Can Trigger

Through the MCP surface, OpenClaw can reach the same public library surfaces that are documented elsewhere in this site, including:

- public workflow entrypoints
- task-oriented skills
- preset-oriented runs
- MCP tool wrappers around the public API

This means the OpenClaw path is an automation layer over the validated workflow, not a separate workflow definition.

## Minimal Runtime Paths

The repository maintains two main OpenClaw runtime tracks:

- `integrations/openclaw/autodl/` for AutoDL-like hosts without nested Docker
- `integrations/openclaw/docker/` for standard Linux hosts with Docker support

Both tracks keep provider credentials out of repository-managed templates and expose the same library-facing workflow surface underneath.

## Minimal AutoDL Launch Path

On AutoDL-like hosts, the normal path is:

```bash
cd integrations/openclaw/autodl
cp provider.env.example provider.env
# edit provider.env
./configure_openai_compatible_provider.sh
./run_openclaw_gateway.sh
./run_openclaw_tui.sh
```

The gateway wrapper starts the OpenClaw gateway together with the local CellPainting-Claw MCP server.

## Minimal Docker Launch Path

On standard Docker-capable Linux hosts, the normal path is:

```bash
cd integrations/openclaw/docker
cp .env.example .env
# edit .env
./compose_up.sh
```

Then open a second shell and start the terminal client:

```bash
cd integrations/openclaw/docker
./compose_acp_client.sh
```

## Natural-Language Usage

A typical OpenClaw request should describe the workflow objective, the config file, and the output location clearly. For example:

```text
Run the standard Cell Painting pipeline with config X and write outputs to Y.
```

Under the hood, the agent should still be routing to the same public workflow surfaces described in the rest of this documentation.

## Boundaries and Expectations

OpenClaw is useful, but it does not remove the need to understand the core workflow.

Important boundaries are:

- the CLI and Python API remain the canonical interfaces
- MCP is the bridge layer, not the workflow implementation itself
- provider configuration, gateway state, and model access remain runtime concerns outside the core pipeline library
- workflow correctness still depends on the underlying config, data paths, and installed backends

## Troubleshooting Logic

When OpenClaw fails, the main failure classes are usually:

- provider authentication or base URL configuration
- gateway not running
- MCP server not reachable
- valid agent connection but invalid workflow config or missing backend dependencies

A useful debugging rule is:

1. confirm the core CLI works first
2. confirm the MCP server starts cleanly
3. only then debug the OpenClaw runtime and provider configuration

That order separates workflow failures from agent-runtime failures.
