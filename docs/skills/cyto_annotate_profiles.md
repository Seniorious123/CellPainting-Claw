# `cyto-annotate-profiles`

`cyto-annotate-profiles` attaches experimental metadata to an aggregated classical profile table.

## Purpose

Use this skill when you want the aggregated profiles joined to plate-map, treatment, or perturbation metadata.

## Inputs

- an aggregated profile table from [cyto-aggregate-profiles](cyto_aggregate_profiles.md)
- metadata from the project config or user-provided metadata tables
- an optional output directory

## Outputs

- `annotated.parquet`: the metadata-annotated profile table
- `pipeline_skill_manifest.json`: the recorded skill run metadata

## Direct Use

```bash
cellpainting-skills run \
  --config configs/project_config.demo.json \
  --skill cyto-annotate-profiles \
  --aggregated-path outputs/cyto_aggregate/aggregated.parquet \
  --output-dir outputs/cyto_annotate
```

## Agent Use

Example request:

```text
Attach metadata to the aggregated profiles in outputs/cyto_aggregate and write the annotated table under outputs/cyto_annotate.
```

## Related Skills

- [cyto-normalize-profiles](cyto_normalize_profiles.md)
