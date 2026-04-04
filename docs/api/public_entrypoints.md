# Public Entrypoints

The main Python toolkit surface is exposed through `cellpainting_claw`.

This page describes the most important public entrypoints and helper families, with an emphasis on **what each one is for**.

## Configuration Layer

### `ProjectConfig`

`ProjectConfig` is the main configuration object used across the toolkit.

Use it when you need:

- one resolved config object for Python calls
- backend-root and output-root resolution
- access to nested config blocks such as data access or CellProfiler selection

Minimal example:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
```

### `CellProfilerConfig`

`CellProfilerConfig` is the nested config object that controls the **public `.cppipe` selection layer**.

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

This block is what allows users to stay inside the public toolkit interface instead of editing backend files as the default workflow.

## `.cppipe` Helper Family

The main package exposes a public helper family for CellProfiler `.cppipe` inspection and validation.

The most important helpers are:

- `available_cppipe_templates`
- `get_cppipe_template`
- `cppipe_template_definition_to_dict`
- `resolve_cppipe_selection`
- `resolved_cppipe_selection_to_dict`
- `validate_cppipe_configuration`
- `cppipe_validation_result_to_dict`

Use this helper family when you want to:

- inspect the bundled `.cppipe` catalog
- resolve which `.cppipe` a config will actually use
- validate a custom `.cppipe` path before a longer task starts

Minimal example:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
selection = cp.resolve_cppipe_selection(config, "segmentation")
validation = cp.validate_cppipe_configuration(config)

print(selection.cppipe_path)
print(validation.ok)
```

Current phase-1 scope:

- **segmentation** consumes the selected `.cppipe` at runtime
- **profiling** exposes the same inspection and validation helpers, while the public profiling route remains post-CellProfiler-oriented

## Task Entry Layer

These are the most important task-oriented entrypoints exposed by the main package.

| Function | When to use it |
| --- | --- |
| `run_pipeline_skill` | when you want a stable named task |
| `run_pipeline_preset` | when you want a named parameter bundle |
| `run_end_to_end_pipeline` | when you intentionally want one broad combined run |
| `run_deepprofiler_pipeline` | when you want the dedicated DeepProfiler path directly |

### `run_pipeline_skill`

This is the most important bridge between the main package and the skills layer.

Use it when:

- task names matter more than low-level option selection
- you are building automation or agent-facing wrappers
- you want one stable task entrypoint such as `run-segmentation-workflow`

Example:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation-workflow")
print(result.ok)
print(result.segmentation_output_dir)
```

### `run_pipeline_preset`

Use `run_pipeline_preset` when you already know the lower-level task shape you want, but you still want to call it through a named bundle.

This is more explicit than a skill and less raw than hand-building all orchestration arguments yourself.

### `run_end_to_end_pipeline`

Use this function only when you intentionally want the broader combined toolkit run.

It is public, but it is **not the only important interface in the repository**. Most users should start with skills or smaller helper families first.

### `run_deepprofiler_pipeline`

Use this function when the task is specifically about the DeepProfiler tool family rather than the broader combined toolkit.

## Tool Execution Helpers

The main package also exposes lower-level execution helpers for users who do not want to start from skills.

Examples include:

- `run_profiling_suite`
- `run_segmentation_suite`
- `run_segmentation_bundle`
- `run_deepprofiler_full_stack`

Use these when you want one **tool-family runner** without moving all the way up to a combined task.

## Data-Access Helpers

The main package also exposes public data-access helpers such as:

- `build_data_request`
- `build_download_plan`
- `execute_download_plan`
- `summarize_data_access`

Use these when the main question is about **dataset discovery and planning**, not yet about profiling or segmentation execution.

## Choosing The Right Python Entry Point

A practical rule is:

- use `run_pipeline_skill` first
- use `run_pipeline_preset` when you want a named bundle with more explicit task shape
- use `run_end_to_end_pipeline` only when you intentionally want the broad combined run
- use lower-level helper families when you want direct control over data access, suites, or `.cppipe` selection

## Relationship To Other Public Layers

If you want:

- the task catalog, continue to [Skills](../skills/index.md)
- shell-facing command groups, continue to [CLI](../cli/index.md)
- natural-language or agent-mediated execution, continue to [OpenClaw](../openclaw/index.md)
