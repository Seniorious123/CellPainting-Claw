# Quick Start

This page shows the shortest reproducible demo path in the repository.

The demo uses the bundled synthetic assets under `demo/` and runs two documented skills:

- `cp-extract-segmentation-artifacts`
- `cp-generate-segmentation-previews`

This is the public demo path because it is the part that has been re-run and verified against the current packaged assets.

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

This is the fastest way to see the current public skill catalog.

## 4. Inspect A Skill

Inspect the segmentation skill:

```bash
cellpainting-skills describe --skill cp-extract-segmentation-artifacts
```

This shows the task definition, expected inputs, and typical outputs.

## 5. Run Segmentation On The Demo Assets

Run the segmentation artifact skill on the bundled demo config:

```bash
SEG_ROOT=demo/workspace/outputs/quick_start_segmentation

cellpainting-skills run \
  --config "$CONFIG" \
  --skill cp-extract-segmentation-artifacts \
  --output-dir "$SEG_ROOT"
```

This skill:

- runs the packaged CellProfiler-based segmentation path
- writes a workflow root that later skills can reuse
- uses the repository-provided `.cppipe` selection from the demo config

Key outputs include:

- `load_data_for_segmentation.csv`
- `CPJUMP1_analysis_mask_export.cppipe`
- `cellprofiler_masks/Image.csv`
- `cellprofiler_masks/Cells.csv`
- `cellprofiler_masks/Nuclei.csv`
- `cellprofiler_masks/labels/`
- `cellprofiler_masks/outlines/`
- `segmentation_summary.json`
- `pipeline_skill_manifest.json`

## 6. Run A Follow-Up Skill

Use the workflow root from the previous step and render preview PNGs:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill cp-generate-segmentation-previews \
  --workflow-root "$SEG_ROOT" \
  --output-dir demo/workspace/outputs/quick_start_previews
```

This follow-up skill reads the segmentation workflow root and writes field-level preview PNGs under `sample_previews_png/`.

## 7. Demo Page

A full recorded run based on the bundled synthetic assets is documented separately in [Demo](../demo/index.md).

That page covers a complete skill-driven path:

- segmentation artifacts
- preview generation
- single-cell crop export
- DeepProfiler input export
- DeepProfiler project assembly
- DeepProfiler inference
- feature collection
- summary outputs

## 8. Python Example

```python
from cellpainting_claw import ProjectConfig
import cellpainting_skills as cps

config = ProjectConfig.from_json("configs/project_config.demo.json")
result = cps.run_pipeline_skill(
    config,
    "cp-extract-segmentation-artifacts",
    output_dir="demo/workspace/outputs/python_demo_segmentation",
)
print(result.ok)
print(result.primary_outputs["image_table_path"])
print(result.primary_outputs["summary_path"])
```

## 9. Natural-Language Path

If you want to run the same skills through an agent instead of calling them directly, continue to [OpenClaw](../openclaw/index.md).

## 10. Next Pages

After this first run, the most useful next pages are:

- [Demo](../demo/index.md) for a complete recorded run
- [Skills](../skills/index.md) for the full skill catalog
- [CLI](../cli/index.md) for command groups and intended use
- [OpenClaw](../openclaw/index.md) for natural-language and agent-mediated execution
