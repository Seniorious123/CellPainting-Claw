# Public Entrypoints

The main Python toolkit surface is exposed through `cellpainting_claw`.

This page describes the most important public Python entrypoints and how they relate to one another.

## What Counts As A Public Entrypoint

In this project, a public entrypoint is a stable top-level function exposed for normal library use.

These functions are the Python-side counterparts of the documented CLI and skills layers. They are the functions users should prefer over internal modules when writing notebooks, scripts, wrappers, or automation.

## Main Public Entrypoints

The most important top-level entrypoints are:

- `ProjectConfig`
- `run_end_to_end_pipeline`
- `run_pipeline_preset`
- `run_pipeline_skill`
- `run_deepprofiler_pipeline`

The package also exposes public helpers for data access and lower-level suite execution, but the functions above are the most important starting points for most readers.

## `ProjectConfig`

`ProjectConfig` is the main configuration object used across the toolkit.

Use it when:

- loading a project config JSON
- resolving backend roots and output roots
- passing one consistent configuration object into the public Python API

Minimal example:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
```

## `run_end_to_end_pipeline`

`run_end_to_end_pipeline` is the broadest top-level orchestration entrypoint.

Use it when:

- you want one standard combined run from the main toolkit surface
- you want the library to coordinate multiple capability groups through one call
- you are intentionally choosing the highest-level orchestration interface

This function is still public, but it should not be treated as the only important interface in the project. CellPainting-Claw is a toolkit, not only one broad orchestration wrapper.

## `run_pipeline_preset`

`run_pipeline_preset` executes a named preset.

Use it when:

- you already know the task shape you want
- you want a named parameter bundle without calling lower-level orchestration options directly
- you are building a reproducible wrapper around known toolkit behavior

A preset is lower-level than a skill and more explicit about the implementation shape.

## `run_pipeline_skill`

`run_pipeline_skill` executes a named skill.

Use it when:

- stable task names are more important than raw parameter bundles
- you are building automation or agent-facing execution
- you want a task-level interface on top of the broader toolkit

This is the most important bridge between the main Python toolkit and the `cellpainting_skills` layer.

## `run_deepprofiler_pipeline`

`run_deepprofiler_pipeline` is the dedicated public entrypoint for the DeepProfiler-oriented path.

Use it when:

- you want to enter the DeepProfiler side of the toolkit directly
- you are working with DeepProfiler preparation, project assembly, or profile collection as a dedicated task
- you do not want to start from the broader combined orchestration surface

## Supporting Public Areas

The package also exposes public helpers for:

- data-access planning through functions such as `build_data_request`, `build_download_plan`, and `execute_download_plan`
- direct suite execution through `run_profiling_suite` and `run_segmentation_suite`
- public API discovery helpers exposed through the public API module

These helpers are still part of the public surface, but they are more specialized than the main entrypoints listed above.

## Minimal Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-profiling-workflow")
print(result.ok)
```

## Relationship To Other Public Layers

This page documents the **main Python toolkit surface**.

If you want:

- stable task names, continue to [CellPainting-Skills](../skills/index.md)
- shell-oriented execution, continue to [Command-Line Interface](../cli/index.md)
- natural-language or agent-mediated execution, continue to [OpenClaw](../openclaw/index.md)
