# `dp-build-deep-feature-project`

`dp-build-deep-feature-project` assembles a runnable DeepProfiler project directory.

## Purpose

Use this skill when you want a DeepProfiler project that is ready to execute next.

## Inputs

- a prepared deep-feature input bundle from [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md), or an equivalent export root provided by the user
- experiment metadata and project settings
- an optional output directory

## Outputs

- `project_manifest.json`: the DeepProfiler project manifest
- `inputs/config/`: staged config files
- `inputs/metadata/`: staged metadata files
- `inputs/locations/`: staged location files
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill dp-build-deep-feature-project \
  --export-root outputs/dp_inputs \
  --output-dir outputs/dp_project
```

## Agent Use

Example request:

```text
Build a runnable DeepProfiler project from outputs/dp_inputs and write it under outputs/dp_project.
```

## Related Skills

- [dp-run-deep-feature-model](dp_run_deep_feature_model.md)
