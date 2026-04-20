---
orphan: true
---

# `generate-sample-previews`

`generate-sample-previews` is the skill for rendering field-level preview PNGs from segmentation input channels.

This skill reads the segmentation load-data table and writes composite preview images for each field.

Use it when you want to:

- quickly inspect representative fields
- review inputs before exporting crops
- let an agent return visual previews from an existing segmentation workflow root

## CLI

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill generate-sample-previews \
  --workflow-root "$WORKFLOW_ROOT" \
  --output-dir outputs/demo_previews
```

## Agent Examples

- `Generate field-level preview PNGs from this segmentation workflow root.`
- `Show preview images for the current segmentation input fields.`

## Outputs

- `sample_previews_png/`
- `pipeline_skill_manifest.json`

## Related Skills

- [run-segmentation-masks](run_segmentation_masks.md)
