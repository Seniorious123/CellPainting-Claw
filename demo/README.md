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
cellpainting-claw run-profiling --config configs/project_config.demo.json --backend native --script-key build-image-manifest
cellpainting-claw run-profiling --config configs/project_config.demo.json --backend native --script-key validate-inputs
cellpainting-claw run-profiling --config configs/project_config.demo.json --backend native --script-key export-cellprofiler-to-singlecell
cellpainting-claw run-profiling --config configs/project_config.demo.json --backend native --script-key run-pycytominer
cellpainting-claw run-segmentation --config configs/project_config.demo.json --backend native --script-key prepare-load-data
cellpainting-claw run-segmentation --config configs/project_config.demo.json --backend native --script-key build-mask-export-pipeline
cellpainting-claw run-segmentation --config configs/project_config.demo.json --backend native --script-key generate-sample-previews --overwrite
cellpainting-claw run-segmentation --config configs/project_config.demo.json --backend native --script-key extract-single-cell-crops --mode masked
cellpainting-claw run-segmentation --config configs/project_config.demo.json --backend native --script-key generate-png-previews --mode masked
```
