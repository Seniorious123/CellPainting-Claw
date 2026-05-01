# `cp-prepare-segmentation-inputs`

`cp-prepare-segmentation-inputs` resolves which image fields will enter segmentation.

This is the planning step before any CellProfiler segmentation run begins. In the demo setup, it determines which plate, well, and site will be segmented next.

## Purpose

Use this skill when you want to:

- confirm which fields will be sent into segmentation
- inspect the segmentation input table before a longer run
- hand a clean field list to [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)

## Main Outcome

After this skill finishes, you know exactly which image fields will go into segmentation.

This is a planning step, not an image-generation step. It does not produce masks, outlines, or single-cell crops yet.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the configured raw-image and illumination roots
- optional plate, well, or site filters
- an optional output directory

In plain language, the config tells the skill where the raw Cell Painting images live and which demo assets belong to the current run.

## Outputs

The main result of this skill is a resolved segmentation scope:

- which plate will be used
- which wells will be used
- which sites or image fields will be used
- which image channels the next segmentation step will read

## Agent Demo

This page is based on a real OpenClaw run:

- session id: `biosegdemo-prepare-v8`
- model: `vibe/gpt-5-mini`

### Request

```text
Which demo wells and image fields are available for segmentation?
```

## Structured Trace

```text
user_input:
Which demo wells and image fields are available for segmentation?

planner_step_1:
intent:
Resolve the current CellPainting skill surface instead of guessing from repository directories.
tool_calls:
- read("~/.openclaw/lib/node_modules/openclaw/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- ENOENT: bundled OpenClaw skill path did not exist on this host

planner_step_2:
intent:
Load the workspace skill file and recover the documented routing rule for segmentation-scope questions.
tool_calls:
- exec("pwd && ls -la .../workspace/skills/cellpaint-pipeline && sed -n '1,220p' .../workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- workspace skill file loaded successfully
- routing guidance pointed to cp-prepare-segmentation-inputs for questions about wells, sites, fields, or image rows

planner_step_3:
intent:
Run the documented segmentation-prep skill against the demo config and write the real load-data table.
tool_calls:
- exec("cd $REPO_ROOT && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config $REPO_ROOT/configs/project_config.demo.json --skill cp-prepare-segmentation-inputs --output-dir $REPO_ROOT/demo/workspace/outputs/agent_demo_segmentation")
observed_result:
- skill_key = cp-prepare-segmentation-inputs
- row_count = 2
- plate_count = 1
- well_count = 2
- site_count = 2
- load_data_path = demo/workspace/outputs/agent_demo_segmentation/load_data_for_segmentation.csv

planner_step_4:
intent:
Read the generated CSV and report the exact field inventory back to the user.
tool_calls:
- exec("python ... read load_data_for_segmentation.csv and print rows, wells, sites, and field records")
observed_result:
- plate = BR00000001
- wells = A01, A02
- site value = 1 for both rows
- exact image rows = 2

final_answer_snapshot:
The demo segmentation scope contains two image rows:
BR00000001 / A01 / site 1 and BR00000001 / A02 / site 1.
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

The resolved segmentation scope covered:

- plate `BR00000001`
- well `A01`, site `1`
- well `A02`, site `1`

## Recorded Reply

```text
[[reply_to_current]] For the demo segmentation input set, the available image fields are:

- Plate: `BR00000001`
- Wells: `A01`, `A02`
- Site/field: `1` for each well

So the demo segmentation scope is exactly 2 image rows:

1. `BR00000001 / A01 / site 1`
2. `BR00000001 / A02 / site 1`

I verified this by running the supported segmentation-prep entrypoint `cp-prepare-segmentation-inputs`.

Summary from that run:

- row count: `2`
- plate count: `1`
- well count: `2`
- site count: `2` total rows, but only one site value: `1` in each row

This prep output is for segmentation planning only. It tells you which fields will be segmented next, but it does not create masks yet. The next step is `cp-extract-segmentation-artifacts`.
```

## Next Skills

- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
