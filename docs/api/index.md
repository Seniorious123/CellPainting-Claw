# API

This section documents the **Python-side public interfaces** exposed by CellPainting-Claw.

The API section is focused on the main toolkit entrypoints exposed through `cellpainting_claw`. The task-oriented `Skills` layer and the shell-facing `CLI` are documented as separate top-level sections.

## Main Public Access Paths

CellPainting-Claw currently exposes four main access paths:

- the main Python package `cellpainting_claw`
- the task-oriented Python package `cellpainting_skills`
- the command-line interfaces `cellpainting-claw` and `cellpainting-skills`
- the MCP surface used by OpenClaw and other agent-facing clients

## What This API Section Covers

This section focuses on the main Python toolkit surface, especially:

- `ProjectConfig`
- public Python entrypoints
- related public helpers exposed by the main package

For the task-oriented layer, continue to [Skills](../skills/index.md).

For shell-facing usage, continue to [CLI](../cli/index.md).

## Page Guide

### Public Entrypoints

This page documents the most important Python entrypoints exposed by `cellpainting_claw`.

Use it when you want to understand the canonical Python toolkit surface.

## Relationship To Other Sections

The Python API, Skills layer, CLI, and MCP tooling all expose related parts of the same toolkit, but they are documented separately so each interface can be learned in the form users actually encounter.

```{toctree}
:maxdepth: 1

public_entrypoints
```
