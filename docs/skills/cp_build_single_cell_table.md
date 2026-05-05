# `cp-build-single-cell-table`

`cp-build-single-cell-table` turns CellProfiler measurement tables into one single-cell table.

It is the step that takes separate CellProfiler outputs and rewrites them into one table where each row represents one cell.

## Purpose

Use this skill when you want:

- one row per cell instead of separate CellProfiler tables
- a single table that downstream classical profiling steps can use directly
- the bridge between CellProfiler outputs and pycytominer-style profiling

## Main Outcome

After this skill finishes, the measurement outputs are no longer split across separate tables.

Instead, you have one merged single-cell table that downstream classical profiling steps can read directly.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the standard CellProfiler measurement tables
- an optional output directory

In the recorded demo run below, the merge used the `Cells` object table.

## Outputs

- `single_cell.csv.gz`
  One compressed table where each row is one cell and each column is a measurement or identifier.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cpsinglecell-local-v1`
- turn timestamp: `2026-05-05 13:48 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I already have the standard Cell Painting measurement tables and want the per-cell table that downstream profiling tools use. Please use configs/project_config.demo.json, build that single-cell table under demo/workspace/outputs/agent_demo_single_cell, and then explain what the resulting table contains and why it is the right input for the next profiling steps.
```

## Structured Trace

```text
user_input:
I already have the standard Cell Painting measurement tables and want the per-cell table that downstream profiling tools use. Please use configs/project_config.demo.json, build that single-cell table under demo/workspace/outputs/agent_demo_single_cell, and then explain what the resulting table contains and why it is the right input for the next profiling steps.

planner_step_1:
intent:
Load the documented Cell Painting skill routing before choosing the single-cell table step.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- the workspace skill file loaded successfully
- the routing guidance identified `cp-build-single-cell-table` as the public step that merges CellProfiler outputs into one per-cell table

planner_step_2:
intent:
Confirm the current skill catalog and inspect the documented description for the selected skill.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills list && echo '---DESCRIBE---' && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills describe --skill cp-build-single-cell-table")
- process.poll("quiet-atlas")
observed_result:
- the public skill catalog listed `cp-build-single-cell-table`
- the skill description confirmed that this step merges CellProfiler image and object tables into a single-cell measurements table

planner_step_3:
intent:
Run the single-cell table step and inspect the output summary.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cp-build-single-cell-table --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_single_cell")
- process.poll("brisk-bison")
observed_result:
- skill_key = cp-build-single-cell-table
- single_cell_path = demo/workspace/outputs/agent_demo_single_cell/single_cell.csv.gz
- row_count = 4
- column_count = 16
- object_table = Cells

planner_step_4:
intent:
Read the resulting single-cell table so its contents and downstream use can be explained concretely.
tool_calls:
- exec("python ... read single_cell.csv.gz, print shape, columns, and preview rows")
- process.poll("oceanic-fjord")
observed_result:
- shape = 4 rows x 16 columns
- the table contained metadata columns, object-link columns, morphology features, and intensity features
- each row represented one segmented cell

final_answer_snapshot:
The resulting table is one row per cell and is the correct handoff table for downstream classical profiling steps.
```

## Observed Result

A real recorded run for this skill wrote:

- `single_cell.csv.gz`
- `pipeline_skill_manifest.json`

The recorded output summary showed:

- `4` single-cell rows
- `16` columns
- object table used for the merge: `Cells`

The table contained:

- metadata columns such as plate, well, and site
- object-link columns that preserve CellProfiler identity
- cell morphology features
- channel-intensity features

## Recorded Reply

```text
Built the single-cell table successfully.

What I ran
- Skill: `cp-build-single-cell-table`
- Config: `/root/pipeline/CellPainting-Claw/configs/project_config.demo.json`
- Output directory requested: `/root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_single_cell`

Main outputs
- Single-cell table: `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_single_cell/single_cell.csv.gz`
- Manifest: `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_single_cell/pipeline_skill_manifest.json`

What the resulting table contains
- one row per segmented cell
- metadata columns saying where that cell came from
- object/link columns preserving CellProfiler identity
- feature columns for size, position, and channel intensities

Why this is the right input for the next profiling steps
- downstream classical profiling tools expect one unified per-cell matrix
- `cyto-aggregate-profiles` can aggregate these rows into well-level profiles
- later steps can annotate, normalize, and select features from this merged table
```

## Next Skills

- [cyto-aggregate-profiles](cyto_aggregate_profiles.md)
