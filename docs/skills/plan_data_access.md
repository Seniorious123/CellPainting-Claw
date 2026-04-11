# `plan-data-access`

`plan-data-access` is the skill for **inspecting a dataset and writing a reusable data-access plan**.

## What It Does

This skill looks at the configured data source and writes planning outputs without running segmentation, profiling, or DeepProfiler.

## When To Use It

Use this skill when you want to:

- understand what data is available before downloading or processing it
- create a reusable access plan for later runs
- start from the input side of the workflow rather than from the analysis side

## Human Use

CLI:

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill plan-data-access
```

Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "plan-data-access")
print(result.ok)
```

## Agent Use

An agent should map requests such as:

- `Inspect the dataset and prepare a reusable access plan.`
- `Tell me what data is available and write the plan for downloading it later.`

onto `plan-data-access`.

## Typical Outputs

Typical outputs include:

- `data_access_summary.json`
- `download_plan.json`

## Related Skills

- [download-data](download_data.md)
- [run-classical-profiling](run_classical_profiling.md)
