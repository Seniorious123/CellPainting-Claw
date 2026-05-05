# `data-plan-download`

`data-plan-download` is the planning step that turns a data request into a concrete download plan before any files are fetched.

It resolves the dataset, source, and prefix that a request points to, and writes that result as a reusable plan file.

## Purpose

Use this skill when you want:

- see which gallery location a request points to
- check what the next download step would use before downloading anything

## Main Outcome

This skill does not download data. It tells you which dataset and source a request resolves to, which prefix will be targeted, and how many download steps the request contains.

In the demo setup, it produces a one-step plan for the demo request and saves that plan as JSON.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- a data request, for example a dataset and source pair
- an optional output directory

In the demo run below, the request uses dataset `cpg0016-jump` and source `source_4`.

## Outputs

- `download_plan.json`
  The saved plan. It records the resolved dataset, source, prefix, and the download steps that would be executed later.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `dataplan-local-v2`
- turn timestamp: `2026-05-05 12:38 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
Before downloading the demo Cell Painting data, I want to see exactly what this request would target. Use configs/project_config.demo.json, plan a request for dataset cpg0016-jump and source_4, save the plan under demo/workspace/outputs/agent_demo_data_plan, and tell me which gallery prefix it points to and how many download steps it contains.
```

## Structured Trace

```text
user_input:
Before downloading the demo Cell Painting data, I want to see exactly what this request would target. Use configs/project_config.demo.json, plan a request for dataset cpg0016-jump and source_4, save the plan under demo/workspace/outputs/agent_demo_data_plan, and tell me which gallery prefix it points to and how many download steps it contains.

planner_step_1:
intent:
Load the documented Cell Painting skill routing before choosing a data-access planning skill.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- the workspace skill file loaded successfully
- the routing guidance identified `data-plan-download` as the public planning skill for previewing a download request without executing it

planner_step_2:
intent:
Confirm the current skill catalog and inspect the documented description for the selected skill.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills list && echo '---DESCRIBE---' && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills describe --skill data-plan-download")
observed_result:
- the public skill catalog listed `data-plan-download`
- the skill description confirmed that this step resolves a request into a saved download plan without downloading files

planner_step_3:
intent:
Build the requested plan under the named demo output directory and inspect the generated plan JSON.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && mkdir -p demo/workspace/outputs/agent_demo_data_plan && python -m cellpaint_pipeline.cli plan-data-access --config configs/project_config.demo.json --dataset-id cpg0016-jump --source-id source_4 --output-path demo/workspace/outputs/agent_demo_data_plan/download_plan.json")
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/python -m cellpainting_skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill data-plan-download --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_plan --dataset-id cpg0016-jump --source-id source_4")
- exec("python ... read download_plan.json and print the resolved prefix and step count")
observed_result:
- the first planning attempt failed because `cellpaint_pipeline.cli` was not importable from that Python/module path
- skill_key = data-plan-download
- resolved dataset = cpg0016-jump
- resolved source = source_4
- resolved prefix = cpg0016-jump/source_4/
- step_count = 1
- step mode = gallery-source
- the plan file was written successfully

final_answer_snapshot:
The request resolves to gallery prefix cpg0016-jump/source_4/ and produces one download step.
```

## Observed Result

The recorded run showed that this demo request resolves to:

- dataset `cpg0016-jump`
- source `source_4`
- gallery prefix `cpg0016-jump/source_4/`

The generated plan contained:

- `1` download step
- adapter `gallery`
- mode `gallery-source`

This means the request is already concrete enough to pass to the next download step.

## Recorded Reply

```text
Planned and saved.

- Skill used: `data-plan-download`
- Config: `/root/pipeline/CellPainting-Claw/configs/project_config.demo.json`
- Plan path: `/root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_plan/download_plan.json`

What it targets:
- Gallery prefix: `cpg0016-jump/source_4/`
- Download steps: `1`

Notes:
- This is a source-based Gallery plan (`gallery-source`), not an executed download.
- The generated plan manifest was written under the requested demo output tree, and the plan resolves the dataset/source pair directly to that single source prefix.
```

## Next Skills

- [data-inspect-availability](data_inspect_availability.md)
- [data-download](data_download.md)
