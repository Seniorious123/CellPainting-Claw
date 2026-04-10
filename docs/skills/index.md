# CellPainting-Skills

`cellpainting_skills` is the **task package** of CellPainting-Claw.

Its job is simple: it exposes a small set of **stable named skills** on top of the toolkit. Those skills are the main public task model of the project.

This page is therefore the main place to understand:

- what skills exist
- what each skill does
- how a human user calls a skill
- how an agent should route a request to the right skill

## What A Skill Is

In this project, a skill is a **stable named task**.

A skill is not a separate backend. It is a public task name that maps onto a validated implementation underneath.

That design gives the project three useful properties:

- the public task names stay stable
- users do not need to learn the lower-level workflow layout first
- agents can route natural-language requests onto a controlled task catalog

## Where Skills Sit In The Stack

The stack should be read in this order:

| Layer | Main tools | What happens here |
| --- | --- | --- |
| data access | `boto3`, `quilt3`, `cpgdata` | inspect datasets, build plans, and download inputs |
| classical processing | `CellProfiler`, `pycytominer` | produce measurement tables, profiles, masks, previews, and crops |
| deep learning | `DeepProfiler` | generate learned features from segmentation-guided single-cell inputs |
| task layer | `cellpainting_skills` | expose stable named tasks across those lower layers |
| agent interface | `OpenClaw` | trigger the same task layer through natural-language requests |

Skills belong to the **task layer**. They are the public task interface across the lower toolkit layers.

## The Six Primary Skills

The public skill catalog is intentionally small.

These are the **six primary skills** that define the current public task surface:

| Skill key | Layer | Main job | Typical outputs |
| --- | --- | --- | --- |
| `plan-data-access` | data access | inspect inputs and write a reusable access plan | `data_access_summary.json`, `download_plan.json` |
| `download-data` | data access | execute the local download step | `download_plan.json`, `download_execution.json` |
| `run-classical-profiling` | classical profiling | produce single-cell tables and pycytominer-facing outputs | `single_cell.csv.gz`, `pycytominer/`, `evaluation/` |
| `run-segmentation` | segmentation | produce masks, previews, and single-cell crops | masks, previews, masked crops, unmasked crops |
| `prepare-deepprofiler-inputs` | DeepProfiler preparation | stop after writing the DeepProfiler-ready export artifacts | export metadata, image inputs, location inputs |
| `run-deepprofiler` | DeepProfiler | run the DeepProfiler-oriented path through export, project assembly, profiling, and feature collection | project files, profile outputs, collected deep features |

## Why The Catalog Stays Small

The skill catalog is designed around **modular public tasks**, not around every possible combined run.

That means:

- each primary skill should cover one clear capability area
- overlapping combined aliases should not be presented as first-class skills
- larger combined runs still exist, but they belong under presets or compatibility layers

This is why names such as `run-full-workflow` are not part of the primary skill catalog.

## Skills For Humans And Agents

The same skills are meant to work for both people and agents.

### Human use

A human user typically reaches a skill through:

- the `cellpainting-skills` CLI
- Python calls through `cellpainting_skills` or `cellpainting_claw`

Minimal CLI pattern:

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill run-segmentation
```

Minimal Python pattern:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation")
print(result.ok)
```

### Agent use

An agent should not invent new task names. It should map a request onto one of the six primary skills.

Examples:

- `Inspect the dataset and prepare a reusable plan.` -> `plan-data-access`
- `Download the selected data locally.` -> `download-data`
- `Generate the classical profiling outputs.` -> `run-classical-profiling`
- `Run segmentation and export single-cell crops.` -> `run-segmentation`
- `Prepare the DeepProfiler inputs but do not run it yet.` -> `prepare-deepprofiler-inputs`
- `Run the DeepProfiler branch and collect deep features.` -> `run-deepprofiler`

## Skill Reference

### `plan-data-access`

**What it does**

This skill inspects the configured data source and writes a reusable access plan without running profiling or segmentation.

**Use it when**

- you need to understand what data is available
- you want to prepare a reproducible download plan before processing
- the first question is about inputs rather than outputs

**Human use**

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill plan-data-access
```

**Agent use**

A request such as `Inspect the dataset and prepare a reusable data-access plan.` should usually land on `plan-data-access`.

**Typical outputs**

- `data_access_summary.json`
- `download_plan.json`

### `download-data`

**What it does**

This skill executes the download step for the current request or plan.

**Use it when**

- the data scope is already known
- you want local files, not just a plan
- the next processing step depends on materialized inputs

**Human use**

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill download-data
```

**Agent use**

A request such as `Download the selected dataset locally before processing.` should usually land on `download-data`.

**Typical outputs**

- `download_plan.json`
- `download_execution.json`

### `run-classical-profiling`

**What it does**

This skill runs the classical profiling path and produces pycytominer-facing outputs.

**Use it when**

- the main goal is classical Cell Painting profiling
- you need single-cell tables or pycytominer outputs
- segmentation artifacts are not the primary target

**Human use**

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill run-classical-profiling
```

**Agent use**

A request such as `Generate the classical profiling outputs for this dataset.` should usually land on `run-classical-profiling`.

**Typical outputs**

- `single_cell.csv.gz`
- `pycytominer/`
- `evaluation/`

### `run-segmentation`

**What it does**

This skill runs the segmentation path and produces masks, previews, and single-cell crops.

**Use it when**

- the main goal is segmentation artifacts
- you need masks or preview images
- you need masked or unmasked single-cell crops

**Human use**

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill run-segmentation
```

**Agent use**

A request such as `Run segmentation and export single-cell crops.` should usually land on `run-segmentation`.

**Typical outputs**

- masks
- sample previews
- masked crops
- unmasked crops

**CellProfiler note**

This skill uses the configured CellProfiler `.cppipe` selection underneath.

### `prepare-deepprofiler-inputs`

**What it does**

This skill stops after preparing the export artifacts needed by DeepProfiler.

**Use it when**

- you want DeepProfiler-ready images and locations
- you are preparing inputs for a later DeepProfiler run
- you do not want the full DeepProfiler branch yet

**Human use**

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill prepare-deepprofiler-inputs
```

**Agent use**

A request such as `Prepare the DeepProfiler inputs but do not run DeepProfiler yet.` should usually land on `prepare-deepprofiler-inputs`.

**Typical outputs**

- export metadata
- DeepProfiler-ready image inputs
- DeepProfiler-ready location inputs

### `run-deepprofiler`

**What it does**

This skill runs the full DeepProfiler-oriented branch through export, project assembly, profiling, and feature collection.

**Use it when**

- you want deep feature extraction, not only export preparation
- you want the standardized DeepProfiler branch end to end

**Human use**

```bash
cellpainting-skills run   --config configs/project_config.demo.json   --skill run-deepprofiler
```

**Agent use**

A request such as `Run the DeepProfiler branch and collect the deep features.` should usually land on `run-deepprofiler`.

**Typical outputs**

- DeepProfiler project files
- profile outputs
- collected deep feature tables

## Legacy Skill Names

Older skill names are still recognized in the Python layer for compatibility, but they are **legacy aliases**, not the recommended public starting point.

Examples include:

- `plan-gallery-data`
- `run-profiling-workflow`
- `run-segmentation-workflow`
- `run-deepprofiler-export`
- `run-deepprofiler-full`
- `run-full-workflow`
- `run-full-workflow-with-data-plan`

Users and agents should prefer the six primary skills listed above.

## Presets Are Not Skills

The library still supports combined runs such as full profiling plus segmentation, but those should be understood as **presets or examples**, not as the main modular skills.

Examples include:

- `full-pipeline`
- `full-pipeline-with-data-plan`

Those are useful convenience bundles, but they should not replace the six primary skills as the public task model.

## Related Pages

- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
- [Quick Start](../quick_start/index.md)
