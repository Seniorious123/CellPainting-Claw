from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import cellpaint_pipeline as package_api
from cellpaint_pipeline.cli import main
from cellpaint_pipeline.config import ProjectConfig
from cellpaint_pipeline.data_access import build_data_request, build_download_plan, write_download_plan
from cellpaint_pipeline.orchestration import EndToEndPipelineResult
from cellpaint_pipeline.skills import (
    available_pipeline_skills,
    get_pipeline_skill_definition,
    pipeline_skill_definition_to_dict,
    run_pipeline_skill,
)

CONFIG_PATH = PROJECT_ROOT / 'configs' / 'project_config.example.json'


class SkillSmokeTests(unittest.TestCase):
    def test_package_api_exports_skill_entrypoints(self) -> None:
        self.assertTrue(callable(package_api.available_pipeline_skills))
        self.assertTrue(callable(package_api.get_pipeline_skill_definition))
        self.assertTrue(callable(package_api.run_pipeline_skill))

    def test_available_pipeline_skills_contains_core_skills(self) -> None:
        skills = available_pipeline_skills()
        self.assertIn('plan-gallery-data', skills)
        self.assertIn('run-full-workflow', skills)
        self.assertIn('run-deepprofiler-full', skills)

    def test_get_pipeline_skill_definition_roundtrip(self) -> None:
        definition = get_pipeline_skill_definition('plan-gallery-data')
        payload = pipeline_skill_definition_to_dict(definition)
        self.assertEqual(payload['key'], 'plan-gallery-data')
        self.assertEqual(payload['preset_key'], 'data-access-plan')
        self.assertEqual(payload['defaults'], {})

    @patch('cellpaint_pipeline.skills.run_pipeline_preset')
    def test_run_pipeline_skill_dispatches_to_preset(self, run_pipeline_preset_mock) -> None:
        config = ProjectConfig.from_json(CONFIG_PATH)
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / 'skill_run'
            run_pipeline_preset_mock.return_value = EndToEndPipelineResult(
                output_dir=output_dir,
                manifest_path=output_dir / 'end_to_end_pipeline_manifest.json',
                run_report_path=output_dir / 'run_report.md',
                data_access_summary_path=output_dir / 'data_access_summary.json',
                download_plan_path=output_dir / 'download_plan.json',
                download_execution_path=None,
                profiling_output_dir=None,
                profiling_manifest_path=None,
                segmentation_output_dir=None,
                segmentation_manifest_path=None,
                validation_report_path=None,
                profiling_suite=None,
                segmentation_suite=None,
                deepprofiler_mode='off',
                stage_count=2,
                ok=True,
            )
            result = run_pipeline_skill(config, 'plan-gallery-data', output_dir=output_dir)
            self.assertTrue(result.ok)
            run_pipeline_preset_mock.assert_called_once()
            args, kwargs = run_pipeline_preset_mock.call_args
            self.assertEqual(args[1], 'data-access-plan')
            self.assertEqual(kwargs['output_dir'], output_dir.resolve())

    def test_run_pipeline_skill_real_lightweight_plan_path(self) -> None:
        config = ProjectConfig.from_json(CONFIG_PATH)
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / 'skill_real_run'
            request = build_data_request(mode='gallery-prefix', prefix='cpg0016-jump/source_4/workspace/', dry_run=True)
            plan = build_download_plan(config, request, validate_with_summary=False)

            result = run_pipeline_skill(
                config,
                'plan-gallery-data',
                output_dir=output_dir,
                download_plan=plan,
                include_data_access_summary=False,
                plan_data_download=False,
            )

            self.assertTrue(result.ok)
            self.assertEqual(result.stage_count, 1)
            self.assertTrue(result.manifest_path.exists())
            self.assertTrue(result.run_report_path.exists())
            self.assertTrue(result.download_plan_path.exists())
            payload = json.loads(result.manifest_path.read_text(encoding='utf-8'))
            self.assertEqual(payload['stage_count'], 1)
            self.assertEqual(payload['stages'][0]['stage'], 'download_plan')
            self.assertEqual(payload['stages'][0]['resolved_prefix'], 'cpg0016-jump/source_4/workspace/')

    def test_cli_list_pipeline_skills(self) -> None:
        with patch('sys.stdout.write') as write_mock:
            returncode = main(['list-pipeline-skills'])
        self.assertEqual(returncode, 0)
        rendered = ''.join(call.args[0] for call in write_mock.call_args_list)
        payload = json.loads(rendered)
        keys = {item['key'] for item in payload}
        self.assertIn('run-full-workflow', keys)

    @patch('cellpaint_pipeline.cli.run_pipeline_skill')
    def test_cli_run_pipeline_skill_with_plan_path(self, run_pipeline_skill_mock) -> None:
        config = ProjectConfig.from_json(CONFIG_PATH)
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            request = build_data_request(mode='gallery-prefix', prefix='cpg0016-jump/source_4/workspace/', dry_run=True)
            plan = build_download_plan(config, request, validate_with_summary=False)
            plan_path = write_download_plan(plan, tmpdir_path / 'download_plan.json')
            output_dir = tmpdir_path / 'skill_cli_output'
            run_pipeline_skill_mock.return_value = EndToEndPipelineResult(
                output_dir=output_dir,
                manifest_path=output_dir / 'end_to_end_pipeline_manifest.json',
                run_report_path=output_dir / 'run_report.md',
                data_access_summary_path=None,
                download_plan_path=output_dir / 'download_plan.json',
                download_execution_path=None,
                profiling_output_dir=None,
                profiling_manifest_path=None,
                segmentation_output_dir=None,
                segmentation_manifest_path=None,
                validation_report_path=None,
                profiling_suite=None,
                segmentation_suite=None,
                deepprofiler_mode='off',
                stage_count=1,
                ok=True,
            )
            returncode = main([
                'run-pipeline-skill',
                '--config',
                str(CONFIG_PATH),
                '--skill',
                'plan-gallery-data',
                '--plan-path',
                str(plan_path),
            ])
            self.assertEqual(returncode, 0)
            _, kwargs = run_pipeline_skill_mock.call_args
            self.assertEqual(kwargs['download_plan'].resolved_prefix, 'cpg0016-jump/source_4/workspace/')
            self.assertIsNone(kwargs['data_request'])


if __name__ == '__main__':
    unittest.main()
