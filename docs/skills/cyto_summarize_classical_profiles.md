# `cyto-summarize-classical-profiles`

`cyto-summarize-classical-profiles` turns classical profile tables into a readable result bundle.

It is the step that makes the final classical profiles easier to inspect by reporting standout features and a simple PCA view.

## Purpose

Use this skill when you want:

- a compact human-readable summary instead of only parquet tables
- a quick view of which features separate wells
- a simple low-dimensional view of the final profile differences

## Main Outcome

After this skill finishes, the final selected profile table is accompanied by summary files that tell you which wells differ and which features drive that difference.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- a final classical profile table, usually from [cyto-select-profile-features](cyto_select_profile_features.md)
- an optional output directory

## Outputs

- `profile_summary.json`
  A compact machine-readable summary of the classical profiling result.
- `well_metadata_summary.csv`
  A per-well summary of the retained metadata.
- `top_variable_features.csv`
  The features that varied the most across wells.
- `pca_coordinates.csv`
  PCA coordinates for each well.
- `pca_plot.png`
  A quick PCA figure.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cytosummary-local-v1`
- turn timestamp: `2026-05-05 14:21 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I already have the final selected Cell Painting profile table and want a quick biological summary of what separates the demo wells. Please use configs/project_config.demo.json, summarize the classical profiles into demo/workspace/outputs/agent_demo_cyto_summary, and then explain which features stand out and what the PCA view means biologically.
```

## Structured Trace

```text
user_input:
I already have the final selected Cell Painting profile table and want a quick biological summary of what separates the demo wells. Please use configs/project_config.demo.json, summarize the classical profiles into demo/workspace/outputs/agent_demo_cyto_summary, and then explain which features stand out and what the PCA view means biologically.

planner_step_1:
intent:
Load the documented Cell Painting skill routing and run the dedicated summary step.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cyto-summarize-classical-profiles --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_summary")
observed_result:
- the workspace skill file loaded successfully
- skill_key = cyto-summarize-classical-profiles
- summary outputs were written under demo/workspace/outputs/agent_demo_cyto_summary

planner_step_2:
intent:
Inspect the summary files to report the standout features and the PCA interpretation.
tool_calls:
- exec("python ... read profile_summary.json, top_variable_features.csv, pca_coordinates.csv, and well_metadata_summary.csv")
observed_result:
- the summary covered 2 wells and 6 selected features
- PC1 explained essentially all variance
- the top variable features included Y-direction shape features and DNA/AGP/RNA intensity features

final_answer_snapshot:
The final classical summary showed that the two demo wells separate along one dominant profile axis driven mainly by selected shape and intensity features.
```

## Observed Result

A real recorded run for this skill wrote:

- `profile_summary.json`
- `well_metadata_summary.csv`
- `top_variable_features.csv`
- `pca_coordinates.csv`
- `pca_plot.png`
- `pipeline_skill_manifest.json`

The recorded output summary showed:

- `2` wells
- `6` selected features
- top variable features:
  - `Cells_AreaShape_BoundingBoxMinimum_Y`
  - `Cells_AreaShape_BoundingBoxMaximum_Y`
  - `Cells_AreaShape_Center_Y`
  - `Cells_Intensity_MeanIntensity_OrigDNA`
  - `Cells_Intensity_MeanIntensity_OrigAGP`
  - `Cells_Intensity_MeanIntensity_OrigRNA`
- `PC1` explained essentially all variance

## Recorded Reply

```text
Done.

Main outputs
- `profile_summary.json`
- `well_metadata_summary.csv`
- `top_variable_features.csv`
- `pca_coordinates.csv`
- `pca_plot.png`

What stands out biologically
- the two demo wells differ along one dominant classical-profile axis
- the most interpretable contributors are DNA, AGP, and RNA mean-intensity features
- some Y-direction shape features also stand out, which suggests part of the contrast may reflect field layout or sampling effects

What the PCA means
- with only 2 wells, PCA reduces to one meaningful axis
- the plot shows a simple binary separation, not a rich phenotype landscape
```

## Next Skills

- [cyto-select-profile-features](cyto_select_profile_features.md)
