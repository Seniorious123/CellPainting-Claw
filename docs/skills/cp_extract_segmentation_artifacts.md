# `cp-extract-segmentation-artifacts`

`cp-extract-segmentation-artifacts` is the segmentation execution step.

It takes the prepared field list, resolves the segmentation `.cppipe`, runs the CellProfiler-based segmentation backend, and writes the artifact bundle that downstream tools can reuse.

## Purpose

Use this skill when you want:

- segmentation tables such as `Image.csv`, `Cells.csv`, and `Nuclei.csv`
- label images for segmented nuclei and cells
- outline PNGs for quick inspection
- a reusable segmentation workflow root for crops or DeepProfiler preparation

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the segmentation input table written by [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or default segmentation inputs resolved from the config
- the segmentation `.cppipe` template or override selected by the config
- the configured raw-image and illumination assets
- an optional output directory

In the demo setup, the config selects the bundled segmentation template and derives a mask-export-ready `.cppipe` at runtime.

## Outputs

This skill writes:

- `load_data_for_segmentation.csv`
  The exact field list used by this run.
- `CPJUMP1_analysis_mask_export.cppipe`
  The pipeline file used for execution.
- `cellprofiler_masks/Image.csv`
  Field-level measurements from the segmentation run.
- `cellprofiler_masks/Cells.csv`
  Cell-level measurements.
- `cellprofiler_masks/Nuclei.csv`
  Nuclei-level measurements.
- `cellprofiler_masks/labels/`
  Label TIFF files for segmented nuclei and cells.
- `cellprofiler_masks/outlines/`
  Outline PNGs for quick visual review.
- `segmentation_summary.json`
  A compact summary of the completed run.
- `pipeline_skill_manifest.json`
  The machine-readable run record for this skill invocation.

## Agent Demo

This page is based on a real OpenClaw turn recorded in the main session transcript:

- session id: `93f63e09-7c61-4f40-8bb7-e75ae56068aa`
- turn timestamp: `2026-04-29 18:21 GMT+8`
- model: `vibe/gpt-5-mini`

### Request

```text
Please run segmentation on the demo Cell Painting images and save the main outputs I would normally review afterward.
```

### Routing

The observed routing sequence was:

- the agent first inspected the skill catalog
- it compared `cp-extract-segmentation-artifacts` with `cp-generate-segmentation-previews`
- it chose `cp-extract-segmentation-artifacts` as the primary response to the request
- it launched the extraction run
- while the run was still active, it polled the process and inspected the output tree
- once the first review artifacts were present, it answered with the concrete files already available

### Observed Tool Call

The raw transcript used absolute checkout paths. The command below is the same call normalized to `$REPO_ROOT`:

```bash
cd $REPO_ROOT
/root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run \
  --config $REPO_ROOT/configs/project_config.demo.json \
  --skill cp-extract-segmentation-artifacts \
  --output-dir $REPO_ROOT/demo/workspace/outputs/agent_demo_segmentation/review_run
```

### Observed Result

The agent reported the review-ready files that were already present when it answered:

- config: `configs/project_config.demo.json`
- output directory: `demo/workspace/outputs/agent_demo_segmentation/review_run`
- load-data rows: `2`
- wells: `2`
- site values: `1`

## Files Written

The recorded turn confirmed these files in the output tree:

- `demo/workspace/outputs/agent_demo_segmentation/review_run/load_data_for_segmentation.csv`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/segmentation_workflow_config.json`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/CPJUMP1_analysis_mask_export.cppipe`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/cellprofiler_masks/load_data_for_segmentation.absolute.csv`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/cellprofiler_masks/labels/BR00000001_A01_s1--cell_labels.tiff`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/cellprofiler_masks/labels/BR00000001_A01_s1--nuclei_labels.tiff`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/cellprofiler_masks/outlines/BR00000001_A01_s1--cell_outlines.png`
- `demo/workspace/outputs/agent_demo_segmentation/review_run/cellprofiler_masks/outlines/BR00000001_A01_s1--nuclei_outlines.png`

## Demo Image

The recorded run produced the following outline image:

![A01 cell outlines](../_static/agent_demo_segmentation/outline_A01_cell.png)

## Next Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
