# CellPainting-Skills

`cellpainting_skills` is the task-oriented public layer of the repository.

It is intended for automation systems and for users who prefer stable task names over lower-level orchestration arguments.

## Main Functions

The key public helpers in this layer are:

- `available_pipeline_skills`
- `get_pipeline_skill_definition`
- `pipeline_skill_definition_to_dict`
- `run_pipeline_skill`

## Current Skill Model

In the current repository, each skill maps onto a named preset-backed workflow objective. Examples include:

- planning gallery data
- running the profiling workflow
- running the segmentation workflow
- running the DeepProfiler export or full branch
- running the full workflow

## Example

```python
import cellpainting_skills as cps

print(cps.available_pipeline_skills())
```

This layer is especially useful for automation and agent-facing routing, but it remains a public Python interface in its own right.
