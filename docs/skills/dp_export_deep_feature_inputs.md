# `dp-export-deep-feature-inputs`

`dp-export-deep-feature-inputs` converts segmentation outputs into the metadata and location files needed by DeepProfiler.

## Purpose

Use this skill when you want to stop at the DeepProfiler export stage instead of building the full project immediately.

## Inputs

- a segmentation workflow root from [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md), or a crop export root from [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- experiment metadata from the repository config or from the user
- an optional output directory

## Outputs

- `images/field_metadata.csv`: field-level metadata for DeepProfiler
- `locations/`: per-field nuclei or object-location files
- `manifest.json`: the deep-feature input manifest
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill dp-export-deep-feature-inputs \
  --workflow-root outputs/demo_segmentation \
  --output-dir outputs/dp_inputs
```

## Agent Use

Example request:

```text
Prepare DeepProfiler input files from outputs/demo_segmentation and write them under outputs/dp_inputs.
```

## Related Skills

- [dp-build-deep-feature-project](dp_build_deep_feature_project.md)
