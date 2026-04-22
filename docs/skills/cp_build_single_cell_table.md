# `cp-build-single-cell-table`

`cp-build-single-cell-table` merges CellProfiler measurement tables into one single-cell table.

## Purpose

Use this skill when you want one tabular output that downstream profiling tools can consume directly.

## Inputs

- CellProfiler measurement tables from [cp-extract-measurements](cp_extract_measurements.md), or equivalent tables provided by the user
- a project config when default profiling outputs should be resolved automatically
- an optional output directory

## Outputs

- `single_cell.csv.gz`: one merged single-cell measurements table
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cp-build-single-cell-table \
  --image-csv-path outputs/profiling_measurements/Image.csv \
  --object-table-path outputs/profiling_measurements/Cells.csv \
  --object-table Cells \
  --output-dir outputs/single_cell_table
```

## Agent Use

Example request:

```text
Build a single-cell table from the profiling outputs in outputs/profiling_measurements and write it under outputs/single_cell_table.
```

## Related Skills

- [cyto-aggregate-profiles](cyto_aggregate_profiles.md)
