# NanoBot MCP Preparation

This document describes how `cellpaint_pipeline_lib` is prepared for NanoBot-style MCP integration.

## Goal

The agent should not have to understand the full internal workflow tree.

Instead, it should be able to operate through:

- stable public API entrypoints
- stable preset and skill names
- a machine-readable MCP tool catalog
- predictable output contracts

## Current MCP Design

The library exposes an MCP-friendly layer through `cellpaint_pipeline.mcp_tools`.

That layer reorganizes the stable library surface into three categories:

- `public_api`
- `preset`
- `skill`

## Current MCP Tool Catalog

Discovery tools:

- `list_public_api_entrypoints`
- `show_public_api_contract`
- `list_pipeline_skills`
- `list_pipeline_presets`

Execution tools:

- `run_public_api_entrypoint`
- `run_pipeline_skill`
- `run_pipeline_preset`

## Python Interface

```python
import cellpaint_pipeline as cp

catalog = cp.mcp_tool_catalog()
payload = cp.run_mcp_tool_to_dict(
    'run_public_api_entrypoint',
    entrypoint='build_data_request',
    params={
        'mode': 'gallery-prefix',
        'prefix': 'cpg0016-jump/source_4/workspace/',
        'dry_run': True,
    },
)
```

## CLI Interface

```bash
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline list-mcp-tools
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline show-mcp-tool-catalog
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-mcp-tool --tool run_public_api_entrypoint --params-json '{"entrypoint":"build_data_request","params":{"mode":"gallery-prefix","prefix":"cpg0016-jump/source_4/workspace/","dry_run":true}}'
```

## Why This Layer Fits NanoBot

NanoBot-style agents benefit from:

- stable tool names
- stable input requirements
- explicit config requirements
- predictable return payloads

They should not be forced to infer internal workflow keys from scratch.

## Current MCP Server Entry

The repository includes `cellpaint_pipeline.mcp_server` and exposes:

- `create_mcp_server()`
- `run_mcp_server()`

CLI example:

```bash
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline serve-mcp --transport stdio
```

If the `mcp` SDK is not installed, the command fails explicitly rather than silently.

## NanoBot Handoff Files

Ready-to-adapt NanoBot artifacts live under:

- `integrations/nanobot/nanobot.yaml.example`
- `integrations/nanobot/quickstart.md`

## Natural Next Steps

1. keep MCP tool schemas stable
2. add long-running task status and run-history tools if needed
3. map NanoBot prompts onto the stable MCP tool catalog instead of low-level scripts
