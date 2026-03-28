# Orchestration

CellPainting-Claw provides several ways to run workflows, but one command is intended to be the main public orchestration entrypoint:

- `cellpainting-claw run-end-to-end-pipeline --config ...`

## Top-Level Orchestration

The top-level orchestration layer is responsible for coordinating data access, profiling, segmentation, validation, and the optional DeepProfiler branch. This makes it the recommended first choice for users who want a stable high-level interface.

The orchestration layer currently supports DeepProfiler modes `off`, `export`, and `full`.

## Lower-Level Workflow Entry Points

For more explicit control, the repository also exposes narrower workflow commands, including:

- `run-profiling-suite`
- `run-segmentation-suite`
- `run-workflow`
- `run-deepprofiler-pipeline`

These commands are useful when you want to enter one branch directly instead of using the top-level orchestration interface.

## Practical Guidance

For most new users, start with the top-level orchestration command. Move to branch-specific commands only when you need tighter control over a specific stage of the workflow.
