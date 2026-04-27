# `cp-extract-segmentation-artifacts`

`cp-extract-segmentation-artifacts` is the skill that actually runs the segmentation branch and writes the main artifact set.

If `cp-prepare-segmentation-inputs` describes **which fields to run**, this skill performs the next step: it resolves the segmentation `.cppipe`, runs the segmentation backend, and writes masks, labels, outlines, and object tables.

## Main Result

The main result is one completed segmentation output bundle.

That bundle typically includes:

- segmentation measurement tables
- exported label images
- exported outline images
- mask-export outputs from the CellProfiler segmentation run

## Main Input

This skill reads:

- a segmentation load-data table from [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or default segmentation inputs resolved from the config
- the segmentation `.cppipe` selected by the config
- runtime settings for the mask-export run
- an optional output directory

## Config Fields Used

For this skill, the config mainly determines:

- which segmentation backend root to use
- which segmentation `.cppipe` template or custom override to select
- where the workspace and output directories live
- which runtime settings to use for the mask-export execution

In the demo config, the default segmentation path uses the bundled `segmentation-base` template and derives a mask-export-ready pipeline at runtime.

## Files Written

Files commonly written by this skill:

- `load_data_for_segmentation.csv`: the concrete field list used for this run
- `CPJUMP1_analysis_mask_export.cppipe`: the pipeline file used for execution
- `cellprofiler_masks/Image.csv`: field-level segmentation measurements
- `cellprofiler_masks/Cells.csv`: cell-level segmentation measurements
- `cellprofiler_masks/Nuclei.csv`: nuclei-level segmentation measurements
- `cellprofiler_masks/labels/`: label images for segmented objects
- `cellprofiler_masks/outlines/`: outline PNGs for quick visual inspection
- `segmentation_summary.json`: a compact summary of the segmentation run
- `pipeline_skill_manifest.json`: a machine-readable record of the skill run

## Recorded Demo Result

In the recorded repository demo, this skill runs on **two fields** and writes:

- one derived `.cppipe` file
- `Image.csv`, `Cells.csv`, and `Nuclei.csv`
- label images for wells `A01` and `A02`
- outline PNGs for wells `A01` and `A02`
- a successful execution record with `returncode = 0`

This is the skill that creates the segmentation outputs later reused by preview generation, crop export, and the DeepProfiler path.

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
Run segmentation with configs/project_config.demo.json and write the masks, labels, outlines, and segmentation tables under outputs/demo_segmentation.
```

## Next Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
