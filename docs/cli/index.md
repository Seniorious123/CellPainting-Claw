# Command-Line Interface

CellPainting-Claw exposes **two public CLI surfaces**:

- `cellpainting-skills`
- `cellpainting-claw`

For most users, the right starting point is **`cellpainting-skills`**.

## Choose The Right CLI

| If you want to... | Start with | Why |
| --- | --- | --- |
| run one clear named task such as segmentation or DeepProfiler preparation | `cellpainting-skills` | this is the shortest path from a user goal to a documented task |
| inspect configuration, inspect `.cppipe` selection, use data-access helpers, or expose MCP tools | `cellpainting-claw` | this is the direct toolkit CLI |

## `cellpainting-skills`: The First CLI For Most Users

`cellpainting-skills` is the named-task CLI.

Its three main commands are:

| Command | What it does |
| --- | --- |
| `list` | show the public skill catalog |
| `describe` | show what one skill does |
| `run` | execute one named skill |

## Minimal First Session

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills list
cellpainting-skills describe --skill run-segmentation
cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-segmentation
```

This is the main CLI path that new users should understand first:

- inspect the available skills
- inspect one skill
- run one named task

## `cellpainting-claw`: The Direct Toolkit CLI

Use `cellpainting-claw` when you need commands that are more specific than a named skill.

The most useful command groups for normal users are:

| Command group | What it is for | Example commands |
| --- | --- | --- |
| configuration and `.cppipe` inspection | inspect config state and CellProfiler pipeline selection | `show-config`, `show-cppipe-selection`, `validate-cppipe-config` |
| data access | inspect data sources, build plans, and execute downloads | `summarize-data-access`, `plan-data-access`, `execute-download-plan` |
| direct toolkit runs | run specific toolkit-side commands when you want more control | `run-segmentation`, `run-profiling`, `run-evaluation`, `run-deepprofiler-pipeline` |
| MCP bridge | expose or inspect the MCP interface used by agent runtimes | `serve-mcp`, `list-mcp-tools`, `run-mcp-tool` |

## Example: Inspect The Selected `.cppipe`

```bash
CONFIG=configs/project_config.demo.json

cellpainting-claw show-cppipe-selection \
  --config "$CONFIG" \
  --kind segmentation

cellpainting-claw validate-cppipe-config \
  --config "$CONFIG"
```

Current public behavior:

- **segmentation** uses the selected `.cppipe` at runtime
- **profiling** exposes the same inspection and validation commands
- custom segmentation overrides are treated as ready-to-run mask-export pipelines

## Example: Inspect Or Plan Data Access

```bash
CONFIG=configs/project_config.demo.json

cellpainting-claw summarize-data-access \
  --config "$CONFIG"

cellpainting-claw plan-data-access \
  --config "$CONFIG"
```

## Example: Expose The MCP Bridge

```bash
cellpainting-claw serve-mcp --transport stdio
```

This is the bridge interface used by OpenClaw and other MCP-capable clients.

## What This Page Does Not Cover

The toolkit CLI also contains additional lower-level or bundled commands. Those exist in the codebase, but they are **not the main starting point for most users**, so this page focuses on the commands that are most useful first.

## Related Pages

- [Skills](../skills/index.md)
- [OpenClaw](../openclaw/index.md)
- [Quick Start](../quick_start/index.md)
