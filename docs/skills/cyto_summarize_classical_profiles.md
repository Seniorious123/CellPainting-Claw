# `cyto-summarize-classical-profiles`

`cyto-summarize-classical-profiles` turns classical profile tables into a readable result bundle.

## Purpose

Use this skill when you want a compact report instead of only raw parquet files.

## Inputs

- one or more classical profile tables, usually from [cyto-select-profile-features](cyto_select_profile_features.md)
- summary settings from the project config or explicit user options
- an optional output directory

## Outputs

- `profile_summary.json`: a compact summary of the classical profiling result
- `well_metadata_summary.csv`: metadata-level summary table
- `top_variable_features.csv`: the top varying features
- `pca_coordinates.csv`: PCA coordinates for downstream inspection
- `pca_plot.png`: a quick PCA figure
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cyto-summarize-classical-profiles \
  --feature-selected-path outputs/cyto_feature_select/feature_selected.parquet \
  --output-dir outputs/cyto_summary
```

## Agent Use

Example request:

```text
Summarize the classical profile outputs in outputs/cyto_feature_select and write a readable report under outputs/cyto_summary.
```

## Related Skills

- [cyto-select-profile-features](cyto_select_profile_features.md)
