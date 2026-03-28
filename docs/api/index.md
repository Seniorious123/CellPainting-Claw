# API

This section documents the **public interfaces** exposed by CellPainting-Claw.

The repository exposes **four public access layers**:

- the main Python package `cellpainting_claw`
- the task-oriented Python package `cellpainting_skills`
- the public command-line interfaces `cellpainting-claw` and `cellpainting-skills`
- the MCP surface used by OpenClaw and other agent-facing clients

## Public Surface Priorities

Not every interface has the same role.

The intended public hierarchy is:

1. use the **main Python API** when you want direct library control
2. use the **main CLI** when you want explicit shell execution
3. use the **skills layer** when stable task names are more useful than raw parameter bundles
4. use the **MCP and OpenClaw path** when you want agent-mediated or natural-language execution

This distinction matters for rigor:

- the **Python API** and the **main CLI** are the canonical execution surfaces
- the **skills layer** is a stable task-routing layer on top of the canonical workflow
- the **MCP surface** exposes the same library for automation systems
- **OpenClaw** is an optional agent front end, not a separate workflow implementation

## What This API Section Covers

- **Public Entrypoints**: the stable top-level Python entrypoints
- **Skills**: the task-oriented layer and its stable skill names
- **Command-Line Interface**: the shell-facing and MCP-facing command surfaces

For the OpenClaw runtime itself, see the dedicated OpenClaw section of the documentation.

## How To Read This Section

For most readers, the best order is:

1. public entrypoints
2. skills
3. command-line interface

That order keeps the API reference centered on **stable public behavior** instead of internal modules.

```{toctree}
:maxdepth: 1

public_entrypoints
skills
cli
```
