# CellPainting-Claw

[Documentation](https://cellpainting-claw.readthedocs.io/en/latest/)

CellPainting-Claw turns a fragmented Cell Painting stack into one documented skill catalog. Instead of asking users to stitch together data-access utilities, CellProfiler steps, pycytominer processing, DeepProfiler preparation, and agent glue by hand, the project exposes the same skills for direct use and for agent-mediated use.

## Public Entry Points

The repository exposes three public entry points.

| Entry point | Use it when | What it gives you |
| --- | --- | --- |
| `cellpainting_skills` | you want to run documented tasks directly | the public skill catalog for data access, profiling, segmentation, crop export, and DeepProfiler |
| `OpenClaw` | you want to use the same skills through natural language | an agent front end that maps prompts onto the same skill catalog |
| `cellpainting_claw` | you need lower-level control | the advanced toolkit package for configuration, direct helpers, and MCP serving |

## Foundation Packages

CellPainting-Claw integrates these package and tool families in workflow order.

| Capability area | Packages or tools | Main capability |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | inspect Cell Painting sources and download dataset slices |
| Measurement extraction | `CellProfiler` | run profiling and segmentation pipelines, write masks, and export object tables |
| Classical profile generation | `pycytominer` | aggregate and normalize Cell Painting features |
| Deep feature extraction | `DeepProfiler` | turn segmentation-guided single-cell inputs into embedding features |

## Public Skill Catalog

The public skill catalog is grouped by concrete user tasks.

### Data Access

| Skill | Main result |
| --- | --- |
| `inspect-cellpainting-data` | inspect configured sources and write a data-access summary |
| `download-cellpainting-data` | download one dataset slice into a local cache |

### Profiling

| Skill | Main result |
| --- | --- |
| `run-cellprofiler-profiling` | write CellProfiler measurement tables |
| `export-single-cell-measurements` | merge CellProfiler tables into one single-cell measurements table |
| `run-pycytominer` | write aggregated, annotated, normalized, and feature-selected outputs |
| `summarize-classical-profiles` | turn classical profile outputs into readable summaries and PCA views |

### Segmentation

| Skill | Main result |
| --- | --- |
| `run-segmentation-masks` | write segmentation masks, labels, outlines, object tables, and sample previews |
| `export-single-cell-crops` | export masked or unmasked single-cell crop stacks |

### DeepProfiler

| Skill | Main result |
| --- | --- |
| `prepare-deepprofiler-project` | prepare a runnable DeepProfiler project directory |
| `run-deepprofiler` | run the DeepProfiler path and return collected feature tables |
| `summarize-deepprofiler-profiles` | turn DeepProfiler outputs into readable summaries and PCA views |

## CellProfiler `.cppipe` Support

CellPainting-Claw exposes a **config-driven CellProfiler `.cppipe` selection layer**.

Users can:

- choose a bundled `.cppipe` template
- point to a custom `.cppipe` path
- inspect the effective selection before a longer run
- validate the selection from Python or CLI

The project config accepts a `cellprofiler` block such as:

```json
{
  "cellprofiler": {
    "profiling_template": "profiling-analysis",
    "segmentation_template": "segmentation-base",
    "custom_profiling_cppipe_path": null,
    "custom_segmentation_cppipe_path": null
  }
}
```

Current phase-1 behavior:

- segmentation consumes the configured `.cppipe` selection at runtime
- profiling exposes the same template listing, selection, and validation helpers
- custom segmentation overrides are treated as ready-to-run mask-export pipelines

Useful inspection commands:

```bash
cellpainting-claw list-cppipe-templates --config configs/project_config.demo.json
cellpainting-claw show-cppipe-selection --config configs/project_config.demo.json --kind all
cellpainting-claw validate-cppipe-config --config configs/project_config.demo.json
```

## Quick Start

Create the environment and install the package:

```bash
cd <repo-root>
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
```

Use the bundled demo config:

```bash
CONFIG=configs/project_config.demo.json
```

Look at the skill catalog and inspect one task:

```bash
cellpainting-skills list
cellpainting-skills describe --skill run-segmentation-masks
```

Optionally inspect the effective `.cppipe` selection:

```bash
cellpainting-claw show-cppipe-selection --config "$CONFIG" --kind segmentation
cellpainting-claw validate-cppipe-config --config "$CONFIG"
```

Run one skill:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-segmentation-masks \
  --output-dir outputs/demo_segmentation
```

## Python API Example

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

## Agent And OpenClaw Integration

OpenClaw is an **optional natural-language entry point** for the same toolkit.

In normal use, OpenClaw connects to the MCP surface and maps natural-language requests onto the documented skills. It does not replace the core library or CLI.

## Documentation

Start here:

- [Read the Docs](https://cellpainting-claw.readthedocs.io/en/latest/)
- `docs/index.md`
- `docs/skills/index.md`
- `docs/cli/index.md`
- `docs/openclaw/index.md`

## Publication Hygiene

Repository-managed docs and config templates are English-only and do not store provider keys.

If a provider key was previously typed into a shell, written into a local config, or pasted into chat, rotate or revoke it before publishing the project.
