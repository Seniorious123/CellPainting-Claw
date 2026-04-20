# `summarize-deepprofiler-profiles`

`summarize-deepprofiler-profiles` is the skill for turning DeepProfiler output tables into a readable summary package.

This skill reads DeepProfiler single-cell and well-level tables, computes feature variability at the well level, writes a metadata overview, and produces a simple PCA view.

It can read those tables either from explicit parquet paths or from the manifest written by `run-deepprofiler`.

## Recommended Use

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

## Agent Examples

- `Summarize the DeepProfiler outputs for me.`
- `Explain the DeepProfiler result tables and produce a PCA view.`

## Outputs

- `profile_summary.json`: high-level summary of the analyzed profile table and the summary statistics used in this report bundle.
- `well_metadata_summary.csv`: well-level metadata table included in the summary bundle.
- `top_variable_features.csv`: ranked list of the most variable features in the selected profile table.
- `pca_coordinates.csv`: PCA coordinates for each well in the summary view.
- `pca_plot.png`: quick PCA plot for visual inspection.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [run-deepprofiler](run_deepprofiler.md)
