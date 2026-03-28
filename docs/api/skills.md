# CellPainting-Skills

`cellpainting_skills` is the **task-oriented public layer** of the repository.

It is intended for automation systems and for users who prefer **stable task names** over lower-level workflow parameters.

## Main Functions

The key public helpers in this layer are:

- `available_pipeline_skills`
- `get_pipeline_skill_definition`
- `pipeline_skill_definition_to_dict`
- `run_pipeline_skill`

## How This Layer Fits The Project

The skills layer sits **above raw workflow arguments** and **below a full agent runtime**.

In practice, it provides a stable set of named tasks such as:

- planning gallery data
- running the profiling workflow
- running the segmentation workflow
- running the DeepProfiler export or full branch
- running the full workflow

This makes the skills layer especially useful for **automation**, **scripting**, and **agent-facing routing**.

## When To Use Skills

Use the skills layer when:

- you want **stable task names** instead of raw workflow parameters
- you are building **automation** on top of the library
- you want a cleaner bridge between **direct API calls** and a **full agent interface**

Use the main `cellpainting_claw` public entrypoints instead when you want the **canonical workflow API** directly.

## Minimal Example

```python
import cellpainting_skills as cps

print(cps.available_pipeline_skills())
```

## Relationship To Other Public Layers

The skills layer is optional, but it remains a **public Python interface** in its own right.

If you want:

- the canonical Python entrypoints, return to [Public Entrypoints](public_entrypoints.md)
- shell-facing execution, continue to [Command-Line Interface](cli.md)
- agent-mediated natural-language execution, continue to [OpenClaw](../openclaw/index.md)
