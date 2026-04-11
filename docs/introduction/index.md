# Introduction

CellPainting-Claw brings together the main tools used in **Cell Painting work** into one public toolkit. Instead of asking users to piece together data access, CellProfiler workflows, pycytominer profiling, DeepProfiler preparation, and agent tooling by hand, the project provides a clearer way to work across those capabilities.

The main idea is simple: **the same validated work should be usable in three ways, through the main toolkit, through named tasks, and through an agent interface**.

## What The Project Brings Together

CellPainting-Claw covers several connected parts of practical Cell Painting work.

| Capability | Packages or tools | What it is used for |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | finding datasets, planning downloads, and preparing local inputs |
| Image processing and measurement export | `CellProfiler` | segmentation, masks, outlines, and single-cell measurement tables |
| Classical profile generation | `pycytominer` | normalization, feature selection, and profile generation from single-cell tables |
| Deep feature extraction | `DeepProfiler` | learned features from segmentation-guided single-cell crops |
| Named task interface | `cellpainting_skills` | stable task names for running common operations without wiring lower-level calls together |
| Agent interface | `OpenClaw` | optional natural-language access to the same tasks through an agent |

These parts are presented in the same order that many users will encounter them in real work: **get data, process images, build profiles, optionally build deep features, and optionally expose the workflow to an agent**.

## Three Ways To Use The Project

The same toolkit can be used in **three different ways**.

### `cellpainting_claw`

`cellpainting_claw` is the **main toolkit entry point**.

Use it when you want to:

- work directly in Python or from the main CLI
- load and inspect project configuration
- call data-access, segmentation, profiling, and DeepProfiler helpers yourself
- inspect or validate CellProfiler `.cppipe` selection
- control more of the workflow details directly

In short, `cellpainting_claw` is the right starting point when you want to **use the toolkit directly**.

### `cellpainting_skills`

`cellpainting_skills` is the **named-task entry point**.

Use it when you want to:

- call a small set of stable named tasks
- run common operations such as segmentation or DeepProfiler preparation without assembling lower-level helpers yourself
- build scripts or automation around clear task names
- give an agent a cleaner and narrower set of actions to call

In short, `cellpainting_skills` is the right starting point when you want to **run well-defined tasks**.

### OpenClaw

OpenClaw is the **agent entry point**.

Use it when you want to:

- describe a task in natural language
- let an agent decide which task to call
- expose the toolkit through a chat-style interface

OpenClaw is optional. It sits on top of the same validated toolkit and task interfaces rather than replacing them.

## What Skills Are For

Skills give users and agents a **small set of named tasks** for common work.

Instead of choosing from many lower-level helpers, users can start from task names such as `plan-data-access`, `run-segmentation`, or `run-deepprofiler`.

This makes the project easier to use in practice:

- a user can choose a task by name
- a script can call the same task repeatedly
- an agent can map a natural-language request onto a stable task name

The relationship between the two main packages is simple:

- `cellpainting_claw` is the broader toolkit for direct use
- `cellpainting_skills` is the smaller task catalog for named-task use

## CellProfiler `.cppipe` Support

The project also exposes a **public CellProfiler `.cppipe` configuration interface**.

This means users can:

- choose bundled `.cppipe` templates
- inspect which `.cppipe` a config will use
- validate that selection before running a longer job
- provide a custom `.cppipe` override path when needed

Current scope is intentionally clear:

- **segmentation** uses the configured `.cppipe` selection at runtime
- **profiling** exposes the same inspection and validation helpers, while the public profiling route remains centered on the downstream pycytominer step

## Scope

CellPainting-Claw is a **toolkit and interface project**.

It does **not** replace:

- CellProfiler
- pycytominer
- DeepProfiler

Its role is to make those tools easier to configure, run, and expose through a stable public interface.

## Where To Go Next

After this page, the most useful next pages are:

- [Skills](../skills/index.md)
- [Quick Start](../quick_start/index.md)
- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
