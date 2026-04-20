# `export-single-cell-measurements`

`export-single-cell-measurements` is the skill for merging CellProfiler image and object tables into one single-cell table.

This skill reads `Image.csv` together with one object table such as `Cells.csv` and writes a merged `single_cell.csv.gz`.

## Recommended Use

Use this skill when you want to:

- prepare one single-cell table for downstream analysis
- convert multiple CellProfiler tables into one analysis-ready file
- hand classical profiling to pycytominer in a simpler format

## CLI

```bash
CONFIG=configs/project_config.demo.json
PROFILING_ROOT=outputs/demo_profiling

cellpainting-skills run \
  --config "$CONFIG" \
  --skill export-single-cell-measurements \
  --image-csv-path "$PROFILING_ROOT/Image.csv" \
  --object-table-path "$PROFILING_ROOT/Cells.csv" \
  --object-table Cells \
  --output-dir outputs/demo_single_cell
```

## Agent Examples

- `Merge the CellProfiler tables into one single-cell file.`
- `Export a single-cell table from Image.csv and Cells.csv.`

## Outputs

- `single_cell.csv.gz`
- `pipeline_skill_manifest.json`

## Related Skills

- [run-cellprofiler-profiling](run_cellprofiler_profiling.md)
- [run-pycytominer](run_pycytominer.md)
- [summarize-classical-profiles](summarize_classical_profiles.md)
