# `run-classical-profiling`

`run-classical-profiling` is the skill for **building classical Cell Painting profiling outputs**.

## What It Does

This skill runs the classical profiling path and produces the single-cell tables and downstream pycytominer-oriented outputs used for classical analysis.

## When To Use It

Use this skill when you want to:

- generate classical Cell Painting profiles
- produce single-cell tables for pycytominer-based analysis
- focus on the classical profiling path rather than on deep features

## Human Use

CLI:

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-classical-profiling
```

Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-classical-profiling")
print(result.ok)
```

## Agent Use

An agent should map requests such as:

- `Generate the classical profiling outputs for this dataset.`
- `Run the pycytominer-oriented path and build the profile tables.`

onto `run-classical-profiling`.

## Typical Outputs

Typical outputs include:

- `single_cell.csv.gz`
- `pycytominer/`
- `evaluation/`

## Related Skills

- [run-segmentation](run_segmentation.md)
- [prepare-deepprofiler-inputs](prepare_deepprofiler_inputs.md)
