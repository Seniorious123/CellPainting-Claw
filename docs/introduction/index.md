# Introduction

CellPainting-Claw is a workflow library for standardized Cell Painting pipelines from raw image data to analysis-ready outputs. It organizes dataset access, CellProfiler-based segmentation, classical profiling through `pycytominer`, and DeepProfiler-based single-cell feature extraction into one reusable public interface, so the same workflow can be run either through explicit CLI commands or through agent-mediated natural-language requests.

## What The Repository Exposes

The current repository exposes two public Python packages:

- `cellpainting_claw` for the main workflow interface
- `cellpainting_skills` for task-oriented routing and automation-friendly skill names

It also exposes two main public command-line interfaces:

- `cellpainting-claw`
- `cellpainting-skills`

In addition, the repository can expose the same workflow through an MCP server for agent-facing runtimes such as OpenClaw.

## Workflow Structure

The workflow is best understood as one shared upstream stage followed by two downstream analysis branches.

### Shared Upstream Stage

The shared upstream stage starts from raw Cell Painting image data and runs segmentation-oriented processing through CellProfiler and the repository's segmentation wrappers. This stage produces the structured outputs that support both downstream branches, including:

- image-level and object-level measurement tables
- segmentation labels, masks, and outlines
- single-cell localization information
- optional single-cell image crops and preview images

In practical terms, this segmentation backbone is the point where raw microscopy data becomes reusable workflow data.

### Classical Profiling Branch

The first downstream branch is the classical profiling path.

In this branch, CellProfiler-derived single-cell tables are exported into a standardized single-cell table and then processed by `pycytominer`. The main outputs of this branch are feature tables for downstream analysis, including:

- aggregated profiles
- annotated profiles
- normalized profiles
- feature-selected profiles

This is the branch used when the goal is a standard Cell Painting profiling output for conventional downstream analysis.

### DeepProfiler Branch

The second downstream branch is the DeepProfiler path.

In this branch, segmentation results are used to identify and crop individual cells from the source images. Those single-cell image crops are then prepared for DeepProfiler, which produces learned feature representations for each cell.

The main outputs of this branch are per-cell deep feature vectors or embeddings rather than classical profile tables.

## Public Interface Design

CellPainting-Claw is designed around a small set of stable top-level entrypoints. The main package is intended to be the default interface for users who want a reproducible workflow surface, while the skills package provides a narrower layer for automation and agent-style routing.

In practical terms, the repository exposes:

- configuration loading through `ProjectConfig`
- top-level workflow execution through `run_end_to_end_pipeline`
- task-oriented routing through `run_pipeline_skill`
- preset-oriented routing through `run_pipeline_preset`
- a dedicated DeepProfiler branch through `run_deepprofiler_pipeline`
- MCP server and tool wrappers for agent integration

## OpenClaw and Agent Integration

The repository includes an OpenClaw integration surface under `integrations/openclaw/`. In this project, OpenClaw is an agent-facing layer on top of the core library rather than the primary runtime. The Python API and CLI remain the canonical interfaces, while the OpenClaw path exposes the same workflow through MCP and natural-language-oriented agent interaction.

CellPainting-Claw therefore supports two usage styles:

- direct use through Python and the command line
- agent-mediated use through OpenClaw and MCP-compatible tooling

OpenClaw is optional. The core workflow can be used directly without any agent layer.

## Scope and Boundaries

This project is a workflow library and automation surface. It is not a replacement for CellProfiler, pycytominer, or DeepProfiler themselves. Instead, it provides a structured way to configure, invoke, and package those workflow stages through one repository.

The public surface is intentionally release-oriented: it emphasizes stable entrypoints, reusable configuration, and documented automation hooks.

## Where To Go Next

After this introduction, the recommended next pages are:

- [Installation](../installation/index.md) for environment setup
- [Quick Start](../quick_start/index.md) for the shortest first run
- [Workflows](../workflows/index.md) for the shared upstream stage and the two downstream branches
- [API](../api/index.md) for the stable public interfaces
- [OpenClaw](../openclaw/index.md) if you want natural-language or agent-mediated execution
