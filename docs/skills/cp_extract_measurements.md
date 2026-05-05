# `cp-extract-measurements`

`cp-extract-measurements` is the CellProfiler measurement step for classical Cell Painting profiling.

It produces the standard measurement tables that later profiling steps use.

## Purpose

Use this skill when you want:

- the standard CellProfiler tables before profile aggregation
- per-image metadata together with per-cell and per-nucleus measurements
- the measurement stage that feeds the single-cell table step

## Main Outcome

After this skill finishes, the profiling step has exposed the standard CellProfiler measurement tables for the run.

In the public demo setup, the current packaged repository reuses bundled demo CellProfiler outputs instead of launching a fresh profiling backend run.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the profiling backend selected by that config
- the profiling `.cppipe` selected by the config
- an optional output directory

## Outputs

- `Image.csv`
  The image-level metadata table. Each row represents one field or site.
- `Cells.csv`
  The whole-cell measurement table. Each row represents one segmented cell.
- `Nuclei.csv`
  The nucleus measurement table. Each row represents one segmented nucleus.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

In this bundled demo output, `Cytoplasm.csv` is not present.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cpmeasure-local-v1`
- turn timestamp: `2026-05-05 13:46 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I want to inspect the standard Cell Painting measurement tables that come out before profile aggregation. Please use configs/project_config.demo.json, run the measurement step into demo/workspace/outputs/agent_demo_measurements, and then tell me which tables were produced and what each one represents biologically.
```

## Structured Trace

```text
user_input:
I want to inspect the standard Cell Painting measurement tables that come out before profile aggregation. Please use configs/project_config.demo.json, run the measurement step into demo/workspace/outputs/agent_demo_measurements, and then tell me which tables were produced and what each one represents biologically.

planner_step_1:
intent:
Load the documented Cell Painting skill routing before choosing the profiling measurement step.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- the workspace skill file loaded successfully
- the routing guidance identified `cp-extract-measurements` as the public measurement-table skill

planner_step_2:
intent:
Run the measurement step with the demo config and inspect the reported primary outputs.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cp-extract-measurements --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_measurements")
observed_result:
- skill_key = cp-extract-measurements
- output_dir = demo/workspace/outputs/agent_demo_measurements
- image_table_path = demo/backend/profiling_backend/outputs/cellprofiler/Image.csv
- cells_table_path = demo/backend/profiling_backend/outputs/cellprofiler/Cells.csv
- nuclei_table_path = demo/backend/profiling_backend/outputs/cellprofiler/Nuclei.csv
- mode = bundled-demo-outputs
- reason = profiling backend runner script is not packaged in this public demo checkout

planner_step_3:
intent:
Inspect the output tree and the table headers so the biological meaning of each table can be reported concretely.
tool_calls:
- exec("find .../agent_demo_measurements -maxdepth 2 -type f | sort")
- exec("find .../demo/backend/profiling_backend/outputs/cellprofiler -maxdepth 1 -type f | sort")
- exec("python ... read headers from Image.csv, Cells.csv, and Nuclei.csv")
- exec("python ... count rows in Image.csv, Cells.csv, and Nuclei.csv")
observed_result:
- Image.csv rows = 2, columns = 4
- Cells.csv rows = 4, columns = 13
- Nuclei.csv rows = 4, columns = 5
- Cytoplasm.csv was not present in the bundled demo output
- the manifest file was written under the requested demo output directory

final_answer_snapshot:
The measurement step exposed Image.csv, Cells.csv, and Nuclei.csv, and each table corresponds to one biological level in the profiling workflow.
```

## Observed Result

The recorded run exposed these standard CellProfiler tables:

- `Image.csv`
  `2` image rows and `4` columns
- `Cells.csv`
  `4` cell rows and `13` columns
- `Nuclei.csv`
  `4` nucleus rows and `5` columns

In this public demo bundle:

- `Cytoplasm.csv` was not present
- the skill reused bundled CellProfiler outputs instead of launching a fresh backend script

## Recorded Reply

```text
I ran the standard measurement step with the demo config.

Entrypoint run
- Skill: `cp-extract-measurements`
- Config: `/root/pipeline/CellPainting-Claw/configs/project_config.demo.json`
- Requested output dir: `/root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_measurements`
- Actual output dir reported by the pipeline: `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_measurements`

What happened
- In this public demo checkout, the profiling backend runner script is missing, so the skill reused bundled demo CellProfiler outputs instead of executing a fresh CellProfiler run.

Tables produced before profile aggregation
- `Image.csv`
- `Cells.csv`
- `Nuclei.csv`

What each one represents biologically
- `Image.csv`: one row per imaged field or site, carrying plate, well, and site metadata
- `Cells.csv`: one row per segmented whole cell, carrying morphology and channel-intensity measurements
- `Nuclei.csv`: one row per segmented nucleus, carrying nucleus position and size measurements

This is the pre-aggregation measurement stage: raw object tables that later steps combine into a single-cell profiling table.
```

## Next Skills

- [cp-build-single-cell-table](cp_build_single_cell_table.md)
