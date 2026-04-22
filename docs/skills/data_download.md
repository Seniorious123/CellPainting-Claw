# `data-download`

`data-download` fetches a requested Cell Painting dataset slice into local storage.

## Purpose

Use this skill when you want local input files for profiling or segmentation.

## Inputs

- a saved download plan from [data-plan-download](data_plan_download.md), or a direct dataset request
- a project config with `data_access` settings
- an optional output directory for the downloaded files

The plan may be produced by a previous skill or provided by the user.

## Outputs

- downloaded raw files under the configured local destination
- `download_plan.json`: the executed plan recorded with the run
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill data-download \
  --dataset-id cpg0016-jump \
  --source-id source_4 \
  --output-dir outputs/data_download
```

## Agent Use

Example request:

```text
Download the configured Cell Painting inputs into outputs/data_download.
```

## Related Skills

- [data-plan-download](data_plan_download.md)
- [cp-extract-measurements](cp_extract_measurements.md)
- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
