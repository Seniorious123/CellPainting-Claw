# CellPainting-Claw

CellPainting-Claw is a **Cell Painting toolkit** that packages commonly used analysis components behind a more consistent interface for both **human users** and **agent runtimes**.

Instead of asking users to work directly across scattered scripts, backend-specific wrappers, and tool-specific command conventions, this project exposes a cleaner public surface for **data access**, **segmentation**, **classical profiling**, **deep feature extraction**, and **agent-facing execution**.

## Supported Packages

CellPainting-Claw currently integrates or wraps the following core packages and tool families:

- **CellProfiler** for segmentation, object measurements, masks, outlines, and single-cell localization outputs
- **pycytominer** for classical Cell Painting profile generation from single-cell measurement tables
- **DeepProfiler** for learned single-cell feature extraction from segmentation-guided crops
- **cpgdata**, **quilt3**, **boto3**, and related data-access tooling for dataset discovery and download planning
- **OpenClaw** through an MCP-facing integration layer for agent-mediated and natural-language execution

## Main Packages

The repository exposes **two main public Python packages**.

### `cellpainting_claw`

`cellpainting_claw` is the **main toolkit interface**.

It is the package you use when you want:

- direct Python entrypoints
- the main command-line interface
- access to segmentation, profiling, DeepProfiler, and data-access tools
- the MCP server surface used by agent runtimes

In practical terms, `cellpainting_claw` is the package that brings the underlying tools together into one reusable interface layer.

### `cellpainting_skills`

`cellpainting_skills` is the **skills layer** of the toolkit.

It is the package you use when you want:

- stable task names
- automation-friendly task routing
- a cleaner interface for scripting and agent use
- a bridge between natural-language requests and concrete tool execution

In practical terms, `cellpainting_skills` does not replace the underlying tools. It organizes them into higher-level named capabilities that are easier for both users and agents to call.

## What The Repository Includes

At the public interface level, the repository includes:

- the **`cellpainting_claw` Python package**
- the **`cellpainting_skills` Python package**
- the **`cellpainting-claw` CLI**
- the **`cellpainting-skills` CLI**
- an **MCP server surface** for agent-facing runtimes
- an **OpenClaw integration path** for natural-language execution

Together, these components make the project usable in several styles:

- as a Python toolkit
- as a command-line toolkit
- as a skills-oriented automation layer
- as an agent-accessible tool surface

```{toctree}
:maxdepth: 2
:caption: Introduction
:hidden:

introduction/index
```

```{toctree}
:maxdepth: 2
:caption: Installation
:hidden:

installation/index
```

```{toctree}
:maxdepth: 2
:caption: Quick Start
:hidden:

quick_start/index
```

```{toctree}
:maxdepth: 2
:caption: Workflows
:hidden:

workflows/index
```

```{toctree}
:maxdepth: 2
:caption: API
:hidden:

api/index
```

```{toctree}
:maxdepth: 2
:caption: OpenClaw
:hidden:

openclaw/index
```
