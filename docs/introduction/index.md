# Introduction

CellPainting-Claw is a **toolkit interface for practical Cell Painting work**. It is built for the situation where the real work is spread across CellProfiler, pycytominer, DeepProfiler, data-access helpers, backend scripts, and agent runtimes, but the user still needs one understandable interface.

The main idea is simple: **the same toolkit should be usable by both people and agents**.

## Why Cell Painting Tooling Is Hard To Use

In practice, Cell Painting work is often difficult to standardize because:

- data access, segmentation, profiling, and deep-feature extraction live in different packages
- many working implementations are script collections rather than clean public APIs
- one user may want direct low-level tools, while another may want named tasks
- agent runtimes need stable entrypoints instead of ad hoc shell procedures

CellPainting-Claw provides a stable interface layer across those tool families.

## Two Public Packages

### `cellpainting_claw`

`cellpainting_claw` is the **main toolkit package**.

It is the package to use when you want:

- one Python API for the main Cell Painting tasks
- the main CLI and config contract
- data-access helpers
- profiling and segmentation tools
- DeepProfiler preparation helpers
- public CellProfiler `.cppipe` inspection and validation helpers
- MCP serving for agent runtimes

In short, import `cellpainting_claw` when you want the **broad toolkit layer**.

### `cellpainting_skills`

`cellpainting_skills` is the **agent- and automation-facing task package**.

It is the package to use when you want:

- stable skill names
- a simple task layer above the lower-level toolkit
- natural-language or scripted requests to resolve to validated toolkit actions
- a narrower public surface for OpenClaw, MCP clients, and other agents

In short, import `cellpainting_skills` when you want the **named-task layer** of the project.

## Integrated Layers In The Stack

CellPainting-Claw spans several layers of a practical Cell Painting stack. They should be read in order from data access to execution surface.

| Layer | Packages or tools | What this layer does |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | finds datasets, prepares access plans, and supports download steps |
| Classical processing | `CellProfiler` | runs segmentation, mask generation, outlines, and measurement export |
| Classical profiling | `pycytominer` | converts CellProfiler-derived single-cell tables into normalized and selected profile outputs |
| Deep learning feature extraction | `DeepProfiler` | generates learned single-cell features from segmentation-guided crops |
| Task interface | `cellpainting_skills`, MCP tools | exposes stable named tasks on top of the lower-level toolkit layers |
| Agent runtime | `OpenClaw` | provides an optional natural-language runtime on top of the toolkit and task layers |

## Skills Matter In This Project

The central public idea of the repository is a **toolkit plus a stable skill layer**.

Skills matter because they provide:

- stable task names for users and agents
- a simpler surface than raw command families
- a reproducible interface that still maps to the validated backend work

This is why the project keeps both the main package and the skills package:

- `cellpainting_claw` exposes the broad tool surface
- `cellpainting_skills` exposes the task surface

## Tool Families Instead Of One Fixed Route

CellPainting-Claw exposes several major capability groups:

- data-access planning
- classical profiling
- segmentation-derived outputs
- DeepProfiler preparation and execution support
- agent-facing execution through MCP and OpenClaw

These are **tool families** that can be used independently or combined through skills, presets, or higher-level runs.

## CellProfiler `.cppipe` Support

The toolkit also exposes a **public CellProfiler `.cppipe` configuration layer**.

This means users can:

- choose bundled `.cppipe` templates
- inspect which `.cppipe` a config will use
- validate the selection before running a longer task
- provide a custom `.cppipe` override path when needed

Current phase-1 scope is intentionally clear:

- **segmentation** consumes the configured `.cppipe` selection at runtime
- **profiling** exposes the same selection and validation helpers, while the public profiling route remains post-CellProfiler-oriented

## Scope

CellPainting-Claw is a **toolkit and interface layer**.

It is **not** a replacement for:

- CellProfiler
- pycytominer
- DeepProfiler

Its role is to make those tool families easier to configure, invoke, package, and expose through a stable public surface.

## Where To Go Next

After this page, the most useful next pages are:

- [Quick Start](../quick_start/index.md)
- [Skills](../skills/index.md)
- [API](../api/index.md)
- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
