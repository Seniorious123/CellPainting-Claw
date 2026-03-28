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
cellpainting-claw show-config   --config configs/project_config.portable.example.json
```

This is the fastest way to catch bad paths, missing files, or an incorrect Python interpreter before starting a workflow run.

## 4. Run a Lightweight Check

A first low-risk execution step is the built-in smoke test:

```bash
cellpainting-claw smoke-test   --config configs/project_config.portable.example.json
```

Use this step to confirm that the installed package, configuration layer, and basic workflow plumbing are working together.

## 5. Run the Main Workflow Entry Point

Once the configuration is valid, run the top-level orchestration entrypoint:

```bash
cellpainting-claw run-end-to-end-pipeline   --config configs/project_config.portable.example.json
```

This command is the main public entrypoint for the standard workflow surface. Depending on the configuration and flags, it can run the classical profiling branch together with the segmentation branch and, optionally, the DeepProfiler branch.

## 6. Optional: Enable the DeepProfiler Branch

If you want the DeepProfiler-oriented segmentation path in the same public entrypoint, add `--deepprofiler-mode`:

```bash
cellpainting-claw run-end-to-end-pipeline   --config configs/project_config.portable.example.json   --deepprofiler-mode full
```

Use `export` when you only want the standardized DeepProfiler export artifacts, or `full` when you want the DeepProfiler-oriented segmentation suite.

## 7. Optional: Use OpenClaw for Natural-Language Execution

The workflow can also be exposed to an agent through MCP and OpenClaw.

If you only need the library-provided MCP server, start it directly from the main CLI:

```bash
cellpainting-claw serve-mcp   --transport streamable-http   --host 127.0.0.1   --port 8768   --path /mcp
```

If you want the repository's ready-to-run OpenClaw integration, use the runtime wrappers under `integrations/openclaw/`. For example, on AutoDL-like hosts:

```bash
cd integrations/openclaw/autodl
./run_openclaw_gateway.sh
./run_openclaw_tui.sh
```

This gives you a natural-language front end to the same workflow library. OpenClaw is optional: the core workflow can always be used directly through Python and the CLI.

## 8. Optional: Explore the Skills Layer

If you want a more task-oriented interface, inspect the skills catalog:

```bash
cellpainting-skills list
```

The skills layer is useful for automation and agent-facing routing, but it is not required for normal use of the core workflow.

## What Comes Next

After Quick Start, the next documentation sections move in two directions:

- workflow-oriented pages that explain the shared upstream stage and the two downstream branches in more detail
- API pages that document the public Python, CLI, MCP, and skills interfaces

This keeps the first reading path practical and task-oriented while still leaving room for a full reference section later in the documentation.
