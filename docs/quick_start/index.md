# Quick Start

This page shows the **shortest practical way** to understand CellPainting-Claw as a toolkit built around modular skills.

The goal is not to run every part of the toolkit at once. The goal is to:

- confirm that the package is installed
- see the public skill catalog
- inspect one skill
- run one skill on the bundled demo config
- run one follow-up skill from the output of the first one

## 1. Install

From the repository root:

```bash
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
```

## 2. Demo Config

For the first run, use the repository's bundled demo config:

```bash
CONFIG=configs/project_config.demo.json
```

This config points to the demo assets included under `demo/`.

## 3. List Skills

```bash
cellpainting-skills list
```

This is the fastest way to see the current public task model.

## 4. Inspect A Skill

Describe the segmentation skill:

```bash
cellpainting-skills describe --skill run-segmentation-masks
```

This shows what the skill is for and how it fits into the public task catalog.

## 5. Run A Skill

Run the segmentation-mask skill on the demo config:

```bash
RUN_ROOT=outputs/demo_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-segmentation-masks \
  --output-dir "$RUN_ROOT"
```

What this skill does:

- runs the segmentation mask-export path
- writes the segmentation outputs that later skills can reuse

Typical outputs include:

- `cellprofiler_masks/`
- `Image.csv`
- `Cells.csv`
- `Nuclei.csv`
- `labels/`
- `outlines/`
- `sample_previews_png/`

## 6. Run A Follow-Up Skill

Use the workflow root from the previous step and export single-cell crops:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill export-single-cell-crops \
  --workflow-root "$RUN_ROOT" \
  --crop-mode masked \
  --output-dir "$RUN_ROOT/crops"
```

This is the main idea behind the skill catalog: one skill produces a concrete output, and later skills can build on that output.

## 7. Python Example

```python
from cellpainting_claw import ProjectConfig
import cellpainting_skills as cps

config = ProjectConfig.from_json("configs/project_config.demo.json")
result = cps.run_pipeline_skill(
    config,
    "run-segmentation-masks",
    output_dir="outputs/demo_segmentation",
)
print(result.ok)
print(result.primary_outputs["summary_path"])
```

## 8. Next Pages

After this first run, the most useful next pages are:

- [Skills](../skills/index.md) for the full skill catalog
- [CLI](../cli/index.md) for command groups and intended use
- [OpenClaw](../openclaw/index.md) for natural-language and agent-mediated execution
