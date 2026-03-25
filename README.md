# cellpaint_pipeline_lib

`cellpaint_pipeline_lib` packages the validated Cell Painting workflow into a reusable Python library, CLI, and agent-facing integration layer.

The library keeps the validated backend workspaces in place while providing:

- stable configuration loading
- stable CLI entrypoints
- stable Python public APIs
- data-access planning helpers for Cell Painting Gallery and JUMP-style sources
- segmentation and DeepProfiler integration paths
- MCP and agent integration surfaces for NanoBot and OpenClaw

## Scope

The current library covers four major areas:

1. Data access and download planning
2. Profiling and evaluation
3. Segmentation, single-cell crops, and preview generation
4. DeepProfiler export, project assembly, profiling, and feature collection

The library is designed to sit alongside the validated backend workspaces rather than replace them immediately.

## Recommended Public API Order

When you need a stable library entrypoint, use this order:

1. `run_end_to_end_pipeline`
2. `run_pipeline_skill`
3. `run_pipeline_preset`
4. `run_deepprofiler_pipeline`

Example:

```python
import cellpaint_pipeline as cp

config = cp.ProjectConfig.from_json(
    "/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json"
)
result = cp.run_end_to_end_pipeline(config)
print(result.output_dir)
```

## Quick Start

Install into `lyx_env`:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
pip install -e .
```

Run the smoke test:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline smoke-test \
  --config configs/project_config.example.json \
  --output-path outputs/smoke_test_report.json
```

Run the default high-level workflow:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-end-to-end-pipeline \
  --config configs/project_config.example.json
```

## Release Workflow

For release-facing verification and packaging:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
./scripts/run_release_smoke_test.sh
./scripts/build_release_bundle.sh
```

Generated release artifacts are written under `dist/`.

## Public Surfaces

Primary Python entrypoints:

- `cellpaint_pipeline.ProjectConfig`
- `cellpaint_pipeline.run_end_to_end_pipeline`
- `cellpaint_pipeline.run_pipeline_skill`
- `cellpaint_pipeline.run_pipeline_preset`
- `cellpaint_pipeline.run_deepprofiler_pipeline`
- `cellpaint_pipeline.summarize_data_access`
- `cellpaint_pipeline.build_data_request`
- `cellpaint_pipeline.build_download_plan`
- `cellpaint_pipeline.execute_download_plan`
- `cellpaint_pipeline.run_mcp_server`

Primary CLI entrypoints:

- `run-end-to-end-pipeline`
- `run-pipeline-skill`
- `run-pipeline-preset`
- `run-deepprofiler-pipeline`
- `run-profiling-suite`
- `run-segmentation-suite`
- `plan-data-access`
- `execute-download-plan`
- `serve-mcp`

## OpenClaw Release Tracks

Two OpenClaw deployment tracks are maintained:

- `integrations/openclaw/autodl/`
  Preferred for AutoDL-like platforms that do not support nested Docker.
- `integrations/openclaw/docker/`
  Preferred for standard Linux hosts with real Docker support.

Both tracks now use env-driven provider setup. Repository-managed JSON templates do not store provider keys.

## Documentation Map

- `docs/install.md`: environment and installation
- `docs/usage_guide.md`: common CLI and workflow usage patterns
- `docs/python_api_help.md`: Python-side API overview
- `docs/public_api_contract.md`: stable public API contract
- `docs/public_api_output_contract.md`: canonical output contract
- `docs/config_contract.md`: configuration schema guidance
- `configs/project_config.portable.example.json`: portable distribution template
- `docs/library_design.md`: architecture and design decisions
- `docs/testing.md`: test tiers and commands
- `docs/first_run_guide.md`: shortest external first-run guide
- `docs/release_quickstart.md`: shortest path from clean checkout to release bundle
- `docs/publishing_guide.md`: publication-safe sharing guidance
- `docs/release_readiness_checklist.md`: publication checklist
- `docs/nanobot_mcp_preparation.md`: MCP and NanoBot integration notes

## Publication Hygiene

Repository docs and config templates are English-only and do not store provider keys.

If a provider key was previously typed into a shell, written into a local config, or pasted into chat, rotate or revoke it before publishing the project.
