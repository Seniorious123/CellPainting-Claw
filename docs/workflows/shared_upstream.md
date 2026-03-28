# Shared Upstream Stage

The shared upstream stage begins with raw Cell Painting image data and passes through segmentation-oriented processing. In the current repository, this stage is centered on CellProfiler and on the native segmentation helpers that wrap the validated backend assets.

## What This Stage Does

This is the common stage that turns raw microscopy data into structured workflow outputs. It is shared by both downstream branches, which means it is the point where the workflow stops being only image data and starts becoming reusable analysis data.

## Inputs

The shared stage expects raw image data together with the metadata required to locate and organize those images. Depending on the workflow entrypoint, this data can come from:

- a local backend workspace that already contains the required image set
- a planned or executed data-access step that populates the workspace before the workflow continues

## Main Outputs

This stage produces the structured outputs that support both downstream branches, including:

- image-level and object-level measurement tables
- segmentation labels, masks, and outlines
- single-cell localization information
- optional single-cell image crops
- optional preview images

Some of these outputs are table-based, while others are image-based. Together they form the shared intermediate layer used by the rest of the workflow.

## When To Use This Stage Directly

Enter this stage directly when you want to focus on segmentation artifacts themselves, for example when you need:

- masks, labels, or outlines
- segmentation summaries
- single-cell crops
- preview images for visual inspection

## Relevant Entry Points

The shared stage can appear through several public commands, depending on how much of the workflow you want to run:

- `cellpainting-claw run-segmentation-suite --config ...`
- `cellpainting-claw run-workflow --config ... --workflow post-cellprofiler-native-segmentation-suite`
- `cellpainting-claw run-end-to-end-pipeline --config ...`

For most users, the top-level orchestration entrypoint remains the preferred default. Use the narrower segmentation commands when you specifically want segmentation outputs without running the full workflow.
