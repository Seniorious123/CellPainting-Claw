# `cp-extract-segmentation-artifacts`

`cp-extract-segmentation-artifacts` is the segmentation execution step.

It takes the prepared field list, resolves the segmentation `.cppipe`, runs the CellProfiler-based segmentation backend, and writes the artifact bundle that downstream tools can reuse.

## Purpose

Use this skill when you want:

- segmented nuclei
- segmented whole cells
- quick review images to inspect whether the boundaries look reasonable
- reusable object definitions for later crop and feature-extraction steps

## Main Outcome

After this skill finishes, the image is no longer just raw pixels. The run has identified nuclei and whole cells as distinct objects that downstream steps can reuse.

In practice, this is the step that gives you:

- segmented nuclei
- segmented whole cells
- quick review images to check whether the boundaries look reasonable
- object-level results that later crop and feature-extraction steps can build on

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the segmentation input table written by [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or default segmentation inputs resolved from the config
- the segmentation `.cppipe` template or override selected by the config
- the configured raw-image and illumination assets
- an optional output directory

In the demo setup, the config selects the bundled segmentation template and derives a mask-export-ready `.cppipe` at runtime.

## Outputs

The main user-facing results are:

- nuclei segmentation
- whole-cell segmentation
- review-ready outline images
- object-level segmentation tables for downstream analysis

## Agent Demo

This page is based on a real local OpenClaw run recorded against the completed segmentation result for one real Cell Painting image:

- run label: `real-fov-segmentation-v2`
- turn timestamp: `2026-05-02 13:29 GMT+8`
- model: `vibe/gpt-5-mini`

### Request

```text
Using configs/project_config.real_fov_demo.json and the completed workflow root
demo/real_fov_workspace/outputs/real_fov_segmentation, summarize the segmentation
result I would review afterward. Tell me which skill produced these outputs, what
the main segmentation result is, which visual result is available for review, and
what that visual result means biologically. Do not rerun a new workflow root if
the completed outputs already exist; inspect the existing completed result.
```

## Structured Trace

```text
user_input:
Using configs/project_config.real_fov_demo.json and the completed workflow root
demo/real_fov_workspace/outputs/real_fov_segmentation, summarize the segmentation
result I would review afterward. Tell me which skill produced these outputs, what
the main segmentation result is, which visual result is available for review, and
what that visual result means biologically. Do not rerun a new workflow root if
the completed outputs already exist; inspect the existing completed result.

planner_step_1:
intent:
Inspect the completed segmentation output tree for the real Cell Painting image before deciding whether a
new segmentation run is necessary.
tool_calls:
- exec("find demo/real_fov_workspace/outputs/real_fov_segmentation -maxdepth 3 -type f | sort")
observed_result:
- completed segmentation output tree already contained:
  - `Image.csv`
  - `Cells.csv`
  - `Nuclei.csv`
  - cell and nuclei label TIFFs
  - cell and nuclei outline PNGs
  - `segmentation_summary.json`

planner_step_2:
intent:
Confirm which skill originally produced this completed output root.
tool_calls:
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/pipeline_skill_manifest.json")
observed_result:
- manifest confirmed:
  - skill key = `cp-extract-segmentation-artifacts`
  - category = `segmentation`
  - returncode = `0`

planner_step_3:
intent:
Summarize the completed segmentation result quantitatively from the existing object tables.
tool_calls:
- exec("python ... read Image.csv, Cells.csv, Nuclei.csv, Cytoplasm.csv and report row and object counts")
observed_result:
- `Image.csv` rows = `1`
- `Cells.csv` objects = `69`
- `Nuclei.csv` objects = `69`
- `Cytoplasm.csv` objects = `69`

planner_step_4:
intent:
Explain which visual segmentation artifacts are available for review.
tool_calls:
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/segmentation_summary.json")
observed_result:
- review-ready visual artifacts available:
  - `cell_outlines.png`
  - `nuclei_outlines.png`
  - raw label TIFFs for cells and nuclei

final_answer_snapshot:
The completed result for the real Cell Painting image came from `cp-extract-segmentation-artifacts` and
produced a successful single-field segmentation with 69 matched nucleus/cell/cytoplasm
objects plus review-ready cell and nuclei outline images.
```

## Representative Figure

The OpenClaw trace above and the figure below now refer to the same completed segmentation result for one real Cell Painting image.

![Representative segmentation output for one real Cell Painting image](../_static/agent_demo_segmentation/real_fov_segmentation_overview.png)

What this figure is meant to show:

- the selected image contains many distinct cells
- nuclei and whole-cell boundaries are different segmentation layers
- this step defines the objects that later crop and feature-extraction steps will reuse

Panels in this figure show:

- `A`
  The full pseudocolor image. The yellow box marks the region chosen for closer inspection.
- `B`
  The selected crop from that field, shown without segmentation overlays.
- `C`
  The same crop with nucleus boundaries overlaid. This corresponds to the nuclei segmentation written by the skill.
- `D`
  The same crop with whole-cell boundaries overlaid. This corresponds to the cell segmentation written by the skill.

Caption: Representative output from `cp-extract-segmentation-artifacts` on public image `BR00117035 / A01 / site 1`.

### Observed Result

The agent confirmed that the completed output already contained the review-ready segmentation result for one real Cell Painting image.

## Recorded Reply

```text
[[reply_to_current]] I inspected the existing completed result under:

- `demo/real_fov_workspace/outputs/real_fov_segmentation`

and did **not** rerun the workflow.

The outputs were produced by the stable segmentation skill:

- **`cp-extract-segmentation-artifacts`**

This completed run produced a successful single-field segmentation result for:

- **1 row**
- **1 plate**
- **1 well**
- **1 site**

The object tables show:

- **69 cells**
- **69 nuclei**
- **69 cytoplasm objects**

The main visual review outputs are:

- cell outlines
- nuclei outlines

Biologically, these review images tell you whether nucleus-centered cell boundaries are being placed in a plausible way and whether neighboring cells are being separated cleanly enough for downstream single-cell analysis.
```

## Next Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
