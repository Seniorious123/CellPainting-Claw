# CellPainting-Claw

CellPainting-Claw is a release-oriented software interface for validated Cell Painting workflows.

It turns a previously script-heavy analysis setup into a cleaner package with four public layers:

- a Python API for reproducible workflow execution
- a CLI for standardized pipeline runs
- a skill layer for agent-facing task routing
- MCP integration surfaces for OpenClaw and related MCP-compatible agents

The project is designed to sit on top of validated backend workspaces rather than hide them. In practice, that means you can keep the proven profiling, segmentation, and DeepProfiler assets, while exposing them through a cleaner and more automatable interface.

## Project Naming

This repository uses two public names on purpose:

- `CellPainting-Claw` is the main project, package distribution, and full workflow interface
- `CellPainting-Skills` is the skill-oriented layer for agent and automation entrypoints

In Python, that maps to:

- `import cellpainting_claw as cp`
- `import cellpainting_skills as cps`

On the command line, that maps to:

- `cellpainting-claw`
- `cellpainting-skills`

## Scope

The current release covers four major areas:

1. Data access and download planning
2. Profiling and evaluation
3. Segmentation, single-cell crops, and preview generation
4. DeepProfiler export, project assembly, profiling, and feature collection

## Recommended Public API Order

When you need a stable top-level entrypoint, use this order:

1. `run_end_to_end_pipeline`
2. `run_pipeline_skill`
3. `run_pipeline_preset`
4. `run_deepprofiler_pipeline`

Main package example:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json(
    "configs/project_config.example.json"
)
result = cp.run_end_to_end_pipeline(config)
print(result.output_dir)
```

Skill-layer example:

```python
import cellpainting_skills as cps

print(cps.available_pipeline_skills())
```

## Quick Start

Create an environment and install the package:

```bash
cd <repo-root>
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
export PYTHON_BIN="$(command -v python)"
```

Run the lightweight smoke test:

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw smoke-test \
  --config configs/project_config.example.json \
  --output-path outputs/smoke_test_report.json
```

Run the default high-level workflow:

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-end-to-end-pipeline \
  --config configs/project_config.example.json
```

Inspect the skill catalog:

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_skills list
```

## Release Workflow

For release-facing verification and packaging:

```bash
cd <repo-root>
./scripts/run_release_smoke_test.sh
./scripts/build_release_bundle.sh
```

Generated release artifacts are written under `dist/`.

## Public Surfaces

Primary Python entrypoints through `cellpainting_claw`:

- `cellpainting_claw.ProjectConfig`
- `cellpainting_claw.run_end_to_end_pipeline`
- `cellpainting_claw.run_pipeline_skill`
- `cellpainting_claw.run_pipeline_preset`
- `cellpainting_claw.run_deepprofiler_pipeline`
- `cellpainting_claw.summarize_data_access`
- `cellpainting_claw.build_data_request`
- `cellpainting_claw.build_download_plan`
- `cellpainting_claw.execute_download_plan`
- `cellpainting_claw.run_mcp_server`

Primary skill-layer entrypoints through `cellpainting_skills`:

- `cellpainting_skills.available_pipeline_skills`
- `cellpainting_skills.get_pipeline_skill_definition`
- `cellpainting_skills.pipeline_skill_definition_to_dict`
- `cellpainting_skills.run_pipeline_skill`

Primary CLI entrypoints:

- `cellpainting-claw`
- `cellpainting-skills`
- `cellpainting-claw-tests`

## OpenClaw Release Tracks

Two OpenClaw deployment tracks are maintained:

- `integrations/openclaw/autodl/`
  Preferred for AutoDL-like platforms that do not support nested Docker.
- `integrations/openclaw/docker/`
  Preferred for standard Linux hosts with real Docker support.

Both tracks use env-driven provider setup. Repository-managed JSON templates do not store provider keys.

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
- `integrations/openclaw/`: OpenClaw deployment and runtime helpers

## Publication Hygiene

Repository docs and config templates are English-only and do not store provider keys.

If a provider key was previously typed into a shell, written into a local config, or pasted into chat, rotate or revoke it before publishing the project.
