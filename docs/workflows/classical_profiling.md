# Classical Profiling Branch

The classical profiling branch starts from CellProfiler-derived tables and continues toward standard Cell Painting profile outputs.

## Workflow Logic

In this branch, CellProfiler-derived tables are exported into a standardized single-cell table. That single-cell table is then processed by `pycytominer`.

This branch is the path used when the desired output is a standard profiling table for downstream analysis rather than per-cell image embeddings.

## Main Outputs

The main outputs of this branch are feature tables, including:

- aggregated profiles
- annotated profiles
- normalized profiles
- feature-selected profiles

These outputs are table-based analysis artifacts, not image artifacts.

## Relevant Entry Points

This branch is exposed through commands such as:

- `cellpainting-claw run-profiling-suite --config ...`
- `cellpainting-claw run-workflow --config ... --workflow post-cellprofiler-native-profiling-with-native-eval`
- `cellpainting-claw run-end-to-end-pipeline --config ...`

The direct profiling suite is useful when you want the classical profiling path without running the entire multi-stage workflow.
