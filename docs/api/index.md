# API

This section documents the public interfaces exposed by CellPainting-Claw.

The repository exposes three main access layers:

- the main Python package `cellpainting_claw`
- the task-oriented Python package `cellpainting_skills`
- the public command-line interfaces `cellpainting-claw` and `cellpainting-skills`

## How To Read This Section

For most users, the best way to approach the API is:

1. start with the main public entrypoints in `cellpainting_claw`
2. use `cellpainting_skills` when stable task names are more useful than raw orchestration arguments
3. use the CLI pages when you prefer command-line execution or want shell-friendly examples

The API documentation is therefore organized around public usage layers rather than around internal implementation modules.

```{toctree}
:maxdepth: 1

public_entrypoints
skills
cli
```
