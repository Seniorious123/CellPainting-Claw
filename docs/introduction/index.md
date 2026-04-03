# Introduction

CellPainting-Claw is a **tool library for Cell Painting analysis**. It brings together the steps that are often difficult to call consistently in practice: **data access planning**, **classical profiling with pycytominer outputs**, **segmentation-derived single-cell exports**, and **DeepProfiler-ready preparation**.

The library is intended to be usable by both **human users** and **agents** through the same public interface.

## At a Glance

CellPainting-Claw provides:

- **a reusable Cell Painting toolkit** for data access, profiling, segmentation-derived outputs, and DeepProfiler preparation
- **two public Python packages**: `cellpainting_claw` and `cellpainting_skills`
- **two main command-line interfaces**: `cellpainting-claw` and `cellpainting-skills`
- **an agent-facing execution path** through MCP and OpenClaw

## Main Interfaces

The repository exposes **two main public Python packages**.

### `cellpainting_claw`

`cellpainting_claw` is the **main toolkit interface**.

Use it when you want:

- direct Python entrypoints
- the main command-line interface
- access to data-access, profiling, segmentation, and DeepProfiler preparation tools
- the MCP server surface used by agent runtimes

### `cellpainting_skills`

`cellpainting_skills` is the **task-oriented interface**.

Use it when you want:

- stable task names
- automation-friendly routing
- a cleaner bridge between user requests and concrete tool execution
- a task layer that is easier for agents and orchestration systems to call

## Integrated Tool Families

CellPainting-Claw works with the main tool families commonly used in practical Cell Painting analysis:

- **CellProfiler** for segmentation, object localization, masks, outlines, and classical measurement export
- **pycytominer** for profile generation from single-cell measurement tables
- **DeepProfiler** for learned single-cell feature extraction from segmentation-guided crops
- **Cell Painting Gallery / JUMP-style data-access helpers** such as `boto3`, `quilt3`, and `cpgdata` for dataset discovery and download planning
- **OpenClaw and MCP-facing execution surfaces** for agent-mediated and natural-language task execution

## What You Can Do With It

At a high level, CellPainting-Claw supports four main capability groups:

- **data access planning** for Cell Painting Gallery and JUMP-style sources
- **classical profiling** that converts CellProfiler-derived tables into pycytominer outputs
- **segmentation-derived exports** such as masks, previews, and single-cell crops
- **DeepProfiler-oriented preparation** for learned single-cell feature extraction workflows

These capabilities are exposed through one documented interface layer rather than through separate script collections.

## Skills And Agent Use

`cellpainting_skills` provides stable task names such as profiling, segmentation, DeepProfiler export, and full-run execution. This makes the library easier to call from:

- shell scripts
- higher-level automation
- MCP-compatible systems
- natural-language agent runtimes

The skills layer uses the same underlying toolkit as the Python API and CLI. It is a task-oriented interface, not a separate backend.

## OpenClaw

The repository includes an OpenClaw integration surface under `integrations/openclaw/`.

OpenClaw is an **optional agent-facing layer** on top of the core library. The Python API and CLI remain the canonical interfaces, while the OpenClaw path exposes the same toolkit through MCP and natural-language-oriented interaction.

You can therefore use CellPainting-Claw in two main ways:

- directly through Python and the command line
- through OpenClaw and other MCP-compatible agent tooling

## Scope

CellPainting-Claw is a **tool library and interface layer**. It is **not a replacement for CellProfiler, pycytominer, or DeepProfiler themselves**.

Its role is to provide a structured way to configure, invoke, and package those tool families through one repository.

## Where To Go Next

After this introduction, the recommended next pages are:

- [Installation](../installation/index.md) for environment setup
- [Quick Start](../quick_start/index.md) for the shortest first run
- [API](../api/index.md) for the public Python, CLI, and skills interfaces
- [OpenClaw](../openclaw/index.md) if you want natural-language or agent-mediated execution
