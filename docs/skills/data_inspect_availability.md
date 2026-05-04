# `data-inspect-availability`

`data-inspect-availability` is the inspection step that checks which Cell Painting data sources are configured before any download begins.

It reads the project config, checks the configured discovery backends, and writes a summary that tells you which dataset and source identifiers are active and which discovery routes are currently usable.

## Purpose

Use this skill when you want:

- the configured dataset ID and source ID
- a quick check that the data-access setup is ready
- a summary of what can currently be discovered through Gallery, Quilt, or CPGData
- a clear starting point before planning or downloading data

## Main Outcome

This skill does not download any data. It tells you what this run is currently pointed at and which discovery options are available.

In the demo setup, it confirms:

- the default dataset
- the default source
- whether Gallery discovery works
- whether Quilt discovery works
- whether CPGData inventory discovery works

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- the data-access settings inside that config
- an optional output directory

In the demo config, those settings already define the default dataset ID, default source ID, and the configured Gallery, Quilt, and CPGData access points.

## Outputs

This skill writes:

- `data_access_summary.json`
  The main inspection result. It records the configured dataset and source identifiers, available packages, and discovery results from the configured access backends.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- turn timestamp: `2026-05-04 15:40 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
Before I download anything, run the configured data-source inspection for configs/project_config.demo.json and write the summary under demo/workspace/outputs/agent_demo_data_access. Then tell me which dataset and source identifiers are configured and what discovery options are currently available.
```

## Structured Trace

```text
user_input:
Before I download anything, run the configured data-source inspection for configs/project_config.demo.json and write the summary under demo/workspace/outputs/agent_demo_data_access. Then tell me which dataset and source identifiers are configured and what discovery options are currently available.

planner_step_1:
intent:
Load the documented Cell Painting skill routing before choosing a data-access skill.
tool_calls:
- read("integrations/openclaw/autodl/workspace/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- the workspace skill file loaded successfully
- the routing guidance pointed to `data-inspect-availability` for source-inspection requests before download

planner_step_2:
intent:
Confirm the current public skill surface and inspect the documented description for the selected skill.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills list && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills describe --skill data-inspect-availability")
observed_result:
- the first two host attempts failed because that OpenClaw session did not have the expected sandbox or node execution route
- the plain `exec` retry succeeded
- the current public skill catalog confirmed `data-inspect-availability` as the documented data-source inspection skill

planner_step_3:
intent:
Run the documented inspection skill against the named demo config and write the inspection output to the requested folder.
tool_calls:
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill data-inspect-availability --output-dir /root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_access")
observed_result:
- skill_key = data-inspect-availability
- configured dataset = cpg0016-jump
- configured source = source_4
- gallery dataset count = 42
- source count under cpg0016-jump = 14
- cpgdata prefix count = 5
- quilt package count = 0
- summary file written successfully

planner_step_4:
intent:
Read the generated inspection summary and turn it into a user-facing answer about what is configured and what discovery routes are available.
tool_calls:
- read("/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_access/data_access_summary.json")
observed_result:
- Gallery discovery was available
- Quilt discovery support was installed, but this query returned no package names
- CPGData inventory discovery was available
- required packages `boto3` and `botocore` were available

final_answer_snapshot:
The demo config is currently pointed at dataset cpg0016-jump and source_4, and the configured discovery routes are ready for planning the next download step.
```

## Observed Result

The recorded run confirmed that the demo config is currently pointed at:

- dataset `cpg0016-jump`
- source `source_4`

The inspection also showed that the configured discovery backends were available:

- Gallery discovery returned `42` dataset IDs
- Gallery source discovery returned `14` source IDs under `cpg0016-jump`
- CPGData inventory discovery returned `5` top-level prefixes
- Quilt support was installed, and this query returned `0` package names

The required access packages were available:

- `boto3`
- `botocore`

Optional helpers available in the demo environment included:

- `cpgdata`
- `quilt3`
- `pycytominer`

## Recorded Reply

```text
Done.

I ran the configured inspection with:

- entrypoint: `cellpainting-skills run`
- skill: `data-inspect-availability`
- config: `/root/pipeline/CellPainting-Claw/configs/project_config.demo.json`
- output dir: `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_access`

Main output written:

- `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_access/data_access_summary.json`
- `/root/autodl-tmp/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_data_access/pipeline_skill_manifest.json`

Configured dataset and source identifiers:
- default dataset ID: `cpg0016-jump`
- default source ID: `source_4`

Configured source backends:
- Gallery bucket: `cellpainting-gallery`
- Quilt registry: `s3://cellpainting-gallery`
- CPGData inventory bucket: `cellpainting-gallery-inventory`
- CPGData inventory prefix: `cellpainting-gallery/whole_bucket/`

Discovery options currently available:
- Gallery discovery: available
  - dataset listing worked
  - source listing for `cpg0016-jump` worked
- Quilt discovery: available at the package-access layer
  - `quilt3` is installed
  - current package listing returned `0` package names
- CPGData discovery: available
  - inventory prefix listing worked

Environment/access readiness:
- required packages available: `boto3`, `botocore`
- optional discovery/download helpers available: `cpgdata`, `quilt3`
- optional CLI available: `aws`
```

## Next Skills

- [data-plan-download](data_plan_download.md)
- [data-download](data_download.md)
