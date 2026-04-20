# Introduction

CellPainting-Claw was built to solve two practical problems in Cell Painting work: the tooling is often fragmented across many packages and scripts, and it is still awkward to expose that work through agents. This project brings those pieces together behind one documented skill catalog that both people and agents can use.

The main idea is simple: **humans should be able to call the documented skills directly, and agents should be able to call the same skills through natural language**.

## Supported Capabilities

CellPainting-Claw covers several connected parts of practical Cell Painting work.

| Capability | Packages or tools | What it is used for |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | finding datasets and downloading local inputs |
| Measurement extraction | `CellProfiler` | profiling tables, segmentation masks, outlines, and object measurements |
| Classical profile generation | `pycytominer` | normalization, feature selection, and profile generation from single-cell tables |
| Deep feature extraction | `DeepProfiler` | learned features from segmentation-guided single-cell crops |

These capabilities are presented in the same order that many users encounter them in practice: **get data, extract measurements, build classical profiles, and optionally build deep features**.

## Interfaces

For most users, CellPainting-Claw should be understood through **two main usage paths**.

### Direct Skills

The main human-facing starting point is `cellpainting_skills`.

Use it when you want to:

- call the documented skills directly from Python or from the CLI
- run clear tasks such as segmentation, classical profiling, or DeepProfiler-related tasks
- work from stable task names instead of assembling lower-level helpers yourself

In short, this is the right starting point when you want to **use the documented skills directly**.

### OpenClaw

OpenClaw is the **natural-language entry point**.

Use it when you want to:

- describe a task in natural language
- let an agent route that request to the right documented skill
- use the same skill catalog through a chat-style interface

In short, this is the right starting point when you want to **use the same skills through an agent**.

### Advanced Toolkit Access

The lower-level `cellpainting_claw` package remains available for advanced direct toolkit access, including direct configuration inspection, lower-level toolkit commands, and MCP serving. It is still part of the project, but it is not the main starting point for most users.

## Public Skills

The public skill catalog is organized around concrete outputs rather than one fixed end-to-end route.

Each skill is meant to do **one practical piece of work** and leave behind a result that later skills, scripts, or agent requests can reuse.

| Skill family | Public skills | What they produce |
| --- | --- | --- |
| Data access | `inspect-cellpainting-data`, `download-cellpainting-data` | discovery summaries and local dataset downloads |
| Profiling | `run-cellprofiler-profiling`, `export-single-cell-measurements`, `run-pycytominer`, `summarize-classical-profiles` | CellProfiler tables, single-cell tables, classical profiles, and readable profile summaries |
| Segmentation | `run-segmentation-masks`, `export-single-cell-crops` | masks, previews, and crop exports |
| DeepProfiler | `prepare-deepprofiler-project`, `run-deepprofiler`, `summarize-deepprofiler-profiles` | runnable DeepProfiler projects, collected feature tables, and readable DeepProfiler summaries |

## `.cppipe`

The project also exposes a **public CellProfiler `.cppipe` configuration interface**.

This means users can:

- choose bundled `.cppipe` templates
- inspect which `.cppipe` a config will use
- validate that selection before running a longer job
- provide a custom `.cppipe` override path when needed

Current scope is intentionally clear:

- **profiling** and **segmentation** both use bundled or custom CellProfiler `.cppipe` assets
- normal users can rely on the bundled defaults
- advanced users can inspect or override the selected `.cppipe` when needed

## Boundaries

CellPainting-Claw is a **toolkit and interface project**.

It does **not** replace:

- CellProfiler
- pycytominer
- DeepProfiler

Its role is to make those tools easier to configure, run, and expose through a stable public interface.

## Next Steps

After this page, the most useful next pages are:

- [Skills](../skills/index.md)
- [Quick Start](../quick_start/index.md)
- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
