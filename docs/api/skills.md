# CellPainting-Skills

`cellpainting_skills` is the **task-oriented public layer** of CellPainting-Claw.

It exists so that common Cell Painting tasks can be called through **stable task names** instead of requiring users or agents to work directly with lower-level parameter combinations.

## What A Skill Means In This Project

In this project, a **skill** is a named task interface.

A skill does not define a separate backend. Instead, it gives a stable name to a commonly used tool-level action or tool combination, such as:

- planning data access
- running classical profiling
- running segmentation exports
- preparing DeepProfiler-oriented outputs
- running a standard full tool combination

This makes the library easier to use from:

- command-line automation
- Python scripts
- MCP-compatible systems
- agent runtimes such as OpenClaw

## Public Python Surface

The main Python helpers exposed by `cellpainting_skills` are:

- `PipelineSkillDefinition`
- `available_pipeline_skills`
- `get_pipeline_skill_definition`
- `pipeline_skill_definition_to_dict`
- `run_pipeline_skill`

## Current Skill Catalog

The current repository defines the following stable skill keys.

### `plan-gallery-data`

Purpose:
Prepare a Cell Painting Gallery or JUMP-style data summary together with a reusable download plan.

Use it when:
You want to inspect or prepare data access before running profiling or segmentation tools.

### `run-profiling-workflow`

Purpose:
Run the classical profiling route and produce profiling-oriented outputs based on the configured backend.

Use it when:
You want the pycytominer-oriented path without also running the segmentation export or DeepProfiler-oriented path.

### `run-segmentation-workflow`

Purpose:
Run the segmentation route and produce masks, previews, and single-cell crop-related artifacts.

Use it when:
You want segmentation-derived outputs without focusing on the classical profiling branch.

### `run-deepprofiler-export`

Purpose:
Run the export-oriented preparation needed before DeepProfiler-style embedding workflows.

Use it when:
You want the segmentation-derived export artifacts used as the upstream input for DeepProfiler.

### `run-deepprofiler-full`

Purpose:
Run the DeepProfiler-oriented branch beyond export and into the full prepared DeepProfiler path.

Use it when:
You want the DeepProfiler side of the toolkit rather than only the classical profiling outputs.

### `run-full-workflow`

Purpose:
Run the standard combined tool set used by the repository for the main profiling and segmentation surfaces.

Use it when:
You want the standard combined run instead of selecting only one capability group.

### `run-full-workflow-with-data-plan`

Purpose:
Prepare a data-access plan first and then run the standard combined tool set.

Use it when:
You want to keep the data-access preparation step explicit as part of the same task-level entrypoint.

## How Skills Are Implemented

In the current implementation, each skill is defined by a small structured object containing:

- a stable `key`
- a human-readable `description`
- a `preset_key` used by the lower-level implementation
- optional `defaults`

This means that the skills layer is currently a **named task layer over the lower-level preset system**.

That is intentional: the skill name is the stable public handle, while the lower-level preset mapping remains an implementation detail.

## CLI Usage

The skills layer has its own CLI:

```bash
cellpainting-skills --help
```

The three main commands are:

### List all skills

```bash
cellpainting-skills list
```

### Describe one skill

```bash
cellpainting-skills describe --skill run-profiling-workflow
```

### Run one skill

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-profiling-workflow
```

## Python Usage

A minimal Python example looks like this:

```python
import cellpainting_skills as cps
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
print(cps.available_pipeline_skills())
result = cps.run_pipeline_skill(config, "run-profiling-workflow")
print(result.ok)
```

## When To Use Skills Instead Of Other Interfaces

Use `cellpainting_skills` when:

- you want **stable task names**
- you are building **automation** on top of the library
- you want a more agent-friendly public surface
- you want one layer above the raw main CLI and Python entrypoints

Use `cellpainting_claw` instead when:

- you want the broader toolkit surface directly
- you need lower-level CLI commands such as profiling-side or data-access commands
- you want the canonical Python package and MCP server surface

## Relationship To OpenClaw

OpenClaw does not introduce a separate workflow implementation.

Instead, OpenClaw can call the same underlying CellPainting-Claw toolkit through MCP, and the skills layer is one of the most natural ways to expose task-level behavior to an agent runtime.

This is why `cellpainting_skills` is important to the project: it is not only a convenience wrapper for users, but also part of the bridge between the toolkit and agent-facing execution.

## Related Pages

- [Public Entrypoints](public_entrypoints.md)
- [Command-Line Interface](cli.md)
- [OpenClaw](../openclaw/index.md)
