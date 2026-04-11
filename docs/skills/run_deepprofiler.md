# `run-deepprofiler`

`run-deepprofiler` is the skill for **running the DeepProfiler path and collecting deep features**.

## What It Does

This skill runs the DeepProfiler-oriented path through export preparation, project assembly, profiling, and feature collection.

## When To Use It

Use this skill when you want to:

- generate deep features rather than only classical profiles
- run the standardized DeepProfiler path end to end
- collect the feature outputs needed for downstream deep-feature analysis

## Human Use

CLI:

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-deepprofiler
```

Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-deepprofiler")
print(result.ok)
```

## Agent Use

An agent should map requests such as:

- `Run the DeepProfiler branch and collect deep features.`
- `Build the DeepProfiler project and return the deep feature outputs.`

onto `run-deepprofiler`.

## Typical Outputs

Typical outputs include:

- DeepProfiler project files
- profile outputs
- collected deep feature tables

## Related Skills

- [prepare-deepprofiler-inputs](prepare_deepprofiler_inputs.md)
- [run-classical-profiling](run_classical_profiling.md)
