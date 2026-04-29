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

## Recorded Agent Demo

The repository includes a real OpenClaw session for this step:

- session id: `segdemo-local-v6-extract`
- config: `configs/project_config.demo.json`
- output directory: `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6`

### User Request

```text
Run the segmentation artifact extraction for /root/pipeline/CellPainting-Claw/configs/project_config.demo.json and write the results under /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6. Then tell me which skill you used, which command you ran, and which main files or directories were written.
```

### Agent Tool Call

```bash
cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run \
  --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json \
  --skill cp-extract-segmentation-artifacts \
  --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6
```

### Observed Result

```json
{
  "skill_key": "cp-extract-segmentation-artifacts",
  "details": {
    "load_data": {
      "row_count": 2,
      "plate_count": 1,
      "well_count": 2,
      "site_count": 2
    },
    "pipeline": {
      "module_count": 37,
      "selected_via": "template",
      "execution_mode": "derive-mask-export"
    },
    "execution": {
      "returncode": 0
    }
  },
  "ok": true
}
```

This real run wrote:

- `Image.csv`, `Cells.csv`, `Nuclei.csv`, `Cytoplasm.csv`, and `Experiment.csv`
- two nuclei label TIFFs and two cell label TIFFs
- two nuclei outline PNGs and two cell outline PNGs
- one derived `.cppipe`
- one successful `segmentation_summary.json`

## Demo Files

The recorded demo files for this step include:

- `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/segmentation_summary.json`
- `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/Image.csv`
- `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/Cells.csv`
- `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/Nuclei.csv`
- `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/outlines/BR00000001_A01_s1--cell_outlines.png`
- `demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/outlines/BR00000001_A02_s1--cell_outlines.png`

## Recorded Outline Examples

![A01 cell outlines](../../demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/outlines/BR00000001_A01_s1--cell_outlines.png)

![A02 cell outlines](../../demo/workspace/outputs/agent_demo_segmentation/02_extract_artifacts_v6/cellprofiler_masks/outlines/BR00000001_A02_s1--cell_outlines.png)

## Next Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
