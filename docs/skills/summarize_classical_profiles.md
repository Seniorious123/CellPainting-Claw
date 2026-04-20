# `summarize-classical-profiles`

`summarize-classical-profiles` is the skill for turning pycytominer profile tables into a readable summary package.

This skill reads a classical profile table, computes feature variability, writes a metadata overview, and produces a simple PCA view.

It can read the profile table either from an explicit `feature_selected` path or from the manifest written by `run-pycytominer`.

## Recommended Use

Use this skill when you want to:

- inspect pycytominer outputs without opening raw parquet files directly
- hand classical profile results to a human reader in a more readable form
- check how wells separate in a first-pass PCA summary

## CLI

```bash
CONFIG=configs/project_config.demo.json
PYCYTOMINER_SKILL_MANIFEST=outputs/demo_pycytominer/pipeline_skill_manifest.json

cellpainting-skills run \
  --config "$CONFIG" \
  --skill summarize-classical-profiles \
  --manifest-path "$PYCYTOMINER_SKILL_MANIFEST" \
  --output-dir outputs/demo_classical_summary
```

## Agent Examples

- `Summarize the classical profile outputs for me.`
- `Explain the pycytominer results and produce a PCA view.`

## Outputs

- `profile_summary.json`: high-level summary of the analyzed profile table and the summary statistics used in this report bundle.
- `well_metadata_summary.csv`: well-level metadata table included in the summary bundle.
- `top_variable_features.csv`: ranked list of the most variable features in the selected profile table.
- `pca_coordinates.csv`: PCA coordinates for each well in the summary view.
- `pca_plot.png`: quick PCA plot for visual inspection.
- `pipeline_skill_manifest.json`: record of the skill run, including inputs, parameters, and the main output paths.

## Related Skills

- [export-single-cell-measurements](export_single_cell_measurements.md)
- [run-pycytominer](run_pycytominer.md)
