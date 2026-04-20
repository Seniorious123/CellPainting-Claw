---
orphan: true
---

# `export-deepprofiler-inputs`

`export-deepprofiler-inputs` is the skill for converting segmentation outputs into DeepProfiler-ready metadata and nuclei-location files.

## What It Does

This skill reads segmentation outputs and writes the `manifest.json`, `images/field_metadata.csv`, and `locations/` layout expected by the next DeepProfiler steps.

Use it when you want to:

- bridge segmentation outputs into the DeepProfiler path
- prepare DeepProfiler inputs without building the project yet
- let an agent stop after the export stage

## CLI

```bash
CONFIG=configs/project_config.demo.json
WORKFLOW_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill export-deepprofiler-inputs \
  --workflow-root "$WORKFLOW_ROOT" \
  --output-dir outputs/demo_deepprofiler_export
```

## Agent Request Examples

- `Prepare DeepProfiler inputs from this segmentation workflow root.`
- `Convert the segmentation outputs into DeepProfiler-ready metadata and location files.`

## Typical Outputs

- `manifest.json`
- `images/field_metadata.csv`
- `locations/`
- `pipeline_skill_manifest.json`

## Related Skills

- [run-segmentation-masks](run_segmentation_masks.md)
- [build-deepprofiler-project](build_deepprofiler_project.md)
