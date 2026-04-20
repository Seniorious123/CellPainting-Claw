# `run-pycytominer`

`run-pycytominer` is the skill for running the configured pycytominer processing path and writing classical profile tables.

## What It Does

This skill runs aggregation, annotation, normalization, and feature selection on the configured single-cell measurements.

## When To Use It

Use this skill when you want to:

- generate classical Cell Painting profiles
- produce pycytominer outputs for downstream statistics or modeling
- standardize single-cell measurements into well-level analysis tables

## CLI

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-pycytominer \
  --output-dir outputs/demo_pycytominer
```

## Agent Request Examples

- `Run pycytominer on the configured single-cell measurements.`
- `Generate the classical Cell Painting profile outputs.`

## Typical Outputs

- `aggregated.parquet`
- `annotated.parquet`
- `normalized.parquet`
- `feature_selected.parquet`
- `pipeline_skill_manifest.json`

## Related Skills

- [export-single-cell-measurements](export_single_cell_measurements.md)
- [summarize-classical-profiles](summarize_classical_profiles.md)
