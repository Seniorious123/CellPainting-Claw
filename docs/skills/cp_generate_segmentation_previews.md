# `cp-generate-segmentation-previews`

`cp-generate-segmentation-previews` renders quick preview PNGs for segmentation inputs or outputs.

## Purpose

Use this skill when you want fast visual inspection without rerunning the full segmentation export.

## Inputs

- segmentation inputs from [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or a segmentation workflow root from [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- preview settings from the project config or explicit user options
- an optional output directory

## Outputs

- `sample_previews_png/`: preview PNGs for quick review
- `pipeline_skill_manifest.json`: the recorded skill run metadata

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

## Related Skills

- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
