# Public Entrypoints

The main public Python surface is exposed through `cellpainting_claw`.

## Recommended Starting Points

For most users, the most important top-level entrypoints are:

- `run_end_to_end_pipeline`
- `run_pipeline_skill`
- `run_pipeline_preset`
- `run_deepprofiler_pipeline`

These functions define the stable high-level API for the library and should be preferred over internal workflow modules.

## How To Choose

Use the public entrypoints in this order:

1. `run_end_to_end_pipeline` when you want one standard workflow run
2. `run_pipeline_skill` when stable task names are more useful than raw workflow arguments
3. `run_pipeline_preset` when you already know the workflow shape and want a named parameter bundle
4. `run_deepprofiler_pipeline` when you want to enter the DeepProfiler branch directly

This ordering reflects the design of the package: top-level public entrypoints are intended to be easier to depend on than lower-level implementation modules.

## Supporting Public Areas

The package also exposes public helpers for:

- configuration loading through `ProjectConfig`
- data-access planning through `build_data_request`, `build_download_plan`, and `execute_download_plan`
- branch-specific execution through `run_profiling_suite` and `run_segmentation_suite`
- public API discovery through `available_public_api_entrypoints` and related summary helpers

These helpers are still public, but they are not the first layer most users should learn.

## Minimal Example

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.portable.example.json")
result = cp.run_end_to_end_pipeline(config)
print(result.output_dir)
```

## Relationship To Other Public Layers

The public entrypoints page documents the canonical Python surface.

If you want:

- stable task names, continue to [CellPainting-Skills](skills.md)
- shell-oriented execution, continue to [Command-Line Interface](cli.md)
- natural-language or agent-mediated execution, continue to [OpenClaw](../openclaw/index.md)
