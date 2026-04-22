# `crop-export-single-cell-crops`

`crop-export-single-cell-crops` exports per-cell crop packages from a completed segmentation result.

## Purpose

Use this skill when you want masked or unmasked single-cell crops that can be inspected directly or sent to the deep-feature branch.

## Inputs

- a segmentation workflow root from [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- a crop mode such as `masked` or `unmasked`
- crop-export settings from the project config or explicit user options
- an optional output directory

## Outputs

- crop image stacks for each exported cell
- crop masks when the chosen mode includes them
- `single_cell_manifest.csv`: the crop manifest
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill crop-export-single-cell-crops \
  --workflow-root outputs/demo_segmentation \
  --crop-mode masked \
  --output-dir outputs/demo_crops
```

## Agent Use

Example request:

```text
Export masked single-cell crops from outputs/demo_segmentation and write them under outputs/demo_crops.
```

## Related Skills

- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
