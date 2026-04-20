# `export-single-cell-crops`

`export-single-cell-crops` is the public skill for exporting single-cell crop stacks from a segmentation workflow root.

This skill reads an existing segmentation workflow root and writes one crop package per segmented cell.

The key choice is the crop mode:

- `masked` removes background outside the cell mask
- `unmasked` keeps the surrounding local context

## Recommended Use

Use this skill when you want to:

- export single-cell crops as a user-facing output
- choose masked or unmasked mode without learning two separate skill names
- reuse one segmentation run for downstream review or modeling

## CLI

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill export-single-cell-crops \
  --workflow-root "$WORKFLOW_ROOT" \
  --crop-mode masked \
  --output-dir outputs/demo_single_cell_crops
```

## Agent Examples

- `Export masked single-cell crops from this segmentation workflow root.`
- `Export unmasked single-cell crops and keep the local context around each cell.`

## Outputs

- `masked/` or `unmasked/`: root directory for the exported crop package in the selected crop mode.
- `image_stacks/`: per-cell image stacks for each exported crop.
- `cell_masks/`: cell mask images aligned to each exported crop.
- `nuclei_masks/`: nucleus mask images aligned to each exported crop.
- `single_cell_manifest.csv`: table listing the exported crops and their associated metadata.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [run-segmentation-masks](run_segmentation_masks.md)
- [prepare-deepprofiler-project](prepare_deepprofiler_project.md)
