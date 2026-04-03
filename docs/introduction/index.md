# Introduction

CellPainting-Claw is a **tool library for Cell Painting analysis**. In practice, Cell Painting work is often difficult to reuse because the relevant steps are spread across backend scripts, separate tools, inconsistent command styles, and environment-specific wrappers. This repository provides a cleaner public interface for the tasks that are usually hard to call consistently: **data access planning**, **classical profiling with pycytominer outputs**, **segmentation-derived single-cell exports**, and **DeepProfiler-ready preparation**.

The same repository is designed to work for both **human users** and **agents**.

## At a Glance

The main ideas of the project are:

- **One toolkit, not one fixed execution route**: the repository exposes reusable tools and skills rather than forcing every user through one linear path.
- **Two public packages**: `cellpainting_claw` is the main library and CLI surface, while `cellpainting_skills` provides stable task-oriented execution.
- **One integration layer over several underlying tools**: CellPainting-Claw organizes CellProfiler, pycytominer, DeepProfiler, and data-access helpers behind a more consistent interface.
- **Two usage styles**: the same capabilities can be called directly through Python and the CLI, or through an agent-facing surface such as MCP and OpenClaw.

## What The Repository Exposes

The repository exposes **two main public Python packages**:

- `cellpainting_claw` for the main toolkit interface
- `cellpainting_skills` for stable task names and automation-friendly routing

It also exposes **two main public command-line interfaces**:

- `cellpainting-claw`
- `cellpainting-skills`

In addition, the same toolkit can be exposed through an **MCP server** for **agent-facing runtimes** such as OpenClaw.

## What CellPainting-Claw Integrates

CellPainting-Claw does not try to replace the existing Cell Painting ecosystem. Instead, it provides a structured way to use the main tool families together.

The current repository integrates or wraps:

- **CellProfiler** for segmentation, object localization, masks, outlines, and classical measurement export
- **pycytominer** for classical profile generation from single-cell measurement tables
- **DeepProfiler** for learned single-cell feature extraction from segmentation-guided crops
- **Cell Painting Gallery / JUMP-style data-access helpers** such as `boto3`, `quilt3`, and `cpgdata` for dataset discovery and download planning
- **OpenClaw and MCP-facing execution surfaces** for agent-mediated and natural-language task execution

## Main Packages

### `cellpainting_claw`

`cellpainting_claw` is the **main public toolkit interface**.

Use it when you want:

- direct Python entrypoints
- the main command-line interface
- access to segmentation, profiling, DeepProfiler, and data-access tools
- the MCP server surface used by agent runtimes

In practical terms, `cellpainting_claw` is the package that brings the underlying tools together into one reusable interface layer.

### `cellpainting_skills`

`cellpainting_skills` is the **skills layer** of the toolkit.

Use it when you want:

- stable task names
- automation-friendly task routing
- a cleaner bridge between user requests and concrete tool execution
- a task layer that is easier for agents and orchestration systems to call

In practical terms, `cellpainting_skills` does not replace the underlying tools. It organizes them into named capabilities that are easier to automate and document.

## How The Toolkit Is Organized

At a high level, CellPainting-Claw covers four main capability groups:

- **data access planning** for Cell Painting Gallery and JUMP-style sources
- **classical profiling** that converts CellProfiler-derived tables into pycytominer outputs
- **segmentation-derived exports** such as masks, previews, and single-cell crops
- **DeepProfiler-oriented preparation** for learned single-cell feature extraction workflows

These are exposed through one public interface layer rather than through separate ad hoc script collections.

## Skills And Agent-Facing Use

A core design goal of this project is to make the toolkit easier to call at the **task level**.

That is why the repository includes `cellpainting_skills`: it defines stable task names such as profiling, segmentation, DeepProfiler export, and full-workflow runs. This makes the library easier to use from:

- shell scripts
- higher-level automation
- MCP-compatible systems
- natural-language agent runtimes

The **skills layer is not a separate backend**. It is a standardized interface over the same underlying toolkit.

## OpenClaw And Natural-Language Execution

The repository includes an OpenClaw integration surface under `integrations/openclaw/`.

In this project, OpenClaw is an **optional agent-facing layer on top of the core library**. The Python API and CLI remain the canonical interfaces, while the OpenClaw path exposes the same toolkit through MCP and natural-language-oriented interaction.

CellPainting-Claw therefore supports **two usage styles**:

- direct use through Python and the command line
- agent-mediated use through OpenClaw and MCP-compatible tooling

**OpenClaw is optional.** The core toolkit can be used directly without any agent runtime.

## Scope And Boundaries

CellPainting-Claw is a **tool library and interface layer**. It is **not a replacement for CellProfiler, pycytominer, or DeepProfiler themselves**.

Instead, it provides a structured way to configure, invoke, and package those tool families through one repository.

The public interface emphasizes:

- **stable entrypoints**
- **reusable configuration**
- **task-oriented skills**
- **documented automation hooks**

## Where To Go Next

After this introduction, the recommended next pages are:

- [Installation](../installation/index.md) for environment setup
- [Quick Start](../quick_start/index.md) for the shortest first run
- [API](../api/index.md) for the public Python, CLI, and skills interfaces
- [OpenClaw](../openclaw/index.md) if you want natural-language or agent-mediated execution
