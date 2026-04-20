# `run-cellprofiler-profiling`

`run-cellprofiler-profiling` is the skill for running the CellProfiler profiling workflow and writing measurement tables.

This skill runs the profiling-side CellProfiler workflow and writes the standard output tables such as `Image.csv`, `Cells.csv`, `Cytoplasm.csv`, and `Nuclei.csv`.

## Recommended Use

Use this skill when you want to:

- extract CellProfiler measurements from raw images
- produce the tables needed for single-cell export
- run the profiling pipeline directly instead of jumping straight to pycytominer

## CLI

```bash
CONFIG=configs/project_config.demo.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-cellprofiler-profiling \
  --output-dir outputs/demo_profiling
```

## Agent Examples

- `Run the CellProfiler profiling pipeline for this config.`
- `Generate the standard CellProfiler measurement tables from the raw images.`

## Outputs

- `Image.csv`: image-level CellProfiler measurements.
- `Cells.csv`: cell-level object measurements from CellProfiler.
- `Cytoplasm.csv`: cytoplasm-level object measurements from CellProfiler.
- `Nuclei.csv`: nuclei-level object measurements from CellProfiler.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [export-single-cell-measurements](export_single_cell_measurements.md)
- [run-pycytominer](run_pycytominer.md)
