# Installation

This page describes the recommended installation path for CellPainting-Claw. The goal of installation is to obtain a working runtime for **raw-data-to-profile workflows**, including **CellProfiler-based segmentation**, **classical profiling through `pycytominer`**, and the **DeepProfiler branch**, with the public **Python**, **CLI**, and **agent-facing MCP** surfaces available on top.

## Prerequisites

Before installing the package, make sure you have:

- a local checkout of the `CellPainting-Claw` repository
- Conda available on the target machine
- permission to create a dedicated environment for the workflow

CellPainting-Claw currently ships with a **validated Conda environment file**:

- `environment/cellpainting-claw.environment.yml`

That environment targets **Python 3.10** and includes the workflow dependencies used by this repository, including **CellProfiler**, **pycytominer**, and the **DeepProfiler-related stack**.

## Recommended Installation Path

From the repository root, create and activate the Conda environment:

```bash
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
```

Then install the package itself in editable mode:

```bash
pip install -e .
```

This is the **recommended installation path** for the current project because the validated workflow depends on a **mixed Conda and pip stack**.

## What Gets Installed

After installation, the repository exposes **these main public interfaces**.

### Python packages

- `cellpainting_claw`
- `cellpainting_skills`

### Command-line entrypoints

- `cellpainting-claw`
- `cellpainting-skills`
- `cellpainting-claw-tests`

## Optional Extras

The project also defines optional extras in `pyproject.toml`. These are mainly useful when building a more customized environment instead of relying on the validated Conda environment.

```bash
pip install -e .[test]
pip install -e .[mcp]
pip install -e .[data-access]
pip install -e .[deepprofiler]
```

In the current repository, the **validated Conda environment already includes the main workflow stack** used by the standard installation path.

## Verify the Installation

A minimal post-installation check is to confirm that the public CLI entrypoints are available:

```bash
cellpainting-claw --help
cellpainting-skills --help
```

You can also verify the import surface in Python:

```python
import cellpainting_claw
import cellpainting_skills
```

If both the **CLI** and **imports** work, the **package layer is installed correctly**.

## Scope and Boundaries

The **Python API** and **CLI** are the **primary runtime interfaces**.

**OpenClaw is optional.** It is an additional agent-facing integration layer and is not required for installation or normal library use.

## Where To Go Next

After installation, the recommended next pages are:

- [Quick Start](../quick_start/index.md) for the shortest first run
- [Workflows](../workflows/index.md) for the pipeline structure
- [API](../api/index.md) for the public interfaces
- [OpenClaw](../openclaw/index.md) if you want natural-language or agent-mediated execution
