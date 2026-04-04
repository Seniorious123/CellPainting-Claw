# Command-Line Interface

CellPainting-Claw provides **two main public CLI surfaces**:

- `cellpainting-claw`
- `cellpainting-skills`

These two CLIs have different jobs.

## Which CLI To Use

### Use `cellpainting-skills` when:

- you want stable named tasks
- you want the simplest automation surface
- you are testing or using the skill catalog directly

### Use `cellpainting-claw` when:

- you want lower-level tool access
- you need configuration, data-access, or `.cppipe` inspection commands
- you want profiling, segmentation, or DeepProfiler command families directly
- you want to serve the toolkit through MCP

## `cellpainting-claw`: Main Command Groups

The main CLI is easier to understand as **tool groups**.

| Command group | What it is for | Example commands |
| --- | --- | --- |
| configuration and inspection | inspect configs, public surfaces, and `.cppipe` selection | `show-config`, `list-cppipe-templates`, `validate-cppipe-config` |
| data access | discover datasets and build download plans | `summarize-data-access`, `plan-data-access`, `execute-download-plan` |
| profiling tools | run profiling-side toolkit commands | `run-profiling`, `run-profiling-suite`, `run-evaluation` |
| segmentation tools | run segmentation-side toolkit commands | `run-segmentation`, `run-segmentation-suite`, `summarize-segmentation` |
| DeepProfiler tools | run DeepProfiler preparation and collection commands | `run-deepprofiler-pipeline`, `run-deepprofiler-full-stack` |
| high-level bundles | run named combined tasks from the main CLI | `run-pipeline-preset`, `run-end-to-end-pipeline` |
| agent-facing tools | expose or inspect the MCP layer | `serve-mcp`, `list-mcp-tools`, `run-mcp-tool` |
| advanced internal helpers | inspect lower-level workflow aliases directly | `run-workflow` |

## Configuration And `.cppipe` Commands

The main CLI includes a public `.cppipe` inspection and validation layer.

These commands are useful when you want to customize CellProfiler selection without editing backend files blindly.

- `list-cppipe-templates`
- `describe-cppipe-template`
- `show-cppipe-selection`
- `validate-cppipe-config`

Minimal examples:

```bash
CONFIG=configs/project_config.demo.json

cellpainting-claw list-cppipe-templates --config "$CONFIG"
cellpainting-claw describe-cppipe-template --template segmentation-base --config "$CONFIG"
cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind all
cellpainting-claw validate-cppipe-config --config "$CONFIG"
```

Current phase-1 behavior:

- **segmentation** uses the selected `.cppipe` at runtime
- **profiling** exposes the same selection and validation commands for inspection
- custom segmentation overrides are treated as ready-to-run mask-export pipelines

## `cellpainting-skills`: The Task CLI

The task-oriented CLI is `cellpainting-skills`.

Its main commands are:

- `list`
- `describe`
- `run`

This is the recommended first CLI for users who want to start from **tasks**.

Minimal examples:

```bash
cellpainting-skills list
cellpainting-skills describe --skill run-segmentation-workflow
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-segmentation-workflow
```

## What The Skills CLI Gives You

The skills CLI gives you:

- stable task names
- a cleaner interface than the lower-level command families
- a better fit for automation and agent use

This is why it is often the best first CLI to show to a new user.

## What `run-workflow` Means

`run-workflow` is an **advanced internal-style command** exposed by the main CLI.

It exists for cases where you want to call a lower-level workflow alias directly.

For normal use:

- prefer `cellpainting-skills run` when you want a named task
- prefer suite commands when you want one tool family
- prefer `run-pipeline-preset` when you want a named bundle from the main CLI

## MCP And Agent-Facing CLI

The same toolkit can also be exposed as MCP tools.

The main MCP-related commands are:

- `serve-mcp`
- `list-mcp-tools`
- `show-mcp-tool-catalog`
- `run-mcp-tool`

This is the bridge layer used by OpenClaw and other MCP-capable clients.

## Minimal First Session

A simple first CLI session can look like this:

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills list
cellpainting-skills describe --skill run-segmentation-workflow
cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind segmentation
cellpainting-skills run --config "$CONFIG" --skill run-segmentation-workflow
```

This already demonstrates the core CLI story of the project:

- inspect the task catalog
- inspect the relevant `.cppipe` selection
- run one named task

## Related Pages

- [Skills](../skills/index.md)
- [API](../api/index.md)
- [OpenClaw](../openclaw/index.md)
