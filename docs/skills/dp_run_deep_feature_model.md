# `dp-run-deep-feature-model`

`dp-run-deep-feature-model` runs the DeepProfiler model on a prepared project.

## Purpose

Use this skill when you want the raw model outputs from DeepProfiler.

## Inputs

- a prepared DeepProfiler project from [dp-build-deep-feature-project](dp_build_deep_feature_project.md)
- runtime settings such as device or GPU selection
- an optional output directory

## Outputs

- DeepProfiler feature files under the project output directories
- model execution logs
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill dp-run-deep-feature-model \
  --project-root outputs/dp_project \
  --output-dir outputs/dp_model_run
```

## Agent Use

Example request:

```text
Run the DeepProfiler model for the prepared project in outputs/dp_project and write the run outputs under outputs/dp_model_run.
```

## Related Skills

- [dp-collect-deep-features](dp_collect_deep_features.md)
