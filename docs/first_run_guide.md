# First Run Guide

This page is the shortest external-facing guide for a new user.

## Goal

Run a minimal validated check of `cellpaint_pipeline_lib` without touching advanced integrations first.

## 1. Create or Reuse `lyx_env`

```bash
conda env create -f /root/pipeline/cellpaint_pipeline_lib/environment/lyx_env_reference.yml
conda activate lyx_env
```

## 2. Install the Package

```bash
cd /root/pipeline/cellpaint_pipeline_lib
pip install -e .
```

## 3. Choose a Config Template

Use one of these:

- `configs/project_config.example.json`
  Validated machine-local reference.
- `configs/project_config.portable.example.json`
  Better starting point for a new machine or for distribution.

## 4. Verify the Config

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline show-config \
  --config configs/project_config.portable.example.json
```

## 5. Run the Minimal Smoke Test

```bash
cd /root/pipeline/cellpaint_pipeline_lib
./scripts/run_release_smoke_test.sh
```

## 6. Run a Main Pipeline Entry

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-end-to-end-pipeline \
  --config configs/project_config.example.json
```

## 7. Agent Integrations

When the core workflow is validated, continue with:

- `integrations/openclaw/`
- `integrations/nanobot/`
- `docs/nanobot_mcp_preparation.md`

## 8. Release Packaging

```bash
cd /root/pipeline/cellpaint_pipeline_lib
./scripts/build_release_bundle.sh
```
