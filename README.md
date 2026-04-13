# CellPainting-Claw

[Documentation](https://cellpainting-claw.readthedocs.io/en/latest/)

CellPainting-Claw brings together the main tools used in **Cell Painting work** into one public toolkit. It covers **data access**, **classical processing**, **deep feature extraction**, **named tasks**, and **natural-language use** in one place.

## Supported Packages

CellPainting-Claw integrates or wraps the following package and tool families:

- **CellProfiler** for segmentation, masks, outlines, localization, and measurement export
- **pycytominer** for classical profile generation from single-cell measurement tables
- **DeepProfiler** for learned single-cell feature extraction
- **boto3**, **quilt3**, and **cpgdata** for Cell Painting Gallery / JUMP-style data discovery and planning
- **OpenClaw** through an MCP-facing integration layer for optional natural-language execution

## Public Entry Points

The project exposes **three public entry points**.

| If you want to... | Start with | What you will use it for |
| --- | --- | --- |
| run the project yourself from Python or from the command line | `cellpainting_claw` | use the main toolkit directly for configuration, data access, segmentation-related utilities, classical profiling, and DeepProfiler-related utilities |
| choose from a small set of ready-made named tasks | `cellpainting_skills` | run clear task units such as planning data access, running segmentation, preparing DeepProfiler inputs, or running classical profiling without wiring together lower-level functions yourself |
| tell an agent in plain language what you want done | `OpenClaw` | use an optional natural-language entry point that maps requests onto the same documented skills, so you do not have to choose Python functions or CLI commands yourself |

## What The Repository Includes

At the public interface level, the repository includes:

- a Python toolkit API
- a named-task API
- command-line interfaces for both direct use and skill-based use
- an MCP server surface for agent-facing integrations
- an OpenClaw integration path

## Skill Catalog

Skills are the **core task interface** of the project.

| Skill key | Main purpose | Typical outputs |
| --- | --- | --- |
| `plan-data-access` | inspect the dataset and build a reusable plan | data-access summary and plan JSON |
| `download-data` | execute the local download step | download plan and download execution JSON |
| `run-classical-profiling` | run the classical profiling tool family | single-cell tables and pycytominer outputs |
| `run-segmentation` | run the segmentation tool family | masks, previews, and single-cell crops |
| `prepare-deepprofiler-inputs` | prepare DeepProfiler-ready export artifacts | export metadata and DeepProfiler inputs |
| `run-deepprofiler` | run the DeepProfiler-oriented task path | project files and collected deep features |

## CellProfiler `.cppipe` Support

CellPainting-Claw exposes a **config-driven CellProfiler `.cppipe` selection layer**.

Users can:

- choose a bundled `.cppipe` template
- point to a custom `.cppipe` path
- inspect the effective selection before a longer run
- validate the selection from Python or CLI

The project config accepts a `cellprofiler` block such as:

```json
{
  "cellprofiler": {
    "profiling_template": "profiling-analysis",
    "segmentation_template": "segmentation-base",
    "custom_profiling_cppipe_path": null,
    "custom_segmentation_cppipe_path": null
  }
}
```

Current phase-1 behavior:

- **segmentation** consumes the configured `.cppipe` selection at runtime
- **profiling** already exposes the same template listing, selection, and validation helpers
- custom segmentation overrides are treated as ready-to-run mask-export pipelines

Useful inspection commands:

```bash
cellpainting-claw list-cppipe-templates --config configs/project_config.demo.json
cellpainting-claw show-cppipe-selection --config configs/project_config.demo.json --kind all
cellpainting-claw validate-cppipe-config --config configs/project_config.demo.json
```

## Quick Start

Create the environment and install the package:

```bash
cd <repo-root>
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
```

Use the bundled demo config:

```bash
CONFIG=configs/project_config.demo.json
```

Look at the skill catalog and inspect one task:

```bash
cellpainting-skills list
cellpainting-skills describe --skill run-segmentation
```

Optionally inspect the effective `.cppipe` selection:

```bash
cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind segmentation
cellpainting-claw validate-cppipe-config --config "$CONFIG"
```

Run one skill:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-segmentation
```

## Python API Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation")
print(result.ok)
print(result.segmentation_output_dir)
```

## Agent And OpenClaw Integration

OpenClaw is an **optional natural-language entry point** for the same toolkit.

In normal use, OpenClaw connects to the MCP surface and maps natural-language requests onto the documented skills. It does not replace the core library or CLI.

## Documentation

Start here:

- [Read the Docs](https://cellpainting-claw.readthedocs.io/en/latest/)
- `docs/index.md`
- `docs/skills/index.md`
- `docs/cli/index.md`
- `docs/openclaw/index.md`

## Publication Hygiene

Repository-managed docs and config templates are English-only and do not store provider keys.

If a provider key was previously typed into a shell, written into a local config, or pasted into chat, rotate or revoke it before publishing the project.
