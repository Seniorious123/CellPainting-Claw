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

This demo is meant to show the **full OpenClaw path** from startup to a routed skill call.

### Step 1. Prepare the provider configuration

Purpose:

- tell OpenClaw which model provider it should use
- provide the credentials and base URL needed for that provider

On an AutoDL-like host:

```bash
cd integrations/openclaw/autodl
cp provider.env.example provider.env
# edit provider.env
./configure_openai_compatible_provider.sh
```

What this step does:

- reads your provider settings from `provider.env`
- writes the OpenClaw-side provider configuration used by the gateway

What success looks like:

- the command finishes without an error
- the configured provider is ready for the later gateway start

### Step 2. Start the gateway

Purpose:

- start the OpenClaw gateway itself
- start the local CellPainting-Claw MCP server that OpenClaw will call underneath

Command:

```bash
./run_openclaw_gateway.sh
```

What this step does:

- launches the OpenClaw gateway
- launches the local CellPainting-Claw MCP server
- keeps the bridge between OpenClaw and the toolkit available for later requests

What success looks like:

- the gateway stays running instead of exiting immediately
- the logs show that the gateway and MCP side have both started cleanly

### Step 3. Start the terminal interface

Purpose:

- open the interface where the user will type natural-language requests

Command:

```bash
./run_openclaw_tui.sh
```

What this step does:

- opens the OpenClaw terminal client
- connects that client to the running gateway session

What success looks like:

- the TUI opens normally
- you can type a request into the session instead of seeing an immediate connection error

### Step 4. Send a natural-language request

Purpose:

- ask for a real pipeline task in plain language

Example prompt:

```text
Run segmentation with config configs/project_config.demo.json and write outputs to outputs/demo_segmentation.
```

What this request means:

- the task objective is segmentation
- the config file is `configs/project_config.demo.json`
- the requested output location is `outputs/demo_segmentation`

What should happen internally:

- OpenClaw receives the natural-language request
- the agent recognizes this as a segmentation request
- the request is routed to the skill `run-segmentation`
- that skill calls the same validated segmentation path used by the CLI and Python API

What success looks like:

- the agent returns a result instead of failing at the provider, gateway, or MCP level
- the request behaves like a routed toolkit task rather than a free-form chat answer

Expected outputs:

- masks
- previews
- masked crops
- unmasked crops

### Step 5. Check the result

Purpose:

- confirm that the request reached the underlying toolkit and produced real outputs

What to check:

- the OpenClaw session should report a task result, not only conversational text
- the requested output location should contain the segmentation artifacts
- those artifacts should match the normal outputs of `run-segmentation`

What this proves:

- OpenClaw can understand a task request in natural language
- OpenClaw can route that request onto the correct documented skill
- the same toolkit path used elsewhere in the project is still the one doing the work underneath

## Another Example

Prompt:

```text
Prepare the DeepProfiler inputs for this config, but do not run DeepProfiler yet.
```

How this request should be interpreted:

- the task objective is DeepProfiler input preparation
- the request should route to `prepare-deepprofiler-inputs`
- the expected outputs are export metadata, image inputs, and location inputs

## What Makes A Good OpenClaw Request

A useful request usually states:

- the task objective
- the config file
- the output location when relevant

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
