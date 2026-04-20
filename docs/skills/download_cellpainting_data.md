# `download-cellpainting-data`

`download-cellpainting-data` is the skill for downloading one Cell Painting dataset slice into a local cache.

## What It Does

This skill resolves a download request, writes a `download_plan.json`, and executes the corresponding download steps.

## When To Use It

Use this skill when you want to:

- fetch local inputs for profiling or segmentation
- download a dataset slice from a configured Gallery-style source
- let an agent turn a data request into local files

## CLI

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill download-cellpainting-data \
  --request-mode gallery-prefix \
  --prefix <gallery-prefix> \
  --output-dir outputs/demo_download
```

## Agent Request Examples

- `Download the requested Cell Painting dataset slice into a local cache.`
- `Fetch the images for this Gallery prefix and save them locally.`

## Typical Outputs

- `download_plan.json`
- `downloads/`
- `pipeline_skill_manifest.json`

## Related Skills

- [inspect-cellpainting-data](inspect_cellpainting_data.md)
- [run-cellprofiler-profiling](run_cellprofiler_profiling.md)
- [run-segmentation-masks](run_segmentation_masks.md)
