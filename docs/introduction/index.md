# Introduction

CellPainting-Claw is a **toolkit interface for practical Cell Painting work**. It is built for the situation where the real work is spread across CellProfiler, pycytominer, DeepProfiler, data-access helpers, backend scripts, and agent interfaces, but the user still needs one understandable public surface.

The main idea is simple: **the same validated toolkit should be usable by both people and agents**.

## Why Cell Painting Tooling Is Hard To Use

In practice, Cell Painting work is often difficult to standardize because:

- data access, segmentation, profiling, and deep-feature extraction live in different packages
- many working implementations are script collections rather than clean public APIs
- one user may want direct low-level tools, while another may want named tasks
- agent interfaces need stable entrypoints instead of ad hoc shell procedures

CellPainting-Claw provides a stable public interface across those tool families.

## Three Public Interfaces

The project is organized around **three public interfaces**.

### `cellpainting_claw`

`cellpainting_claw` is the **main toolkit package**.

Use it when you want:

- one Python package across data access, processing, and deep-feature extraction
- the main CLI and config contract
- direct access to data-access helpers
- direct access to profiling, segmentation, and DeepProfiler helpers
- public CellProfiler `.cppipe` inspection and validation helpers
- MCP serving for agent-facing integrations

In short, use `cellpainting_claw` when you want the **full toolkit surface**.

### `cellpainting_skills`

`cellpainting_skills` is the **task package**.

Use it when you want:

- stable skill names
- a simpler task interface above the lower-level toolkit
- natural-language or scripted requests to resolve to validated toolkit actions
- a narrower public surface for automation and agent routing

In short, use `cellpainting_skills` when you want the **named-task interface**.

### OpenClaw

OpenClaw is the **agent interface**.

Use it when you want:

- natural-language interaction
- an MCP-connected agent that can trigger toolkit tasks
- a controlled agent interface on top of the same validated toolkit

OpenClaw is optional. It sits on top of `cellpainting_claw`, `cellpainting_skills`, and the MCP interface.

## Main Capabilities In The Toolkit

CellPainting-Claw brings together several main capabilities in a practical Cell Painting toolkit. They are shown here in the order users will usually encounter them.

| Capability | Packages or tools | What this part of the toolkit does |
| --- | --- | --- |
| Data access | `boto3`, `quilt3`, `cpgdata` | finds datasets, prepares access plans, and supports download steps |
| Classical processing | `CellProfiler` | runs segmentation, mask generation, outlines, and measurement export |
| Classical profiling | `pycytominer` | converts CellProfiler-derived single-cell tables into normalized and selected profile outputs |
| Deep learning feature extraction | `DeepProfiler` | generates learned single-cell features from segmentation-guided crops |
| Task interface | `cellpainting_skills`, MCP tools | exposes stable named tasks on top of the lower-level toolkit |
| Agent interface | `OpenClaw` | provides an optional natural-language interface on top of the toolkit and task interfaces |

## Why Skills Matter

The central public idea of the repository is a **toolkit plus a stable skill catalog**.

Skills matter because they provide:

- stable task names for users and agents
- a simpler public surface than raw command families
- a reproducible interface that still maps to the validated backend work

This is why the project keeps both the main package and the task package:

- `cellpainting_claw` exposes the broad toolkit surface
- `cellpainting_skills` exposes the public task surface

## Main Capability Groups

CellPainting-Claw exposes several major capability groups:

- data-access planning
- classical profiling
- segmentation-derived outputs
- DeepProfiler preparation and execution support
- agent-facing execution through MCP and OpenClaw

These capability groups can be used independently or combined through skills, presets, or higher-level runs.

## CellProfiler `.cppipe` Support

The toolkit also exposes a **public CellProfiler `.cppipe` configuration interface**.

This means users can:

- choose bundled `.cppipe` templates
- inspect which `.cppipe` a config will use
- validate the selection before running a longer task
- provide a custom `.cppipe` override path when needed

Current phase-1 scope is intentionally clear:

- **segmentation** consumes the configured `.cppipe` selection at runtime
- **profiling** exposes the same selection and validation helpers, while the public profiling route remains post-CellProfiler-oriented

## Scope

CellPainting-Claw is a **toolkit and interface surface**.

It is **not** a replacement for:

- CellProfiler
- pycytominer
- DeepProfiler

Its role is to make those tool families easier to configure, invoke, package, and expose through a stable public surface.

## Where To Go Next

After this page, the most useful next pages are:

- [Quick Start](../quick_start/index.md)
- [Skills](../skills/index.md)
- [CLI](../cli/index.md)
- [OpenClaw](../openclaw/index.md)
