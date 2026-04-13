# CellPainting-Claw

CellPainting-Claw brings together the main tools used in **Cell Painting work** into one public toolkit. It covers **data access**, **classical processing**, **deep feature extraction**, **named tasks**, and **natural-language use** in one place.

The same validated work can be reached in three different ways:

- through the **main toolkit**
- through the **named-task interface**
- through the **natural-language interface**

## Supported Capabilities And Packages

CellPainting-Claw brings together several core capabilities and the packages that support them.

| Capability | Packages or tools | Role in the toolkit |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | dataset discovery, access planning, and download preparation |
| Classical processing | `CellProfiler`, `pycytominer` | segmentation, measurement export, profile generation, normalization, and feature selection |
| Deep learning feature extraction | `DeepProfiler` | learned single-cell feature extraction from segmentation-guided crops |
| Named-task interface | `cellpainting_skills` | stable named tasks for automation, scripting, and direct task execution |
| Natural-language interface | `OpenClaw` | optional natural-language access to the same documented skills |

## Public Interfaces

The public surface is organized around **three public entry points**.

| If you want to... | Start with | What you will use it for |
| --- | --- | --- |
| run the project yourself from Python or from the command line | `cellpainting_claw` | use the main toolkit directly for configuration, data access, segmentation-related utilities, classical profiling, and DeepProfiler-related utilities |
| choose from a small set of ready-made named tasks | `cellpainting_skills` | run clear task units such as planning data access, running segmentation, preparing DeepProfiler inputs, or running classical profiling without wiring together lower-level functions yourself |
| tell an agent in plain language what you want done | `OpenClaw` | use an optional natural-language entry point that maps requests onto the same documented skills, so you do not have to choose Python functions or CLI commands yourself |

## Current Skill Catalog

Skills are the **core public task interface** of the project.

| Skill key | Main purpose | Typical result |
| --- | --- | --- |
| `plan-data-access` | inspect a dataset and write a reusable plan | data-access summary and plan JSON |
| `download-data` | execute the local download step | download plan and download execution JSON |
| `run-classical-profiling` | run the classical profiling tool path | single-cell tables and pycytominer outputs |
| `run-segmentation` | run the segmentation tool path | masks, previews, and single-cell crops |
| `prepare-deepprofiler-inputs` | prepare DeepProfiler-ready inputs | DeepProfiler export metadata and inputs |
| `run-deepprofiler` | run the DeepProfiler-oriented tool path | project files and collected deep features |

## Where To Start

Start with these pages:

- [Introduction](introduction/index.md)
- [Quick Start](quick_start/index.md)
- [Skills](skills/index.md)
- [CLI](cli/index.md)
- [OpenClaw](openclaw/index.md)

```{toctree}
:maxdepth: 2
:caption: Introduction
:hidden:

introduction/index
```

```{toctree}
:maxdepth: 2
:caption: Installation
:hidden:

installation/index
```

```{toctree}
:maxdepth: 2
:caption: Quick Start
:hidden:

quick_start/index
```

```{toctree}
:maxdepth: 2
:caption: Skills
:hidden:

skills/index
```

```{toctree}
:maxdepth: 2
:caption: CLI
:hidden:

cli/index
```

```{toctree}
:maxdepth: 2
:caption: OpenClaw
:hidden:

openclaw/index
```
