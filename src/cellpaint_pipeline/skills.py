from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from cellpaint_pipeline.config import ProjectConfig
from cellpaint_pipeline.data_access import DataDownloadPlan, DataRequest
from cellpaint_pipeline.orchestration import EndToEndPipelineResult
from cellpaint_pipeline.presets import run_pipeline_preset


@dataclass(frozen=True)
class PipelineSkillDefinition:
    key: str
    description: str
    preset_key: str
    defaults: dict[str, Any]


PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    'plan-gallery-data': PipelineSkillDefinition(
        key='plan-gallery-data',
        description='Prepare a gallery-focused data summary and reusable download plan.',
        preset_key='data-access-plan',
        defaults={},
    ),
    'run-profiling-workflow': PipelineSkillDefinition(
        key='run-profiling-workflow',
        description='Run the profiling branch as a standalone workflow task.',
        preset_key='profiling-only',
        defaults={},
    ),
    'run-segmentation-workflow': PipelineSkillDefinition(
        key='run-segmentation-workflow',
        description='Run the segmentation branch with the standard mask-export route.',
        preset_key='segmentation-only',
        defaults={},
    ),
    'run-deepprofiler-export': PipelineSkillDefinition(
        key='run-deepprofiler-export',
        description='Run the segmentation branch in DeepProfiler export mode.',
        preset_key='deepprofiler-export',
        defaults={},
    ),
    'run-deepprofiler-full': PipelineSkillDefinition(
        key='run-deepprofiler-full',
        description='Run the DeepProfiler full-stack branch.',
        preset_key='deepprofiler-full',
        defaults={},
    ),
    'run-full-workflow': PipelineSkillDefinition(
        key='run-full-workflow',
        description='Run the standard profiling plus segmentation workflow.',
        preset_key='full-pipeline',
        defaults={},
    ),
    'run-full-workflow-with-data-plan': PipelineSkillDefinition(
        key='run-full-workflow-with-data-plan',
        description='Build a data plan first, then run the standard full workflow.',
        preset_key='full-pipeline-with-data-plan',
        defaults={},
    ),
}


def available_pipeline_skills() -> list[str]:
    return list(PIPELINE_SKILLS)


def get_pipeline_skill_definition(skill_key: str) -> PipelineSkillDefinition:
    if skill_key not in PIPELINE_SKILLS:
        available = ', '.join(available_pipeline_skills())
        raise KeyError(f'Unknown pipeline skill: {skill_key}. Available: {available}')
    return PIPELINE_SKILLS[skill_key]


def pipeline_skill_definition_to_dict(definition: PipelineSkillDefinition) -> dict[str, Any]:
    return {
        'key': definition.key,
        'description': definition.description,
        'preset_key': definition.preset_key,
        'defaults': dict(definition.defaults),
    }


def run_pipeline_skill(
    config: ProjectConfig,
    skill_key: str,
    *,
    output_dir: Path | None = None,
    data_request: DataRequest | None = None,
    download_plan: DataDownloadPlan | None = None,
    profiling_suite: str | None = None,
    segmentation_suite: str | None = None,
    deepprofiler_mode: str | None = None,
    include_validation_report: bool | None = None,
    include_data_access_summary: bool | None = None,
    plan_data_download: bool | None = None,
    execute_data_download_step: bool | None = None,
) -> EndToEndPipelineResult:
    definition = get_pipeline_skill_definition(skill_key)
    options = dict(definition.defaults)

    if profiling_suite is not None:
        options['profiling_suite'] = profiling_suite
    if segmentation_suite is not None:
        options['segmentation_suite'] = segmentation_suite
    if deepprofiler_mode is not None:
        options['deepprofiler_mode'] = deepprofiler_mode
    if include_validation_report is not None:
        options['include_validation_report'] = include_validation_report
    if include_data_access_summary is not None:
        options['include_data_access_summary'] = include_data_access_summary
    if plan_data_download is not None:
        options['plan_data_download'] = plan_data_download
    if execute_data_download_step is not None:
        options['execute_data_download_step'] = execute_data_download_step

    resolved_output_dir = output_dir.resolve() if output_dir is not None else (config.default_output_root / 'skills' / skill_key)
    return run_pipeline_preset(
        config,
        definition.preset_key,
        output_dir=resolved_output_dir,
        data_request=data_request,
        download_plan=download_plan,
        **options,
    )
