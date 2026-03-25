---
name: cellpaint-pipeline
description: Use the validated Cell Painting pipeline library through stable CLI, public API, and optional MCP entrypoints.
---

# Cell Painting Pipeline

Use this skill when the user wants to discover, run, or summarize the standardized Cell Painting workflow library.

## Goal

Translate natural-language requests into stable `cellpaint_pipeline_lib` entrypoints rather than custom shell chains.

## Base command

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline
```

## Preferred order

1. Discovery

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline list-mcp-tools
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline show-public-api-contract
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline list-pipeline-skills
```

2. Task-oriented execution

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-pipeline-skill --config /root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json --skill run-full-workflow
```

3. Stable public API dispatch

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-public-api-entrypoint --config /root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json --entrypoint run_end_to_end_pipeline
```

## Useful skill keys

- `plan-gallery-data`
- `run-profiling-workflow`
- `run-segmentation-workflow`
- `run-deepprofiler-export`
- `run-deepprofiler-full`
- `run-full-workflow`
- `run-full-workflow-with-data-plan`

## Reporting expectations

For each run, report:

- command or entrypoint used
- config path
- output directory
- whether artifacts include masks, pycytominer outputs, or DeepProfiler outputs

## Optional MCP route

If the host is configured to use MCP, start the server with:

```bash
/root/pipeline/cellpaint_pipeline_lib/integrations/openclaw/start_cellpaint_mcp_http.sh
```

Then prefer the MCP tools that mirror the same public surfaces:

- `list_public_api_entrypoints`
- `show_public_api_contract`
- `list_pipeline_skills`
- `run_pipeline_skill`
- `run_public_api_entrypoint`
