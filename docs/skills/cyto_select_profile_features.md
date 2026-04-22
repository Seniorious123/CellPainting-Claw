# `cyto-select-profile-features`

`cyto-select-profile-features` reduces normalized classical profiles to the retained feature set.

## Purpose

Use this skill when you want the final feature-selected classical profile table.

## Inputs

- a normalized profile table from [cyto-normalize-profiles](cyto_normalize_profiles.md)
- feature-selection settings from the project config or explicit user options
- an optional output directory

## Outputs

- `feature_selected.parquet`: the feature-selected classical profile table
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cyto-select-profile-features \
  --normalized-path outputs/cyto_normalize/normalized.parquet \
  --output-dir outputs/cyto_feature_select
```

## Agent Use

Example request:

```text
Select the final classical profile features from outputs/cyto_normalize and write the result under outputs/cyto_feature_select.
```

## Related Skills

- [cyto-summarize-classical-profiles](cyto_summarize_classical_profiles.md)
