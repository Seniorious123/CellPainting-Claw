# Workflows

This section documents the main workflow structure exposed by CellPainting-Claw.

At the highest level, the repository organizes the workflow into one shared upstream stage and two downstream analysis branches. The shared stage is segmentation-oriented and produces the structured outputs used by both the classical profiling path and the DeepProfiler path.

```{toctree}
:maxdepth: 1

shared_upstream
classical_profiling
deepprofiler
orchestration
```
