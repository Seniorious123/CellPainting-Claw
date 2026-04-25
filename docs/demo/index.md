# Demo Run

This page documents one complete recorded run on the bundled synthetic demo assets.

The page is organized around the public skill catalog. The numbered output directories under the recorded run root are only archival labels for this specific run.

## Goal

This recorded run validates that the packaged demo assets can move through a multi-skill path from segmentation to DeepProfiler summary outputs.

## Inputs

The recorded run used:

- the bundled demo config at `configs/project_config.demo.json`
- the bundled synthetic assets under `demo/`
- the recorded output root `demo/workspace/outputs/demo_record_2026_04_25_gpu_final`

## Skill Sequence

| Skill | Role | Recorded directory |
| --- | --- | --- |
| `cp-extract-segmentation-artifacts` | build the segmentation workflow root and write CellProfiler outputs | `01_segmentation` |
| `cp-generate-segmentation-previews` | render field-level preview PNGs | `02_previews` |
| `crop-export-single-cell-crops` | export masked single-cell crops | `03_crops_masked` |
| `dp-export-deep-feature-inputs` | build DeepProfiler metadata and location files | `04_dp_inputs` |
| `dp-build-deep-feature-project` | assemble the runnable DeepProfiler project directory | `05_dp_project` |
| `dp-run-deep-feature-model` | run DeepProfiler inference | `06_dp_run` |
| `dp-collect-deep-features` | collect raw DeepProfiler outputs into tables | `07_dp_features` |
| `dp-summarize-deep-features` | write summary statistics and PCA outputs | `08_dp_summary` |

## Segmentation Artifacts

This step creates the workflow root that later segmentation and DeepProfiler skills reuse.

```bash
CONFIG=configs/project_config.demo.json
RUN_ROOT=demo/workspace/outputs/demo_record_2026_04_25_gpu_final

cellpainting-skills run \
  --config "$CONFIG" \
  --skill cp-extract-segmentation-artifacts \
  --output-dir "$RUN_ROOT/01_segmentation"
```

Recorded result:

- processed `2` fields across `1` plate and `2` wells
- generated a derived mask-export pipeline with `37` CellProfiler modules
- wrote `Image.csv`, `Cells.csv`, `Nuclei.csv`, label TIFFs, outline PNGs, and `segmentation_summary.json`

Key files:

- `01_segmentation/load_data_for_segmentation.csv`
- `01_segmentation/CPJUMP1_analysis_mask_export.cppipe`
- `01_segmentation/cellprofiler_masks/Image.csv`
- `01_segmentation/cellprofiler_masks/Cells.csv`
- `01_segmentation/cellprofiler_masks/Nuclei.csv`

## Preview Images

This step reuses the segmentation workflow root and writes field-level preview PNGs.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill cp-generate-segmentation-previews \
  --workflow-root "$RUN_ROOT/01_segmentation" \
  --output-dir "$RUN_ROOT/02_previews"
```

Recorded result:

- generated `2` preview PNG files
- covered both recorded fields

Key files:

- `02_previews/sample_previews_png/`

## Single-Cell Crops

This step exports masked single-cell crops from the same workflow root.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill crop-export-single-cell-crops \
  --workflow-root "$RUN_ROOT/01_segmentation" \
  --output-dir "$RUN_ROOT/03_crops_masked"
```

Recorded result:

- exported `4` masked single-cell crops
- wrote one crop manifest for the run

Key files:

- `03_crops_masked/masked/single_cell_manifest.csv`

## DeepProfiler Inputs

This step converts the segmentation workflow root into the metadata and location files expected by DeepProfiler.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill dp-export-deep-feature-inputs \
  --workflow-root "$RUN_ROOT/01_segmentation" \
  --output-dir "$RUN_ROOT/04_dp_inputs"
```

Recorded result:

- wrote metadata for `2` fields
- wrote `2` nuclei location files
- covered `4` nuclei in total

Key files:

- `04_dp_inputs/manifest.json`
- `04_dp_inputs/images/field_metadata.csv`
- `04_dp_inputs/locations/`

## DeepProfiler Project

This step assembles the runnable DeepProfiler project directory.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill dp-build-deep-feature-project \
  --workflow-root "$RUN_ROOT/01_segmentation" \
  --export-root "$RUN_ROOT/04_dp_inputs" \
  --output-dir "$RUN_ROOT/05_dp_project"
```

Recorded result:

- assembled a project for `2` fields
- wrote the config, metadata, locations, and checkpoint layout expected by DeepProfiler

Key files:

- `05_dp_project/project_manifest.json`
- `05_dp_project/inputs/config/profile_config.json`
- `05_dp_project/inputs/metadata/index.csv`

## DeepProfiler Inference

This step runs the packaged DeepProfiler model on the prepared project.

The recorded run used a GPU-visible TensorFlow setup. If your TensorFlow 2.10 environment does not already expose compatible CUDA 11 runtime and cuDNN 8 libraries, set `LD_LIBRARY_PATH` so that those libraries are visible before running this skill.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill dp-run-deep-feature-model \
  --project-root "$RUN_ROOT/05_dp_project" \
  --gpu 0 \
  --output-dir "$RUN_ROOT/06_dp_run"
```

Recorded result:

- completed with `returncode: 0`
- wrote raw DeepProfiler feature files under the project output tree
- used a GPU-visible execution path during the recorded run

Recorded log highlights:

```text
Loaded cuDNN version 8902
Extracting output from layer: block6a_activation
BR00000001/A01-1 (2 cells) : 145.73 secs
BR00000001/A02-1 (2 cells) : 0.07 secs
Profiling: done
```

## Feature Tables

This step collects the raw DeepProfiler feature outputs into analysis-ready tables.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill dp-collect-deep-features \
  --project-root "$RUN_ROOT/05_dp_project" \
  --output-dir "$RUN_ROOT/07_dp_features"
```

Recorded result:

- wrote `4` single-cell rows
- wrote `2` well-level rows
- wrote `672` feature columns

Key files:

- `07_dp_features/deepprofiler_single_cell.parquet`
- `07_dp_features/deepprofiler_well_aggregated.parquet`
- `07_dp_features/deepprofiler_feature_manifest.json`

## Summary Outputs

This step turns the collected DeepProfiler tables into summary files and PCA outputs.

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill dp-summarize-deep-features \
  --single-cell-parquet-path "$RUN_ROOT/07_dp_features/deepprofiler_single_cell.parquet" \
  --well-aggregated-parquet-path "$RUN_ROOT/07_dp_features/deepprofiler_well_aggregated.parquet" \
  --manifest-path "$RUN_ROOT/07_dp_features/deepprofiler_feature_manifest.json" \
  --output-dir "$RUN_ROOT/08_dp_summary"
```

Recorded result:

- wrote `profile_summary.json`
- wrote `well_metadata_summary.csv`
- wrote `top_variable_features.csv`
- wrote `pca_coordinates.csv`
- wrote `pca_plot.png`

## Notes

This recorded run is useful as an environment-validation example because it reaches the full DeepProfiler path on the bundled demo assets.

It should not be treated as a throughput benchmark. The demo is intentionally tiny, so GPU initialization dominates the first field and hides the scaling benefit that would matter more on larger runs.
