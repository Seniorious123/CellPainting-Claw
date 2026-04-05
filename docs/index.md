# CellPainting-Claw

CellPainting-Claw is a **Cell Painting toolkit for both humans and agents**. It turns a stack that is usually spread across backend scripts, package-specific conventions, and separate runtimes into a cleaner public interface.

It packages the main task families needed for practical Cell Painting work into one reusable interface.

## Supported Packages

CellPainting-Claw integrates or wraps the following package and tool families.

| Package or tool | Role in the toolkit |
| --- | --- |
| `CellProfiler` | segmentation, masks, outlines, object localization, and classical measurement export |
| `pycytominer` | single-cell to well-level profile generation, normalization, and feature selection |
| `DeepProfiler` | learned single-cell feature extraction from segmentation-guided crops |
| `boto3` | direct Cell Painting Gallery and S3-style access |
| `quilt3` | package-oriented dataset discovery for Cell Painting Gallery / JUMP-style sources |
| `cpgdata` | inventory-style data browsing and sync helpers |
| `OpenClaw` | optional natural-language and MCP-based agent front end |

## Public Python Packages

The repository exposes **two main public Python packages**.

### `cellpainting_claw`

`cellpainting_claw` is the **main Python package** of the toolkit.

Use it when you want to:

- load a project config and inspect what a run will do
- plan data access or prepare dataset downloads
- run profiling, segmentation, or DeepProfiler helper steps from Python
- inspect which CellProfiler `.cppipe` template a config will use
- expose the toolkit to an MCP-compatible agent runtime

In practical terms, this is the package to import when you want the **full toolkit surface** in Python.

### `cellpainting_skills`

`cellpainting_skills` is the **agent- and automation-facing Python package**.

Use it when you want to:

- browse the skill catalog
- inspect what each named task will do before running it
- run stable tasks such as profiling, segmentation, or DeepProfiler export
- map scripted or natural-language requests onto validated toolkit actions
- give agents a narrower and more stable execution surface

In practical terms, import `cellpainting_skills` when you want to say **"run this named task"** and let the toolkit route that request to the right validated implementation.

## What The Toolkit Contains

At the release surface, CellPainting-Claw provides:

- the `cellpainting_claw` Python API
- the `cellpainting_skills` Python API
- the `cellpainting-claw` command-line interface
- the `cellpainting-skills` command-line interface
- an MCP server surface for agent runtimes
- an OpenClaw integration path

This means the same repository can be used as:

- a Python toolkit
- a shell toolkit
- a skills-oriented automation layer
- an agent-facing tool surface

## Current Skill Catalog

Skills are the **core task interface** of the project.

| Skill key | Main purpose | Typical result |
| --- | --- | --- |
| `plan-gallery-data` | prepare a data summary and reusable download plan | data-access summary and plan JSON |
| `run-profiling-workflow` | run the classical profiling tool path | single-cell tables and pycytominer outputs |
| `run-segmentation-workflow` | run the segmentation tool path | masks, previews, and single-cell crops |
| `run-deepprofiler-export` | prepare DeepProfiler-ready inputs | DeepProfiler export metadata and inputs |
| `run-deepprofiler-full` | run the DeepProfiler-oriented tool path | project files and collected deep features |
| `run-full-workflow` | run the standard profiling and segmentation tool set together | combined profiling and segmentation outputs |
| `run-full-workflow-with-data-plan` | plan data access first, then run the standard combined tool set | plan artifacts plus combined outputs |

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
- [API](api/index.md)
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
:caption: API
:hidden:

api/index
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
