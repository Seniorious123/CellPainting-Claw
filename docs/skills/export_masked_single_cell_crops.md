---
orphan: true
---

# `export-masked-single-cell-crops`

`export-masked-single-cell-crops` is the skill for exporting masked single-cell image stacks from a segmentation workflow root.

This skill reads a segmentation workflow root and writes per-cell image stacks together with cell and nuclei masks.

Use it when you want to:

- create masked single-cell crops for review
- build masked crop packages for downstream modeling
- reuse one segmentation run without rerunning CellProfiler

## CLI

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill export-masked-single-cell-crops \
  --workflow-root "$WORKFLOW_ROOT" \
  --output-dir outputs/demo_masked_crops
```

## Agent Examples

- `Export masked single-cell crops from this segmentation workflow root.`
- `Create one masked crop package per segmented cell.`

## Outputs

- `masked/image_stacks/`: per-cell masked image stacks for each exported crop.
- `masked/cell_masks/`: cell mask images for the masked crop export.
- `masked/nuclei_masks/`: nucleus mask images for the masked crop export.
- `masked/single_cell_manifest.csv`: manifest table for the masked crop export.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [run-segmentation-masks](run_segmentation_masks.md)
- [export-deepprofiler-inputs](export_deepprofiler_inputs.md)
