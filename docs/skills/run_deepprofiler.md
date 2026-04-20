# `run-deepprofiler`

`run-deepprofiler` is the public skill for running the DeepProfiler path and returning analysis-ready tables.

This skill gives users the final DeepProfiler result rather than one intermediate stage.

Depending on the inputs you provide, it can:

- start from a prepared `project_root`
- or start from a segmentation workflow root or explicit source CSVs and run the full DeepProfiler chain

The final result is the collected single-cell and well-level feature tables.

## Recommended Use

Use this skill when you want to:

- run the DeepProfiler branch as one user-facing task
- get collected feature tables instead of only raw feature files
- let an agent complete the whole deep-feature step without exposing internal stages

## CLI

```bash
CONFIG=configs/project_config.demo.json
PROJECT_ROOT=outputs/demo_deepprofiler_project_ready/deepprofiler_project

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-deepprofiler \
  --project-root "$PROJECT_ROOT" \
  --output-dir outputs/demo_deepprofiler_results \
  --gpu 0
```

You can also start from a workflow root instead of a prepared project:

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-deepprofiler \
  --workflow-root "$WORKFLOW_ROOT" \
  --output-dir outputs/demo_deepprofiler_results \
  --gpu 0
```

## Agent Examples

- `Run DeepProfiler from this segmentation workflow root and return the final tables.`
- `Run DeepProfiler on this prepared project and collect the feature outputs into analysis-ready files.`

## Outputs

- `deepprofiler_single_cell.parquet`
- `deepprofiler_single_cell.csv.gz`
- `deepprofiler_well_aggregated.parquet`
- `deepprofiler_well_aggregated.csv.gz`
- `deepprofiler_feature_manifest.json`
- `pipeline_skill_manifest.json`

## Related Skills

- [prepare-deepprofiler-project](prepare_deepprofiler_project.md)
- [summarize-deepprofiler-profiles](summarize_deepprofiler_profiles.md)
