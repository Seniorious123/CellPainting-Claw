# CellPainting-Claw

[Documentation](https://cellpainting-claw.readthedocs.io/en/latest/)

CellPainting-Claw is a **tool library for Cell Painting analysis**. It provides a cleaner public interface for the tasks that are usually scattered across backend scripts and separate tools: **data access planning**, **classical profiling with pycytominer outputs**, **segmentation-derived single-cell exports**, and **DeepProfiler-ready preparation**.

The same repository is designed to work for both **human users** and **agents**.

The repository is built around two public Python packages:

- `cellpainting_claw`: the main Python API and CLI for Cell Painting tools
- `cellpainting_skills`: the skill-oriented layer for automation, task routing, and agent-facing execution

Rather than replacing the underlying ecosystem, CellPainting-Claw provides a stable way to work with it.

## What This Repository Integrates

CellPainting-Claw brings together the main tool families needed for a practical Cell Painting stack:

- **CellProfiler** for image-based segmentation and classical measurement export
- **pycytominer** for single-cell tables, normalization, feature selection, and well-level profiling outputs
- **DeepProfiler** for single-cell image embedding workflows
- **Cell Painting Gallery / JUMP-style data access helpers** for planning and preparing data retrieval
- **MCP and OpenClaw integration** for agent-facing execution and natural-language-driven task routing

## Public Packages

| Package | Purpose | Typical user |
| --- | --- | --- |
| `cellpainting_claw` | Main library surface for configs, CLI commands, profiling, segmentation, DeepProfiler export, and MCP serving | Python users, CLI users, reproducible workflow scripts |
| `cellpainting_skills` | Skill catalog and skill runner for standardized task execution | Agents, automation layers, natural-language orchestration |

Public CLI entrypoints:

- `cellpainting-claw`
- `cellpainting-skills`
- `cellpainting-claw-tests`

## How The Pieces Fit Together

```text
Cell Painting data sources
        |
        v
Data-access helpers
        |
        +------------------------------+
        |                              |
        v                              v
Classical profiling tools        Segmentation tools
(CellProfiler -> pycytominer)    (masks, previews, single-cell crops)
        |                              |
        |                              v
        |                        DeepProfiler-ready export
        |                              |
        +--------------+---------------+
                       |
                       v
        Python API / CLI / Skills / MCP / OpenClaw
```

This repository is intended to be used as a **toolbox**, not only as one fixed linear workflow.

## Core Capabilities

Current capabilities include:

- **data access planning** for Cell Painting Gallery and JUMP-style sources
- **classical profiling outputs** from CellProfiler-style tables into pycytominer outputs
- **segmentation-derived artifacts** including label masks, preview images, and single-cell crops
- **DeepProfiler preparation** including export-ready inputs and project assembly
- **agent-facing execution** through skills, MCP tools, and OpenClaw integration

## Skills

`cellpainting_skills` defines stable task-level interfaces on top of the lower-level tools.

Current skill catalog:

| Skill key | What it does |
| --- | --- |
| `plan-gallery-data` | Builds a Cell Painting Gallery or JUMP-style data request summary and reusable download plan |
| `run-profiling-workflow` | Runs the classical profiling route and produces pycytominer-oriented outputs |
| `run-segmentation-workflow` | Runs the segmentation route and produces masks, previews, and single-cell crop artifacts |
| `run-deepprofiler-export` | Runs the segmentation-derived export route needed before DeepProfiler-style embedding workflows |
| `run-deepprofiler-full` | Runs the DeepProfiler branch beyond export, including project-oriented preparation |
| `run-full-workflow` | Runs the standard profiling and segmentation tool set together |
| `run-full-workflow-with-data-plan` | Builds a data-access plan first, then runs the standard full workflow |

The point of the skill layer is to make common tasks easier to call consistently from:

- the command line
- Python scripts
- MCP-compatible agent runtimes
- natural-language-driven automation layers

## Runnable Demo

The repository includes a **minimal runnable demo** with bundled backend assets and generated example outputs.

Demo config:

- `configs/project_config.demo.json`

Demo backend roots:

- `demo/backend/profiling_backend/`
- `demo/backend/segmentation_backend/`

Example generated outputs already included in the repository:

- `demo/backend/profiling_backend/outputs/pycytominer/well_aggregated.parquet`
- `demo/backend/profiling_backend/outputs/pycytominer/well_normalized.parquet`
- `demo/backend/segmentation_backend/outputs/cellprofiler_masks/labels/`
- `demo/backend/segmentation_backend/outputs/sample_previews_png/`
- `demo/backend/segmentation_backend/outputs/single_cell_crops_masked/`

This demo is meant to show the public interface on a small, publication-safe example rather than to provide a biologically meaningful benchmark dataset.

## Quick Start

Create the environment and install the package:

```bash
cd <repo-root>
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
```

List the available skills:

```bash
cd <repo-root>
cellpainting-skills list
```

Run a lightweight demo step on the bundled demo config:

```bash
cd <repo-root>
cellpainting-claw run-profiling \
  --config configs/project_config.demo.json \
  --backend native \
  --script-key validate-inputs
```

Run one skill on the same demo config:

```bash
cd <repo-root>
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-profiling-workflow
```

## Python API Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-profiling-workflow")
print(result.ok)
```

## Agent and OpenClaw Integration

CellPainting-Claw can be used directly through Python and CLI, but it also exposes an **agent-facing interface**.

That layer is built around:

- `cellpainting_skills` for stable task-level execution
- MCP serving through the main package
- OpenClaw runtime helpers under `integrations/openclaw/`

OpenClaw is **optional**. The core library does not depend on an agent runtime to be usable.

## What CellPainting-Claw Is Not

CellPainting-Claw is not a replacement for CellProfiler, pycytominer, or DeepProfiler themselves.

It is a **structured interface layer** over those tools so they can be used more consistently, packaged more cleanly, and exposed more safely to scripts, users, and agents.

## Documentation

Start here:

- [Read the Docs](https://cellpainting-claw.readthedocs.io/en/latest/)
- `docs/introduction/`
- `docs/installation/`
- `docs/quick_start/`
- `docs/api/skills.md`
- `integrations/openclaw/`

## Publication Hygiene

Repository-managed docs and config templates are English-only and do not store provider keys.

If a provider key was previously typed into a shell, written into a local config, or pasted into chat, rotate or revoke it before publishing the project.
