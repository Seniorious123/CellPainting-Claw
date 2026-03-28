# Public Entrypoints

The main public Python surface is exposed through `cellpainting_claw`.

## Recommended Starting Points

For most users, the most important top-level entrypoints are:

- `run_end_to_end_pipeline`
- `run_pipeline_skill`
- `run_pipeline_preset`
- `run_deepprofiler_pipeline`

These functions define the stable high-level API for the library and should be preferred over internal workflow modules.

## When To Use Each Entrypoint

- `run_end_to_end_pipeline` is the default first choice when you want one standard workflow run.
- `run_pipeline_skill` is useful when you want stable task names rather than raw workflow arguments.
- `run_pipeline_preset` is useful when you already know the workflow shape and want a named configuration bundle.
- `run_deepprofiler_pipeline` is the direct entrypoint for the DeepProfiler branch.

## Supporting Public Areas

The package also exposes public helpers for:

- configuration loading through `ProjectConfig`
- data access planning through `build_data_request`, `build_download_plan`, and `execute_download_plan`
- branch-specific execution through `run_profiling_suite` and `run_segmentation_suite`
- public API discovery through `available_public_api_entrypoints` and related summary helpers

## Minimal Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.portable.example.json")
result = cp.run_end_to_end_pipeline(config)
print(result.output_dir)
```

## Design Rule

The public API is designed so that top-level workflow entrypoints are easier to depend on than internal workflow modules. The more specialized helpers remain available, but they are not meant to be the first layer most users learn.
