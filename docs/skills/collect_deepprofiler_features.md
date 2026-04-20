---
orphan: true
---

# `collect-deepprofiler-features`

`collect-deepprofiler-features` is the skill for collecting DeepProfiler feature files into analysis-ready tables.

This skill reads DeepProfiler `.npz` feature outputs and writes single-cell and well-level tabular outputs.

Use it when you want to:

- convert DeepProfiler outputs into tables
- prepare deep features for downstream analysis
- let an agent hand back a concrete feature directory instead of raw `.npz` files

## CLI

```bash
CONFIG=configs/project_config.demo.json
PROJECT_ROOT=outputs/demo_deepprofiler_project

cellpainting-skills run \
  --config "$CONFIG" \
  --skill collect-deepprofiler-features \
  --project-root "$PROJECT_ROOT" \
  --output-dir outputs/demo_deepprofiler_features
```

## Agent Examples

- `Collect the DeepProfiler outputs into single-cell and well-level tables.`
- `Turn the DeepProfiler feature files into analysis-ready tabular outputs.`

## Outputs

- `deepprofiler_single_cell.parquet`: single-cell DeepProfiler feature table in parquet format.
- `deepprofiler_single_cell.csv.gz`: single-cell DeepProfiler feature table in compressed CSV format.
- `deepprofiler_well_aggregated.parquet`: well-level aggregated DeepProfiler feature table in parquet format.
- `deepprofiler_well_aggregated.csv.gz`: well-level aggregated DeepProfiler feature table in compressed CSV format.
- `deepprofiler_feature_manifest.json`: manifest describing the collected DeepProfiler feature tables and source files.

## Related Skills

- [run-deepprofiler-profile](run_deepprofiler_profile.md)
