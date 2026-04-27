# `cp-generate-segmentation-previews`

`cp-generate-segmentation-previews` writes lightweight preview PNGs for quick visual review.

This skill is for the stage where the user or agent does **not** want to rerun the full segmentation export, but does want to check the fields visually before continuing.

## Main Result

The main result is one directory of preview PNGs:

- `sample_previews_png/`

These preview images are a fast inspection layer. They help confirm that the expected fields are being read and that the segmentation source images look reasonable before moving on to crops or deeper downstream analysis.

## Main Input

This skill reads either:

- prepared segmentation inputs from [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or
- a completed segmentation workflow root from [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)

It also reads:

- preview settings from the project config or explicit user options
- an optional output directory

## Config Fields Used

For this skill, the config mainly provides:

- the source channel layout used to render the preview images
- the workspace and output roots
- any default image-selection behavior already encoded in the project setup

In normal use, the simplest path is to point this skill at a segmentation workflow root that was already produced by `cp-extract-segmentation-artifacts`.

## Files Written

Files written by this skill:

- `sample_previews_png/`: one preview PNG per selected field
- `pipeline_skill_manifest.json`: a machine-readable record of the skill run

## Recorded Demo Result

In the recorded repository demo, this skill writes **two preview PNGs**:

- one for well `A01`
- one for well `A02`

The recorded manifest shows:

- `generated_count = 2`
- `field_count = 2`
- `skipped_existing = 0`

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cp-generate-segmentation-previews \
  --workflow-root outputs/demo_segmentation \
  --output-dir outputs/segmentation_previews
```

## Agent Use

Example request:

```text
Generate segmentation preview PNGs from outputs/demo_segmentation and save them under outputs/segmentation_previews.
```

## Previous And Next Skills

- [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md)
- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
