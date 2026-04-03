# Quick Start

This page shows the **shortest practical path** from an installed CellPainting-Claw checkout to a **first successful use of the toolkit**.

The goal here is not to run every available component at once. The goal is to confirm that you can:

- use the public CLI
- inspect the skills layer
- run a small bundled demo step
- understand where to go next for Python, skills, or agent-facing use

## 1. Install The Package

From the repository root:

```bash
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
pip install -e .
```

## 2. Use The Bundled Demo Config

For the quickest first run, use the repository's bundled demo config:

```bash
CONFIG=configs/project_config.demo.json
```

This config points at the small demo assets bundled in the repository under `demo/`.

## 3. Confirm The Main CLI Works

A simple first check is to inspect the resolved configuration:

```bash
cellpainting-claw show-config --config "$CONFIG"
```

If this command works, the main package, CLI, and config layer are installed correctly.

## 4. Run One Small Demo Step

Run a lightweight profiling-side validation step on the demo config:

```bash
cellpainting-claw run-profiling \
  --config "$CONFIG" \
  --backend native \
  --script-key validate-inputs
```

This is a small first execution step that confirms the toolkit can find the demo backend inputs and run a real command successfully.

## 5. Inspect The Skills Layer

List the currently available skills:

```bash
cellpainting-skills list
```

If you want details for one skill:

```bash
cellpainting-skills describe --skill run-profiling-workflow
```

## 6. Run One Skill

Run one skill on the same demo config:

```bash
cellpainting-skills run \
  --config "$CONFIG" \
  --skill run-profiling-workflow
```

This is the shortest path to understanding what the skills layer adds on top of the main CLI: stable task names and a more automation-friendly interface.

## 7. Understand The Three Main Entry Styles

After the first successful run, the project can be used in three main ways:

- **main CLI** through `cellpainting-claw`
- **skills CLI** through `cellpainting-skills`
- **Python API** through `cellpainting_claw` and `cellpainting_skills`

A minimal Python example looks like this:

```python
import cellpainting_claw as cp

config = cp.ProjectConfig.from_json("configs/project_config.demo.json")
result = cp.run_pipeline_skill(config, "run-profiling-workflow")
print(result.ok)
```

## 8. Optional: Agent-Facing Use Through OpenClaw

If you want natural-language task execution, the same toolkit can also be exposed through MCP and OpenClaw.

That path is optional and should come **after** the core CLI and skills interfaces are already working.

For OpenClaw-specific setup, continue to [OpenClaw](../openclaw/index.md).

## What To Read Next

After Quick Start, the most useful next pages are:

- [Introduction](../introduction/index.md) for the project scope and interface model
- [API](../api/index.md) for the public Python interfaces
- [OpenClaw](../openclaw/index.md) if you want agent-mediated execution
