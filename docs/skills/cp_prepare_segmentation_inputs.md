# `cp-prepare-segmentation-inputs`

`cp-prepare-segmentation-inputs` writes the segmentation input table before any CellProfiler segmentation run begins.

This is the step that turns a project config into a concrete field list. In the demo setup, it resolves which plate, well, and site will be segmented, and it writes the channel paths that the next segmentation step will read.

## Purpose

Use this skill when you want to:

- confirm which fields will be sent into segmentation
- inspect the segmentation input table before a longer run
- hand a clean field list to [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the configured raw-image and illumination roots
- optional plate, well, or site filters
- an optional output directory

In plain language, the config tells the skill where the raw Cell Painting images live and which demo assets belong to the current run.

## Outputs

This skill writes:

- `load_data_for_segmentation.csv`
  The field-level input table for segmentation. Each row names one field and includes the channel filenames and path columns needed by the segmentation pipeline.
- `pipeline_skill_manifest.json`
  The machine-readable run record for this skill invocation.

## Recorded Agent Demo

The repository includes a real OpenClaw session for this step:

- session id: `segdemo-local-v8-prepare`

### User Request

```text
I want to segment the demo Cell Painting images, but before running segmentation I want to check which fields will be included. Please prepare the segmentation input table and tell me how many wells and sites are going to be processed.
```

### Recorded Execution Setup

For this recorded demo run, the agent used:

- config: `configs/project_config.demo.json`
- output directory: `demo/workspace/outputs/agent_demo_segmentation/01_prepare_inputs_v8`
- repository root: `/root/pipeline/CellPainting-Claw`

### Agent Tool Call

```bash
/root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run \
  --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json \
  --skill cp-prepare-segmentation-inputs \
  --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_segmentation/01_prepare_inputs_v8
```

### Observed Result

```json
{
  "skill_key": "cp-prepare-segmentation-inputs",
  "details": {
    "row_count": 2,
    "plate_count": 1,
    "well_count": 2,
    "site_count": 2
  },
  "ok": true
}
```

The generated table covers:

- plate `BR00000001`
- well `A01`, site `1`
- well `A02`, site `1`

## Demo Files

The recorded demo files for this step are:

- `demo/workspace/outputs/agent_demo_segmentation/01_prepare_inputs_v8/load_data_for_segmentation.csv`
- `demo/workspace/outputs/agent_demo_segmentation/01_prepare_inputs_v8/pipeline_skill_manifest.json`

## Next Skills

- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
