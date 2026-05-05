# `cyto-select-profile-features`

`cyto-select-profile-features` reduces normalized classical profiles to the retained feature set.

It is the step that keeps the final profile features judged useful enough for downstream interpretation.

## Purpose

Use this skill when you want:

- a smaller final classical profile table
- fewer redundant or weakly informative features
- the retained feature set for downstream summary and comparison

## Main Outcome

After this skill finishes, the normalized profile table has been reduced to a smaller feature set.

The metadata stay in place, but only the retained profile features move forward.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- a normalized profile table from [cyto-normalize-profiles](cyto_normalize_profiles.md), or an equivalent table provided by the user
- an optional output directory

## Outputs

- `feature_selected.parquet`
  The feature-selected classical profile table.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cytoselect-local-v1`
- turn timestamp: `2026-05-05 14:19 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I already have normalized Cell Painting profiles and want to reduce them to the retained feature set for downstream interpretation. Please use configs/project_config.demo.json, select the final profile features into demo/workspace/outputs/agent_demo_cyto_select, and then explain what was kept and why this feature-selection step matters biologically.
```

## Structured Trace

```text
user_input:
I already have normalized Cell Painting profiles and want to reduce them to the retained feature set for downstream interpretation. Please use configs/project_config.demo.json, select the final profile features into demo/workspace/outputs/agent_demo_cyto_select, and then explain what was kept and why this feature-selection step matters biologically.

planner_step_1:
intent:
Load the documented Cell Painting skill routing and run the stable feature-selection step.
tool_calls:
- read("~/.openclaw/lib/node_modules/openclaw/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- that packaged path did not exist on this host

planner_step_2:
intent:
Recover the workspace instructions and run the feature-selection surface with the demo config.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cyto-select-profile-features --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_select")
observed_result:
- skill_key = cyto-select-profile-features
- feature_selected_path = demo/workspace/outputs/agent_demo_cyto_select/pycytominer/feature_selected.parquet
- row_count = 2
- column_count = 12

planner_step_3:
intent:
Inspect the resulting table to see exactly which metadata columns and profile features were retained.
tool_calls:
- exec("python ... read feature_selected.parquet and print retained metadata columns and retained profile features")
observed_result:
- 6 metadata columns were retained
- 6 selected profile features were retained
- retained measurement features covered shape and intensity

final_answer_snapshot:
The final reduced profile table kept 6 metadata columns and 6 selected profile features.
```

## Observed Result

A real recorded run for this skill wrote:

- `pycytominer/feature_selected.parquet`
- `pipeline_skill_manifest.json`

The recorded output summary showed:

- `2` profile rows
- `12` total columns
- `6` metadata columns
- `6` selected profile features

The retained profile features were:

- `Cells_AreaShape_BoundingBoxMinimum_Y`
- `Cells_AreaShape_BoundingBoxMaximum_Y`
- `Cells_AreaShape_Center_Y`
- `Cells_Intensity_MeanIntensity_OrigDNA`
- `Cells_Intensity_MeanIntensity_OrigAGP`
- `Cells_Intensity_MeanIntensity_OrigRNA`

## Recorded Reply

```text
Done.

What was kept
- metadata columns for plate, well, object count, treatment, control type, and batch
- a reduced set of shape and intensity profile features

Why this matters biologically
- Cell Painting begins with a high-dimensional phenotype representation
- feature selection reduces redundancy and noise
- the retained set keeps more useful morphology and staining features for downstream comparison and interpretation
```

## Next Skills

- [cyto-summarize-classical-profiles](cyto_summarize_classical_profiles.md)
