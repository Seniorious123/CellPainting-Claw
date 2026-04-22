# `cp-extract-segmentation-artifacts`

`cp-extract-segmentation-artifacts` runs the segmentation CellProfiler pipeline and produces the main segmentation artifact set.

## Purpose

Use this skill when you want masks, labels, outlines, and segmentation measurement tables.

## Inputs

- a segmentation load-data table from [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or default segmentation inputs resolved from the project config
- the segmentation `.cppipe` selected by the config
- runtime settings from the project config or explicit user options
- an optional output directory

The segmentation `.cppipe` is provided by the repository by default unless the config overrides it.

## Outputs

- `cellprofiler_masks/`: exported mask files
- `Image.csv`, `Cells.csv`, `Nuclei.csv`: segmentation measurement tables
- `labels/`: label images for segmented objects
- `outlines/`: outline images for quick inspection
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cp-extract-segmentation-artifacts \
  --output-dir outputs/demo_segmentation
```

## Agent Use

Example request:

```text
Run the segmentation pipeline with configs/project_config.demo.json and write masks, labels, and outlines under outputs/demo_segmentation.
```

## Related Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
