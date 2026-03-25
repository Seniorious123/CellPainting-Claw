# CellPainting-Claw

CellPainting-Claw is a release-oriented software interface for validated Cell Painting workflows.

It turns a previously script-heavy analysis setup into a cleaner package with four public layers:

- a Python API for reproducible workflow execution
- a CLI for standardized pipeline runs
- a skill layer for agent-facing task routing
- MCP integration surfaces for OpenClaw and related MCP-compatible agents

The project is designed to sit on top of validated backend workspaces rather than hide them. In practice, that means you can keep the proven profiling, segmentation, and DeepProfiler assets while exposing them through a cleaner and more automatable interface.

## Sections

```{toctree}
:maxdepth: 2
:caption: Introduction

introduction
```

```{toctree}
:maxdepth: 2
:caption: Installation

installation/index
```

```{toctree}
:maxdepth: 2
:caption: Get Started

get_started/index
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
:caption: Release and Deployment

release/index
faq
```
