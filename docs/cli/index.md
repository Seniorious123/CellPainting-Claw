# Command-Line Interface

CellPainting-Claw exposes **two public CLI surfaces**:

- `cellpainting-skills`
- `cellpainting-claw`

These two CLIs are meant for different levels of use.

## Start With The Right CLI

### Start with `cellpainting-skills`

Use `cellpainting-skills` when you want:

- the **main public task interface**
- stable named tasks
- the shortest path from a user goal to a validated run
- the best first CLI for humans and agents

In most cases, this should be the **first CLI** a new user sees.

### Use `cellpainting-claw` when needed

Use `cellpainting-claw` when you want:

- lower-level toolkit commands
- `.cppipe` inspection and validation
- direct access to data-access helpers
- direct access to profiling, segmentation, or DeepProfiler tool families
- MCP serving and MCP tool inspection

In other words:

- `cellpainting-skills` is the **task CLI**
- `cellpainting-claw` is the **toolkit CLI**

## `cellpainting-skills`: The Main Task CLI

The task-oriented CLI is `cellpainting-skills`.

Its main commands are:

- `list`
- `describe`
- `run`

### What each command is for

| Command | What it does |
| --- | --- |
| `list` | show the public skill catalog |
| `describe` | show what one skill does |
| `run` | execute one named skill |

### Minimal first session

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills list
cellpainting-skills describe --skill run-segmentation
cellpainting-skills run   --config "$CONFIG"   --skill run-segmentation
```

This already demonstrates the main task story of the project:

- inspect the public skill catalog
- inspect one skill
- run one named task

### What the task CLI gives you

The task CLI gives you:

- stable task names
- a cleaner public interface than lower-level command groups
- a direct match to the [Skills](../skills/index.md) page
- a natural bridge for automation and agent routing

## `cellpainting-claw`: The Toolkit CLI

The main CLI is easier to understand as **tool groups**.

| Command group | What it is for | Example commands |
| --- | --- | --- |
| configuration and inspection | inspect configs, public surfaces, and `.cppipe` selection | `show-config`, `list-cppipe-templates`, `validate-cppipe-config` |
| data access | discover datasets and build download plans | `summarize-data-access`, `plan-data-access`, `execute-download-plan` |
| profiling tools | run profiling-side toolkit commands | `run-profiling`, `run-profiling-suite`, `run-evaluation` |
| segmentation tools | run segmentation-side toolkit commands | `run-segmentation`, `run-segmentation-suite`, `summarize-segmentation` |
| DeepProfiler tools | run DeepProfiler preparation and collection commands | `run-deepprofiler-pipeline`, `run-deepprofiler-full-stack` |
| named bundles | run named combined task bundles | `run-pipeline-preset`, `run-end-to-end-pipeline` |
| agent-facing tools | expose or inspect the MCP layer | `serve-mcp`, `list-mcp-tools`, `run-mcp-tool` |
| advanced internal helpers | inspect lower-level workflow aliases directly | `run-workflow` |

## The `.cppipe` Commands

The main CLI includes a public `.cppipe` inspection and validation layer.

These commands are useful when you want to inspect the CellProfiler pipeline selection before a longer run.

Key commands:

- `list-cppipe-templates`
- `describe-cppipe-template`
- `show-cppipe-selection`
- `validate-cppipe-config`

Minimal example:

```bash
CONFIG=configs/project_config.demo.json

cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind segmentation
cellpainting-claw validate-cppipe-config --config "$CONFIG"
```

Current phase-1 behavior:

- **segmentation** uses the selected `.cppipe` at runtime
- **profiling** exposes the same selection and validation commands for inspection
- custom segmentation overrides are treated as ready-to-run mask-export pipelines

## Presets And Internal Commands

### `run-pipeline-preset`

Use `run-pipeline-preset` when you intentionally want a **named bundle**, not one modular skill.

Examples include:

- `full-pipeline`
- `full-pipeline-with-data-plan`

### `run-workflow`

`run-workflow` is an **advanced internal-style command**.

It exists for cases where you want to call a lower-level workflow alias directly.

For normal use:

- prefer `cellpainting-skills run` when you want a named task
- prefer toolkit command groups when you want one tool family
- prefer `run-pipeline-preset` when you want a named bundle

## MCP And Agent-Facing CLI

The same toolkit can also be exposed as MCP tools.

The main MCP-related commands are:

- `serve-mcp`
- `list-mcp-tools`
- `show-mcp-tool-catalog`
- `run-mcp-tool`

This is the bridge layer used by OpenClaw and other MCP-capable clients.

## Related Pages

- [Skills](../skills/index.md)
- [OpenClaw](../openclaw/index.md)
- [Quick Start](../quick_start/index.md)
