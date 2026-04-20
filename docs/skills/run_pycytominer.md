# `run-pycytominer`

`run-pycytominer` is the skill for running pycytominer on single-cell measurements and writing classical profile tables.

This skill runs aggregation, annotation, normalization, and feature selection on the single-cell measurements produced earlier in the workflow.

## Recommended Use

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

## Agent Examples

- `Run pycytominer on the single-cell measurements from this workflow.`
- `Generate the classical Cell Painting profile outputs.`

## Outputs

- `aggregated.parquet`
- `annotated.parquet`
- `normalized.parquet`
- `feature_selected.parquet`
- `pipeline_skill_manifest.json`

## Related Skills

- [export-single-cell-measurements](export_single_cell_measurements.md)
- [summarize-classical-profiles](summarize_classical_profiles.md)
