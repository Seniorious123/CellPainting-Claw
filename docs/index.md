# CellPainting-Claw

CellPainting-Claw is a documentation and workflow surface for **standardized Cell Painting pipelines from raw image data to analysis-ready outputs**. It brings together **dataset access**, **CellProfiler-based segmentation**, **classical profiling through `pycytominer`**, **DeepProfiler-based single-cell feature extraction**, and **agent-mediated natural-language execution** through one documented public interface.

## At a Glance

The main ideas of the project are:

- **One shared upstream workflow backbone**: raw image data is converted into structured segmentation-derived outputs.
- **Two downstream analysis branches**: the same upstream stage can continue toward either classical profile tables or DeepProfiler embeddings.
- **Two execution styles**: the workflow can be run through Python and the CLI, or through an agent layer such as OpenClaw.
- **One release-oriented interface layer**: validated backend assets stay in place, but the public surface becomes easier to reuse, automate, and document.

## Documentation Guide

The documentation is organized around the main stages of use:

- **Introduction** explains the workflow structure, including the shared segmentation backbone and the two downstream analysis branches.
- **Installation** describes the recommended environment and package installation path.
- **Quick Start** shows the shortest path from installation to a first workflow run.
- **Workflows** explains the shared upstream stage, the classical profiling branch, the DeepProfiler branch, and the orchestration layer.
- **API** documents the public Python packages and command-line interfaces.
- **OpenClaw** documents the optional natural-language and MCP-facing integration layer.

## Reading Path

For a first pass through the project, the recommended reading order is:

1. Introduction
2. Installation
3. Quick Start
4. Workflows
5. API
6. OpenClaw, if you want agent-mediated or natural-language execution

```{toctree}
:maxdepth: 2
:caption: Introduction

introduction/index
```

```{toctree}
:maxdepth: 2
:caption: Installation

installation/index
```

```{toctree}
:maxdepth: 2
:caption: Quick Start

quick_start/index
```

```{toctree}
:maxdepth: 2
:caption: Workflows

workflows/index
```

```{toctree}
:maxdepth: 2
:caption: API

api/index
```

```{toctree}
:maxdepth: 2
:caption: OpenClaw

openclaw/index
```
