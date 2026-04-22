# `cp-extract-measurements`

`cp-extract-measurements` runs the profiling CellProfiler pipeline and writes the standard measurement tables.

## Purpose

Use this skill when you want CellProfiler to extract per-image and per-object measurements from raw Cell Painting images.

## Inputs

- Cell Painting images
- a project config
- the profiling `.cppipe` selected by the config
- an optional output directory for the profiling run

The images can come from the repository demo assets, from a previous data-download step, or from user-provided inputs. The profiling `.cppipe` is provided by the repository by default unless the config overrides it.

## Outputs

- `Image.csv`: per-image measurements and metadata
- `Cells.csv`, `Cytoplasm.csv`, `Nuclei.csv`: object-level measurement tables
- profiling run logs and workflow outputs
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cp-extract-measurements \
  --output-dir outputs/profiling_measurements
```

## Agent Use

Example request:

```text
Run the profiling CellProfiler pipeline with configs/project_config.demo.json and write the measurement tables under outputs/profiling_measurements.
```

## Related Skills

- [cp-build-single-cell-table](cp_build_single_cell_table.md)
