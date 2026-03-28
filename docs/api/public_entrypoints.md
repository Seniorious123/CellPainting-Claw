# Public Entrypoints

The main public Python surface is exposed through `cellpainting_claw`.

## Recommended Top-Level Entrypoints

For most users, the most important public entrypoints are:

- `run_end_to_end_pipeline`
- `run_pipeline_skill`
- `run_pipeline_preset`
- `run_deepprofiler_pipeline`

These functions define the stable high-level API for the library.

## Supporting Public Areas

The package also exposes public helpers for:

- configuration loading through `ProjectConfig`
- data access planning through `build_data_request`, `build_download_plan`, and `execute_download_plan`
- branch-specific execution through `run_profiling_suite` and `run_segmentation_suite`
- public API discovery through `available_public_api_entrypoints` and related summary helpers

## Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.portable.example.json")
result = cp.run_end_to_end_pipeline(config)
print(result.output_dir)
```

The API section will expand over time, but the main design rule is already fixed: top-level workflow entrypoints should be easier to depend on than internal workflow modules.
