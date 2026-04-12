# CellPainting-Skills

`cellpainting_skills` is the **named-task package** of CellPainting-Claw.

Its job is simple: it gives users and agents a **small set of stable task names** for common work. Instead of starting from many lower-level helpers, a user can start from tasks such as `run-segmentation` or `run-deepprofiler`.

## What A Skill Is

In this project, a skill is a **named task**.

A skill is not a separate backend. It is a public task name that maps onto an implementation in the main toolkit.

This makes the project easier to use in practice:

- a human user can choose a task by name
- a script can call the same task repeatedly
- an agent can map a natural-language request onto a stable task name

## Where Skills Fit

The toolkit brings together several connected capability areas.

| Capability | Main tools | What this part does |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | inspect datasets, build plans, and download inputs |
| Image processing and measurement export | `CellProfiler` | produce masks, outlines, crops, and single-cell measurement tables |
| Classical profile generation | `pycytominer` | build classical profiles from single-cell tables |
| Deep feature extraction | `DeepProfiler` | build learned features from segmentation-guided crops |
| Named task interface | `cellpainting_skills` | expose stable named tasks across those capabilities |
| Agent interface | `OpenClaw` | trigger the same named tasks through natural-language requests |

## The Six Primary Skills

These are the **six primary skills** in the current public task catalog.

| Skill key | Main use | Typical outputs |
| --- | --- | --- |
| [`plan-data-access`](plan_data_access.md) | inspect a dataset and write a reusable plan | `data_access_summary.json`, `download_plan.json` |
| [`download-data`](download_data.md) | execute the local download step | `download_plan.json`, `download_execution.json` |
| [`run-classical-profiling`](run_classical_profiling.md) | build classical profiling outputs | `single_cell.csv.gz`, `pycytominer/`, `evaluation/` |
| [`run-segmentation`](run_segmentation.md) | build masks, previews, and single-cell crops | masks, previews, masked crops, unmasked crops |
| [`prepare-deepprofiler-inputs`](prepare_deepprofiler_inputs.md) | prepare DeepProfiler-ready export artifacts | export metadata, image inputs, location inputs |
| [`run-deepprofiler`](run_deepprofiler.md) | run the DeepProfiler path and collect deep features | project files, profile outputs, deep feature tables |

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

plan_data_access
download_data
run_classical_profiling
run_segmentation
prepare_deepprofiler_inputs
run_deepprofiler
```

## Related Pages

- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
- [Quick Start](../quick_start/index.md)
