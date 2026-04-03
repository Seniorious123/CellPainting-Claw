# API

This section documents the **public interfaces** exposed by CellPainting-Claw.

The project is intended to be used through a small number of public access paths rather than through internal modules or backend-specific script collections.

## Main Public Access Paths

CellPainting-Claw currently exposes four main access paths:

- the main Python package `cellpainting_claw`
- the task-oriented Python package `cellpainting_skills`
- the command-line interfaces `cellpainting-claw` and `cellpainting-skills`
- the MCP surface used by OpenClaw and other agent-facing clients

## How To Read This Section

For most readers, the most useful order is:

1. **Public Entrypoints** for the main Python toolkit surface
2. **CellPainting-Skills** for the task-oriented interface
3. **Command-Line Interface** for shell-facing execution

That order keeps the API section centered on the public interfaces that users and agents actually call.

## What Each Page Covers

### Public Entrypoints

This page documents the main Python-side entrypoints exposed by `cellpainting_claw`.

Use it when you want to understand the canonical Python toolkit surface.

### CellPainting-Skills

This page documents the task-oriented public layer exposed by `cellpainting_skills`.

Use it when you want to understand:

- what a skill means in this project
- which stable skill keys currently exist
- how the skills layer relates to the lower-level toolkit
- how skills fit into automation and agent-facing execution

### Command-Line Interface

This page documents the public CLI surfaces.

Use it when you want explicit shell commands instead of Python calls.

## Relationship Between The Interfaces

The interfaces are related, but they are not identical.

- `cellpainting_claw` is the **main toolkit surface**
- `cellpainting_skills` is the **task-oriented layer** on top of that toolkit
- the CLI exposes those same capabilities for shell use
- MCP exposes the same library for agent-facing runtimes

OpenClaw is therefore **not a separate workflow implementation**. It is one of the agent-facing ways to use the same underlying public interfaces.

```{toctree}
:maxdepth: 1

public_entrypoints
skills
cli
```
