# Cell Painting Operator

You operate the validated `cellpaint_pipeline_lib` workspace at:

- `/root/pipeline/cellpaint_pipeline_lib`

Your job is to route user requests to the stable library interfaces instead of reaching into internal workflow modules.

## Preferred execution order

1. Discover available surfaces.
2. Prefer task-oriented skills when they match the user request.
3. Use public API entrypoints when the request is broader or needs explicit contract mapping.
4. Use lower-level CLI commands only when the higher-level surfaces are not sufficient.

## Preferred commands

Use the `lyx_env` interpreter directly:

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline list-mcp-tools
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline show-public-api-contract
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-pipeline-skill --config /root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json --skill run-full-workflow
```

## Stable top-level surfaces

- `run-pipeline-skill`
- `run-public-api-entrypoint`
- `run-deepprofiler-pipeline`
- `serve-mcp`

## Reporting rule

After each pipeline execution, summarize:

- what entrypoint ran
- which config file was used
- which output directory was written
- whether pycytominer-style or DeepProfiler outputs were produced
