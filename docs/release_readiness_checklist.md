# Release Readiness Checklist

This checklist is for moving `CellPainting-Claw` from a validated internal library to a cleaner release candidate.

## P0: Public Surface

- Confirm the top-level entrypoint order in `README.md` and `docs/public_api_contract.md`.
- Keep `run_end_to_end_pipeline(...)` as the default first choice.
- Keep skill and preset names stable across Python API, CLI, and MCP tools.
- Document canonical outputs for each public entrypoint.

## P0: Configuration Contract

- Keep `configs/project_config.example.json` usable as the reference template.
- Separate required, recommended, and advanced settings in `docs/config_contract.md`.
- Avoid storing provider keys or machine-specific secrets in repository-managed config files.

## P0: Error Reporting

- Prefer actionable configuration errors over raw subprocess failures.
- Preserve workflow key, working directory, and log-path context in failure messages.
- Distinguish configuration errors from retryable runtime failures where possible.

## P1: Validation

- Run `fast` for routine regression checks.
- Run `extended` before publishing or after changing delivery or DeepProfiler paths.
- Keep at least one real lightweight end-to-end smoke path.
- Keep at least one real lightweight segmentation path.
- Keep the DeepProfiler branch continuously verifiable.

## P1: Output Validation

- Check that manifests are written for run-style entrypoints.
- Check that canonical output directories exist.
- Treat previews and sample images as supporting artifacts, not primary contract artifacts, unless explicitly documented otherwise.

## P2: Repository Hygiene

- Remove temporary files, `__pycache__`, and build metadata before release.
- Keep docs English-only.
- Keep provider setup env-driven.
- Keep ignored runtime state out of version control.
- Re-run a secret scan before publication.

## P2: Integration Packaging

- Keep AutoDL and Docker OpenClaw tracks documented separately.
- Prefer the TUI path for current OpenClaw releases.
- Keep MCP usage aligned with the stable public API contract.

## P3: Agent Readiness

- Keep MCP tool names stable.
- Keep machine-readable tool metadata available.
- Provide one clear handoff path for OpenClaw or other MCP-compatible clients.
- Avoid exposing unstable low-level workflow details as default agent tools.
