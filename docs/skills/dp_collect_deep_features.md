# `dp-collect-deep-features`

`dp-collect-deep-features` converts raw DeepProfiler outputs into analysis-ready tables.

## Purpose

Use this skill when you want single-cell and aggregated deep-feature tables instead of only raw model files.

## Inputs

- a completed DeepProfiler project or run directory from [dp-run-deep-feature-model](dp_run_deep_feature_model.md)
- collection settings from the project config or explicit user options
- an optional output directory

## Outputs

- `deepprofiler_single_cell.parquet`: single-cell deep-feature table
- `deepprofiler_well_aggregated.parquet`: aggregated deep-feature table
- `deepprofiler_feature_manifest.json`: the collected feature manifest
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill dp-collect-deep-features \
  --project-root outputs/dp_project \
  --output-dir outputs/dp_features
```

## Agent Use

Example request:

```text
Collect the DeepProfiler outputs from outputs/dp_project into tabular feature files under outputs/dp_features.
```

## Related Skills

- [dp-summarize-deep-features](dp_summarize_deep_features.md)
