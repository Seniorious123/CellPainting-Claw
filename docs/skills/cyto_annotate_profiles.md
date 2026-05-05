# `cyto-annotate-profiles`

`cyto-annotate-profiles` adds experimental metadata to an aggregated classical profile table.

It is the step that turns a numeric well-level profile into a table that can be interpreted in the context of the experiment.

## Purpose

Use this skill when you want:

- treatment labels attached to aggregated profile rows
- control labels attached before normalization or downstream comparison
- batch information preserved for later QC and interpretation

## Main Outcome

After this skill finishes, the aggregated profile rows are no longer just numeric summaries.

They also carry the metadata needed to say what each well represents biologically.

## Inputs

This skill reads:

- a project config such as `configs/project_config.demo.json`
- an aggregated profile table from [cyto-aggregate-profiles](cyto_aggregate_profiles.md), or an equivalent table provided by the user
- an optional output directory

## Outputs

- `annotated.parquet`
  The metadata-annotated classical profile table.
- `pipeline_skill_manifest.json`
  The run record for this skill invocation.

## Agent Demo

This page is based on a real local OpenClaw run against the repository demo config:

- session id: `cytoannotate-local-v1`
- turn timestamp: `2026-05-05 14:06 UTC`
- model: `vibe/gpt-5-mini`

### Request

```text
I already have the aggregated Cell Painting profile table and want to add the experimental metadata that makes the wells interpretable. Please use configs/project_config.demo.json, annotate the aggregated profiles into demo/workspace/outputs/agent_demo_cyto_annotate, and then explain what metadata was attached and why this annotation step matters biologically.
```

## Structured Trace

```text
user_input:
I already have the aggregated Cell Painting profile table and want to add the experimental metadata that makes the wells interpretable. Please use configs/project_config.demo.json, annotate the aggregated profiles into demo/workspace/outputs/agent_demo_cyto_annotate, and then explain what metadata was attached and why this annotation step matters biologically.

planner_step_1:
intent:
Load the documented Cell Painting skill routing before choosing the annotation step.
tool_calls:
- read("~/.openclaw/lib/node_modules/openclaw/skills/cellpaint-pipeline/SKILL.md")
observed_result:
- that packaged path did not exist on this host

planner_step_2:
intent:
Recover the workspace skill instructions and then run the stable annotation surface.
tool_calls:
- exec("pwd && ls -la .../workspace/skills/cellpaint-pipeline && sed -n '1,240p' .../workspace/skills/cellpaint-pipeline/SKILL.md")
- exec("cd /root/pipeline/CellPainting-Claw && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills describe --skill cyto-annotate-profiles && echo '===RUN===' && /root/autodl-tmp/miniconda3_envs/lyx_env/bin/cellpainting-skills run --config /root/pipeline/CellPainting-Claw/configs/project_config.demo.json --skill cyto-annotate-profiles --output-dir /root/pipeline/CellPainting-Claw/demo/workspace/outputs/agent_demo_cyto_annotate")
- process.poll("vivid-comet")
observed_result:
- the workspace skill file loaded successfully
- the skill description confirmed that this step returns the annotated classical profile table
- skill_key = cyto-annotate-profiles
- annotated_path = demo/workspace/outputs/agent_demo_cyto_annotate/pycytominer/annotated.parquet
- row_count = 2
- column_count = 17

planner_step_3:
intent:
Inspect the annotated table schema and preview rows so the attached metadata can be reported concretely.
tool_calls:
- exec("python ... read annotated.parquet, print row count, column count, schema, and preview rows")
observed_result:
- annotated columns included Metadata_Treatment, Metadata_ControlType, and Metadata_Batch
- the two wells were labeled DEMO_A01 and DEMO_A02
- both wells were marked negative_control
- both wells were marked demo_batch_01

final_answer_snapshot:
The annotation step attached treatment, control-type, and batch metadata to the aggregated profile table.
```

## Observed Result

A real recorded run for this skill wrote:

- `pycytominer/annotated.parquet`
- `pipeline_skill_manifest.json`

The recorded output summary showed:

- `2` well-level rows
- `17` columns
- three metadata columns added on top of the aggregated profile table:
  - `Metadata_Treatment`
  - `Metadata_ControlType`
  - `Metadata_Batch`

## Recorded Reply

```text
Done — I ran the stable annotation skill on the demo config and wrote the result here:

- Entrypoint: `cyto-annotate-profiles`
- Config: `configs/project_config.demo.json`
- Output directory: `demo/workspace/outputs/agent_demo_cyto_annotate`
- Primary output: `demo/workspace/outputs/agent_demo_cyto_annotate/pycytominer/annotated.parquet`

What metadata was attached
- `Metadata_Treatment`
- `Metadata_ControlType`
- `Metadata_Batch`

From the demo output:
- `A01` -> `DEMO_A01`, `negative_control`, `demo_batch_01`
- `A02` -> `DEMO_A02`, `negative_control`, `demo_batch_01`

Why this matters biologically
- treatment metadata links each profile back to the perturbation or condition
- control metadata defines the reference wells used later for comparison
- batch metadata preserves experimental grouping so technical variation is not mistaken for biology
```

## Next Skills

- [cyto-normalize-profiles](cyto_normalize_profiles.md)
