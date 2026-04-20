# `summarize-deepprofiler-profiles`

`summarize-deepprofiler-profiles` is the skill for turning DeepProfiler output tables into a readable summary package.

## What It Does

This skill reads DeepProfiler single-cell and well-level tables, computes feature variability at the well level, writes a metadata overview, and produces a simple PCA view.

It can read those tables either from explicit parquet paths or from the manifest written by `run-deepprofiler`.

## When To Use It

Use this skill when you want to:

- inspect DeepProfiler outputs without opening raw embedding tables directly
- hand DeepProfiler results to a human reader in a more readable form
- check how wells separate in a first-pass PCA summary

## CLI

```bash
CONFIG=configs/project_config.demo.json
DEEPPROFILER_SKILL_MANIFEST=outputs/demo_deepprofiler/pipeline_skill_manifest.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill summarize-deepprofiler-profiles \
  --manifest-path "$DEEPPROFILER_SKILL_MANIFEST" \
  --output-dir outputs/demo_deepprofiler_summary
```

## Agent Request Examples

- `Summarize the DeepProfiler outputs for me.`
- `Explain the DeepProfiler result tables and produce a PCA view.`

## Typical Outputs

- `profile_summary.json`
- `well_metadata_summary.csv`
- `top_variable_features.csv`
- `pca_coordinates.csv`
- `pca_plot.png`
- `pipeline_skill_manifest.json`

## Related Skills

- [run-deepprofiler](run_deepprofiler.md)
