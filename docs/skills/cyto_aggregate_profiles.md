# `cyto-aggregate-profiles`

`cyto-aggregate-profiles` turns a single-cell table into the first well-level classical profile table.

It is the step that compresses many measured cells from the same well into one summarized profile row.

## Purpose

Use this skill when you want:

- one profile row per well instead of one row per cell
- the first pycytominer-style table for classical Cell Painting analysis
- a more stable biological summary before annotation, normalization, and feature selection

## Main Outcome

After this skill finishes, the data are no longer organized cell by cell.

Instead, you have a well-level profile table that summarizes the measured cells in each well.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- a single-cell table from [cp-build-single-cell-table](cp_build_single_cell_table.md), or an equivalent table provided by the user
- an optional output directory

## Outputs

- `aggregated.parquet`
  The aggregated classical profile table. Each row is one well-level profile.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cytoaggregate-local-v1`
- turn timestamp: `2026-05-05 14:04 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I already have the single-cell Cell Painting table and want the first classical profile table that summarizes cells at the well level. Please use configs/project_config.demo.json, aggregate the single-cell table into demo/workspace/outputs/agent_demo_cyto_aggregate, and then explain what the aggregated profile contains and why this step is useful biologically.
```

## Structured Trace

```text
user_input:
I already have the single-cell Cell Painting table and want the first classical profile table that summarizes cells at the well level. Please use configs/project_config.demo.json, aggregate the single-cell table into demo/workspace/outputs/agent_demo_cyto_aggregate, and then explain what the aggregated profile contains and why this step is useful biologically.

planner_step_1:
intent:
Load the documented Cell Painting skill routing before choosing the well-level aggregation step.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- the workspace skill file loaded successfully
- the routing guidance identified `cyto-aggregate-profiles` as the public step for aggregating single-cell measurements into classical profiles

planner_step_2:
intent:
Confirm the documented skill description and then run the aggregation step under the requested demo output directory.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills describe --skill cyto-aggregate-profiles && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cyto-aggregate-profiles --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_aggregate")
- process.poll("fresh-claw")
observed_result:
- the skill description confirmed that this step aggregates single-cell measurements into classical profiles
- skill_key = cyto-aggregate-profiles
- aggregated_path = demo/workspace/outputs/agent_demo_cyto_aggregate/pycytominer/aggregated.parquet
- row_count = 2
- column_count = 14

planner_step_3:
intent:
Read the aggregated table so the result can be explained concretely.
tool_calls:
- exec("python ... read aggregated.parquet, print shape, columns, and preview rows")
observed_result:
- shape = 2 rows x 14 columns
- the table contained plate and well metadata
- each row summarized one well
- the feature columns contained aggregated morphology and intensity measurements

final_answer_snapshot:
The result is a well-level classical profile table with one summarized row per well.
```

## Observed Result

A real recorded run for this skill wrote:

- `pycytominer/aggregated.parquet`
- `pipeline_skill_manifest.json`

The recorded output summary showed:

- `2` well-level rows
- `14` columns
- wells `A01` and `A02`

The table contained:

- plate and well identifiers
- cell counts per well
- aggregated cell morphology measurements
- aggregated channel-intensity measurements

## Recorded Reply

```text
Done.

What I ran
- Skill: `cyto-aggregate-profiles`
- Config: `/root/pipeline/CellPainting-Claw/configs/project_config.demo.json`
- Output dir requested: `/root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_aggregate`
- Command used:
  cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cyto-aggregate-profiles --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_aggregate

What was produced
- Entrypoint ran: `cyto-aggregate-profiles`
- Main output: `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_aggregate/pycytominer/aggregated.parquet`
- Manifest: `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_aggregate/pipeline_skill_manifest.json`
- Table shape: `2 rows × 14 columns`

Artifact type
- This step produced a pycytominer-style well-level classical profile table
- It is a well-level summary, not a single-cell table and not segmentation masks

What the aggregated profile contains
- one row per well
- metadata columns such as plate and well identity
- aggregated feature values computed from the single-cell measurements in that well

Why this step is useful biologically
- it turns many cell-level measurements into one per-well morphological fingerprint
- it reduces single-cell noise before comparing treatments or conditions
- it provides the standard input for annotation, normalization, and feature-selection steps
```

## Next Skills

- [cyto-annotate-profiles](cyto_annotate_profiles.md)
- [cyto-normalize-profiles](cyto_normalize_profiles.md)
