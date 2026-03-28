# DeepProfiler Branch

The DeepProfiler branch starts from segmentation-guided cell localization and continues toward learned single-cell feature representations.

## Workflow Logic

In this branch, segmentation outputs are used to identify individual cells and crop them from the source images. Those single-cell crops are then prepared for DeepProfiler, which extracts learned features for each cell.

This branch is used when the desired output is a deep feature representation or embedding rather than a classical profile table.

## Main Outputs

The main outputs of this branch are DeepProfiler artifacts such as:

- exported DeepProfiler input bundles
- materialized DeepProfiler project directories
- DeepProfiler feature collections
- per-cell feature vectors or embeddings

These outputs are distinct from the `pycytominer` tables produced by the classical profiling branch.

## Relevant Entry Points

This branch is exposed through commands such as:

- `cellpainting-claw run-deepprofiler-pipeline --config ...`
- `cellpainting-claw run-workflow --config ... --workflow segmentation-and-deepprofiler-full-stack`
- `cellpainting-claw run-end-to-end-pipeline --config ... --deepprofiler-mode full`

When using the top-level orchestration command, the DeepProfiler branch is enabled through the `deepprofiler_mode` setting.
