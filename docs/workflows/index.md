# Workflows

This section documents the workflow logic exposed by CellPainting-Claw.

The project is organized around one shared upstream stage and two downstream branches:

- a shared segmentation-oriented upstream stage
- a classical profiling branch built around `pycytominer`
- a DeepProfiler branch built around segmentation-guided single-cell crops

## Workflow at a Glance

The workflow is easiest to understand in this order:

1. raw Cell Painting images enter the shared upstream stage
2. CellProfiler-driven segmentation produces masks, outlines, labels, measurements, and localization outputs
3. those shared outputs feed one of two downstream branches
4. the classical branch turns measurement tables into profile tables through `pycytominer`
5. the DeepProfiler branch turns single-cell crops into learned feature vectors

This means that segmentation is not a side product. It is the backbone that connects the raw images to both downstream analysis paths.

## What Each Workflow Page Covers

- **Shared Upstream Stage** explains how raw microscopy inputs become segmentation-derived workflow outputs.
- **Classical Profiling Branch** explains how CellProfiler-derived tables are standardized and passed into `pycytominer`.
- **DeepProfiler Branch** explains how segmentation-guided crops are exported and prepared for deep feature extraction.
- **Running the Full Pipeline** explains how to run the full public workflow from configuration inspection to final output directories.

## Output Logic

The outputs of the workflow fall into three groups:

- segmentation outputs such as masks, outlines, object tables, and crop-ready localization data
- classical profiling outputs such as aggregated, annotated, normalized, and feature-selected profile tables
- DeepProfiler outputs such as per-cell embeddings and collected feature tables

That separation is important for interpreting the repository correctly:

- `pycytominer` produces profile tables
- the segmentation branch produces masks and crop-related artifacts
- DeepProfiler consumes segmentation-guided image crops rather than replacing segmentation itself

## How To Read This Section

If you are learning the project for the first time, read these pages in order.

If you already understand the branches and only need the execution recipe, jump directly to **Running the Full Pipeline**.

```{toctree}
:maxdepth: 1

shared_upstream
classical_profiling
deepprofiler
running_the_full_pipeline
```
