# Quick Start

This page shows the shortest practical path from an installed CellPainting-Claw checkout to a first workflow run.

## 1. Choose a Configuration Template

The repository currently includes two config examples:

- `configs/project_config.portable.example.json` as the recommended starting point for a new machine or a new deployment
- `configs/project_config.example.json` as a repository-local validation example

For most users, start from the portable template and edit it for your environment.

## 2. Fill in the Core Paths

Before running the workflow, make sure the configuration points at real locations on your machine. The most important fields are:

- `python_executable`
- `profiling_backend_root`
- `segmentation_backend_root`
- `workspace_root`
- `default_output_root`
- `deepprofiler_export_root`
- `deepprofiler_project_root`

Those fields determine where the library finds the validated backend assets and where it writes workflow outputs.

## 3. Inspect the Resolved Configuration

Before running anything expensive, check that the configuration resolves correctly:

```bash
cellpainting-claw show-config \
  --config configs/project_config.portable.example.json
```

This is the fastest way to catch bad paths, missing files, or an incorrect Python interpreter before starting a workflow run.

## 4. Run a Lightweight Check

A first low-risk execution step is the built-in smoke test:

```bash
cellpainting-claw smoke-test \
  --config configs/project_config.portable.example.json
```

Use this step to confirm that the installed package, configuration layer, and basic workflow plumbing are working together.

## 5. Run the Main Workflow Entry Point

Once the configuration is valid, run the top-level orchestration entrypoint:

```bash
cellpainting-claw run-end-to-end-pipeline \
  --config configs/project_config.portable.example.json
```

This command is the main public entrypoint for the standard workflow surface. Depending on the configuration and flags, it can run the shared segmentation backbone together with the classical profiling branch and, optionally, the DeepProfiler branch.

## 6. Understand the Two Downstream Branches

After the shared segmentation stage, the workflow can continue in two different directions:

- the classical profiling branch, where CellProfiler-derived tables are processed by `pycytominer` into profile tables
- the DeepProfiler branch, where segmentation-guided single-cell crops are converted into learned feature vectors

The top-level orchestration command is designed to manage this branching through configuration and runtime options rather than forcing users to assemble each step manually.

## 7. Optional: Explore the Skills Layer

If you want a more task-oriented interface, inspect the skills catalog:

```bash
cellpainting-skills list
```

The skills layer is useful for automation and agent-facing routing, but it is not required for normal use of the core workflow.

## What Comes Next

After Quick Start, the next documentation sections move in two directions:

- workflow-oriented pages that explain the shared upstream stage and the two downstream branches in more detail
- API pages that document the public Python and CLI interfaces

This keeps the first reading path practical and task-oriented while still leaving room for a full reference section later in the documentation.
