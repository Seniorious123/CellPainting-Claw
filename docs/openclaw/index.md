# OpenClaw

This section documents the **OpenClaw integration surface** for CellPainting-Claw.

OpenClaw is the **agent interface** for this project. It is an optional natural-language front end that connects to CellPainting-Claw through MCP. It does **not** introduce a separate backend.

## What OpenClaw Does

In practical terms, OpenClaw should do one thing well:

1. receive a natural-language request
2. map that request onto the right public skill
3. call the same underlying toolkit through MCP
4. return the result through the agent session

So the OpenClaw path should be understood as an **agent interface over the existing skill catalog**, not as a different workflow implementation.

## Before You Use OpenClaw

OpenClaw should **not be the first thing you debug**.

A reliable order is:

1. confirm that the core `cellpainting-claw` CLI works
2. confirm that the MCP server starts cleanly
3. only then add the OpenClaw interface on top

That order separates toolkit failures from agent-interface failures.

## Agent Demo

This is the simplest way to think about OpenClaw as a working agent demo.

### 1. Start the gateway and the TUI

On an AutoDL-like host:

```bash
cd integrations/openclaw/autodl
cp provider.env.example provider.env
# edit provider.env
./configure_openai_compatible_provider.sh
./run_openclaw_gateway.sh
./run_openclaw_tui.sh
```

The gateway wrapper starts:

- the OpenClaw gateway
- the local CellPainting-Claw MCP server

### 2. Give the agent a natural-language request

For example:

```text
Run segmentation with config configs/project_config.demo.json and write outputs to outputs/demo_segmentation.
```

What should happen:

- the agent identifies the request as a **segmentation task**
- the request maps to the skill `run-segmentation`
- the underlying toolkit runs the same validated segmentation path used by the CLI and Python API
- the result is returned through the agent session

Typical outputs for that request:

- masks
- previews
- masked crops
- unmasked crops

### 3. Another example: prepare DeepProfiler inputs

Prompt:

```text
Prepare the DeepProfiler inputs for this config, but do not run DeepProfiler yet.
```

Expected routing:

- skill: `prepare-deepprofiler-inputs`
- task type: DeepProfiler preparation
- typical outputs: export metadata, image inputs, and location inputs

### 4. What this demo proves

This kind of interaction demonstrates that OpenClaw can:

- understand the task request in natural language
- route to the correct public skill
- call the same toolkit capabilities exposed elsewhere in the project
- return an agent-mediated result without introducing a separate workflow model

## A Concrete Interaction Pattern

A useful OpenClaw request should describe:

- the task objective
- the config file
- the output location

For example:

```text
Run segmentation with config configs/project_config.demo.json and write outputs to outputs/demo_segmentation.
```

That request should normally resolve to:

- skill: `run-segmentation`
- implementation path: the standard segmentation task surface underneath
- typical outputs: masks, previews, masked crops, and unmasked crops

Another example:

```text
Prepare the DeepProfiler inputs for this config, but do not run DeepProfiler yet.
```

That request should normally resolve to:

- skill: `prepare-deepprofiler-inputs`
- implementation path: the DeepProfiler preparation task underneath
- typical outputs: export metadata, image inputs, and location inputs

## What OpenClaw Should Trigger

In normal use, OpenClaw should route requests onto the **public skills** documented in this site.

That keeps the agent behavior predictable: the user asks for a task in natural language, and the agent resolves it to a stable task name such as `run-segmentation` or `prepare-deepprofiler-inputs`.

## When To Use OpenClaw

Use OpenClaw when you want:

- **natural-language task execution**
- an **agent-facing interface** for the toolkit
- **MCP-based integration** with a controlled agent interface

Use the Python API or the CLI directly when you want:

- the most explicit and reproducible interface
- shell scripts, notebooks, or direct library calls
- easier debugging of configuration and toolkit errors

## OpenClaw Setups

The repository maintains **two main OpenClaw setup tracks**:

- `integrations/openclaw/autodl/` for AutoDL-like hosts without nested Docker
- `integrations/openclaw/docker/` for standard Linux hosts with Docker support

For current OpenClaw releases, prefer the **TUI path** rather than the ACP client path.

Both setup tracks keep provider credentials out of repository-managed templates and expose the same library-facing toolkit surface underneath.

## Shortest AutoDL Path

On AutoDL-like hosts, the normal path is:

```bash
cd integrations/openclaw/autodl
cp provider.env.example provider.env
# edit provider.env
./configure_openai_compatible_provider.sh
./run_openclaw_gateway.sh
./run_openclaw_tui.sh
```

The gateway wrapper starts the **OpenClaw gateway** together with the local **CellPainting-Claw MCP server**.

## Shortest Docker Path

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

## Boundaries And Expectations

OpenClaw is useful, but it does **not remove the need to understand the core toolkit interfaces**.

Important boundaries are:

- the CLI and Python API remain the **canonical interfaces**
- MCP is the **bridge interface**, not the toolkit implementation itself
- provider configuration, gateway state, and model access remain deployment concerns outside the core pipeline library
- toolkit correctness still depends on the underlying config, data paths, and installed backends

## Troubleshooting Logic

When OpenClaw fails, the main failure classes are usually:

- provider authentication or base URL configuration
- gateway not running
- MCP server not reachable
- valid agent connection but invalid toolkit config or missing backend dependencies

A useful debugging order is:

1. run the core CLI directly
2. start the MCP server and confirm it stays healthy
3. start the OpenClaw interface
4. only then debug provider configuration or prompt-level behavior

## Related Pages

- [Skills](../skills/index.md)
- [CLI](../cli/index.md)
- [Quick Start](../quick_start/index.md)
