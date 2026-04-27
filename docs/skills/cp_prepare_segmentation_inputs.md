# `cp-prepare-segmentation-inputs`

`cp-prepare-segmentation-inputs` writes the `load_data_for_segmentation.csv` file that the segmentation pipeline will read.

This skill does **not** run CellProfiler yet. Its job is to assemble the field list, channel file paths, and illumination references needed by the segmentation step.

## Main Result

The main result is one segmentation input table:

- `load_data_for_segmentation.csv`

Each row in that table represents one field that will be sent into segmentation. In practice, this is the point where the project turns “which wells and sites should I segment?” into a concrete run description.

## Main Input

This skill reads:

- a project config
- image metadata resolved from the configured demo or user workspace
- optional plate, well, or site filters
- an optional output directory

## Config Fields Used

For this skill, the config mainly provides:

- the backend roots where the raw Cell Painting images and illumination assets live
- the workspace and default output roots
- any dataset-specific defaults already encoded in the project setup

The important distinction is:

- the config tells the skill **where to find the inputs**
- this skill writes the table that tells the next segmentation step **which fields to run**

## Files Written

Files written by this skill:

- `load_data_for_segmentation.csv`: one row per segmentation field, including channel filenames, channel paths, and illumination references
- `pipeline_skill_manifest.json`: a machine-readable record of the skill run

## Recorded Demo Result

In the repository demo, this step prepares **two fields**:

- plate `BR00000001`, well `A01`, site `1`
- plate `BR00000001`, well `A02`, site `1`

That recorded demo table is the direct input for the next skill, [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md).

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cp-prepare-segmentation-inputs \
  --output-dir outputs/segmentation_inputs
```

## Agent Use

Example request:

```text
Prepare the segmentation inputs for configs/project_config.demo.json and write the segmentation load-data table under outputs/segmentation_inputs.
```

## Next Skills

- [cp-extract-segmentation-artifacts](cp_extract_segmentation_artifacts.md)
- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
