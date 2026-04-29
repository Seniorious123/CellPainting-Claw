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

## Agent Demo

This page is based on a real OpenClaw run:

- session id: `biosegdemo-prepare-v8`
- model: `vibe/gpt-5-mini`

### Request

```text
Which demo wells and image fields are available for segmentation?
```

### Routing

The observed routing sequence was:

- the agent first tried to load `cellpaint-pipeline/SKILL.md` from a bundled OpenClaw path
- that read failed with `ENOENT`
- the agent then loaded the workspace copy under `integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md`
- from that skill file, it chose `cp-prepare-segmentation-inputs`
- after the skill finished, it inspected the generated CSV to report the exact plate, well, and site inventory

### Observed Tool Call

The raw transcript used absolute checkout paths. The command below is the same call normalized to `$REPO_ROOT`:

```bash
cd $REPO_ROOT
/root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run \
  --config $REPO_ROOT/configs/project_config.demo.json \
  --skill cp-prepare-segmentation-inputs \
  --output-dir $REPO_ROOT/demo/workspace/outputs/agent_demo_segmentation
```

### Observed Result

```json
{
  "skill_key": "cp-prepare-segmentation-inputs",
  "category": "segmentation",
  "details": {
    "row_count": 2,
    "plate_count": 1,
    "well_count": 2,
    "site_count": 2
  },
  "ok": true
}
```

The generated table covered:

- plate `BR00000001`
- well `A01`, site `1`
- well `A02`, site `1`

The agent then read the CSV rows and reported the same two field records back to the user instead of guessing from directory names.

## Files Written

This recorded run wrote:

- `demo/workspace/outputs/agent_demo_segmentation/load_data_for_segmentation.csv`
- `demo/workspace/outputs/agent_demo_segmentation/pipeline_skill_manifest.json`

## Next Skills

- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
