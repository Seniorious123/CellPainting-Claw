# Introduction

CellPainting-Claw brings together the fragmented tools used in **Cell Painting work** into one skill-driven interface. Instead of asking users to piece together data access, CellProfiler workflows, pycytominer profiling, DeepProfiler preparation, and agent tooling by hand, the project lets both humans and agents reach the same documented skills through a clearer public surface.

The main idea is simple: **humans should be able to call the documented skills directly, and agents should be able to call the same skills through natural language**.

## What The Project Brings Together

CellPainting-Claw covers several connected parts of practical Cell Painting work.

| Capability | Packages or tools | What it is used for |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | finding datasets, planning downloads, and preparing local inputs |
| Image processing and measurement export | `CellProfiler` | segmentation, masks, outlines, and single-cell measurement tables |
| Classical profile generation | `pycytominer` | normalization, feature selection, and profile generation from single-cell tables |
| Deep feature extraction | `DeepProfiler` | learned features from segmentation-guided single-cell crops |
| Named task interface | `cellpainting_skills` | stable task names for running common operations without wiring lower-level calls together |
| Natural-language interface | `OpenClaw` | optional natural-language access to the same tasks through OpenClaw |

These parts are presented in the same order that many users will encounter them in real work: **get data, process images, build profiles, optionally build deep features, and optionally expose the workflow to an agent**.

## Two Ways To Use CellPainting-Claw

For most users, CellPainting-Claw should be understood through **two main usage paths**.

### Run The Skills Directly

The main human-facing starting point is `cellpainting_skills`.

Use it when you want to:

- call the documented skills directly from Python or from the CLI
- run clear tasks such as segmentation, classical profiling, or DeepProfiler-related tasks
- work from stable task names instead of assembling lower-level helpers yourself

In short, this is the right starting point when you want to **use the documented skills directly**.

### Run The Same Skills Through OpenClaw

OpenClaw is the **natural-language entry point**.

Use it when you want to:

- describe a task in natural language
- let an agent route that request to the right documented skill
- use the same skill catalog through a chat-style interface

In short, this is the right starting point when you want to **use the same skills through an agent**.

### Advanced Direct Package Use

The lower-level `cellpainting_claw` package remains available for advanced direct package use, including direct configuration inspection, lower-level toolkit commands, and MCP serving. It is still part of the project, but it is not the main starting point for most users.

## What Skills Are For

Skills give users and agents a **small set of named tasks** for common work.

Instead of choosing from many lower-level helpers, users can start from task names such as `plan-data-access`, `run-segmentation`, or `run-deepprofiler`.

This makes the project easier to use in practice:

- a user can choose a task by name
- a script can call the same task repeatedly
- an agent can map a natural-language request onto a stable task name

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
