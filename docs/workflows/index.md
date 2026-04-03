# Workflow Reference

This section is a **supplementary reference** for readers who want extra detail about how the underlying processing chain fits together.

It is not the main reading path for the project.

For most users, the primary documentation path is:

- [Introduction](../introduction/index.md)
- [Quick Start](../quick_start/index.md)
- [API](../api/index.md)
- [Skills](../skills/index.md)
- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)

## What This Section Contains

The pages in this section describe the processing logic that connects:

- raw Cell Painting image inputs
- segmentation-derived outputs such as labels, masks, and single-cell crops
- classical profiling outputs through `pycytominer`
- DeepProfiler-oriented preparation and downstream embedding workflows

Use this section when you want a more process-oriented explanation of how those components fit together.

## Suggested Use

Treat these pages as supporting reference, not as the main way to learn the project structure.

If you want to understand the public interfaces first, return to:

- [API](../api/index.md)
- [Skills](../skills/index.md)
- [CLI](../cli/index.md)

```{toctree}
:maxdepth: 1

shared_upstream
classical_profiling
deepprofiler
running_the_full_pipeline
```
