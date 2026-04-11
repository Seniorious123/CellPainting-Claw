# `run-segmentation`

`run-segmentation` is the skill for **building segmentation outputs and single-cell crops**.

## What It Does

This skill runs the segmentation path and produces artifacts such as masks, preview images, and masked or unmasked single-cell crops.

## When To Use It

Use this skill when you want to:

- generate segmentation artifacts directly
- inspect masks or preview images
- export single-cell crops for later review or downstream use

## Human Use

CLI:

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill run-segmentation
```

Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation")
print(result.ok)
```

## Agent Use

An agent should map requests such as:

- `Run segmentation and export the single-cell crops.`
- `Generate the masks and preview images for this dataset.`

onto `run-segmentation`.

## Typical Outputs

Typical outputs include:

- masks
- preview images
- masked single-cell crops
- unmasked single-cell crops

## CellProfiler Note

This skill uses the configured CellProfiler `.cppipe` selection underneath.

## Related Skills

- [run-classical-profiling](run_classical_profiling.md)
- [prepare-deepprofiler-inputs](prepare_deepprofiler_inputs.md)
