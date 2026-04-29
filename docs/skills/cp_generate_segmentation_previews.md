# `cp-generate-segmentation-previews`

`cp-generate-segmentation-previews` writes lightweight field-level preview PNGs.

This skill is useful when you want to check the segmentation source images visually without rerunning the heavier segmentation export.

## Purpose

Use this skill when you want:

- quick PNG previews for the selected segmentation fields
- a fast visual check before moving on to crops or DeepProfiler preparation
- a lightweight inspection step after [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md) or [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- prepared segmentation inputs or a valid segmentation workflow root
- the source channel paths needed to render the preview RGB images
- an optional output directory

For the demo config, this skill depends on the same raw Cell Painting image layout used by the segmentation steps above.

## Outputs

This skill writes:

- `sample_previews_png/`
  One preview PNG per selected field.
- `pipeline_skill_manifest.json`
  The machine-readable run record for this skill invocation.

## Agent Demo

This page is based on a real OpenClaw turn recorded in the main session transcript:

- session id: `93f63e09-7c61-4f40-8bb7-e75ae56068aa`
- turn timestamp: `2026-04-29 18:25 GMT+8`
- model: `vibe/gpt-5-mini`

### Request

```text
Please make a few quick preview images from the demo Cell Painting inputs so I can visually check that the images look right before going further.
```

## Structured Trace

```text
user_input:
Please make a few quick preview images from the demo Cell Painting inputs so I can visually check that the images look right before going further.

planner_step_1:
intent:
Run the preview-only segmentation skill against the existing demo workflow root.
tool_calls:
- exec("cd $REPO_ROOT && cellpainting-skills run --config $REPO_ROOT/configs/project_config.demo.json --skill cp-generate-segmentation-previews --workflow-root $REPO_ROOT/demo/workspace/outputs/agent_demo_segmentation/review_run --output-dir $REPO_ROOT/demo/workspace/outputs/agent_demo_segmentation/review_previews")
observed_result:
- process started successfully
- background session = clear-mist

planner_step_2:
intent:
Poll the background run and recover the structured preview result object.
tool_calls:
- process.poll("clear-mist")
observed_result:
- skill_key = cp-generate-segmentation-previews
- generated_count = 2
- skipped_existing = 0
- field_count = 2
- sample_previews_dir = demo/workspace/outputs/agent_demo_segmentation/review_previews/sample_previews_png

planner_step_3:
intent:
List the generated PNG files and report them back to the user.
tool_calls:
- exec("find $REPO_ROOT/demo/workspace/outputs/agent_demo_segmentation/review_previews/sample_previews_png -maxdepth 2 -type f | sort")
observed_result:
- BR00000001_A01_s1_sample.png
- BR00000001_A02_s1_sample.png

final_answer_snapshot:
Two field-level RGB preview PNGs were generated for a quick visual QC pass before continuing.
```

### Observed Result

```json
{
  "skill_key": "cp-generate-segmentation-previews",
  "category": "segmentation",
  "details": {
    "generated_count": 2,
    "skipped_existing": 0,
    "field_count": 2
  },
  "ok": true
}
```

## Files Written

This recorded run wrote:

- `demo/workspace/outputs/agent_demo_segmentation/review_previews/pipeline_skill_manifest.json`
- `demo/workspace/outputs/agent_demo_segmentation/review_previews/segmentation_source_config.json`
- `demo/workspace/outputs/agent_demo_segmentation/review_previews/sample_previews_png/BR00000001_A01_s1_sample.png`
- `demo/workspace/outputs/agent_demo_segmentation/review_previews/sample_previews_png/BR00000001_A02_s1_sample.png`

## Demo Images

![A01 sample preview](../_static/agent_demo_segmentation/preview_A01.png)

![A02 sample preview](../_static/agent_demo_segmentation/preview_A02.png)

## Related Skills

- [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md)
- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
