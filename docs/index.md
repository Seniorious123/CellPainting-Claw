# CellPainting-Claw

CellPainting-Claw is a release-oriented workflow library for standardized Cell Painting analysis. It provides a structured public surface around a validated workflow that spans segmentation, classical profiling, DeepProfiler integration, and automation-facing access layers.

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
