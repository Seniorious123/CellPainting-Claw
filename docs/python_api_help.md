# Python API Help

This document is the Python-side equivalent of CLI `--help`.

It focuses on the importable, publication-facing surface rather than internal helper functions.

## Recommended Import Style

```python
import cellpaint_pipeline as cp

config = cp.ProjectConfig.from_json(
    "/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json"
)
```

## Recommended Top-Level Calls

In order of preference:

1. `cp.run_end_to_end_pipeline(config, ...)`
2. `cp.run_pipeline_skill(config, skill_key, ...)`
3. `cp.run_pipeline_preset(config, preset_key, ...)`
4. `cp.run_deepprofiler_pipeline(config, ...)`

Discovery helpers for automation layers:

- `cp.recommended_public_api_pathways()`
- `cp.available_public_api_entrypoints()`
- `cp.public_api_contract_summary()`
- `cp.available_pipeline_skills()`
- `cp.available_pipeline_presets()`

## Core Public Types

- `ProjectConfig`
- `DataAccessConfig`
- `PublicApiContractError`
- `ConfigContractError`

## Public API Categories

### Configuration

- `ProjectConfig.from_json(path)`
- `project_config_field_guide()`
- `data_access_config_field_guide()`
- `project_config_contract_summary()`

### Data Access

- `summarize_data_access(config, ...)`
- `build_data_request(...)`
- `build_download_plan(config, request, ...)`
- `execute_download_plan(config, plan, ...)`
- `write_download_plan(plan, path)`
- `load_download_plan(path)`
- `list_gallery_datasets(config, ...)`
- `list_gallery_sources(config, ...)`
- `list_gallery_prefixes(config, ...)`
- `download_gallery_prefix(config, ...)`
- `download_gallery_source(config, ...)`
- `list_quilt_packages(config, ...)`
- `browse_quilt_package(config, ...)`
- `list_cpgdata_prefixes(config, ...)`
- `sync_cpgdata_index(config, ...)`
- `sync_cpgdata_inventory(config, ...)`

### Delivery and Orchestration

- `run_profiling_suite(config, suite_key, ...)`
- `run_segmentation_suite(config, suite_key, ...)`
- `run_full_pipeline(config, ...)`
- `run_smoke_test(config, ...)`
- `run_end_to_end_pipeline(config, ...)`
- `run_workflow(config, workflow_key, ...)`

### Presets and Skills

- `available_pipeline_presets()`
- `get_pipeline_preset_definition(key)`
- `pipeline_preset_definition_to_dict(definition)`
- `run_pipeline_preset(config, preset_key, ...)`
- `available_pipeline_skills()`
- `get_pipeline_skill_definition(key)`
- `pipeline_skill_definition_to_dict(definition)`
- `run_pipeline_skill(config, skill_key, ...)`

### Public API Dispatcher

- `available_public_api_entrypoints()`
- `get_public_api_entrypoint(name)`
- `public_api_entrypoint_to_dict(entry)`
- `public_api_contract_summary()`
- `available_public_api_output_contracts()`
- `get_public_api_output_contract(name)`
- `public_api_output_contract_summary()`
- `run_public_api_entrypoint(name, config=None, **kwargs)`
- `run_public_api_entrypoint_to_dict(name, config=None, **kwargs)`

### DeepProfiler

- `run_deepprofiler_pipeline(config, ...)`
- `deepprofiler_pipeline_result_to_dict(result)`

### MCP and Agent Integration

- `available_mcp_tools()`
- `get_mcp_tool_definition(name)`
- `mcp_tool_catalog()`
- `mcp_tool_definition_to_dict(definition)`
- `run_mcp_tool(name, **kwargs)`
- `run_mcp_tool_to_dict(name, **kwargs)`
- `create_mcp_server()`
- `run_mcp_server(...)`

## Minimal Examples

End-to-end pipeline:

```python
import cellpaint_pipeline as cp

config = cp.ProjectConfig.from_json(
    "/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json"
)
result = cp.run_end_to_end_pipeline(config)
print(result.output_dir)
```

Skill execution:

```python
result = cp.run_pipeline_skill(config, "run-full-workflow")
print(result.manifest_path)
```

Data-access planning:

```python
request = cp.build_data_request(
    mode="gallery-source",
    dataset_id="cpg0016-jump",
    source_id="source_4",
    subprefix="workspace",
    dry_run=True,
)
plan = cp.build_download_plan(config, request)
print(cp.data_download_plan_to_dict(plan))
```

MCP tool discovery:

```python
import cellpaint_pipeline as cp

for tool_name in cp.available_mcp_tools():
    print(tool_name)
```
