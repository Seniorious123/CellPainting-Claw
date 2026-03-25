# FAQ

## Why are there two public names?

`CellPainting-Claw` is the main project and package distribution. `CellPainting-Skills` is the skill-oriented layer for automation and agent-facing task routing.

## Does the project require an environment named `lyx_env`?

No. The release-facing configuration no longer requires that environment name. Local users can still run the project from any working environment as long as the configured Python interpreter and required dependencies are available.

## Is Read the Docs the runtime environment for the pipeline?

No. Read the Docs is only the hosted documentation build and publishing platform. It does not run the Cell Painting pipeline itself.

## Do I need NanoBot or OpenClaw to use the library?

No. They are optional integration layers. The project can be used directly through the Python API and CLI without any agent framework.
