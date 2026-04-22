# `data-inspect-availability`

`data-inspect-availability` inspects the configured Cell Painting data-access settings before any download happens.

## Purpose

Use this skill to confirm which data source, identifiers, and access settings are currently configured for the project.

## Inputs

- a project config with `data_access` settings
- optional output directory for the inspection result

For demo runs, the config can come from the repository. For custom runs, it is provided by the user.

## Outputs

- `data_access_summary.json`: a structured summary of the configured source identifiers, backend settings, and access checks
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill data-inspect-availability \
  --output-dir outputs/data_inspect
```

## Agent Use

Example request:

```text
Inspect which Cell Painting data sources are configured and write a summary under outputs/data_inspect.
```

## Related Skills

- [data-plan-download](data_plan_download.md)
- [data-download](data_download.md)
