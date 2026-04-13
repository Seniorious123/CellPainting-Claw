# OpenClaw

OpenClaw is the **natural-language entry point** for CellPainting-Claw.

Use it when you want to describe a task in plain language and let an agent route that request onto the documented skills.

## What OpenClaw Is For

In normal use, OpenClaw should do one thing well:

1. receive a natural-language request
2. map that request onto the right skill
3. call the toolkit through MCP
4. return the result through the agent session

So OpenClaw should be understood as a **natural-language front end for the existing skills**, not as a separate workflow.

## When To Use It

Use OpenClaw when you want:

- natural-language task execution
- a natural-language interface for the project
- a chat-style way to run documented skills

Use the CLI or Python directly when you want:

- the most explicit and reproducible interface
- shell scripts, notebooks, or direct library calls
- easier debugging of configuration or backend problems

## Before You Start

OpenClaw should **not be the first thing you debug**.

A reliable order is:

1. confirm that the core `cellpainting-claw` CLI works
2. confirm that the MCP server starts cleanly
3. only then add the OpenClaw interface on top

That order separates toolkit problems from OpenClaw-side problems.

## A Minimal OpenClaw Demo

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

This starts:

- the OpenClaw gateway
- the local CellPainting-Claw MCP server

### 2. Ask for a task in natural language

For example:

```text
Run segmentation with config configs/project_config.demo.json and write outputs to outputs/demo_segmentation.
```

What should happen:

- the request is recognized as a segmentation task
- the agent routes it to `run-segmentation`
- the same validated segmentation path used elsewhere in the project is called underneath
- the result comes back through the agent session

Typical outputs for that request include:

- masks
- previews
- masked crops
- unmasked crops

### 3. Another example

```text
Prepare the DeepProfiler inputs for this config, but do not run DeepProfiler yet.
```

That request should normally resolve to:

- skill: `prepare-deepprofiler-inputs`
- typical outputs: export metadata, image inputs, and location inputs

## What Makes A Good OpenClaw Request

A useful request usually states:

- the task objective
- the config file
- the output location when relevant

For example:

```text
Run segmentation with config configs/project_config.demo.json and write outputs to outputs/demo_segmentation.
```

The important point is that the request should describe the **task you want done**, not the internal implementation details.

## Setup Options

The repository maintains two main setup paths:

- `integrations/openclaw/autodl/` for AutoDL-like hosts without nested Docker
- `integrations/openclaw/docker/` for standard Linux hosts with Docker support

For current OpenClaw releases, prefer the **TUI path** rather than the ACP client path.

## Shortest AutoDL Path

```bash
cd integrations/openclaw/autodl
cp provider.env.example provider.env
# edit provider.env
./configure_openai_compatible_provider.sh
./run_openclaw_gateway.sh
./run_openclaw_tui.sh
```

## Shortest Docker Path

```bash
cd integrations/openclaw/docker
cp .env.example .env
# edit .env
./compose_up.sh
```

Then start the terminal client in a second shell:

```bash
cd integrations/openclaw/docker
./compose_acp_client.sh
```

## Boundaries

OpenClaw is useful, but it does **not** replace the core toolkit.

Important boundaries are:

- toolkit correctness still depends on the underlying config, data paths, and installed backends
- MCP is the connection path, not the toolkit itself
- provider configuration and gateway state are deployment concerns outside the core pipeline library

## Troubleshooting Order

When OpenClaw fails, a useful debugging order is:

1. run the core CLI directly
2. start the MCP server and confirm it stays healthy
3. start the OpenClaw interface
4. only then debug provider configuration or prompt-level behavior

Common failure classes are:

- provider authentication or base URL configuration
- gateway not running
- MCP server not reachable
- valid agent connection but invalid toolkit config or missing backend dependencies

## Related Pages

- [Skills](../skills/index.md)
- [CLI](../cli/index.md)
- [Quick Start](../quick_start/index.md)
