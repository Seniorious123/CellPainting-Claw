# Running the Full Pipeline

This page shows the practical end-to-end command sequence for the main public workflow surface.

The standard high-level entrypoint is:

- `cellpainting-claw run-end-to-end-pipeline --config ...`

In one run directory, this command can coordinate:

- configuration-backed execution
- optional data-access inspection and download planning
- the classical profiling branch
- the segmentation branch
- optional DeepProfiler export or full DeepProfiler execution
- validation report collection

## Before You Start

This page assumes that you already have:

- an installed CellPainting-Claw environment
- a project config JSON file
- the validated backend roots and output paths filled in for your machine

If not, start with the earlier installation and quick start pages first.

## 1. Define the Core Run Variables

Most users should start from the portable config template and define one output directory for the run:

```bash
CONFIG=configs/project_config.portable.example.json
OUTPUT=runs/end_to_end_standard
```

If you maintain your own runtime-specific config, substitute that path in the commands below.

## 2. Inspect the Resolved Configuration

Before running anything expensive, inspect the resolved config:

```bash
cellpainting-claw show-config --config "$CONFIG"
```

This is the fastest way to catch missing paths, wrong interpreter settings, or backend roots that still point at placeholder values.

## 3. Run a Lightweight Smoke Test

Use the smoke test before a first real run on a new machine:

```bash
cellpainting-claw smoke-test --config "$CONFIG"
```

This does not replace a real workflow run, but it is a cheap way to verify that the public CLI, the config loader, and the packaged delivery layer are wired together correctly.

## 4. Optional: Inspect or Plan Data Access

If your workflow also needs dataset discovery or download planning, inspect the resolved data-access layer first:

```bash
cellpainting-claw show-data-access --config "$CONFIG"
cellpainting-claw check-data-access --config "$CONFIG"
cellpainting-claw summarize-data-access --config "$CONFIG"
```

When you want a reusable transfer plan before the workflow run, create it explicitly:

```bash
cellpainting-claw plan-data-access   --config "$CONFIG"   --dataset-id YOUR_DATASET_ID   --source-id YOUR_SOURCE_ID   --output-path runs/download_plan.json
```

Then execute that saved plan:

```bash
cellpainting-claw execute-download-plan   --config "$CONFIG"   --plan-path runs/download_plan.json
```

These steps are optional. If your data is already available locally, move directly to the workflow run itself.

## 5. Run the Standard End-to-End Workflow

The minimal full workflow command is:

```bash
cellpainting-claw run-end-to-end-pipeline   --config "$CONFIG"   --output-dir "$OUTPUT"
```

By default, this orchestration run includes:

- the configured profiling suite
- the configured segmentation suite
- a manifest and run report under the selected output directory
- a validation report unless you disable it

The command prints a JSON summary to standard output and also writes persistent run metadata into the run directory.

## 6. Understand What This Run Produces

A standard orchestration run writes a small set of top-level orchestration artifacts together with branch-specific subdirectories.

At the run root, the main files are:

- `end_to_end_pipeline_manifest.json`
- `run_report.md`
- `validation_report.json` when validation reporting is enabled

Depending on the selected options, the run root can also contain:

- `data_access_summary.json`
- `download_plan.json`
- `download_execution.json`
- `profiling/`
- `segmentation/`

The profiling branch writes its own manifest under `profiling/`, and the segmentation branch writes its own manifest under `segmentation/`.

## 7. Inspect the Output Directory

After a successful run, inspect the run root first:

```bash
ls "$OUTPUT"
```

Then inspect the orchestration manifest directly if you want the machine-readable summary of what ran:

```bash
cat "$OUTPUT/end_to_end_pipeline_manifest.json"
```

This is usually the fastest way to confirm which stages ran, which suite names were selected, and where the branch-specific outputs were written.

## 8. Include a Data-Access Summary or Download Step in the Same Run

If you want the orchestration layer itself to write a data summary or execute a download plan as part of the same run, add the relevant flags:

```bash
cellpainting-claw run-end-to-end-pipeline   --config "$CONFIG"   --output-dir runs/end_to_end_with_data   --include-data-access-summary   --plan-data-download   --dataset-id YOUR_DATASET_ID   --source-id YOUR_SOURCE_ID
```

To execute the planned download step in the same orchestration run, add:

```bash
  --execute-data-download-step
```

Use this integrated path when you want one run root to contain both workflow artifacts and the data-access planning metadata that produced them.

## 9. Enable the DeepProfiler Branch

The top-level orchestration entrypoint also supports the DeepProfiler branch through `--deepprofiler-mode`.

The available modes are:

- `off` for the standard workflow
- `export` to produce the standardized DeepProfiler export artifacts
- `full` to run the DeepProfiler-oriented segmentation suite

A typical DeepProfiler-oriented run looks like this:

```bash
cellpainting-claw run-end-to-end-pipeline   --config "$CONFIG"   --output-dir runs/end_to_end_deepprofiler   --deepprofiler-mode full
```

If you want the DeepProfiler branch without running the classical profiling branch in the same orchestration call, you can make that explicit:

```bash
cellpainting-claw run-end-to-end-pipeline   --config "$CONFIG"   --output-dir runs/end_to_end_deepprofiler_only   --skip-profiling   --deepprofiler-mode full
```

When `--deepprofiler-mode` is not `off`, the orchestration layer switches the segmentation side into the DeepProfiler-oriented segmentation suite automatically.

## 10. Run the Same Workflow Through OpenClaw

The CLI remains the canonical interface, but the same library can also be exposed to an agent through MCP and OpenClaw.

At the library level, the MCP server entrypoint is:

```bash
cellpainting-claw serve-mcp   --transport streamable-http   --host 127.0.0.1   --port 8768   --path /mcp
```

In practice, most users should use the repository integration wrappers under `integrations/openclaw/` rather than launching OpenClaw manually. On AutoDL-like hosts, the usual path is:

```bash
cd integrations/openclaw/autodl
./run_openclaw_gateway.sh
./run_openclaw_tui.sh
```

That path gives you a natural-language front end, while the library continues to provide the stable workflow, CLI, public API, and MCP surfaces underneath.

## When To Drop Down to Lower-Level Commands

Use `run-end-to-end-pipeline` when you want one stable top-level execution surface.

Drop down to narrower entrypoints only when you already know you want one branch directly, for example:

- `run-profiling-suite`
- `run-segmentation-suite`
- `run-workflow`
- `run-deepprofiler-pipeline`
