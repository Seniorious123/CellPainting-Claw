# Workflows

This section documents the main workflow structure exposed by CellPainting-Claw.

At the highest level, the repository organizes the workflow into one shared upstream stage and two downstream analysis branches. The shared stage is segmentation-oriented and produces the structured outputs used by both the classical profiling path and the DeepProfiler path.

## Workflow Map

The documentation in this section is organized in the same order as the workflow itself:

- **Shared Upstream Stage** explains how raw image data is converted into segmentation-driven workflow outputs.
- **Classical Profiling Branch** explains how CellProfiler-derived tables are turned into standard profile tables through `pycytominer`.
- **DeepProfiler Branch** explains how segmentation-guided single-cell crops are turned into learned feature vectors.
- **Orchestration** explains how the public workflow entrypoints connect these pieces together.

```{toctree}
:maxdepth: 1

shared_upstream
classical_profiling
deepprofiler
orchestration
```
