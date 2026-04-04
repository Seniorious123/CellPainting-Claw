# Quick Start

This page shows the **shortest practical way** to understand CellPainting-Claw as a toolkit.

The goal is not to run every tool at once. The goal is to:

- confirm that the package is installed
- see the skill catalog
- inspect one skill
- run one skill on the bundled demo config
- understand what kind of result that skill produces

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

## 3. Look At The Skill Catalog

List the currently available skills:

```bash
cellpainting-skills list
```

This is the fastest way to see how the toolkit is exposed as named tasks.

## 4. Inspect One Skill

Describe the segmentation skill:

```bash
cellpainting-skills describe --skill run-segmentation-workflow
```

This shows the stable skill name together with the task description.

## 5. Optional: Inspect CellProfiler `.cppipe` Selection

Before running a segmentation-oriented task, you can inspect the effective CellProfiler pipeline selection:

```bash
cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind segmentation
cellpainting-claw validate-cppipe-config --config "$CONFIG"
```

This is useful if you plan to switch from a bundled `.cppipe` template to a custom `.cppipe` later.

## 6. Run One Skill

Run the segmentation skill on the demo config:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-segmentation-workflow
```

What this skill does:

- runs the segmentation tool family
- uses the configured segmentation-side `.cppipe` selection
- produces segmentation-oriented artifacts rather than pycytominer outputs

Typical result artifacts include:

- label masks
- sample preview images
- masked single-cell crops
- unmasked single-cell crops

## 7. Python Version Of The Same Idea

The same task can be called from Python:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-segmentation-workflow")
print(result.ok)
print(result.segmentation_output_dir)
```

## 8. What To Read Next

After this first run, the most useful next pages are:

- [Skills](../skills/index.md) for the full skill catalog
- [API](../api/index.md) for the main Python toolkit surface
- [CLI](../cli/index.md) for command groups and their intended use
- [OpenClaw](../openclaw/index.md) if you want natural-language or agent-mediated execution
