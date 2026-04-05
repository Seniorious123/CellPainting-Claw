# CellPainting-Claw

[Documentation](https://cellpainting-claw.readthedocs.io/en/latest/)

CellPainting-Claw is a **Cell Painting toolkit for both humans and agents**. It provides a cleaner public interface for the tasks that are usually spread across backend scripts, package-specific wrappers, and separate runtimes.

It packages the main task families needed for practical Cell Painting work into one reusable interface.

## Supported Packages

CellPainting-Claw integrates or wraps the following package and tool families:

- **CellProfiler** for segmentation, masks, outlines, localization, and measurement export
- **pycytominer** for classical profile generation from single-cell measurement tables
- **DeepProfiler** for learned single-cell feature extraction
- **boto3**, **quilt3**, and **cpgdata** for Cell Painting Gallery / JUMP-style data discovery and planning
- **OpenClaw** through an MCP-facing integration layer for optional natural-language execution

## Public Python Packages

The repository exposes **two main public Python packages**.

| Package | Role | When to use it |
| --- | --- | --- |
| `cellpainting_claw` | main toolkit package | use this when you want one Python package for config loading, data access, profiling, segmentation, DeepProfiler helpers, `.cppipe` inspection, and MCP serving |
| `cellpainting_skills` | agent- and automation-facing task package | use this when you want stable named tasks that map scripts or natural-language requests onto validated toolkit actions |

## What The Repository Includes

At the public interface level, the repository includes:

- the `cellpainting_claw` Python API
- the `cellpainting_skills` Python API
- the `cellpainting-claw` CLI
- the `cellpainting-skills` CLI
- an MCP server surface
- an OpenClaw integration path

## Skill Catalog

Skills are the **core task interface** of the project.

| Skill key | Main purpose | Typical outputs |
| --- | --- | --- |
| `plan-gallery-data` | inspect data access and build a reusable plan | data-access summary and plan JSON |
| `run-profiling-workflow` | run the classical profiling tool family | single-cell tables and pycytominer outputs |
| `run-segmentation-workflow` | run the segmentation tool family | masks, previews, and single-cell crops |
| `run-deepprofiler-export` | prepare DeepProfiler-ready inputs | export metadata and DeepProfiler inputs |
| `run-deepprofiler-full` | run the DeepProfiler-oriented task path | project files and collected deep features |
| `run-full-workflow` | run the standard combined toolkit task | profiling plus segmentation outputs |
| `run-full-workflow-with-data-plan` | build a data plan first, then run the standard combined task | plan artifacts plus combined outputs |

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
cellpainting-skills describe --skill run-segmentation-workflow
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
  --skill run-segmentation-workflow
```

## Python API Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation-workflow")
print(result.ok)
print(result.segmentation_output_dir)
```

## Agent And OpenClaw Integration

OpenClaw is an **optional natural-language front end** for the same toolkit.

The relationship is:

1. `cellpainting_claw` provides the canonical library and CLI
2. the library can be exposed through MCP
3. OpenClaw can connect to that MCP surface
4. the agent can then call the same toolkit through natural-language requests

OpenClaw does not replace the core library implementation.

## Documentation

Start here:

- [Read the Docs](https://cellpainting-claw.readthedocs.io/en/latest/)
- `docs/index.md`
- `docs/skills/index.md`
- `docs/api/index.md`
- `docs/cli/index.md`
- `docs/openclaw/index.md`

## Publication Hygiene

Repository-managed docs and config templates are English-only and do not store provider keys.

If a provider key was previously typed into a shell, written into a local config, or pasted into chat, rotate or revoke it before publishing the project.
