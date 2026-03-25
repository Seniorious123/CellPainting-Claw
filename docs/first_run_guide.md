# First Run Guide

This page is the shortest external-facing guide for a new user.

## Goal

Run a minimal validated check of `CellPainting-Claw` without touching advanced integrations first.

## 1. Create or Reuse `cellpainting-claw`

```bash
conda env create -f /root/pipeline/CellPainting-Claw/environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
```

## 2. Install the Package

```bash
cd /root/pipeline/CellPainting-Claw
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
cd /root/pipeline/CellPainting-Claw
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw show-config \
  --config configs/project_config.portable.example.json
```

## 5. Run the Minimal Smoke Test

```bash
cd /root/pipeline/CellPainting-Claw
./scripts/run_release_smoke_test.sh
```

## 6. Run a Main Pipeline Entry

```bash
cd /root/pipeline/CellPainting-Claw
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw run-end-to-end-pipeline \
  --config configs/project_config.example.json
```

## 7. Agent Integrations

When the core workflow is validated, continue with:

- `integrations/openclaw/`
- `integrations/nanobot/`
- `docs/nanobot_mcp_preparation.md`

## 8. Release Packaging

```bash
cd /root/pipeline/CellPainting-Claw
./scripts/build_release_bundle.sh
```
