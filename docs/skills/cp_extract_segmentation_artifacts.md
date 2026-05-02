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
- cell-level results that later crop and feature-extraction steps can build on

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the segmentation input table written by [cp-prepare-segmentation-inputs](cp_prepare_segmentation_inputs.md), or default segmentation inputs resolved from the config
- the segmentation `.cppipe` template or override selected by the config
- the raw Cell Painting images and illumination-correction files from the project config
- an optional output directory

In the demo setup, the config selects the bundled segmentation template and derives a mask-export-ready `.cppipe` at runtime.

## Outputs

The main user-facing results are:

- nuclei segmentation
- whole-cell segmentation
- review-ready outline images
- cell-level segmentation tables for downstream analysis

## Agent Demo

This page is based on a real local OpenClaw run recorded against the completed segmentation result for one real Cell Painting image:

- turn timestamp: `2026-05-02 19:53 GMT+8`
- model: `vibe/gpt-5-mini`

### Request

```text
I already generated a segmentation result under demo/real_fov_workspace/outputs/real_fov_segmentation. Please check whether the nuclei and cell boundaries look biologically reasonable before I use it downstream.
```

## Structured Trace

```text
user_input:
I already generated a segmentation result under demo/real_fov_workspace/outputs/real_fov_segmentation. Please check whether the nuclei and cell boundaries look biologically reasonable before I use it downstream.

planner_step_1:
intent:
Try the default OpenClaw skill path first, then fall back to direct inspection if that bundled path is unavailable on this host.
tool_calls:
- read("~/.openclaw/lib/node_modules/openclaw/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- bundled OpenClaw skill path was missing on this host
- the agent switched to direct inspection of the user-named segmentation output folder

planner_step_2:
intent:
Inspect the named output folder and confirm which segmentation artifacts are already present.
tool_calls:
- exec("find demo/real_fov_workspace/outputs/real_fov_segmentation -maxdepth 3 | head -300")
observed_result:
- the named folder already contained:
  - outline PNGs
  - label TIFFs
  - `Image.csv`
  - `Cells.csv`
  - `Nuclei.csv`
  - `Cytoplasm.csv`
  - `segmentation_summary.json`
  - `pipeline_skill_manifest.json`

planner_step_3:
intent:
Read the segmentation summary and the main CellProfiler tables before judging the outline images.
tool_calls:
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/segmentation_summary.json")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/Image.csv")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/Nuclei.csv")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/Cells.csv")
observed_result:
- the segmentation summary loaded successfully
- the CSV headers were too large for direct read output
- the agent decided to compute a compact quantitative summary instead of dumping raw tables

planner_step_4:
intent:
Combine direct outline inspection with compact quantitative QC from the CellProfiler outputs.
tool_calls:
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/outlines/BR00117035_A01_s1--nuclei_outlines.png")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/outlines/BR00117035_A01_s1--cell_outlines.png")
- exec("python ... summarize Image.csv, Cells.csv, Nuclei.csv, Cytoplasm.csv")
observed_result:
- outline images loaded successfully
- compact quantitative QC showed:
  - `69` nuclei
  - `69` cells
  - `69` cytoplasm objects
  - nucleus median area `1157 px`
  - cell median area `4432 px`
- the agent judged the result likely usable downstream for one field, with normal caution around crowded regions

final_answer_snapshot:
The named segmentation result under `demo/real_fov_workspace/outputs/real_fov_segmentation` looked biologically reasonable overall and likely usable downstream as a first-pass single-field segmentation.
```

## Representative Figure

The OpenClaw trace above and the figure below refer to the same completed segmentation result for one real Cell Painting image.

![Representative segmentation output for one real Cell Painting image](../_static/agent_demo_segmentation/real_fov_segmentation_overview.png)

What this figure is meant to show:

- the selected image contains many distinct cells
- nuclei and whole-cell boundaries are different segmentation layers
- this step defines the objects that later crop and feature-extraction steps will reuse

Panels in this figure show:

- `A`
  The full pseudocolor image. The yellow box marks the region chosen for closer inspection.
- `B`
  The selected image crop, shown without segmentation overlays.
- `C`
  The same crop with nucleus boundaries overlaid. This corresponds to the nuclei segmentation written by the skill.
- `D`
  The same crop with whole-cell boundaries overlaid. This corresponds to the cell segmentation written by the skill.

Caption: Representative output from `cp-extract-segmentation-artifacts` on real Cell Painting image `BR00117035 / well A01 / site 1`.

### Observed Result

The agent inspected the exact output folder named in the request, checked both the exported outline images and the CellProfiler tables, and judged the segmentation likely usable downstream for this one field.

## Recorded Reply

```text
[[reply_to_current]] Overall: **likely usable downstream**, with **reasonable-looking nuclei and cell boundaries for a single field**, but best treated as **pass with a quick visual caveat** rather than perfect segmentation.

What I checked:
- output directory: `demo/real_fov_workspace/outputs/real_fov_segmentation`
- outline images:
  - `BR00117035_A01_s1--nuclei_outlines.png`
  - `BR00117035_A01_s1--cell_outlines.png`
- CellProfiler outputs:
  - `Image.csv`
  - `Nuclei.csv`
  - `Cells.csv`
  - `segmentation_summary.json`

Quick quantitative QC:
- **69 nuclei**
- **69 cells**
- **69 cytoplasm objects**
- nucleus median area: **1157 px**
- cell median area: **4432 px**

What looks good:
- nuclei outlines appear broadly consistent in size and spacing
- cell boundaries expand around nuclei in a generally plausible way
- the 1:1:1 nucleus/cell/cytoplasm mapping is a good sign for downstream profiling
- object counts are reasonable for one 1080×1080 field

What still needs caution:
- crowded touching cells are the most likely place for mistakes
- some boundaries look watershed-like, which is common but worth spot-checking
- this is only one field, so it is enough for a local QC pass, not a full-batch validation

Practical recommendation:
- **okay to proceed for exploratory downstream use**
- add one stronger QC step later by overlaying masks on the raw DNA and cell-body channels
```

## Next Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
