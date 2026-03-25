# Usage Guide

## Configuration

Start from:

- `configs/project_config.example.json`

The most important fields to edit are:

- `python_executable`
- `profiling_backend_root`
- `segmentation_backend_root`
- `workspace_root`
- `default_output_root`
- `deepprofiler_export_root`

Runtime tuning blocks:

- `mask_export_runtime`
- `deepprofiler_runtime`

## Common CLI Commands

Show the resolved configuration:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw show-config           --config configs/project_config.example.json
```

Run the default top-level pipeline:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-end-to-end-pipeline           --config configs/project_config.example.json
```

Run a named skill:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-pipeline-skill           --config configs/project_config.example.json           --skill run-full-workflow
```

Run a named preset:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-pipeline-preset           --config configs/project_config.example.json           --preset full-pipeline
```

Run a profiling-only suite:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-profiling-suite           --config configs/project_config.example.json           --suite native
```

Run a segmentation-only suite:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-segmentation-suite           --config configs/project_config.example.json           --suite mask-export
```

Run the standardized DeepProfiler branch:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-deepprofiler-pipeline           --config configs/project_config.example.json           --workflow-root /path/to/segmentation_workflow
```

## Data-Access CLI

Summarize the available data-access backends:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw summarize-data-access           --config configs/project_config.example.json
```

Build a gallery download plan:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw plan-data-access           --config configs/project_config.example.json           --mode gallery-source           --dataset-id cpg0016-jump           --source-id source_4           --subprefix workspace           --dry-run           --output-path outputs/download_plan.json
```

Execute a saved plan:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw execute-download-plan           --config configs/project_config.example.json           --plan-path outputs/download_plan.json
```

## MCP Server

Start the MCP server with HTTP transport:

```bash
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw serve-mcp           --transport streamable-http           --host 127.0.0.1           --port 8768           --path /mcp
```

## OpenClaw on AutoDL-Like Hosts

Configure an OpenAI-compatible provider for the active OpenClaw runtime:

```bash
cd /root/pipeline/CellPainting-Claw/integrations/openclaw/autodl
cp provider.env.example provider.env
# edit provider.env
./configure_openai_compatible_provider.sh
```

Start the background stack:

```bash
./start_openclaw_stack_bg.sh
./check_openclaw_stack.sh
```

Launch the terminal UI:

```bash
./run_openclaw_tui.sh
```

## Validated Example Outputs

The repository already contains validated DeepProfiler workflow artifacts under:

- `outputs/workflows/deepprofiler_full_stack_validation`
- `outputs/workflows/deepprofiler_full_stack_validation/workflow_manifest.json`
- `outputs/workflows/deepprofiler_full_stack_validation/run_report.md`
- `outputs/workflows/deepprofiler_full_stack_validation/deepprofiler_tables/deepprofiler_feature_manifest.json`

These are useful demonstration artifacts, but they are not part of the stable public API contract.
