# Quick Start

This page shows the **shortest practical way** to understand CellPainting-Claw as a toolkit built around modular skills.

The goal is not to run every layer at once. The goal is to:

- confirm that the package is installed
- see the public skill catalog
- inspect one skill
- inspect the CellProfiler `.cppipe` used by that skill
- run one skill on the bundled demo config

## 1. Install The Package

From the repository root:

```bash
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
```

## 2. Use The Bundled Demo Config

For the first run, use the repository's bundled demo config:

```bash
CONFIG=configs/project_config.demo.json
```

This config points to the demo assets included under `demo/`.

## 3. List The Skill Catalog

```bash
cellpainting-skills list
```

This is the fastest way to see the current public task model.

## 4. Inspect One Skill

Describe the segmentation skill:

```bash
cellpainting-skills describe --skill run-segmentation
```

This shows what the skill is for and how it fits into the public task catalog.

## 5. Inspect The CellProfiler `.cppipe` Selection

Before running a segmentation-oriented skill, inspect the effective CellProfiler pipeline selection:

```bash
cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind segmentation
cellpainting-claw validate-cppipe-config --config "$CONFIG"
```

What this means:

- `.cppipe` is the CellProfiler pipeline file format
- this step shows which CellProfiler pipeline the segmentation skill will use
- this is the right place to check or customize the CellProfiler-side pipeline selection

## 6. Run One Skill

Run the segmentation skill on the demo config:

```bash
cellpainting-skills run   --config "$CONFIG"   --skill run-segmentation
```

What this skill does:

- runs the segmentation path
- uses the configured segmentation-side CellProfiler `.cppipe`
- produces segmentation artifacts rather than pycytominer outputs

Typical outputs include:

- label masks
- sample preview images
- masked single-cell crops
- unmasked single-cell crops

## 7. Python Version Of The Same Idea

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation")
print(result.ok)
print(result.segmentation_output_dir)
```

## 8. Combined Runs Use Presets

If you intentionally want a combined run such as profiling plus segmentation, use a preset rather than treating that combined path as one of the core skills.

For example:

```bash
cellpainting-claw run-pipeline-preset   --config "$CONFIG"   --preset full-pipeline
```

## 9. What To Read Next

After this first run, the most useful next pages are:

- [Skills](../skills/index.md) for the full skill catalog
- [CLI](../cli/index.md) for command groups and intended use
- [OpenClaw](../openclaw/index.md) for natural-language and agent-mediated execution
