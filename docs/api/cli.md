# Command-Line Interface

CellPainting-Claw provides two main public CLI surfaces:

- `cellpainting-claw`
- `cellpainting-skills`

It also exposes an agent-facing MCP surface through the main CLI, which is the bridge used by OpenClaw and other MCP-capable clients.

## How To Read This Page

The command-line layer is easiest to understand in three parts:

- the main workflow CLI for direct pipeline execution
- the skills CLI for task-oriented execution
- the MCP-facing CLI for agent runtimes such as OpenClaw

The main CLI remains the canonical shell-facing interface.

## Main Workflow CLI

The main CLI is the broadest command-line surface. Important commands include:

- `show-config`
- `show-data-access`
- `check-data-access`
- `summarize-data-access`
- `plan-data-access`
- `execute-download-plan`
- `smoke-test`
- `run-end-to-end-pipeline`
- `run-profiling-suite`
- `run-segmentation-suite`
- `run-workflow`
- `run-deepprofiler-pipeline`

For most users, `run-end-to-end-pipeline` is the default CLI entrypoint.

## Skills CLI

The skills CLI is a narrower task-oriented surface. Its main commands are:

- `list`
- `describe`
- `run`

Use this CLI when named task execution is a better fit than working directly with lower-level workflow options.

## MCP and Agent-Facing CLI

The same library can also be exposed as MCP tools.

The main MCP-oriented commands are:

- `serve-mcp`
- `list-mcp-tools`
- `show-mcp-tool-catalog`
- `run-mcp-tool`
- `list-public-api-entrypoints`
- `show-public-api-contract`
- `run-public-api-entrypoint`

This is the layer that OpenClaw talks to. In other words:

- `cellpainting-claw` is the direct human-facing CLI
- `serve-mcp` exposes the workflow as MCP tools
- OpenClaw provides the natural-language agent front end on top of that MCP surface

## Minimal Examples

Define one config variable first:

```bash
CONFIG=configs/project_config.portable.example.json
```

Inspect the CLI surface:

```bash
cellpainting-claw --help
cellpainting-skills --help
```

Run the standard top-level workflow:

```bash
cellpainting-claw run-end-to-end-pipeline --config "$CONFIG"
```

Start the MCP server for OpenClaw or another MCP client:

```bash
cellpainting-claw serve-mcp \
  --transport streamable-http \
  --host 127.0.0.1 \
  --port 8768 \
  --path /mcp
```

Inspect the MCP tool layer directly:

```bash
cellpainting-claw list-mcp-tools
cellpainting-claw show-mcp-tool-catalog
```

Inspect the skills catalog:

```bash
cellpainting-skills list
```

## Related Pages

For more detail, continue to:

- [Quick Start](../quick_start/index.md)
- [Running the Full Pipeline](../workflows/running_the_full_pipeline.md)
- [OpenClaw](../openclaw/index.md)
