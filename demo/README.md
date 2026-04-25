# Demo Backend

This directory contains a **sanitized minimal demo backend** for CellPainting-Claw.

It is intentionally small and self-contained. The demo bundle includes:

- synthetic CPJUMP-style raw TIFF images
- minimal profiling metadata and CellProfiler-style tables
- CellProfiler `.cppipe` files copied into a repo-local demo backend
- a minimal segmentation backend with precomputed label masks and measurement tables
- a repo-local project config at `configs/project_config.demo.json`

The demo bundle is designed for **public validation of the toolkit surface**. It does not represent a biological dataset and is not intended for scientific interpretation.

Recommended public demo commands from the repository root:

```bash
CONFIG=configs/project_config.demo.json
SEG_ROOT=demo/workspace/outputs/demo_segmentation
PREVIEW_ROOT=demo/workspace/outputs/demo_previews

cellpainting-skills run \
  --config "$CONFIG" \
  --skill cp-extract-segmentation-artifacts \
  --output-dir "$SEG_ROOT"

cellpainting-skills run \
  --config "$CONFIG" \
  --skill cp-generate-segmentation-previews \
  --workflow-root "$SEG_ROOT" \
  --output-dir "$PREVIEW_ROOT"
```

The current public demo path is intentionally narrow: segmentation first, then preview generation from the produced workflow root. This is the part of the packaged demo assets that is currently re-run and documented in the public RTD pages.
