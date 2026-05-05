# `cyto-normalize-profiles`

`cyto-normalize-profiles` normalizes an annotated classical profile table.

It is the step that puts different profile features onto a more comparable scale before feature selection and downstream comparison.

## Purpose

Use this skill when you want:

- wells compared on the same feature scale
- raw profile magnitudes converted into relative deviations
- the standard normalized input for feature selection

## Main Outcome

After this skill finishes, the annotated table still has the same wells and metadata.

What changes is the feature matrix: varying profile features are centered and scaled so downstream comparisons are more interpretable.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- an annotated profile table from [cyto-annotate-profiles](cyto_annotate_profiles.md), or an equivalent table provided by the user
- an optional output directory

## Outputs

- `normalized.parquet`
  The normalized classical profile table.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cytonormalize-local-v1`
- turn timestamp: `2026-05-05 14:08 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I already have the annotated Cell Painting profile table and want to make the wells comparable before downstream interpretation. Please use configs/project_config.demo.json, normalize the annotated profiles into demo/workspace/outputs/agent_demo_cyto_normalize, and then explain what normalization changed and why this step matters biologically.
```

## Structured Trace

```text
user_input:
I already have the annotated Cell Painting profile table and want to make the wells comparable before downstream interpretation. Please use configs/project_config.demo.json, normalize the annotated profiles into demo/workspace/outputs/agent_demo_cyto_normalize, and then explain what normalization changed and why this step matters biologically.

planner_step_1:
intent:
Load the documented Cell Painting skill routing and run the stable normalization step.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cyto-normalize-profiles --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_normalize")
observed_result:
- the workspace skill file loaded successfully
- skill_key = cyto-normalize-profiles
- normalized_path = demo/workspace/outputs/agent_demo_cyto_normalize/pycytominer/normalized.parquet
- row_count = 2
- column_count = 17

planner_step_2:
intent:
Inspect how selected annotated features changed after normalization.
tool_calls:
- exec("python ... compare annotated.parquet and normalized.parquet for representative DNA, AGP, RNA, and shape features")
observed_result:
- varying features changed from raw values to symmetric normalized values
- non-varying features became 0.0 for both wells
- metadata columns were preserved

final_answer_snapshot:
Normalization kept the same wells and metadata but converted the varying feature columns into comparable scaled values.
```

## Observed Result

A real recorded run for this skill wrote:

- `pycytominer/normalized.parquet`
- `pipeline_skill_manifest.json`

The recorded output summary showed:

- `2` well-level rows
- `17` columns
- `6` metadata columns
- `11` normalized profile features

Representative changes included:

- `Cells_Intensity_MeanIntensity_OrigDNA`
  from `[1122.5, 1222.5]` to `[-0.6745, 0.6745]`
- `Cells_Intensity_MeanIntensity_OrigAGP`
  from `[1010.0, 1090.0]` to `[-0.6745, 0.6745]`
- `Cells_Intensity_MeanIntensity_OrigRNA`
  from `[947.0, 1017.0]` to `[-0.6745, 0.6745]`

## Recorded Reply

```text
Done — I normalized the annotated profiles with the demo config.

Main output
- `demo/workspace/outputs/agent_demo_cyto_normalize/pycytominer/normalized.parquet`

What normalization changed
- the same wells and metadata were preserved
- varying features were centered and scaled
- features with no between-well variation became `0.0`

Why this matters biologically
- raw Cell Painting features live on different numeric scales
- normalization makes wells more directly comparable
- it reduces technical bias before feature selection, similarity analysis, clustering, and downstream interpretation
```

## Next Skills

- [cyto-select-profile-features](cyto_select_profile_features.md)
