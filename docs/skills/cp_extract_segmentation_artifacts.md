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

This skill produces the reusable segmentation outputs for one image:

- segmented nuclei
- segmented whole cells
- review-ready outline images
- cell-level results for downstream crop and feature-extraction steps

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

- turn timestamp: `2026-05-02 20:42 GMT+8`
- model: `vibe/gpt-5-mini`

### Request

```text
I already generated a segmentation result under demo/real_fov_workspace/outputs/real_fov_segmentation. Please inspect the outline PNGs and CellProfiler tables there and tell me whether the nuclei and cell boundaries look biologically reasonable.
```

## Structured Trace

```text
user_input:
I already generated a segmentation result under demo/real_fov_workspace/outputs/real_fov_segmentation. Please inspect the outline PNGs and CellProfiler tables there and tell me whether the nuclei and cell boundaries look biologically reasonable.

planner_step_1:
intent:
Load the documented Cell Painting routing guidance before inspecting the named outputs.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- the workspace skill file loaded successfully
- routing guidance confirmed that masks, labels, outlines, and segmentation tables belong to the segmentation artifact skill

planner_step_2:
intent:
Inspect the named output folder and confirm that the requested outline PNGs and CellProfiler tables are present.
tool_calls:
- exec("find .../real_fov_segmentation -maxdepth 3 \\( -iname '*.png' -o -iname '*.csv' -o -iname '*.txt' -o -iname '*.sqlite' -o -iname '*.db' \\) | sort")
- exec("python ... walk the output tree and summarize key files")
observed_result:
- the named folder already contained:
  - outline PNGs
  - `Image.csv`
  - `Cells.csv`
  - `Nuclei.csv`
  - `Cytoplasm.csv`
  - `load_data_for_segmentation.csv`
  - label TIFFs
  - the usual segmentation summary files

planner_step_3:
intent:
Inspect the CellProfiler tables for object counts and parent-child consistency.
tool_calls:
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/Image.csv")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/Nuclei.csv")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/Cells.csv")
observed_result:
- the main tables reported `69` nuclei, `69` cells, and `69` cytoplasm objects
- `Children_Nuclei_Count = 1` for all cells
- no obvious parent-child mismatch appeared in the exported tables

planner_step_4:
intent:
Combine direct outline inspection with compact morphology summaries from the exported segmentation tables.
tool_calls:
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/outlines/BR00117035_A01_s1--nuclei_outlines.png")
- read("demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/outlines/BR00117035_A01_s1--cell_outlines.png")
- exec("python ... inspect outline image dimensions")
- exec("python ... summarize nuclei and cell morphology metrics from the tables")
observed_result:
- outline images loaded successfully
- compact quantitative QC showed:
  - `69` nuclei
  - `69` cells
  - `69` cytoplasm objects
  - nucleus median area `1157 px`
  - cell median area `4432 px`
  - nucleus median solidity `0.974`
  - cell median solidity `0.794`
- the agent judged the result biologically reasonable overall for this field, with expected caveats for crowded regions and outline-only review

final_answer_snapshot:
The named segmentation result looked biologically reasonable overall for this field and passed quick-review QC for downstream single-cell profiling.
```

## Representative Figure

The OpenClaw trace above and the figure below refer to the same completed segmentation result for one real Cell Painting image.

![Representative segmentation output for one real Cell Painting image](../_static/agent_demo_segmentation/real_fov_segmentation_overview.png)

What this figure is meant to show:

- many distinct cells in one image
- nuclei and whole-cell boundaries as separate segmentation layers
- the segmentation objects reused by downstream steps

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

The agent inspected the exact outline PNGs and CellProfiler tables named in the request and judged the segmentation biologically reasonable overall for this field.

## Recorded Reply

```text
[[reply_to_current]] I inspected the two outline PNGs and the CellProfiler object tables under:

- `demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/outlines/`
- `demo/real_fov_workspace/outputs/real_fov_segmentation/cellprofiler_masks/{Nuclei.csv,Cells.csv,Cytoplasm.csv,Image.csv}`

Short answer: **yes, the segmentation looks broadly biologically reasonable for this field**, with a couple of normal caveats.

What looks good:
- **69 nuclei**
- **69 cells**
- **69 cytoplasm objects**
- each cell has exactly one nucleus
- nucleus median area ≈ **1157 px**
- nucleus median solidity ≈ **0.974**
- nucleus median form factor ≈ **0.875**
- cell median area ≈ **4432 px**
- cell median solidity ≈ **0.794**
- cell median form factor ≈ **0.402**

What I noticed visually:
- nuclear outlines track discrete compact objects rather than spilling across neighbors
- cell outlines are more irregular than nuclei, which is expected for propagation-based whole-cell segmentation
- there is no sign of catastrophic failure such as severe nucleus loss, giant merged masks, or debris-level fragmentation

Mild caveats:
- some cell boundaries are irregular in crowded regions
- these PNGs are outline-only exports, not overlays on the original DNA or cell-body channels

Practical recommendation:
- **pass for segmentation QC at a quick-review level**
- suitable for downstream single-cell profiling unless you need very high-fidelity membrane boundaries
```

## Next Skills

- [cp-generate-segmentation-previews](cp_generate_segmentation_previews.md)
- [crop-export-single-cell-crops](crop_export_single_cell_crops.md)
- [dp-export-deep-feature-inputs](dp_export_deep_feature_inputs.md)
