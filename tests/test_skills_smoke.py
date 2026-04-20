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
from cellpaint_pipeline.data_access import DataDownloadExecutionResult, build_data_request, build_download_plan, write_download_plan
from cellpaint_pipeline.skills import (
    PipelineSkillResult,
    available_pipeline_skills,
    get_pipeline_skill_definition,
    pipeline_skill_definition_to_dict,
    pipeline_skill_result_to_dict,
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
        self.assertIn('inspect-cellpainting-data', skills)
        self.assertIn('download-cellpainting-data', skills)
        self.assertIn('run-cellprofiler-profiling', skills)
        self.assertIn('export-single-cell-measurements', skills)
        self.assertIn('run-pycytominer', skills)
        self.assertIn('summarize-classical-profiles', skills)
        self.assertIn('run-segmentation-masks', skills)
        self.assertIn('export-single-cell-crops', skills)
        self.assertIn('prepare-deepprofiler-project', skills)
        self.assertIn('run-deepprofiler', skills)
        self.assertIn('summarize-deepprofiler-profiles', skills)
        self.assertNotIn('collect-deepprofiler-features', skills)
        self.assertNotIn('generate-sample-previews', skills)
        self.assertNotIn('plan-data-access', skills)
        self.assertNotIn('run-segmentation', skills)

    def test_available_pipeline_skills_can_include_advanced(self) -> None:
        skills = available_pipeline_skills(include_advanced=True)
        self.assertIn('generate-sample-previews', skills)
        self.assertIn('collect-deepprofiler-features', skills)

    def test_get_pipeline_skill_definition_roundtrip(self) -> None:
        definition = get_pipeline_skill_definition('download-cellpainting-data')
        payload = pipeline_skill_definition_to_dict(definition)
        self.assertEqual(payload['key'], 'download-cellpainting-data')
        self.assertEqual(payload['category'], 'data-access')
        self.assertIn('cellpaint_pipeline.data_access', payload['implements_with'])

    @patch('cellpaint_pipeline.data_access.execute_download_plan')
    @patch('cellpaint_pipeline.data_access.build_download_plan')
    def test_run_pipeline_skill_dispatches_to_download_runner(self, build_download_plan_mock, execute_download_plan_mock) -> None:
        config = ProjectConfig.from_json(CONFIG_PATH)
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / 'skill_run'
            request = build_data_request(mode='gallery-prefix', prefix='cpg0016-jump/source_4/workspace/', dry_run=True)
            fake_plan = build_download_plan(config, request, validate_with_summary=False)
            build_download_plan_mock.return_value = fake_plan
            execute_download_plan_mock.return_value = DataDownloadExecutionResult(
                plan=fake_plan,
                step_results=[],
                ok=True,
            )
            result = run_pipeline_skill(config, 'download-cellpainting-data', output_dir=output_dir)
            self.assertTrue(result.ok)
            build_download_plan_mock.assert_called_once()
            execute_download_plan_mock.assert_called_once()
            self.assertEqual(result.output_dir, output_dir.resolve())
            self.assertTrue(result.manifest_path.exists())

    def test_pipeline_skill_result_to_dict_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir)
            result = PipelineSkillResult(
                skill_key='run-pycytominer',
                category='profiling',
                implementation='cellpaint_pipeline.profiling_native',
                output_dir=output_dir,
                manifest_path=output_dir / 'pipeline_skill_manifest.json',
                primary_outputs={'feature_selected_path': output_dir / 'feature_selected.parquet'},
                details={'row_count': 10},
                ok=True,
            )
            payload = pipeline_skill_result_to_dict(result)
            self.assertEqual(payload['skill_key'], 'run-pycytominer')
            self.assertEqual(payload['primary_outputs']['feature_selected_path'], str(output_dir / 'feature_selected.parquet'))

    def test_cli_list_pipeline_skills(self) -> None:
        with patch('sys.stdout.write') as write_mock:
            returncode = main(['list-pipeline-skills'])
        self.assertEqual(returncode, 0)
        rendered = ''.join(call.args[0] for call in write_mock.call_args_list)
        payload = json.loads(rendered)
        keys = {item['key'] for item in payload}
        self.assertIn('run-segmentation-masks', keys)

    @patch('cellpaint_pipeline.cli.run_pipeline_skill')
    def test_cli_run_pipeline_skill_with_plan_path(self, run_pipeline_skill_mock) -> None:
        config = ProjectConfig.from_json(CONFIG_PATH)
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            request = build_data_request(mode='gallery-prefix', prefix='cpg0016-jump/source_4/workspace/', dry_run=True)
            plan = build_download_plan(config, request, validate_with_summary=False)
            plan_path = write_download_plan(plan, tmpdir_path / 'download_plan.json')
            output_dir = tmpdir_path / 'skill_cli_output'
            run_pipeline_skill_mock.return_value = PipelineSkillResult(
                skill_key='download-cellpainting-data',
                category='data-access',
                implementation='cellpaint_pipeline.data_access',
                output_dir=output_dir,
                manifest_path=output_dir / 'pipeline_skill_manifest.json',
                primary_outputs={'download_plan_path': output_dir / 'download_plan.json'},
                details={},
                ok=True,
            )
            returncode = main([
                'run-pipeline-skill',
                '--config',
                str(CONFIG_PATH),
                '--skill',
                'download-cellpainting-data',
                '--plan-path',
                str(plan_path),
            ])
            self.assertEqual(returncode, 0)
            _, kwargs = run_pipeline_skill_mock.call_args
            self.assertEqual(kwargs['download_plan'].resolved_prefix, 'cpg0016-jump/source_4/workspace/')
            self.assertIsNone(kwargs['data_request'])


if __name__ == '__main__':
    unittest.main()
