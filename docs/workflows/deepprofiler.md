# DeepProfiler

CellPainting-Claw includes a standardized DeepProfiler branch that can:

- export DeepProfiler-ready inputs
- materialize a DeepProfiler project directory
- run profiling
- collect features into pycytominer-friendly outputs

Typical high-level entrypoints include:

- `run_deepprofiler_pipeline`
- `run_pipeline_skill(..., skill_key="run-deepprofiler-full")`

Related documentation:

- [Usage Guide](../usage_guide.md)
- [Python API Help](../python_api_help.md)
- [Public API Contract](../public_api_contract.md)
