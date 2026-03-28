# Classical Profiling Branch

The classical profiling branch starts from CellProfiler-derived tables and continues toward standard Cell Painting profile outputs.

## Workflow Logic

In this branch, CellProfiler-derived tables are exported into a standardized single-cell table. That single-cell table is then processed by `pycytominer`.

This branch is the path used when the desired result is a standard profile table for downstream analysis rather than a set of per-cell image embeddings.

## Main Outputs

The main outputs of this branch are feature tables, including:

- aggregated profiles
- annotated profiles
- normalized profiles
- feature-selected profiles

These outputs are table-based analysis artifacts. They are intended for classical downstream analysis rather than for image-centric representation learning.

## When To Use This Branch

Use the classical profiling branch when your main target is a standard Cell Painting profile workflow, for example when you need:

- a well-level or aggregated feature table
- metadata-annotated profiles
- normalized features for comparison across conditions
- a feature-selected table for downstream modeling or evaluation

## Relevant Entry Points

This branch is exposed through commands such as:

- `cellpainting-claw run-profiling-suite --config ...`
- `cellpainting-claw run-workflow --config ... --workflow post-cellprofiler-native-profiling-with-native-eval`
- `cellpainting-claw run-end-to-end-pipeline --config ...`

The direct profiling suite is useful when you want the classical profiling path without running the entire multi-stage workflow.
