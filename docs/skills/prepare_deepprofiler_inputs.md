# `prepare-deepprofiler-inputs`

`prepare-deepprofiler-inputs` is the skill for **preparing the export artifacts needed by DeepProfiler**.

## What It Does

This skill stops after writing the images, metadata, and location files needed for a later DeepProfiler run.

## When To Use It

Use this skill when you want to:

- prepare DeepProfiler-ready inputs without running DeepProfiler yet
- inspect the export artifacts first
- split export preparation from the later deep-feature run

## Human Use

CLI:

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill prepare-deepprofiler-inputs
```

Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "prepare-deepprofiler-inputs")
print(result.ok)
```

## Agent Use

An agent should map requests such as:

- `Prepare the DeepProfiler inputs but do not run DeepProfiler yet.`
- `Write the images and locations needed for a later DeepProfiler run.`

onto `prepare-deepprofiler-inputs`.

## Typical Outputs

Typical outputs include:

- export metadata
- DeepProfiler-ready image inputs
- DeepProfiler-ready location inputs

## Related Skills

- [run-segmentation](run_segmentation.md)
- [run-deepprofiler](run_deepprofiler.md)
