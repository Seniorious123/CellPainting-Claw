# Introduction

CellPainting-Claw is a release-oriented software interface for validated Cell Painting workflows.

It exposes a cleaner and more automatable layer over existing profiling, segmentation, evaluation, and DeepProfiler assets without forcing users to rewrite the validated backend workspaces.

## Why This Project Exists

In many Cell Painting projects, the practical workflow is proven but fragmented across scripts, local conventions, and machine-specific execution details. CellPainting-Claw packages that workflow into a cleaner public surface with:

- a Python API for reproducible orchestration
- a CLI for standardized runs
- a skill layer for task-oriented automation
- MCP integration surfaces for agent systems such as NanoBot and OpenClaw

## Public Naming

This project intentionally uses two public names:

- `CellPainting-Claw` is the main project, package distribution, and full workflow interface
- `CellPainting-Skills` is the skill-oriented layer for automation and agent-facing task routing

In practice, that means:

- Python API: `import cellpainting_claw as cp`
- Skill API: `import cellpainting_skills as cps`
- Main CLI: `cellpainting-claw`
- Skill CLI: `cellpainting-skills`

## Next Steps

Continue with the main documentation sections from the left navigation: Installation, Get Started, Workflows, API, Release and Deployment, and FAQ.
