# `inspect-cellpainting-data`

`inspect-cellpainting-data` is the skill for inspecting which Cell Painting data sources are configured and reachable before starting a download.

## Summary

This skill queries the configured data-access layer and writes a `data_access_summary.json` file.

## Recommended Use

Use this skill when you want to:

- confirm that a dataset or source is visible
- check the configured access layer before downloading anything
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

- `Inspect the configured Cell Painting data sources for this project.`
- `Check what Cell Painting data is available before downloading anything.`

## Outputs

- `data_access_summary.json`
- `pipeline_skill_manifest.json`

## Related Skills

- [download-cellpainting-data](download_cellpainting_data.md)
