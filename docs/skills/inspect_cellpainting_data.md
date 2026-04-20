# `inspect-cellpainting-data`

`inspect-cellpainting-data` is the skill for checking which Cell Painting data sources are available before starting a download.

This skill checks the data sources defined in the project config and writes the result to `data_access_summary.json`.

## Recommended Use

Use this skill when you want to:

- confirm that a dataset or source is visible
- check which data sources the project can access before downloading anything
- let an agent answer "what data is available?" with a concrete result

## CLI

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill inspect-cellpainting-data \
  --output-dir outputs/demo_data_access
```

## Agent Examples

- `Inspect the Cell Painting data sources defined for this project.`
- `Check what Cell Painting data is available before downloading anything.`

## Outputs

- `data_access_summary.json`
- `pipeline_skill_manifest.json`

## Related Skills

- [download-cellpainting-data](download_cellpainting_data.md)
