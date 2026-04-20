# `run-segmentation-masks`

`run-segmentation-masks` is the skill for running segmentation and writing mask artifacts plus sample previews.

## Summary

This skill prepares the segmentation load-data table, runs CellProfiler, generates sample previews, and summarizes the result.

## Recommended Use

Use this skill when you want to:

- produce segmentation masks, labels, and outlines
- generate quick preview PNGs for the segmentation inputs
- generate the object tables needed for crop export
- create the workflow root that later segmentation and DeepProfiler skills can reuse

## CLI

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-segmentation-masks \
  --output-dir outputs/demo_segmentation
```

## Agent Examples

- `Run the segmentation mask export for this config.`
- `Generate masks, labels, previews, and object tables for the segmentation workflow.`

## Outputs

- `cellprofiler_masks/`
- `labels/`
- `outlines/`
- `sample_previews_png/`
- `segmentation_summary.json`
- `pipeline_skill_manifest.json`

## Related Skills

- [export-single-cell-crops](export_single_cell_crops.md)
- [prepare-deepprofiler-project](prepare_deepprofiler_project.md)
