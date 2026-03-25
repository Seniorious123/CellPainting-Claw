# Read the Docs Guide

This guide describes how to publish the documentation site for `CellPainting-Claw` on Read the Docs.

## What Is Already Configured

The repository already contains the core RTD build files:

- `.readthedocs.yaml`
- `docs/conf.py`
- `docs/requirements.txt`
- the `docs/` content tree with RTD-style section landing pages

Read the Docs should therefore be able to build the site directly from the GitHub repository without relying on the local runtime environment.

## Recommended Publication Flow

1. Push the latest repository changes to GitHub.
2. Sign in to Read the Docs.
3. Import the GitHub repository `Seniorious123/CellPainting-Claw`.
4. Confirm that the default branch is `main`.
5. Trigger the first documentation build.
6. Review the build log for any missing dependency or parsing errors.
7. After the first successful build, enable pull-request or branch preview builds if desired.

## RTD Configuration Used by This Repository

The current RTD build uses:

- Python `3.10`
- Sphinx configured by `docs/conf.py`
- docs dependencies from `docs/requirements.txt`
- editable installation of the package itself via `pip install -e .`

## Expected Outcome

After a successful import and build, Read the Docs will host a documentation site with:

- an introduction section
- installation and getting-started pages
- workflow-oriented documentation pages
- API reference pages for `cellpainting_claw` and `cellpainting_skills`
- release and deployment documentation
- FAQ

## Notes

- Read the Docs is only the hosted documentation platform. It does not execute the Cell Painting pipeline itself.
- The main runtime environment for pipeline execution remains separate from the RTD build environment.
- Because the RTD build runs in its own hosted environment, the repository no longer needs to hard-code a specific local environment name for online documentation publishing.
