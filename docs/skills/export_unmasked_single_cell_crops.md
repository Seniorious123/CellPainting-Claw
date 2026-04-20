---
orphan: true
---

# `export-unmasked-single-cell-crops`

`export-unmasked-single-cell-crops` is the skill for exporting unmasked single-cell image stacks from a segmentation workflow root.

This skill writes per-cell image stacks together with the corresponding cell and nuclei masks, while keeping the surrounding image context.

Use it when you want to:

- create unmasked single-cell crops for review
- preserve local context around each segmented cell
- build crop packages for downstream models that expect unmasked inputs

## CLI

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill export-unmasked-single-cell-crops \
  --workflow-root "$WORKFLOW_ROOT" \
  --output-dir outputs/demo_unmasked_crops
```

## Agent Examples

- `Export unmasked single-cell crops from this segmentation workflow root.`
- `Create one unmasked crop package per segmented cell.`

## Outputs

- `unmasked/image_stacks/`: per-cell unmasked image stacks for each exported crop.
- `unmasked/cell_masks/`: cell mask images for the unmasked crop export.
- `unmasked/nuclei_masks/`: nucleus mask images for the unmasked crop export.
- `unmasked/single_cell_manifest.csv`: manifest table for the unmasked crop export.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [run-segmentation-masks](run_segmentation_masks.md)
- [export-deepprofiler-inputs](export_deepprofiler_inputs.md)
