# Quick Start

This page shows the shortest practical path from an installed CellPainting-Claw checkout to a first workflow run.

## 1. Choose a Configuration Template

The repository currently includes two config examples:

- `configs/project_config.portable.example.json` as the recommended starting point for a new machine or a new deployment
- `configs/project_config.example.json` as a repository-local validation example

For most users, start from the portable template and edit it for your environment.

For the commands below, it is convenient to define one config variable first:

```bash
CONFIG=configs/project_config.portable.example.json
```

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
cellpainting-claw show-config --config "$CONFIG"
```

This is the fastest way to catch bad paths, missing files, or an incorrect Python interpreter before starting a workflow run.

## 4. Run a Lightweight Check

A first low-risk execution step is the built-in smoke test:

```bash
cellpainting-claw smoke-test --config "$CONFIG"
```

Use this step to confirm that the installed package, configuration layer, and basic workflow plumbing are working together.

## 5. Run the Main Workflow Entry Point

Once the configuration is valid, run the top-level orchestration entrypoint:

```bash
cellpainting-claw run-end-to-end-pipeline --config "$CONFIG"
```

This command is the main public entrypoint for the standard workflow surface. Depending on the configuration and flags, it can run the classical profiling branch together with the segmentation branch and, optionally, the DeepProfiler branch.

## 6. Inspect the First Run Outputs

After the first successful run, inspect the generated run root and the orchestration manifest.

At minimum, a standard end-to-end run writes metadata such as:

- `end_to_end_pipeline_manifest.json`
- `run_report.md`
- `validation_report.json` when validation reporting is enabled

For a fuller walkthrough of output structure, branch behavior, and optional data-access steps, continue to [Running the Full Pipeline](../workflows/running_the_full_pipeline.md).

## 7. Optional: Enable the DeepProfiler Branch

If you want the DeepProfiler-oriented segmentation path in the same public entrypoint, add `--deepprofiler-mode`:

```bash
cellpainting-claw run-end-to-end-pipeline   --config "$CONFIG"   --deepprofiler-mode full
```

Use `export` when you only want the standardized DeepProfiler export artifacts, or `full` when you want the DeepProfiler-oriented segmentation suite.

## 8. Optional: Use OpenClaw for Natural-Language Execution

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

## 9. Optional: Explore the Skills Layer

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
