# Introduction

CellPainting-Claw is a workflow library, command-line interface, and automation surface for standardized Cell Painting analysis. It packages a validated workflow into a cleaner public interface without requiring users to work directly through scattered scripts.

## Overview

The current repository exposes two public Python packages:

- `cellpainting_claw` for the main workflow interface
- `cellpainting_skills` for skill-oriented task routing

It also exposes three command-line entrypoints:

- `cellpainting-claw`
- `cellpainting-skills`
- `cellpainting-claw-tests`

## What CellPainting-Claw Covers

Based on the current repository structure and public API, CellPainting-Claw covers four major areas:

1. data access and download planning
2. profiling and evaluation
3. segmentation and single-cell crop generation
4. DeepProfiler export, project assembly, profiling, and feature collection

## Public Interface Design

CellPainting-Claw is designed around a small set of stable top-level entrypoints. The main package is intended to be the default interface for users who want a reproducible workflow surface, while the skills package provides a narrower layer for automation and agent-style routing.

In practical terms, the repository currently exposes:

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

## Scope and Boundaries

This project is a workflow library and automation surface. It is not a replacement for CellProfiler, pycytominer, or DeepProfiler themselves. Instead, it provides a structured way to configure, invoke, and package those workflow stages through one repository.

The current public surface is intentionally release-oriented: it emphasizes stable entrypoints, reusable configuration, and documented automation hooks.

## Next Step

The next documentation sections will rebuild installation, quick start, workflows, and API reference around this public interface.
