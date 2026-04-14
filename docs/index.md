# CellPainting-Claw

CellPainting-Claw turns a **fragmented Cell Painting toolchain** into one skill-driven interface, bringing scattered packages and workflow steps together while making the same work easier to use directly and easier to access through agent-friendly natural-language requests.

The same documented skills can be used in two ways:

- **run the skills directly**
- **run the same skills through an agent**

## Supported Capabilities And Packages

CellPainting-Claw brings together several core capabilities and the packages that support them.

| Capability | Packages or tools | Role in the toolkit |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | dataset discovery, access planning, and download preparation |
| Classical processing | `CellProfiler`, `pycytominer` | segmentation, measurement export, profile generation, normalization, and feature selection |
| Deep learning feature extraction | `DeepProfiler` | learned single-cell feature extraction from segmentation-guided crops |
| Named-task interface | `cellpainting_skills` | stable named tasks for automation, scripting, and direct task execution |
| Natural-language interface | `OpenClaw` | optional natural-language access to the same documented skills |

## How To Use CellPainting-Claw

For most users, CellPainting-Claw should be understood through **two main usage paths**.

| If you want to... | Start with | What happens underneath |
| --- | --- | --- |
| run documented tasks yourself from Python or from the command line | `cellpainting_skills` | you call the documented skills directly, such as segmentation, classical profiling, or DeepProfiler-related tasks |
| tell an agent in plain language what you want done | `OpenClaw` | the agent maps your request onto the same documented skills and runs them through the same underlying toolkit |

The lower-level `cellpainting_claw` package remains available for advanced direct package use, but it is not the main starting point for most users.

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
