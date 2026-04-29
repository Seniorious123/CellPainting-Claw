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

## Recorded Agent Demo

The repository includes a real OpenClaw session for this step:

- session id: `segdemo-local-v7-previews`

### User Request

```text
Please make quick preview images for the demo Cell Painting fields so I can visually check that the segmentation inputs look reasonable before going further.
```

### Recorded Execution Setup

For this recorded demo run, the agent used:

- config: `configs/project_config.demo.json`
- output directory: `demo/workspace/outputs/agent_demo_segmentation/03_generate_previews_v7`
- repository root: `/root/pipeline/CellPainting-Claw`

### Agent Tool Call

```bash
/root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run \
  --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json \
  --skill cp-generate-segmentation-previews \
  --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_segmentation/03_generate_previews_v7
```

The successful run was issued with `workdir=/root/pipeline/CellPainting-Claw`. In this demo setup, running from the repository root matters because the configured demo image paths are resolved relative to the repository layout.

### Observed Result

```json
{
  "skill_key": "cp-generate-segmentation-previews",
  "details": {
    "generated_count": 2,
    "skipped_existing": 0,
    "field_count": 2
  },
  "ok": true
}
```

This real run wrote:

- `sample_previews_png/BR00000001_A01_s1_sample.png`
- `sample_previews_png/BR00000001_A02_s1_sample.png`
- `pipeline_skill_manifest.json`

## Recorded Preview Images

![A01 sample preview](../../demo/workspace/outputs/agent_demo_segmentation/03_generate_previews_v7/sample_previews_png/BR00000001_A01_s1_sample.png)

![A02 sample preview](../../demo/workspace/outputs/agent_demo_segmentation/03_generate_previews_v7/sample_previews_png/BR00000001_A02_s1_sample.png)

## Execution Note

During trace capture, a separate OpenClaw session failed when the preview skill was launched from the OpenClaw workspace instead of the repository root. That failure was path-related rather than algorithm-related. For the demo config, keep the run rooted at `/root/pipeline/CellPainting-Claw`.

## Related Skills

- [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md)
- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
