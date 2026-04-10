"""Focused CLI wrapper for CellPainting-Skills."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from cellpaint_pipeline import end_to_end_pipeline_result_to_dict
from cellpaint_pipeline.config import ProjectConfig
from cellpaint_pipeline.data_access import build_data_request, load_download_plan
from cellpaint_pipeline.delivery import available_profiling_suites, available_segmentation_suites
from cellpaint_pipeline.orchestration import available_deepprofiler_modes
from cellpaint_pipeline.skills import (
    available_pipeline_skills,
    get_pipeline_skill_definition,
    pipeline_skill_definition_to_dict,
    run_pipeline_skill,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cellpainting-skills",
        description="Focused skill catalog and runner for CellPainting-Claw.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List available Cell Painting skills.")
    list_parser.add_argument("--include-legacy", action="store_true", help="Also show legacy compatibility skill names.")

    describe_parser = subparsers.add_parser("describe", help="Describe one named Cell Painting skill.")
    describe_parser.add_argument("--skill", required=True, help="Named pipeline skill.")

    run_parser = subparsers.add_parser("run", help="Run one named Cell Painting skill.")
    run_parser.add_argument("--config", required=True, help="Path to project config JSON.")
    run_parser.add_argument("--skill", required=True, help="Named pipeline skill.")
    run_parser.add_argument("--output-dir", default=None, help="Optional output directory for the skill run.")
    run_parser.add_argument("--plan-path", default=None, help="Optional path to a previously saved download plan JSON.")
    run_parser.add_argument("--profiling-suite", default=None, choices=available_profiling_suites(), help="Optional profiling suite override.")
    run_parser.add_argument("--segmentation-suite", default=None, choices=available_segmentation_suites(), help="Optional segmentation suite override.")
    run_parser.add_argument("--deepprofiler-mode", default=None, choices=available_deepprofiler_modes(), help="Optional DeepProfiler mode override.")
    run_parser.add_argument("--request-mode", default="gallery-source", choices=["gallery-source", "gallery-prefix"], help="How to interpret optional request inputs when no plan-path is supplied.")
    run_parser.add_argument("--dataset-id", default=None, help="Optional dataset id override for gallery-source requests.")
    run_parser.add_argument("--source-id", default=None, help="Optional source id override for gallery-source requests.")
    run_parser.add_argument("--prefix", default=None, help="Raw gallery prefix used by gallery-prefix requests.")
    run_parser.add_argument("--subprefix", default="", help="Optional nested subprefix under a dataset/source root.")
    run_parser.add_argument("--bucket", default=None, help="Optional bucket override for the data request.")
    run_parser.add_argument("--include-substring", action="append", default=None, help="Only keep object keys containing this substring. May be repeated.")
    run_parser.add_argument("--exclude-substring", action="append", default=None, help="Skip object keys containing this substring. May be repeated.")
    run_parser.add_argument("--max-files", type=int, default=None, help="Optional max file count for the data request.")
    run_parser.add_argument("--overwrite", action="store_true", help="Overwrite existing local files during download execution.")
    run_parser.add_argument("--dry-run", action="store_true", help="Mark the embedded data request as dry-run.")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "list":
        payload = [
            pipeline_skill_definition_to_dict(get_pipeline_skill_definition(skill_key))
            for skill_key in available_pipeline_skills(include_legacy=args.include_legacy)
        ]
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    if args.command == "describe":
        payload = pipeline_skill_definition_to_dict(get_pipeline_skill_definition(args.skill))
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return 0

    config = ProjectConfig.from_json(args.config)
    download_plan = load_download_plan(Path(args.plan_path).expanduser().resolve()) if args.plan_path else None
    data_request = None
    if download_plan is None:
        data_request = build_data_request(
            mode=args.request_mode,
            dataset_id=args.dataset_id,
            source_id=args.source_id,
            prefix=args.prefix,
            subprefix=args.subprefix,
            bucket=args.bucket,
            include_substrings=args.include_substring or [],
            exclude_substrings=args.exclude_substring or [],
            max_files=args.max_files,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )

    result = run_pipeline_skill(
        config,
        args.skill,
        output_dir=Path(args.output_dir).expanduser().resolve() if args.output_dir else None,
        data_request=data_request,
        download_plan=download_plan,
        profiling_suite=args.profiling_suite,
        segmentation_suite=args.segmentation_suite,
        deepprofiler_mode=args.deepprofiler_mode,
    )
    print(json.dumps(end_to_end_pipeline_result_to_dict(result), indent=2, ensure_ascii=False))
    return 0 if result.ok else 1
