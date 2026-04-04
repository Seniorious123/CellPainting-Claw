# CellPainting-Skills

`cellpainting_skills` is the **task-oriented package** of CellPainting-Claw.

This package exposes the toolkit through **stable named tasks** for users, automation, and agent runtimes.

## What A Skill Is

In this project, a skill is a **named task interface**.

A skill does not define a separate backend. It maps a stable task name onto the validated toolkit implementation underneath.

This makes the project easier to use from:

- Python automation
- shell automation
- MCP-compatible systems
- OpenClaw and other agent runtimes

## Public Python Surface

The main Python helpers exposed by `cellpainting_skills` are:

- `PipelineSkillDefinition`
- `available_pipeline_skills`
- `get_pipeline_skill_definition`
- `pipeline_skill_definition_to_dict`
- `run_pipeline_skill`

## Skill Catalog

The current repository defines the following stable skills.

| Skill key | Main tool families | What it is for | Typical outputs |
| --- | --- | --- | --- |
| `plan-gallery-data` | data access | inspect a dataset and build a reusable download plan | data-access summary and plan JSON |
| `run-profiling-workflow` | classical profiling | run the pycytominer-oriented profiling path | single-cell tables, pycytominer outputs, validation report |
| `run-segmentation-workflow` | segmentation | run the segmentation tool family | masks, previews, masked crops, unmasked crops |
| `run-deepprofiler-export` | segmentation + DeepProfiler preparation | prepare the export artifacts needed before DeepProfiler profiling | DeepProfiler-ready export inputs and manifests |
| `run-deepprofiler-full` | segmentation + DeepProfiler | run the DeepProfiler-oriented task path | project files, profile outputs, collected deep features |
| `run-full-workflow` | profiling + segmentation | run the standard combined tool set | profiling outputs plus segmentation outputs |
| `run-full-workflow-with-data-plan` | data access + profiling + segmentation | build a data plan first, then run the standard combined tool set | plan artifacts plus combined toolkit outputs |

## Each Skill In Plain Terms

### `plan-gallery-data`

Use this skill when the main question is **what data should be downloaded**.

Typical result:

- a dataset summary
- a reusable download plan
- no profiling or segmentation run

### `run-profiling-workflow`

Use this skill when the main goal is **classical Cell Painting profiling**.

Typical result:

- single-cell measurement tables
- pycytominer-oriented outputs
- validation reporting for the profiling-side task

### `run-segmentation-workflow`

Use this skill when the main goal is **segmentation-derived artifacts**.

Typical result:

- CellProfiler-style masks and related outputs
- preview images
- single-cell crop artifacts

This skill is also the clearest place where the current `.cppipe` selection layer matters at runtime.

### `run-deepprofiler-export`

Use this skill when you want to **stop after preparing DeepProfiler-ready inputs**.

Typical result:

- export metadata
- DeepProfiler-ready image and location inputs
- no full DeepProfiler project or profile run yet

### `run-deepprofiler-full`

Use this skill when you want the **DeepProfiler-oriented tool path itself**.

Typical result:

- export artifacts
- project assembly
- profiling outputs
- collected deep feature tables

### `run-full-workflow`

Use this skill when you want the **standard combined toolkit task**.

Typical result:

- profiling outputs
- segmentation outputs
- validation reporting

### `run-full-workflow-with-data-plan`

Use this skill when you want the same combined toolkit task, but with the **data-planning step made explicit** as part of the same task.

Typical result:

- data-access summary and plan
- profiling outputs
- segmentation outputs
- validation reporting

## How Skills Relate To The Toolkit

The skills layer is intentionally one step above the lower-level toolkit surface.

In the current implementation, each skill maps to:

- a stable skill `key`
- a task `description`
- a lower-level `preset_key`
- optional default options

That design is intentional:

- the **skill name** is the stable public handle
- the **preset mapping** remains an implementation detail

## Skills And `.cppipe` Configuration

Skills do **not** expose raw CellProfiler `.cppipe` complexity directly.

Instead:

- the skill chooses the task
- the project config chooses the effective `.cppipe`
- the toolkit validates the selection before a longer run

This keeps skills stable while still allowing advanced CellProfiler customization underneath.

## CLI Usage

The skills layer has its own CLI.

### List all skills

```bash
cellpainting-skills list
```

### Describe one skill

```bash
cellpainting-skills describe --skill run-segmentation-workflow
```

### Run one skill

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-segmentation-workflow
```

## Python Usage

```python
import cellpainting_claw as cp
import cellpainting_skills as cps

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
print(cps.available_pipeline_skills())
result = cps.run_pipeline_skill(config, "run-segmentation-workflow")
print(result.ok)
```

## When To Use Skills

Use `cellpainting_skills` when:

- stable task names matter more than low-level command selection
- you are building automation on top of the toolkit
- you want the most agent-friendly public surface
- you want one clear task entrypoint

Use `cellpainting_claw` instead when:

- you want lower-level tool access directly
- you need data-access helpers, suite runners, or configuration helpers
- you want the canonical Python package and main CLI

## Related Pages

- [API](../api/index.md)
- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
