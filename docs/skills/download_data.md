# `download-data`

`download-data` is the skill for **executing the local download step**.

## What It Does

This skill turns a configured request or plan into local files that can be used by later processing steps.

## When To Use It

Use this skill when you want to:

- materialize the selected dataset locally
- move from planning to actual file download
- prepare local inputs for later profiling or segmentation runs

## Human Use

CLI:

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill download-data
```

Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "download-data")
print(result.ok)
```

## Agent Use

An agent should map requests such as:

- `Download the selected dataset locally.`
- `Fetch the files we need before running the next processing step.`

onto `download-data`.

## Typical Outputs

Typical outputs include:

- `download_plan.json`
- `download_execution.json`

## Related Skills

- [plan-data-access](plan_data_access.md)
- [run-classical-profiling](run_classical_profiling.md)
- [run-segmentation](run_segmentation.md)
