# Public API Contract

This document defines the recommended public entrypoints for `cellpaint_pipeline_lib`.

## Goal

Keep the library callable through a small, stable surface while allowing internal workflow, adapter, and runner details to evolve.

## Recommended Public Entry Points

### Entry-Selection Rule

When choosing between the top-level public entrypoints, use this order:

1. `run_end_to_end_pipeline`
   Default choice for most human-driven or service-driven runs.
2. `run_pipeline_skill`
   Prefer for agents, MCP clients, or other automation that should use stable task names.
3. `run_pipeline_preset`
   Prefer when the workflow shape is already known and you want a stable preset key.
4. `run_deepprofiler_pipeline`
   Use only when you are intentionally entering the DeepProfiler branch directly.

The dispatcher `run_public_api_entrypoint(...)` does not replace this ordering. It is a wrapper for automation layers that still need to route into one of the recommended entrypoints above.


### Top-Level Orchestration

- `run_end_to_end_pipeline`
  Purpose: default full Cell Painting pipeline entrypoint.
  Use when: you want one standard run spanning data access, profiling, segmentation, optional DeepProfiler routing, and validation.
  CLI: `run-end-to-end-pipeline`

- `run_pipeline_skill`
  Purpose: named task-oriented entrypoints above presets.
  Use when: an automation layer wants stable task names such as `plan-gallery-data` or `run-full-workflow`.
  CLI: `run-pipeline-skill`

- `run_pipeline_preset`
  Purpose: named orchestration parameter bundles.
  Use when: you know the workflow shape and want a stable preset key instead of raw arguments.
  CLI: `run-pipeline-preset`

- `run_deepprofiler_pipeline`
  Purpose: standardized DeepProfiler branch entrypoint.
  Use when: you already have segmentation outputs or source CSVs and want export, project-build, profile, and collection in one call.
  CLI: `run-deepprofiler-pipeline`

### Data-Access Planning

- `summarize_data_access`
  Purpose: inspect what data-access backends can currently see.
  CLI: `summarize-data-access`

- `build_data_request`
  Purpose: express the desired dataset/source/prefix request in a serializable object.

- `build_download_plan`
  Purpose: convert a request into an explicit plan that can be reviewed or reused.
  CLI: `plan-data-access`

- `execute_download_plan`
  Purpose: execute a previously generated plan.
  CLI: `execute-download-plan`

### Delivery-Level Direct Execution

- `run_profiling_suite`
  Purpose: direct profiling-only execution.
  CLI: `run-profiling-suite`

- `run_segmentation_suite`
  Purpose: direct segmentation-only execution.
  CLI: `run-segmentation-suite`

## Layers That Are Public But Not Preferred As First Choice

These APIs remain public, but they are lower-level than the recommended surface above:

- `run_workflow`
- adapter-level DeepProfiler helpers such as `export_deepprofiler_input`, `build_deepprofiler_project`, `run_deepprofiler_profile`, and `collect_deepprofiler_features`
- data-access serialization helpers such as `write_download_plan` and `load_download_plan`

Use these when you explicitly need lower-level control.

## Internal Layers

The following areas should be treated as internal implementation details, even if they are importable:

- `cellpaint_pipeline.workflows.*` internal branching details
- `cellpaint_pipeline.runner` subprocess plumbing
- adapter internals and helper functions beginning with `_`

These may change to support future packaging, OpenClaw integration, or runtime compatibility work.

## Stability Rule

When adding a new top-level capability, prefer one of these paths:

1. extend an existing public entrypoint
2. add a new public entrypoint here and document it before treating it as stable
3. keep it in lower layers until its input/output contract is clear

## Machine-Readable Contract

The same contract is also exposed in Python through:

- `available_public_api_entrypoints()`
- `get_public_api_entrypoint(name)`
- `public_api_entrypoint_to_dict(entry)`
- `public_api_contract_summary()`
- `recommended_public_api_pathways()`


## Unified Dispatcher

The contract is also executable through one automation-friendly wrapper layer:

- `run_public_api_entrypoint(name, config=None, **kwargs)`
- `run_public_api_entrypoint_to_dict(name, config=None, **kwargs)`

This makes it possible to keep one stable dispatcher while still routing into the recommended public entrypoints above.

CLI equivalents:

- `list-public-api-entrypoints`
- `show-public-api-contract`
- `run-public-api-entrypoint --entrypoint <name> --params-json '{...}'`


## Output Contract

The public API now exposes a second machine-readable layer for result shapes:

- `available_public_api_output_contracts()`
- `get_public_api_output_contract(name)`
- `public_api_output_contract_summary()`

Use these helpers when you need to know which returned fields are the canonical ones to depend on and which path fields represent formal output artifacts.

Current top-level rule:

- `output_dir` and `manifest_path` are canonical for all run-style entrypoints
- `run_report_path` is canonical for standard end-to-end style orchestration outputs
- Preview PNGs, sample images, and other helper visuals are supporting artifacts unless the contract explicitly marks them as primary
- DeepProfiler formal outputs are centered on the export/project/collection manifests and the collected feature tables, not on intermediate temporary directories
