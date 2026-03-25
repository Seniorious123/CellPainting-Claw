# Library Design

## Goal

`CellPainting-Claw` is not meant to be another loose collection of scripts. Its role is to turn the validated Cell Painting workflow into a reusable software interface.

The practical goals are:

1. Stabilize the main raw-image-to-pycytominer path.
2. Bring segmentation, single-cell crops, previews, and DeepProfiler exports under the same interface.
3. Expose a clean contract for future automation layers such as MCP, NanoBot, and OpenClaw.

## Why a Separate Parallel Directory

The library lives in its own directory instead of being merged into `pycytominer_mvp` or `pycytominer_post_mvp` because those trees are primarily experiment and output workspaces.

The library needs to emphasize:

- stable interfaces
- configuration-driven execution
- documentation
- testability
- release hygiene

## First-Stage Design Rule

The first stage does not rewrite the validated algorithms.

Instead, the library uses a wrapper architecture:

- the library owns configuration, orchestration, parameter validation, output organization, and agent-facing surfaces
- the validated backend workspaces still execute the heavy workflow steps

This lowers risk while still giving the project a stable top-level interface.

## Layer Model

The library distinguishes several layers:

- `config`
  Loads project configuration and validates runtime contracts.
- `delivery`
  Exposes high-level suites that are easy for users and automation systems to call.
- `orchestration`
  Coordinates multi-stage runs such as end-to-end execution.
- `workflows`
  Maps validated backend scripts to stable workflow keys.
- `adapters`
  Converts workflow outputs into downstream formats such as DeepProfiler input packages.
- `data_access`
  Handles discovery, planning, and controlled download execution.
- `mcp_tools` and `mcp_server`
  Expose the stable library surface to agent systems.

## DeepProfiler Positioning

DeepProfiler is treated as an adapter and integration branch, not as the structure that defines the rest of the project.

The intended order is:

1. stabilize the main workflow library
2. standardize the DeepProfiler bridge
3. let agents call both through the same public contract

This keeps the core library valuable even if the downstream embedding branch evolves independently.

## Public Entry Hierarchy

The preferred public entry hierarchy is:

1. `run_end_to_end_pipeline`
2. `run_pipeline_skill`
3. `run_pipeline_preset`
4. `run_deepprofiler_pipeline`

Lower-level workflow helpers remain importable, but they are not the first choice for release-facing usage.

## Output Philosophy

The library keeps the validated output formats from the backend workspaces.

That means:

- pycytominer outputs stay aligned with the validated profiling backend
- segmentation outputs still include masks, outlines, single-cell crops, and previews where enabled
- DeepProfiler export packages are standardized wrappers around the validated segmentation outputs

## Why This Makes Agent Integration Easier

Once configuration, entrypoints, and output contracts are stable, an agent does not need to understand the full internal workflow tree.

It can operate against:

- a fixed set of public API names
- a fixed set of MCP tools
- predictable output directories and manifests

That is the core reason the library exists.
