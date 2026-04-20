# CellPainting-Skills

`cellpainting_skills` is the **public task package** of CellPainting-Claw.

Its job is simple: it gives users and agents a stable set of skill names for concrete Cell Painting tasks. The same skill names can be called directly by a person or chosen by an agent from a natural-language request.

## Skill Model

In this project, a skill is a **named task with a concrete output**.

A skill is not a separate backend. It is a public task name that maps onto an implementation in the toolkit.

This makes the project easier to use in practice:

- a human user can choose a task by name
- a script can call the same task repeatedly
- an agent can map a natural-language request onto a stable task name

The intended pattern is simple:

- choose one task
- run it through the CLI, Python, or an agent
- keep the output and pass it to the next task when needed

## Coverage

The skills sit on top of several connected capability areas.

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

The tables below are written from a user point of view:

- **main input** tells you what the skill expects to start from
- **main result** tells you what you will have when the skill finishes
- **main tools** shows which backend package or component does most of the work

### Data Access

| Skill key | Main input | Main result | Main tools |
| --- | --- | --- | --- |
| [`inspect-cellpainting-data`](inspect_cellpainting_data.md) | a project config with data-access settings | a summary of what sources, identifiers, and download settings are configured | `boto3`, `quilt3`, `cpgdata` |
| [`download-cellpainting-data`](download_cellpainting_data.md) | a project config plus dataset selection settings | a local download cache and the recorded download plan | `boto3`, `quilt3`, `cpgdata` |

### Profiling

| Skill key | Main input | Main result | Main tools |
| --- | --- | --- | --- |
| [`run-cellprofiler-profiling`](run_cellprofiler_profiling.md) | raw Cell Painting images plus profiling configuration | CellProfiler measurement tables such as `Image.csv`, `Cells.csv`, `Cytoplasm.csv`, and `Nuclei.csv` | `CellProfiler` |
| [`export-single-cell-measurements`](export_single_cell_measurements.md) | CellProfiler measurement tables from a profiling run | one merged single-cell table for later classical profiling | `cellpaint_pipeline.profiling_native` |
| [`run-pycytominer`](run_pycytominer.md) | single-cell measurements | analysis-ready classical profile tables such as aggregated and feature-selected outputs | `pycytominer` |
| [`summarize-classical-profiles`](summarize_classical_profiles.md) | classical profile tables from pycytominer | a readable summary bundle with metadata and PCA outputs | `pandas`, `numpy` |

### Segmentation

| Skill key | Main input | Main result | Main tools |
| --- | --- | --- | --- |
| [`run-segmentation-masks`](run_segmentation_masks.md) | raw Cell Painting images plus segmentation configuration | a segmentation workflow root with masks, labels, outlines, previews, and object tables | `CellProfiler` |
| [`export-single-cell-crops`](export_single_cell_crops.md) | a completed segmentation workflow root | masked or unmasked single-cell crop stacks plus a crop manifest | `cellpaint_pipeline.segmentation_native` |

### DeepProfiler

| Skill key | Main input | Main result | Main tools |
| --- | --- | --- | --- |
| [`prepare-deepprofiler-project`](prepare_deepprofiler_project.md) | a segmentation workflow root or crop export root | a runnable DeepProfiler project directory with the expected config and metadata layout | DeepProfiler export and project helpers |
| [`run-deepprofiler`](run_deepprofiler.md) | a prepared DeepProfiler project | collected DeepProfiler feature tables at single-cell and aggregated levels | `DeepProfiler`, `pandas`, `pyarrow` |
| [`summarize-deepprofiler-profiles`](summarize_deepprofiler_profiles.md) | DeepProfiler feature tables | a readable summary bundle with metadata and PCA outputs | `pandas`, `numpy` |

## Individual Skill Pages

Each skill has its **own page**.

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
