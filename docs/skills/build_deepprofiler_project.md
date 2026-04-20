---
orphan: true
---

# `build-deepprofiler-project`

`build-deepprofiler-project` is the skill for assembling a runnable DeepProfiler project directory from a DeepProfiler export.

This skill reads the DeepProfiler export manifest, builds the project config and metadata files, stages the location files, and writes a `project_manifest.json`.

Use it when you want to:

- turn a DeepProfiler export into a runnable project
- inspect the exact project layout before profiling
- hand a complete project directory to DeepProfiler

## CLI

```bash
CONFIG=configs/project_config.demo.json
EXPORT_ROOT=outputs/demo_deepprofiler_export

cellpainting-skills run \
  --config "$CONFIG" \
  --skill build-deepprofiler-project \
  --export-root "$EXPORT_ROOT" \
  --output-dir outputs/demo_deepprofiler_project
```

## Agent Examples

- `Build a runnable DeepProfiler project from this export root.`
- `Assemble the DeepProfiler project directory but do not profile it yet.`

## Outputs

- `project_manifest.json`
- `inputs/config/`
- `inputs/metadata/`
- `inputs/locations/`
- `pipeline_skill_manifest.json`

## Related Skills

- [export-deepprofiler-inputs](export_deepprofiler_inputs.md)
- [run-deepprofiler-profile](run_deepprofiler_profile.md)
