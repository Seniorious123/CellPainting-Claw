# `download-cellpainting-data`

`download-cellpainting-data` is the skill for downloading one Cell Painting dataset slice into a local cache.

This skill turns a data request into a download plan, writes `download_plan.json`, and downloads the requested files.

## Recommended Use

Use this skill when you want to:

- fetch local inputs for profiling or segmentation
- download a dataset slice from the data source defined in the project config
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

## Agent Examples

- `Download the requested Cell Painting dataset slice into a local cache.`
- `Fetch the images for this Gallery prefix and save them locally.`

## Outputs

- `download_plan.json`: resolved download request showing what will be fetched and where it will be stored.
- `downloads/`: downloaded files placed in the local cache or output directory.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [inspect-cellpainting-data](inspect_cellpainting_data.md)
- [run-cellprofiler-profiling](run_cellprofiler_profiling.md)
- [run-segmentation-masks](run_segmentation_masks.md)
