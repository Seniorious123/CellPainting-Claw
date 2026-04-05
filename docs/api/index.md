# API

This section documents the **Python-side toolkit surface** exposed by CellPainting-Claw.

The main API package is `cellpainting_claw`. The agent- and automation-facing task package `cellpainting_skills` is documented separately under [Skills](../skills/index.md).

## What The Python API Covers

The Python API is easier to understand as **five helper families**.

| API family | What it covers |
| --- | --- |
| configuration | `ProjectConfig`, `CellProfilerConfig`, and config-contract helpers |
| task entrypoints | `run_pipeline_skill`, `run_pipeline_preset`, `run_end_to_end_pipeline` |
| tool execution | profiling suites, segmentation suites, DeepProfiler helpers |
| data access | request building, download planning, download execution |
| CellProfiler `.cppipe` helpers | template listing, selection resolution, and validation |

## Which Package To Use

### `cellpainting_claw`

Use `cellpainting_claw` when you want:

- the main Python toolkit surface
- direct access to configuration, data access, profiling, segmentation, and DeepProfiler helpers
- direct control over configuration and tool selection
- public `.cppipe` inspection and validation helpers

### `cellpainting_skills`

Use `cellpainting_skills` when you want:

- stable named tasks
- one layer above the lower-level API
- a simpler task surface for automation and agent callers

## What This API Section Focuses On

This section focuses on:

- the main config objects
- the most important public entrypoints
- the public helper families exposed by the main package
- the `.cppipe` configuration and validation layer

## Relationship To Other Sections

If you want:

- the full skill catalog, continue to [Skills](../skills/index.md)
- shell-facing command groups, continue to [CLI](../cli/index.md)
- agent-mediated use, continue to [OpenClaw](../openclaw/index.md)

## Page Guide

### Public Entrypoints

This page documents the main top-level functions and helper families exposed by `cellpainting_claw`.

Use it when you want to answer questions such as:

- which Python entrypoint should I call first?
- which helper family is responsible for `.cppipe` selection?
- when should I use skills instead of the lower-level API?

```{toctree}
:maxdepth: 1

public_entrypoints
```
