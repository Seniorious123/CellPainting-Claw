# Installation

This page describes the current installation path for CellPainting-Claw based on the validated repository environment.

## Requirements

CellPainting-Claw currently targets Python 3.10 and provides a validated Conda environment file in `environment/cellpainting-claw.environment.yml`. That environment includes the dependencies required for the main workflow surface, including CellProfiler, pycytominer, and DeepProfiler-related packages.

The repository is designed around Conda-based installation because the validated workflow depends on packages that are easier to manage together through Conda and pip in one environment.

## Create the Environment

From the repository root:

```bash
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
```

If the environment already exists, reuse it instead of recreating it.

## Install the Package

Install CellPainting-Claw in editable mode from the repository root:

```bash
pip install -e .
```

This exposes the public Python packages and CLI entrypoints defined by the project:

- `cellpainting_claw`
- `cellpainting_skills`
- `cellpainting-claw`
- `cellpainting-skills`
- `cellpainting-claw-tests`

## Optional Dependency Groups

The project also defines optional extras in `pyproject.toml`. If needed, you can install them explicitly:

```bash
pip install -e .[test]
pip install -e .[mcp]
pip install -e .[data-access]
pip install -e .[deepprofiler]
```

In practice, the validated Conda environment already includes the main workflow stack used by this repository.

## Verify the Installation

A minimal verification step is to check that the CLI is available:

```bash
cellpainting-claw --help
cellpainting-skills --help
```

You can also verify the import surface in Python:

```python
import cellpainting_claw
import cellpainting_skills
```

## Notes

- The Python API and CLI are the primary runtime interfaces.
- OpenClaw is an additional agent-facing integration layer, not a requirement for installation.
- Configuration and first workflow execution are covered in later documentation sections.
