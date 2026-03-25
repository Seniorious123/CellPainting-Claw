# Release Quickstart

This document is the shortest path from a clean checkout to a releasable `CellPainting-Claw` package bundle.

## 1. Prepare the Environment

Use the validated Conda environment:

```bash
cd <repo-root>
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
```

If `cellpainting-claw` already exists, reuse it.

## 2. Install the Library

```bash
cd <repo-root>
pip install -e .
```

Optional extras:

```bash
pip install -e .[test]
pip install -e .[mcp]
pip install -e .[data-access,test]
pip install -e .[deepprofiler,test]
```

Use `configs/project_config.portable.example.json` when you need a distribution-friendly starting point.

Keep `configs/project_config.example.json` as the validated machine-local reference.

## 3. Verify the Release Surface

Run the release smoke-test wrapper:

```bash
cd <repo-root>
./scripts/run_release_smoke_test.sh
```

This wrapper performs:

- config parsing through `show-config`
- the lightweight `smoke-test` CLI check
- optional `fast` test-suite execution when `RUN_FAST_TESTS=1`

Default output location:

- `dist/release_smoke/`

## 4. Build the Release Bundle

```bash
cd <repo-root>
./scripts/build_release_bundle.sh
```

Default output location:

- `dist/`

The bundle script creates:

- a staged release directory
- a `tar.gz` archive
- a SHA256 checksum file
- a small JSON manifest summarizing the release contents

## 5. What Is Included

The release bundle is source-oriented. It includes:

- `README.md`
- `CHANGELOG.md`
- `RELEASE_NOTES.md`
- `pyproject.toml`
- `docs/`
- `configs/`
  Includes both a validated local example and a portable distribution template.
- `environment/`
- `src/`
- `tests/`
- `scripts/`
- `release/`
- `integrations/openclaw/`

## 6. What Is Excluded

The bundle intentionally excludes large or machine-local runtime state, including:

- `cache/`
- `exports/`
- `outputs/`
- OpenClaw runtime `state/`
- local provider env files
- local databases and logs
- `__pycache__`
- `*.egg-info`

## 7. Secret Handling

Before publishing or sharing a release:

- do not include provider keys in JSON templates
- do not include `provider.env` or Docker `.env` files
- rotate any key that was previously exposed in shell history, config files, or chat logs

## 8. Recommended Final Check

Immediately before publication:

```bash
cd <repo-root>
./scripts/run_release_smoke_test.sh
./scripts/build_release_bundle.sh
```

Then review the generated files under `dist/`.
