# Command-Line Interface

CellPainting-Claw provides **two main public CLI surfaces**:

- `cellpainting-claw`
- `cellpainting-skills`

It also exposes an **MCP-facing command layer** through `cellpainting-claw`, which is the bridge used by OpenClaw and other MCP-capable clients.

## How To Think About The CLI

The command-line layer is easiest to understand as **three interface groups**:

- the **main toolkit CLI** for direct shell access to toolkit capabilities
- the **skills CLI** for task-oriented execution through stable skill names
- the **MCP-facing CLI** for agent runtimes and automation systems

The main CLI is the broadest shell-facing surface, but it is not the only useful one.

## Main Toolkit CLI

The main toolkit CLI is `cellpainting-claw`.

It covers several capability groups.

### Configuration And Inspection

These commands help you inspect configuration and public surfaces:

- `show-config`
- `show-data-access`
- `check-data-access`
- `list-public-api-entrypoints`
- `show-public-api-contract`

### Data Access

These commands support dataset discovery, planning, and download preparation:

- `summarize-data-access`
- `plan-data-access`
- `execute-download-plan`
- `list-gallery-prefixes`
- `list-gallery-datasets`
- `list-gallery-sources`
- `cache-gallery-prefixes`
- `download-gallery-prefix`
- `download-gallery-source`
- `list-quilt-packages`
- `browse-quilt-package`
- `list-cpgdata-prefixes`
- `sync-cpgdata-index`
- `sync-cpgdata-inventory`

### Profiling And Segmentation Tools

These commands provide direct access to profiling-side and segmentation-side toolkit tasks:

- `run-profiling`
- `run-profiling-task`
- `run-profiling-suite`
- `run-evaluation`
- `run-segmentation`
- `run-segmentation-task`
- `run-segmentation-suite`
- `run-segmentation-bundle`
- `summarize-segmentation`
- `collect-validation-report`

### Combined And Preset-Oriented Runs

These commands expose broader combined runs and named task bundles:

- `run-full-pipeline`
- `run-end-to-end-pipeline`
- `list-pipeline-presets`
- `run-pipeline-preset`
- `list-pipeline-skills`
- `run-pipeline-skill`

### DeepProfiler-Oriented Commands

These commands cover DeepProfiler preparation and the dedicated DeepProfiler pipeline path:

- `export-deepprofiler-metadata`
- `build-deepprofiler-project`
- `run-deepprofiler-profile`
- `collect-deepprofiler-features`
- `run-deepprofiler-pipeline`
- `run-deepprofiler-full-stack`

### Utility Commands

Additional utility commands include:

- `smoke-test`
- `run-workflow`

## Skills CLI

The task-oriented CLI is `cellpainting-skills`.

Its main commands are:

- `list`
- `describe`
- `run`

Use this CLI when **named task execution** is a better fit than working directly with lower-level command families.

Minimal examples:

```bash
cellpainting-skills list
cellpainting-skills describe --skill run-profiling-workflow
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-profiling-workflow
```

## MCP And Agent-Facing CLI

The same toolkit can also be exposed as MCP tools.

The main MCP-oriented commands are:

- `serve-mcp`
- `list-mcp-tools`
- `show-mcp-tool-catalog`
- `run-mcp-tool`

This is the layer that OpenClaw talks to.

In practical terms:

- `cellpainting-claw` is the **direct shell-facing CLI**
- `serve-mcp` exposes the toolkit as **MCP tools**
- OpenClaw provides the **natural-language agent front end** on top of that MCP surface

## Minimal Examples

Use the bundled demo config first:

```bash
CONFIG=configs/project_config.demo.json
```

Inspect the two public CLI surfaces:

```bash
cellpainting-claw --help
cellpainting-skills --help
```

Run one small toolkit command:

```bash
cellpainting-claw run-profiling \
  --config "$CONFIG" \
  --backend native \
  --script-key validate-inputs
```

Run one task-oriented skill:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-profiling-workflow
```

Start the MCP server for OpenClaw or another MCP client:

```bash
cellpainting-claw serve-mcp \
  --transport streamable-http \
  --host 127.0.0.1 \
  --port 8768 \
  --path /mcp
```

## Relationship To Other Interfaces

For Python-side use, continue to:

- [Public Entrypoints](../api/public_entrypoints.md)
- [CellPainting-Skills](../skills/index.md)

For agent-mediated use, continue to:

- [OpenClaw](../openclaw/index.md)
