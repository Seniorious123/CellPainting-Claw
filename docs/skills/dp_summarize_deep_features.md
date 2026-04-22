# `dp-summarize-deep-features`

`dp-summarize-deep-features` turns deep-feature tables into a readable result bundle.

## Purpose

Use this skill when you want a compact summary of the DeepProfiler result instead of only raw feature tables.

## Inputs

- deep-feature tables from [dp-collect-deep-features](dp_collect_deep_features.md), or equivalent tables provided by the user
- summary settings from the project config or explicit user options
- an optional output directory

## Outputs

- `profile_summary.json`: a compact summary of the deep-feature result
- `well_metadata_summary.csv`: metadata-level summary table
- `top_variable_features.csv`: the top varying features
- `pca_coordinates.csv`: PCA coordinates for downstream inspection
- `pca_plot.png`: a quick PCA figure
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill dp-summarize-deep-features \
  --single-cell-parquet-path outputs/dp_features/deepprofiler_single_cell.parquet \
  --well-aggregated-parquet-path outputs/dp_features/deepprofiler_well_aggregated.parquet \
  --output-dir outputs/dp_summary
```

## Agent Use

Example request:

```text
Summarize the DeepProfiler outputs in outputs/dp_features and write a readable report under outputs/dp_summary.
```

## Related Skills

- [dp-collect-deep-features](dp_collect_deep_features.md)
