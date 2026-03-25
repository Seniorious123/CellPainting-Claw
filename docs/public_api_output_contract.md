# Public API Output Contract

This document defines which output fields from the stable public API should be treated as canonical.

## Canonical Rule

For public run-style entrypoints, prefer depending on these fields first:

1. `output_dir`
2. `manifest_path`
3. any additional manifest or report path explicitly listed in the output contract helper

Do not treat preview PNG directories, sample visualizations, or other helper images as the primary contract unless an output contract explicitly says so.

## Machine-Readable Helpers

Use these helpers from `cellpainting_claw`:

- `available_public_api_output_contracts()`
- `get_public_api_output_contract(name)`
- `public_api_output_contract_summary()`

These helpers annotate each stable public entrypoint with:

- `output_kind`
- `primary_fields`
- `primary_artifacts`
- `supporting_fields`
- `notes`

## Important Cases

### `run_end_to_end_pipeline`

Canonical top-level artifacts:

- `output_dir`
- `manifest_path`
- `run_report_path`

Optional but formal artifacts when enabled:

- `download_plan_path`
- `download_execution_path`
- `profiling_manifest_path`
- `segmentation_manifest_path`
- `validation_report_path`

Nested preview images, sample PNGs, and similar branch-specific visuals are supporting artifacts under nested workflow roots.

### `run_pipeline_skill` and `run_pipeline_preset`

These reuse the same end-to-end contract as `run_end_to_end_pipeline`.

### `run_deepprofiler_pipeline`

Canonical artifacts:

- `output_dir`
- `manifest_path`
- `export_manifest_path`
- `project_manifest_path`
- `collection_manifest_path`

The collected tables under `collection_output_dir` are the primary DeepProfiler feature outputs.

### `run_profiling_suite` and `run_segmentation_suite`

Canonical artifacts:

- `output_dir`
- `manifest_path`

The exact nested files under those suite roots may vary by workflow key; the suite manifest remains the stable top-level contract.

### data-access planning entrypoints

`build_data_request(...)` and `build_download_plan(...)` primarily return structured objects.
They may contain resolved path fields, but those paths are part of the planned object, not guaranteed already-written files.

`execute_download_plan(...)` is the first data-access public entrypoint that writes formal output artifacts by default.
