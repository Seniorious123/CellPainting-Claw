# `cp-prepare-segmentation-inputs`

`cp-prepare-segmentation-inputs` prepares the load-data table used by the segmentation pipeline.

## Purpose

Use this skill when you want to confirm which fields will be sent into segmentation before running CellProfiler.

## Inputs

- image metadata
- a project config
- optional plate, well, or site filters
- an optional output directory

The image metadata can be provided by the repository for demo runs or by the user for custom runs.

## Outputs

- `load_data_for_segmentation.csv`: the load-data table used by segmentation
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cp-prepare-segmentation-inputs \
  --output-dir outputs/segmentation_inputs
```

## Agent Use

Example request:

```text
Prepare the segmentation inputs for configs/project_config.demo.json and write the load-data table under outputs/segmentation_inputs.
```

## Related Skills

- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
