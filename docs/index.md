# CellPainting-Claw

CellPainting-Claw is a **toolkit interface for practical Cell Painting work**. It brings together **data access**, **classical processing**, **deep feature extraction**, **task-level execution**, and **agent-facing use** into one public surface.

The project is designed so that the same validated backend work can be reached in three different ways:

- through the **main toolkit package**
- through the **skills layer**
- through the **OpenClaw agent interface**

## Supported Layers And Packages

CellPainting-Claw integrates packages across several distinct layers of the stack.

| Layer | Packages or tools | Role in the toolkit |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | dataset discovery, access planning, and download preparation |
| Classical processing | `CellProfiler`, `pycytominer` | segmentation, measurement export, profile generation, normalization, and feature selection |
| Deep learning feature extraction | `DeepProfiler` | learned single-cell feature extraction from segmentation-guided crops |
| Task interface | `cellpainting_skills`, MCP tools | stable named tasks for automation, scripting, and controlled agent calls |
| Agent interface | `OpenClaw` | optional natural-language interface on top of the task and MCP layers |

## Public Interfaces

The public surface is organized around **three interface levels**.

| Interface | What it is | Use it when |
| --- | --- | --- |
| `cellpainting_claw` | the main toolkit package | you want the full Python toolkit surface, `.cppipe` inspection, lower-level helpers, or MCP support |
| `cellpainting_skills` | the task package | you want stable named tasks such as `run-segmentation` or `run-deepprofiler` |
| `OpenClaw` | the agent interface | you want natural-language interaction on top of the same validated task layer |

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

## Why This Project Exists

Cell Painting stacks are powerful, but they are often difficult to use consistently because:

- the important tools live in different packages
- one user may want low-level control while another wants task-oriented commands
- human users and agents need different interaction styles
- backend script collections are difficult to expose as a stable public interface

CellPainting-Claw exists to solve that interface problem.

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
