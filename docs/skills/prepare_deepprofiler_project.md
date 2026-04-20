# `prepare-deepprofiler-project`

`prepare-deepprofiler-project` is the public skill for stopping at a runnable DeepProfiler project directory.

This skill prepares the DeepProfiler project stage and writes the project manifest, config, metadata, and locations layout.

It can start from:

- a segmentation workflow root
- an existing DeepProfiler export root
- explicit `Image.csv`, `Nuclei.csv`, and load-data CSV paths

## Recommended Use

Use this skill when you want to:

- prepare the DeepProfiler inputs and project, but not run the model yet
- inspect the exact project layout before profiling
- hand a ready-to-run project directory to another user or system

## CLI

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill prepare-deepprofiler-project \
  --workflow-root "$WORKFLOW_ROOT" \
  --output-dir outputs/demo_deepprofiler_project_ready
```

## Agent Examples

- `Prepare a runnable DeepProfiler project from this segmentation workflow root, but do not run DeepProfiler yet.`
- `Build the DeepProfiler project directory and stop there.`

## Outputs

- `project_manifest.json`: manifest describing the prepared DeepProfiler project layout and key paths.
- `inputs/config/`: DeepProfiler config files staged for the runnable project.
- `inputs/metadata/`: metadata files staged for the runnable project.
- `inputs/locations/`: location files staged for the runnable project.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [export-single-cell-crops](export_single_cell_crops.md)
- [run-deepprofiler](run_deepprofiler.md)
