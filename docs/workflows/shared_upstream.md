# Shared Upstream Stage

The shared upstream stage begins with raw Cell Painting image data and passes through segmentation-oriented processing. In the current repository, this stage is centered on CellProfiler and on the native segmentation helpers that wrap the validated backend assets.

## Inputs

The shared stage expects raw microscopy image data together with the metadata required to locate and organize those images. Depending on the workflow entrypoint, this data can come from a local backend workspace or from a planned download through the data-access layer.

## Main Outputs

This stage produces the structured outputs that support both downstream branches, including:

- image-level and object-level measurement tables
- segmentation labels, masks, and outlines
- single-cell localization information
- optional single-cell image crops
- optional preview images

These outputs are the point where raw image data becomes reusable workflow data.

## Relevant Entry Points

The shared stage can appear through several public commands, depending on how much of the workflow you want to run:

- `cellpainting-claw run-segmentation-suite --config ...`
- `cellpainting-claw run-workflow --config ... --workflow post-cellprofiler-native-segmentation-suite`
- `cellpainting-claw run-end-to-end-pipeline --config ...`

The top-level orchestration entrypoint is the main public interface for most users.
