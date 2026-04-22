# `cyto-aggregate-profiles`

`cyto-aggregate-profiles` aggregates single-cell measurements into a classical profile table.

## Purpose

Use this skill to start the pycytominer branch from a single-cell table.

## Inputs

- a single-cell table from [cp-build-single-cell-table](cp_build_single_cell_table.md), or an equivalent table provided by the user
- a project config with pycytominer settings
- an optional output directory

## Outputs

- `aggregated.parquet`: the aggregated classical profile table
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cyto-aggregate-profiles \
  --single-cell-path outputs/single_cell_table/single_cell.csv.gz \
  --output-dir outputs/cyto_aggregate
```

## Agent Use

Example request:

```text
Aggregate the single-cell measurements in outputs/single_cell_table into a classical profile table under outputs/cyto_aggregate.
```

## Related Skills

- [cyto-annotate-profiles](cyto_annotate_profiles.md)
