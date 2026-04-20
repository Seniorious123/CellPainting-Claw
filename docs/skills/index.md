# CellPainting-Skills

`cellpainting_skills` is the **public task package** of CellPainting-Claw.

Its job is simple: it gives users and agents a stable set of skill names for concrete Cell Painting tasks. The same skill names can be called directly by a person or chosen by an agent from a natural-language request.

## What A Skill Is

In this project, a skill is a **named task with a concrete output**.

A skill is not a separate backend. It is a public task name that maps onto an implementation in the toolkit.

This makes the project easier to use in practice:

- a human user can choose a task by name
- a script can call the same task repeatedly
- an agent can map a natural-language request onto a stable task name

## Where Skills Fit

The toolkit brings together several connected capability areas.

| Capability | Main tools | What this part does |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | inspect datasets, build plans, and download inputs |
| Measurement extraction | `CellProfiler` | produce profiling tables, masks, outlines, crops, and single-cell measurement tables |
| Classical profile generation | `pycytominer` | build classical profiles from single-cell tables |
| Deep feature extraction | `DeepProfiler` | build learned features from segmentation-guided crops |
| Named-task interface | `cellpainting_skills` | expose stable named tasks across those capabilities |
| Natural-language interface | `OpenClaw` | trigger the same named tasks through natural-language requests |

## Public Skill Catalog

The main public catalog is grouped by workflow stage and keeps the focus on tasks with meaningful standalone outputs.

### Data Access

| Skill key | What it does | Implemented with | Typical outputs |
| --- | --- | --- | --- |
| [`inspect-cellpainting-data`](inspect_cellpainting_data.md) | inspect configured sources before downloading anything | `boto3`, `quilt3`, `cpgdata` | `data_access_summary.json` |
| [`download-cellpainting-data`](download_cellpainting_data.md) | download one dataset slice into a local cache | `boto3`, `quilt3`, `cpgdata` | `download_plan.json`, `downloads/` |

### Profiling

| Skill key | What it does | Implemented with | Typical outputs |
| --- | --- | --- | --- |
| [`run-cellprofiler-profiling`](run_cellprofiler_profiling.md) | run the profiling CellProfiler pipeline | `CellProfiler` | `Image.csv`, `Cells.csv`, `Cytoplasm.csv`, `Nuclei.csv` |
| [`export-single-cell-measurements`](export_single_cell_measurements.md) | merge CellProfiler tables into one single-cell table | `cellpaint_pipeline.profiling_native` | `single_cell.csv.gz` |
| [`run-pycytominer`](run_pycytominer.md) | build classical profile tables | `pycytominer` | `aggregated.parquet`, `feature_selected.parquet` |
| [`summarize-classical-profiles`](summarize_classical_profiles.md) | turn classical profile tables into readable summary outputs | `pandas`, `numpy` | `profile_summary.json`, `pca_plot.png` |

### Segmentation

| Skill key | What it does | Implemented with | Typical outputs |
| --- | --- | --- | --- |
| [`run-segmentation-masks`](run_segmentation_masks.md) | run segmentation and write mask artifacts plus sample previews | `CellProfiler` | `cellprofiler_masks/`, `labels/`, `outlines/`, `sample_previews_png/` |
| [`export-single-cell-crops`](export_single_cell_crops.md) | export masked or unmasked single-cell crop stacks | `cellpaint_pipeline.segmentation_native` | `masked/` or `unmasked/`, `single_cell_manifest.csv` |

### DeepProfiler

| Skill key | What it does | Implemented with | Typical outputs |
| --- | --- | --- | --- |
| [`prepare-deepprofiler-project`](prepare_deepprofiler_project.md) | prepare a runnable DeepProfiler project from a workflow root or export root | DeepProfiler export and project helpers | `project_manifest.json`, `inputs/config/`, `inputs/metadata/` |
| [`run-deepprofiler`](run_deepprofiler.md) | run the DeepProfiler path and return collected tables | `DeepProfiler`, `pandas`, `pyarrow` | `deepprofiler_single_cell.parquet`, `deepprofiler_well_aggregated.parquet` |
| [`summarize-deepprofiler-profiles`](summarize_deepprofiler_profiles.md) | turn DeepProfiler tables into readable summary outputs | `pandas`, `numpy` | `profile_summary.json`, `pca_plot.png` |

## How To Read This Section

Each skill now has its **own page**.

Each page explains:

- what the skill does
- when to use it
- how a human user runs it
- how an agent should map requests onto it
- what outputs to expect

## Skill Pages

```{toctree}
:maxdepth: 1

inspect_cellpainting_data
download_cellpainting_data
run_cellprofiler_profiling
export_single_cell_measurements
run_pycytominer
summarize_classical_profiles
run_segmentation_masks
export_single_cell_crops
prepare_deepprofiler_project
run_deepprofiler
summarize_deepprofiler_profiles
```

## Related Pages

- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
- [Quick Start](../quick_start/index.md)
