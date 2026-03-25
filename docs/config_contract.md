# Config Contract

This document defines how to read `project_config.example.json` and which configuration fields should be treated as required, recommended, or advanced.

## Machine-Readable Helpers

Use these helpers from `cellpaint_pipeline.config` or the package root:

- `project_config_field_guide()`
- `data_access_config_field_guide()`
- `project_config_contract_summary()`

## Top-Level Rule

### Required top-level fields

These must be present in the JSON for `ProjectConfig.from_json(...)` to succeed cleanly:

- `project_name`
- `profiling_backend_root`
- `segmentation_backend_root`
- `workspace_root`
- `default_output_root`
- `deepprofiler_export_root`

### Recommended top-level fields

These have defaults or fallback behavior, but should usually be set explicitly for reproducibility:

- `python_executable`
- `profiling_backend_config`
- `segmentation_backend_config`
- `deepprofiler_project_root`
- `data_access`

### Advanced top-level fields

These are runtime-tuning blocks and are not required for a minimal successful parse:

- `mask_export_runtime`
- `deepprofiler_runtime`

## data_access block

The entire `data_access` block is optional, but these fields are strongly recommended if you want stable planning behavior:

- `default_dataset_id`
- `default_source_id`
- `data_cache_root`
- `index_cache_root`

Most infrastructure fields already have defaults aligned with the current Cell Painting Gallery environment, including:

- `gallery_bucket = cellpainting-gallery`
- `gallery_region = us-east-1`
- `quilt_registry = s3://cellpainting-gallery`
- `cpgdata_inventory_bucket = cellpainting-gallery-inventory`

## Minimal practical config

A minimal practical config for this library should explicitly pin:

- backend roots
- workspace root
- default output root
- DeepProfiler export root
- Python executable
- default dataset/source for data-access planning

## Example files

Validated machine-local reference:

- `/root/pipeline/CellPainting-Claw/configs/project_config.example.json`

Portable distribution template:

- `/root/pipeline/CellPainting-Claw/configs/project_config.portable.example.json`

Use `show-config` after editing the JSON to confirm all relative paths resolve the way you expect.
