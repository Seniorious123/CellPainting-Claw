from __future__ import annotations

from dataclasses import dataclass, field
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
    category: str
    preset_key: str
    defaults: dict[str, Any]
    user_summary: str
    agent_summary: str
    typical_outputs: tuple[str, ...] = field(default_factory=tuple)
    composes_with: tuple[str, ...] = field(default_factory=tuple)
    status: str = 'primary'
    replaced_by: tuple[str, ...] = field(default_factory=tuple)


PRIMARY_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    'plan-data-access': PipelineSkillDefinition(
        key='plan-data-access',
        description='Inspect configured data sources and build a reusable data-access plan.',
        category='data-access',
        preset_key='data-access-plan',
        defaults={},
        user_summary='Use this skill before processing when you want to inspect a dataset and write a reusable plan.',
        agent_summary='Choose this skill when the request is about discovering inputs or preparing a reusable download plan.',
        typical_outputs=('data_access_summary.json', 'download_plan.json'),
        composes_with=('download-data', 'run-classical-profiling', 'run-segmentation'),
    ),
    'download-data': PipelineSkillDefinition(
        key='download-data',
        description='Execute the data download path for the current request or plan.',
        category='data-access',
        preset_key='data-access-download',
        defaults={},
        user_summary='Use this skill when you already know what data should be pulled locally and want to execute that step.',
        agent_summary='Choose this skill when the user has already selected the data scope and wants the download step to run.',
        typical_outputs=('download_plan.json', 'download_execution.json'),
        composes_with=('plan-data-access', 'run-classical-profiling', 'run-segmentation'),
    ),
    'run-classical-profiling': PipelineSkillDefinition(
        key='run-classical-profiling',
        description='Run the classical profiling path and produce pycytominer-facing outputs.',
        category='profiling',
        preset_key='profiling-only',
        defaults={},
        user_summary='Use this skill when the goal is classical Cell Painting profiling rather than segmentation artifacts.',
        agent_summary='Choose this skill when the request is about single-cell tables, pycytominer outputs, or classical evaluation.',
        typical_outputs=('single_cell.csv.gz', 'pycytominer/', 'evaluation/'),
        composes_with=('plan-data-access', 'download-data'),
    ),
    'run-segmentation': PipelineSkillDefinition(
        key='run-segmentation',
        description='Run the segmentation path and produce masks, previews, and single-cell crops.',
        category='segmentation',
        preset_key='segmentation-only',
        defaults={},
        user_summary='Use this skill when the goal is segmentation artifacts such as masks, previews, and single-cell crops.',
        agent_summary='Choose this skill when the request is about segmentation outputs, mask export, or crop generation.',
        typical_outputs=('masks', 'sample_previews_png', 'single_cell_crops_masked', 'single_cell_crops_unmasked'),
        composes_with=('prepare-deepprofiler-inputs', 'run-deepprofiler'),
    ),
    'prepare-deepprofiler-inputs': PipelineSkillDefinition(
        key='prepare-deepprofiler-inputs',
        description='Prepare the DeepProfiler-ready export artifacts without running DeepProfiler profiling itself.',
        category='deepprofiler',
        preset_key='deepprofiler-export',
        defaults={},
        user_summary='Use this skill when you want to stop after creating the images, metadata, and locations needed by DeepProfiler.',
        agent_summary='Choose this skill when the request is specifically about preparing DeepProfiler inputs, not the full DeepProfiler run.',
        typical_outputs=('deepprofiler export metadata', 'DeepProfiler-ready image inputs', 'DeepProfiler-ready location inputs'),
        composes_with=('run-deepprofiler',),
    ),
    'run-deepprofiler': PipelineSkillDefinition(
        key='run-deepprofiler',
        description='Run the DeepProfiler-oriented path through export, project assembly, profiling, and feature collection.',
        category='deepprofiler',
        preset_key='deepprofiler-full',
        defaults={},
        user_summary='Use this skill when you want the full DeepProfiler branch rather than only the export preparation step.',
        agent_summary='Choose this skill when the request is to generate deep features from the standardized segmentation-driven path.',
        typical_outputs=('DeepProfiler project files', 'DeepProfiler profile outputs', 'collected deep feature tables'),
        composes_with=('prepare-deepprofiler-inputs',),
    ),
}

LEGACY_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    'plan-gallery-data': PipelineSkillDefinition(
        key='plan-gallery-data',
        description='Legacy skill name. Prefer plan-data-access.',
        category='data-access',
        preset_key='data-access-plan',
        defaults={},
        user_summary='Legacy alias retained for compatibility.',
        agent_summary='Legacy alias retained for compatibility.',
        status='legacy',
        replaced_by=('plan-data-access',),
    ),
    'run-profiling-workflow': PipelineSkillDefinition(
        key='run-profiling-workflow',
        description='Legacy skill name. Prefer run-classical-profiling.',
        category='profiling',
        preset_key='profiling-only',
        defaults={},
        user_summary='Legacy alias retained for compatibility.',
        agent_summary='Legacy alias retained for compatibility.',
        status='legacy',
        replaced_by=('run-classical-profiling',),
    ),
    'run-segmentation-workflow': PipelineSkillDefinition(
        key='run-segmentation-workflow',
        description='Legacy skill name. Prefer run-segmentation.',
        category='segmentation',
        preset_key='segmentation-only',
        defaults={},
        user_summary='Legacy alias retained for compatibility.',
        agent_summary='Legacy alias retained for compatibility.',
        status='legacy',
        replaced_by=('run-segmentation',),
    ),
    'run-deepprofiler-export': PipelineSkillDefinition(
        key='run-deepprofiler-export',
        description='Legacy skill name. Prefer prepare-deepprofiler-inputs.',
        category='deepprofiler',
        preset_key='deepprofiler-export',
        defaults={},
        user_summary='Legacy alias retained for compatibility.',
        agent_summary='Legacy alias retained for compatibility.',
        status='legacy',
        replaced_by=('prepare-deepprofiler-inputs',),
    ),
    'run-deepprofiler-full': PipelineSkillDefinition(
        key='run-deepprofiler-full',
        description='Legacy skill name. Prefer run-deepprofiler.',
        category='deepprofiler',
        preset_key='deepprofiler-full',
        defaults={},
        user_summary='Legacy alias retained for compatibility.',
        agent_summary='Legacy alias retained for compatibility.',
        status='legacy',
        replaced_by=('run-deepprofiler',),
    ),
    'run-full-workflow': PipelineSkillDefinition(
        key='run-full-workflow',
        description='Legacy combined skill. Prefer combining modular skills or using the full-pipeline preset.',
        category='combined',
        preset_key='full-pipeline',
        defaults={},
        user_summary='Legacy combined alias retained for compatibility.',
        agent_summary='Legacy combined alias retained for compatibility.',
        status='legacy',
        replaced_by=('run-classical-profiling', 'run-segmentation'),
    ),
    'run-full-workflow-with-data-plan': PipelineSkillDefinition(
        key='run-full-workflow-with-data-plan',
        description='Legacy combined skill. Prefer plan-data-access plus modular skills, or the full-pipeline-with-data-plan preset.',
        category='combined',
        preset_key='full-pipeline-with-data-plan',
        defaults={},
        user_summary='Legacy combined alias retained for compatibility.',
        agent_summary='Legacy combined alias retained for compatibility.',
        status='legacy',
        replaced_by=('plan-data-access', 'run-classical-profiling', 'run-segmentation'),
    ),
}


ALL_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    **PRIMARY_PIPELINE_SKILLS,
    **LEGACY_PIPELINE_SKILLS,
}


def available_pipeline_skills(*, include_legacy: bool = False) -> list[str]:
    catalog = ALL_PIPELINE_SKILLS if include_legacy else PRIMARY_PIPELINE_SKILLS
    return list(catalog)


def get_pipeline_skill_definition(skill_key: str) -> PipelineSkillDefinition:
    if skill_key not in ALL_PIPELINE_SKILLS:
        available = ', '.join(available_pipeline_skills(include_legacy=True))
        raise KeyError(f'Unknown pipeline skill: {skill_key}. Available: {available}')
    return ALL_PIPELINE_SKILLS[skill_key]


def pipeline_skill_definition_to_dict(definition: PipelineSkillDefinition) -> dict[str, Any]:
    return {
        'key': definition.key,
        'description': definition.description,
        'category': definition.category,
        'preset_key': definition.preset_key,
        'defaults': dict(definition.defaults),
        'user_summary': definition.user_summary,
        'agent_summary': definition.agent_summary,
        'typical_outputs': list(definition.typical_outputs),
        'composes_with': list(definition.composes_with),
        'status': definition.status,
        'replaced_by': list(definition.replaced_by),
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
