---
orphan: true
---

# `run-deepprofiler-profile`

`run-deepprofiler-profile` is the skill for executing the DeepProfiler model on a prepared project directory.

This skill runs the DeepProfiler `profile` command against an existing project and writes feature files under the project output directory.

Use it when you want to:

- generate DeepProfiler embeddings
- run the deep model after the project has been assembled
- let an agent launch the model itself rather than only preparing inputs

## CLI

```bash
CONFIG=configs/project_config.demo.json
PROJECT_ROOT=outputs/demo_deepprofiler_project

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-deepprofiler-profile \
  --project-root "$PROJECT_ROOT" \
  --output-dir outputs/demo_deepprofiler_profile \
  --gpu 0
```

## Agent Examples

- `Run the DeepProfiler model on this prepared project.`
- `Profile the DeepProfiler project and generate embedding files.`

## Outputs

- `outputs/<experiment>/features/` under the project root
- DeepProfiler log output
- `pipeline_skill_manifest.json`

## Related Skills

- [build-deepprofiler-project](build_deepprofiler_project.md)
- [collect-deepprofiler-features](collect_deepprofiler_features.md)
