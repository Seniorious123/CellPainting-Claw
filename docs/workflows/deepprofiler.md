# DeepProfiler Branch

The DeepProfiler branch starts from segmentation-guided cell localization and continues toward learned single-cell feature representations.

## Workflow Logic

In this branch, segmentation outputs are used to identify individual cells and crop them from the source images. Those single-cell crops are then prepared for DeepProfiler, which extracts learned features for each cell.

This branch is used when the desired result is a deep feature representation or embedding rather than a classical profile table.

## Main Outputs

The main outputs of this branch are DeepProfiler artifacts such as:

- exported DeepProfiler input bundles
- materialized DeepProfiler project directories
- DeepProfiler feature collections
- per-cell feature vectors or embeddings

These outputs are distinct from the `pycytominer` tables produced by the classical profiling branch.

## Export Mode vs Full Mode

The orchestration layer currently supports two DeepProfiler-oriented workflow modes beyond `off`:

- `export`, which runs the segmentation branch in DeepProfiler export mode
- `full`, which continues through DeepProfiler project creation, feature extraction, and collection

This distinction is useful when you want to prepare DeepProfiler inputs first and postpone the full feature-extraction run.

## When To Enter This Branch Directly

Use the DeepProfiler branch when your main target is a learned per-cell representation rather than a classical profile table.

## Relevant Public Entry Points

This branch is exposed through commands such as:

- `cellpainting-claw run-deepprofiler-pipeline --config ...`
- `cellpainting-claw run-workflow --config ... --workflow segmentation-and-deepprofiler-full-stack`
- `cellpainting-claw run-end-to-end-pipeline --config ... --deepprofiler-mode full`

When using the top-level orchestration command, the DeepProfiler branch is enabled through the `deepprofiler_mode` setting.

## Related Pages

- [Shared Upstream Stage](shared_upstream.md)
- [Classical Profiling Branch](classical_profiling.md)
- [Running the Full Pipeline](running_the_full_pipeline.md)
