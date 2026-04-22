# `data-plan-download`

`data-plan-download` turns a dataset request into a concrete download plan without downloading files yet.

## Purpose

Use this skill when you want to preview or validate what a requested download would fetch before executing it.

## Inputs

- a project config with `data_access` settings
- a dataset request, source selection, or prefix override
- an optional output directory for the saved plan

The config can be provided by the repository for demo runs or by the user for custom runs.

## Outputs

- `download_plan.json`: the resolved list of files or prefixes to fetch
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill data-plan-download \
  --dataset-id cpg0016-jump \
  --source-id source_4 \
  --output-dir outputs/data_plan
```

## Agent Use

Example request:

```text
Build a download plan for dataset cpg0016-jump source_4 and save it under outputs/data_plan.
```

## Related Skills

- [data-inspect-availability](data_inspect_availability.md)
- [data-download](data_download.md)
