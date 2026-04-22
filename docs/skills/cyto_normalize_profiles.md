# `cyto-normalize-profiles`

`cyto-normalize-profiles` normalizes an annotated classical profile table.

## Purpose

Use this skill when you want pycytominer normalization before feature selection or downstream comparison.

## Inputs

- an annotated profile table from [cyto-annotate-profiles](cyto_annotate_profiles.md)
- normalization settings from the project config or explicit user options
- an optional output directory

## Outputs

- `normalized.parquet`: the normalized profile table
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cyto-normalize-profiles \
  --annotated-path outputs/cyto_annotate/annotated.parquet \
  --output-dir outputs/cyto_normalize
```

## Agent Use

Example request:

```text
Normalize the annotated classical profiles in outputs/cyto_annotate and write the result under outputs/cyto_normalize.
```

## Related Skills

- [cyto-select-profile-features](cyto_select_profile_features.md)
