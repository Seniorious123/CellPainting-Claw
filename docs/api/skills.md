# CellPainting-Skills

`cellpainting_skills` is the task-oriented public layer of the repository.

It is intended for automation systems and for users who prefer stable task names over lower-level orchestration arguments.

## Main Functions

The key public helpers in this layer are:

- `available_pipeline_skills`
- `get_pipeline_skill_definition`
- `pipeline_skill_definition_to_dict`
- `run_pipeline_skill`

## How This Layer Fits The Project

The skills layer sits above the raw workflow arguments and below a full agent interface. In practice, it gives the project a stable set of named tasks such as:

- planning gallery data
- running the profiling workflow
- running the segmentation workflow
- running the DeepProfiler export or full branch
- running the full workflow

This makes the skills layer especially useful for automation, scripting, and agent-facing routing.

## Minimal Example

```python
import cellpainting_skills as cps

print(cps.available_pipeline_skills())
```

The skills layer is optional, but it remains a public Python interface in its own right.
