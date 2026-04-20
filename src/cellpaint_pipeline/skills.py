from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field, is_dataclass, replace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from cellpaint_pipeline.config import ProjectConfig
from cellpaint_pipeline.profile_summaries import (
    summarize_classical_profiles,
    summarize_deepprofiler_profiles,
)
from cellpaint_pipeline.profiling_native import (
    export_cellprofiler_to_singlecell_native,
    run_pycytominer_native,
)
from cellpaint_pipeline.runner import ExecutionResult
from cellpaint_pipeline.segmentation_native import (
    build_mask_export_pipeline_native,
    extract_single_cell_crops_native,
    generate_sample_previews_native,
    prepare_segmentation_load_data_native,
)
from cellpaint_pipeline.workflows.profiling import run_profiling_script
from cellpaint_pipeline.workflows.segmentation import run_segmentation_script


@dataclass(frozen=True)
class PipelineSkillDefinition:
    key: str
    description: str
    category: str
    input_keys: tuple[str, ...]
    typical_outputs: tuple[str, ...]
    implements_with: tuple[str, ...]
    user_summary: str
    agent_summary: str
    composes_with: tuple[str, ...] = field(default_factory=tuple)
    status: str = 'primary'
    replaced_by: tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class PipelineSkillResult:
    skill_key: str
    category: str
    implementation: str
    output_dir: Path
    manifest_path: Path
    primary_outputs: dict[str, Path | None]
    details: dict[str, Any]
    ok: bool


PRIMARY_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    'inspect-cellpainting-data': PipelineSkillDefinition(
        key='inspect-cellpainting-data',
        description='Inspect the configured Cell Painting data sources and return a usable availability summary.',
        category='data-access',
        input_keys=('output_dir',),
        typical_outputs=('data_access_summary.json',),
        implements_with=('cellpaint_pipeline.data_access', 'boto3', 'cpgdata', 'quilt3'),
        user_summary='Use this skill when you want to see what Cell Painting data can be accessed before downloading anything.',
        agent_summary='Choose this skill when the request is to inspect accessible datasets, sources, or access status.',
        composes_with=('download-cellpainting-data',),
    ),
    'download-cellpainting-data': PipelineSkillDefinition(
        key='download-cellpainting-data',
        description='Download one configured Cell Painting dataset slice into a local cache directory.',
        category='data-access',
        input_keys=('data_request', 'download_plan', 'output_dir'),
        typical_outputs=('download_plan.json', 'downloads/', 'download manifests'),
        implements_with=('cellpaint_pipeline.data_access', 'boto3', 'cpgdata', 'quilt3'),
        user_summary='Use this skill when you want local input files for the rest of the toolkit.',
        agent_summary='Choose this skill when the request is to fetch Cell Painting inputs from the configured access layer.',
        composes_with=('run-cellprofiler-profiling', 'run-segmentation-masks'),
    ),
    'run-cellprofiler-profiling': PipelineSkillDefinition(
        key='run-cellprofiler-profiling',
        description='Run the configured CellProfiler profiling pipeline against the active profiling backend.',
        category='profiling',
        input_keys=('output_dir',),
        typical_outputs=('Image.csv', 'Cells.csv', 'Cytoplasm.csv', 'Nuclei.csv', 'CellProfiler log'),
        implements_with=('cellpaint_pipeline.workflows.profiling', 'CellProfiler'),
        user_summary='Use this skill when you want CellProfiler to generate profiling tables from raw images.',
        agent_summary='Choose this skill when the request is to run the configured profiling .cppipe and produce measurement tables.',
        composes_with=('export-single-cell-measurements', 'run-pycytominer'),
    ),
    'export-single-cell-measurements': PipelineSkillDefinition(
        key='export-single-cell-measurements',
        description='Merge CellProfiler image and object tables into a single-cell measurements table.',
        category='profiling',
        input_keys=('image_csv_path', 'object_table_path', 'object_table', 'output_dir'),
        typical_outputs=('single_cell.csv.gz',),
        implements_with=('cellpaint_pipeline.profiling_native',),
        user_summary='Use this skill when you want one single-cell measurements table after CellProfiler has produced the compartment tables.',
        agent_summary='Choose this skill when the request is to turn CellProfiler output tables into one single-cell table.',
        composes_with=('run-pycytominer',),
    ),
    'run-pycytominer': PipelineSkillDefinition(
        key='run-pycytominer',
        description='Run the configured pycytominer aggregation, annotation, normalization, and feature-selection path.',
        category='profiling',
        input_keys=('output_dir',),
        typical_outputs=('aggregated.parquet', 'annotated.parquet', 'normalized.parquet', 'feature_selected.parquet'),
        implements_with=('cellpaint_pipeline.profiling_native', 'pycytominer'),
        user_summary='Use this skill when you want classical Cell Painting profile tables.',
        agent_summary='Choose this skill when the request is about classical profile generation from single-cell measurements.',
        composes_with=('summarize-classical-profiles',),
    ),
    'summarize-classical-profiles': PipelineSkillDefinition(
        key='summarize-classical-profiles',
        description='Summarize classical Cell Painting profile tables into readable metadata, variability, and PCA outputs.',
        category='profiling',
        input_keys=('feature_selected_path', 'manifest_path', 'output_dir'),
        typical_outputs=('profile_summary.json', 'well_metadata_summary.csv', 'top_variable_features.csv', 'pca_coordinates.csv', 'pca_plot.png'),
        implements_with=('cellpaint_pipeline.profile_summaries', 'pandas', 'numpy'),
        user_summary='Use this skill when you want a readable summary of pycytominer outputs instead of raw profile tables only.',
        agent_summary='Choose this skill when the request is to explain or summarize classical profile outputs for a human reader.',
    ),
    'run-segmentation-masks': PipelineSkillDefinition(
        key='run-segmentation-masks',
        description='Run the segmentation CellProfiler pipeline and produce mask tables, labels, outlines, and sample previews.',
        category='segmentation',
        input_keys=('output_dir',),
        typical_outputs=('cellprofiler_masks/', 'Image.csv', 'Cells.csv', 'Nuclei.csv', 'labels/', 'outlines/', 'sample_previews_png/'),
        implements_with=('cellpaint_pipeline.segmentation_native', 'cellpaint_pipeline.workflows.segmentation', 'CellProfiler'),
        user_summary='Use this skill when you want segmentation outputs, including masks, object tables, and quick field previews.',
        agent_summary='Choose this skill when the request is to execute the segmentation branch and produce mask artifacts plus quick previews.',
        composes_with=('export-single-cell-crops', 'prepare-deepprofiler-project'),
    ),
    'export-single-cell-crops': PipelineSkillDefinition(
        key='export-single-cell-crops',
        description='Export single-cell image stacks from a segmentation workflow root in masked or unmasked mode.',
        category='segmentation',
        input_keys=('workflow_root', 'output_dir', 'workers', 'crop_mode'),
        typical_outputs=('masked/ or unmasked/', 'single_cell_manifest.csv'),
        implements_with=('cellpaint_pipeline.segmentation_native',),
        user_summary='Use this skill when you want single-cell crops as a user-facing result and choose masked or unmasked mode explicitly.',
        agent_summary='Choose this skill when the request is to export single-cell crops and the only decision is masked versus unmasked mode.',
        composes_with=('prepare-deepprofiler-project',),
    ),
    'prepare-deepprofiler-project': PipelineSkillDefinition(
        key='prepare-deepprofiler-project',
        description='Prepare a runnable DeepProfiler project from a segmentation workflow root, explicit source tables, or an existing export root.',
        category='deepprofiler',
        input_keys=('workflow_root', 'export_root', 'image_csv_path', 'nuclei_csv_path', 'load_data_csv_path', 'output_dir', 'experiment_name', 'config_filename', 'metadata_filename'),
        typical_outputs=('project_manifest.json', 'inputs/config/', 'inputs/metadata/', 'inputs/locations/'),
        implements_with=('cellpaint_pipeline.adapters.deepprofiler', 'cellpaint_pipeline.adapters.deepprofiler_project', 'DeepProfiler'),
        user_summary='Use this skill when you want a DeepProfiler project directory that is ready to run next.',
        agent_summary='Choose this skill when the request is to stop at a runnable DeepProfiler project rather than executing the model.',
        composes_with=('run-deepprofiler',),
    ),
    'run-deepprofiler': PipelineSkillDefinition(
        key='run-deepprofiler',
        description='Run the DeepProfiler path and return collected single-cell and well-level feature tables.',
        category='deepprofiler',
        input_keys=('project_root', 'workflow_root', 'image_csv_path', 'nuclei_csv_path', 'load_data_csv_path', 'output_dir', 'experiment_name', 'config_filename', 'metadata_filename', 'gpu'),
        typical_outputs=('deepprofiler_single_cell.parquet', 'deepprofiler_well_aggregated.parquet', 'deepprofiler_feature_manifest.json'),
        implements_with=('cellpaint_pipeline.deepprofiler_pipeline', 'DeepProfiler', 'pandas', 'pyarrow'),
        user_summary='Use this skill when you want final DeepProfiler tables rather than only intermediate project or feature directories.',
        agent_summary='Choose this skill when the request is to run DeepProfiler and hand back analysis-ready outputs.',
        composes_with=('summarize-deepprofiler-profiles',),
    ),
    'summarize-deepprofiler-profiles': PipelineSkillDefinition(
        key='summarize-deepprofiler-profiles',
        description='Summarize DeepProfiler single-cell and well-level tables into readable metadata, variability, and PCA outputs.',
        category='deepprofiler',
        input_keys=('single_cell_parquet_path', 'well_aggregated_parquet_path', 'manifest_path', 'output_dir'),
        typical_outputs=('profile_summary.json', 'well_metadata_summary.csv', 'top_variable_features.csv', 'pca_coordinates.csv', 'pca_plot.png'),
        implements_with=('cellpaint_pipeline.profile_summaries', 'pandas', 'numpy'),
        user_summary='Use this skill when you want a readable summary of DeepProfiler outputs instead of raw embedding tables only.',
        agent_summary='Choose this skill when the request is to explain or summarize DeepProfiler outputs for a human reader.',
    ),
}

ADVANCED_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    'generate-sample-previews': PipelineSkillDefinition(
        key='generate-sample-previews',
        description='Render field-level RGB preview PNGs from the segmentation source channels.',
        category='segmentation',
        input_keys=('workflow_root', 'output_dir', 'overwrite'),
        typical_outputs=('sample_previews_png/',),
        implements_with=('cellpaint_pipeline.segmentation_native', 'Pillow', 'numpy'),
        user_summary='Direct-control skill for users who want only preview PNGs from a segmentation workflow root.',
        agent_summary='Direct-control skill for explicitly producing preview PNGs without rerunning the full segmentation skill.',
        status='advanced',
    ),
    'export-masked-single-cell-crops': PipelineSkillDefinition(
        key='export-masked-single-cell-crops',
        description='Export masked single-cell image stacks and masks for each segmented cell.',
        category='segmentation',
        input_keys=('workflow_root', 'output_dir', 'workers'),
        typical_outputs=('masked/image_stacks/', 'masked/cell_masks/', 'masked/nuclei_masks/', 'masked/single_cell_manifest.csv'),
        implements_with=('cellpaint_pipeline.segmentation_native',),
        user_summary='Advanced direct-control skill for explicitly requesting masked crop export.',
        agent_summary='Advanced direct-control skill for explicitly requesting masked crop export.',
        composes_with=('export-deepprofiler-inputs',),
        status='advanced',
    ),
    'export-unmasked-single-cell-crops': PipelineSkillDefinition(
        key='export-unmasked-single-cell-crops',
        description='Export unmasked single-cell image stacks and masks for each segmented cell.',
        category='segmentation',
        input_keys=('workflow_root', 'output_dir', 'workers'),
        typical_outputs=('unmasked/image_stacks/', 'unmasked/cell_masks/', 'unmasked/nuclei_masks/', 'unmasked/single_cell_manifest.csv'),
        implements_with=('cellpaint_pipeline.segmentation_native',),
        user_summary='Advanced direct-control skill for explicitly requesting unmasked crop export.',
        agent_summary='Advanced direct-control skill for explicitly requesting unmasked crop export.',
        composes_with=('export-deepprofiler-inputs',),
        status='advanced',
    ),
    'export-deepprofiler-inputs': PipelineSkillDefinition(
        key='export-deepprofiler-inputs',
        description='Write the DeepProfiler field metadata and per-field nuclei location CSV files.',
        category='deepprofiler',
        input_keys=('workflow_root', 'image_csv_path', 'nuclei_csv_path', 'load_data_csv_path', 'output_dir'),
        typical_outputs=('manifest.json', 'images/field_metadata.csv', 'locations/'),
        implements_with=('cellpaint_pipeline.adapters.deepprofiler',),
        user_summary='Advanced direct-control skill for stopping at the DeepProfiler export stage.',
        agent_summary='Advanced direct-control skill for stopping at the DeepProfiler export stage.',
        composes_with=('build-deepprofiler-project',),
        status='advanced',
    ),
    'build-deepprofiler-project': PipelineSkillDefinition(
        key='build-deepprofiler-project',
        description='Build a runnable DeepProfiler project directory from a DeepProfiler export.',
        category='deepprofiler',
        input_keys=('workflow_root', 'export_root', 'output_dir', 'experiment_name', 'config_filename', 'metadata_filename'),
        typical_outputs=('project_manifest.json', 'inputs/config/', 'inputs/metadata/', 'inputs/locations/'),
        implements_with=('cellpaint_pipeline.adapters.deepprofiler_project', 'DeepProfiler'),
        user_summary='Advanced direct-control skill for explicitly building the DeepProfiler project stage.',
        agent_summary='Advanced direct-control skill for explicitly building the DeepProfiler project stage.',
        composes_with=('run-deepprofiler-profile',),
        status='advanced',
    ),
    'run-deepprofiler-profile': PipelineSkillDefinition(
        key='run-deepprofiler-profile',
        description='Run the DeepProfiler profile command against a prepared DeepProfiler project.',
        category='deepprofiler',
        input_keys=('project_root', 'output_dir', 'experiment_name', 'config_filename', 'metadata_filename', 'gpu'),
        typical_outputs=('outputs/<experiment>/features/', 'deepprofiler_profile log'),
        implements_with=('cellpaint_pipeline.adapters.deepprofiler_project', 'DeepProfiler'),
        user_summary='Advanced direct-control skill for generating raw DeepProfiler feature files.',
        agent_summary='Advanced direct-control skill for generating raw DeepProfiler feature files.',
        composes_with=('collect-deepprofiler-features',),
        status='advanced',
    ),
    'collect-deepprofiler-features': PipelineSkillDefinition(
        key='collect-deepprofiler-features',
        description='Collect DeepProfiler .npz outputs into single-cell and well-level tabular feature files.',
        category='deepprofiler',
        input_keys=('project_root', 'output_dir', 'experiment_name'),
        typical_outputs=('deepprofiler_single_cell.parquet', 'deepprofiler_single_cell.csv.gz', 'deepprofiler_well_aggregated.parquet', 'deepprofiler_well_aggregated.csv.gz', 'deepprofiler_feature_manifest.json'),
        implements_with=('cellpaint_pipeline.adapters.deepprofiler_features', 'pandas', 'pyarrow'),
        user_summary='Advanced direct-control skill for collecting already-generated DeepProfiler feature files into tables.',
        agent_summary='Advanced direct-control skill for collecting already-generated DeepProfiler feature files into tables.',
        status='advanced',
    ),
}

LEGACY_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    'build-image-manifest': PipelineSkillDefinition(
        key='build-image-manifest',
        description='Former helper-style skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy helper alias. Prefer run-cellprofiler-profiling.',
        agent_summary='Legacy helper alias. Prefer run-cellprofiler-profiling.',
        status='legacy',
        replaced_by=('run-cellprofiler-profiling',),
    ),
    'validate-profiling-inputs': PipelineSkillDefinition(
        key='validate-profiling-inputs',
        description='Former helper-style skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy helper alias. Prefer run-cellprofiler-profiling or export-single-cell-measurements depending on the actual task.',
        agent_summary='Legacy helper alias. Prefer run-cellprofiler-profiling or export-single-cell-measurements depending on the actual task.',
        status='legacy',
        replaced_by=('run-cellprofiler-profiling', 'export-single-cell-measurements'),
    ),
    'export-segmentation-load-data': PipelineSkillDefinition(
        key='export-segmentation-load-data',
        description='Former helper-style skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy helper alias. Prefer run-segmentation-masks.',
        agent_summary='Legacy helper alias. Prefer run-segmentation-masks.',
        status='legacy',
        replaced_by=('run-segmentation-masks',),
    ),
    'plan-data-access': PipelineSkillDefinition(
        key='plan-data-access',
        description='Legacy skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy alias. Prefer inspect-cellpainting-data or download-cellpainting-data.',
        agent_summary='Legacy alias. Prefer inspect-cellpainting-data or download-cellpainting-data.',
        status='legacy',
        replaced_by=('inspect-cellpainting-data', 'download-cellpainting-data'),
    ),
    'download-data': PipelineSkillDefinition(
        key='download-data',
        description='Legacy skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy alias. Prefer download-cellpainting-data.',
        agent_summary='Legacy alias. Prefer download-cellpainting-data.',
        status='legacy',
        replaced_by=('download-cellpainting-data',),
    ),
    'run-classical-profiling': PipelineSkillDefinition(
        key='run-classical-profiling',
        description='Legacy skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy alias. Prefer export-single-cell-measurements plus run-pycytominer.',
        agent_summary='Legacy alias. Prefer export-single-cell-measurements plus run-pycytominer.',
        status='legacy',
        replaced_by=('export-single-cell-measurements', 'run-pycytominer'),
    ),
    'run-segmentation': PipelineSkillDefinition(
        key='run-segmentation',
        description='Legacy skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy alias. Prefer run-segmentation-masks.',
        agent_summary='Legacy alias. Prefer run-segmentation-masks.',
        status='legacy',
        replaced_by=('run-segmentation-masks',),
    ),
    'prepare-deepprofiler-inputs': PipelineSkillDefinition(
        key='prepare-deepprofiler-inputs',
        description='Legacy skill name retained for compatibility discovery only.',
        category='legacy',
        input_keys=(),
        typical_outputs=(),
        implements_with=(),
        user_summary='Legacy alias. Prefer prepare-deepprofiler-project or export-deepprofiler-inputs depending on how far you want to go.',
        agent_summary='Legacy alias. Prefer prepare-deepprofiler-project or export-deepprofiler-inputs depending on how far you want to go.',
        status='legacy',
        replaced_by=('prepare-deepprofiler-project', 'export-deepprofiler-inputs'),
    ),
}

ALL_PIPELINE_SKILLS: dict[str, PipelineSkillDefinition] = {
    **PRIMARY_PIPELINE_SKILLS,
    **ADVANCED_PIPELINE_SKILLS,
    **LEGACY_PIPELINE_SKILLS,
}


def available_pipeline_skills(*, include_advanced: bool = False, include_legacy: bool = False) -> list[str]:
    catalog: dict[str, PipelineSkillDefinition] = dict(PRIMARY_PIPELINE_SKILLS)
    if include_advanced:
        catalog.update(ADVANCED_PIPELINE_SKILLS)
    if include_legacy:
        catalog.update(LEGACY_PIPELINE_SKILLS)
    return list(catalog)


def get_pipeline_skill_definition(skill_key: str) -> PipelineSkillDefinition:
    if skill_key not in ALL_PIPELINE_SKILLS:
        available = ', '.join(available_pipeline_skills(include_advanced=True, include_legacy=True))
        raise KeyError(f'Unknown pipeline skill: {skill_key}. Available: {available}')
    return ALL_PIPELINE_SKILLS[skill_key]


def pipeline_skill_definition_to_dict(definition: PipelineSkillDefinition) -> dict[str, Any]:
    return {
        'key': definition.key,
        'description': definition.description,
        'category': definition.category,
        'input_keys': list(definition.input_keys),
        'typical_outputs': list(definition.typical_outputs),
        'implements_with': list(definition.implements_with),
        'user_summary': definition.user_summary,
        'agent_summary': definition.agent_summary,
        'composes_with': list(definition.composes_with),
        'status': definition.status,
        'replaced_by': list(definition.replaced_by),
    }


def pipeline_skill_result_to_dict(result: PipelineSkillResult) -> dict[str, Any]:
    return {
        'skill_key': result.skill_key,
        'category': result.category,
        'implementation': result.implementation,
        'output_dir': str(result.output_dir),
        'manifest_path': str(result.manifest_path),
        'primary_outputs': {key: str(value) if value is not None else None for key, value in result.primary_outputs.items()},
        'details': result.details,
        'ok': result.ok,
    }


@dataclass(frozen=True)
class SkillRuntimeContext:
    config: ProjectConfig
    definition: PipelineSkillDefinition
    run_root: Path
    data_request: DataRequest | None
    download_plan: DataDownloadPlan | None
    workflow_root: Path | None
    export_root: Path | None
    project_root: Path | None
    image_csv_path: Path | None
    nuclei_csv_path: Path | None
    load_data_csv_path: Path | None
    manifest_path: Path | None
    object_table_path: Path | None
    feature_selected_path: Path | None
    single_cell_parquet_path: Path | None
    well_aggregated_parquet_path: Path | None
    object_table: str | None
    crop_mode: str | None
    gpu: str | None
    experiment_name: str | None
    config_filename: str | None
    metadata_filename: str | None
    workers: int
    chunk_size: int
    overwrite: bool


def run_pipeline_skill(
    config: ProjectConfig,
    skill_key: str,
    *,
    output_dir: Path | None = None,
    data_request: DataRequest | None = None,
    download_plan: DataDownloadPlan | None = None,
    workflow_root: Path | None = None,
    export_root: Path | None = None,
    project_root: Path | None = None,
    image_csv_path: Path | None = None,
    nuclei_csv_path: Path | None = None,
    load_data_csv_path: Path | None = None,
    manifest_path: Path | None = None,
    object_table_path: Path | None = None,
    feature_selected_path: Path | None = None,
    single_cell_parquet_path: Path | None = None,
    well_aggregated_parquet_path: Path | None = None,
    object_table: str | None = None,
    crop_mode: str | None = None,
    gpu: str | None = None,
    experiment_name: str | None = None,
    config_filename: str | None = None,
    metadata_filename: str | None = None,
    workers: int = 0,
    chunk_size: int = 64,
    overwrite: bool = False,
    profiling_suite: str | None = None,
    segmentation_suite: str | None = None,
    deepprofiler_mode: str | None = None,
    include_validation_report: bool | None = None,
    include_data_access_summary: bool | None = None,
    plan_data_download: bool | None = None,
    execute_data_download_step: bool | None = None,
) -> PipelineSkillResult:
    del profiling_suite
    del segmentation_suite
    del deepprofiler_mode
    del include_validation_report
    del include_data_access_summary
    del plan_data_download
    del execute_data_download_step

    definition = get_pipeline_skill_definition(skill_key)
    if definition.status == 'legacy':
        replacements = ', '.join(definition.replaced_by) or 'the primary skill catalog'
        raise KeyError(f'Legacy pipeline skill {skill_key!r} is no longer executable. Use: {replacements}')

    run_root = output_dir.resolve() if output_dir is not None else (config.default_output_root / 'skills' / skill_key)
    run_root.mkdir(parents=True, exist_ok=True)
    context = SkillRuntimeContext(
        config=config,
        definition=definition,
        run_root=run_root,
        data_request=data_request,
        download_plan=download_plan,
        workflow_root=workflow_root.expanduser().resolve() if workflow_root is not None else None,
        export_root=export_root.expanduser().resolve() if export_root is not None else None,
        project_root=project_root.expanduser().resolve() if project_root is not None else None,
        image_csv_path=image_csv_path.expanduser().resolve() if image_csv_path is not None else None,
        nuclei_csv_path=nuclei_csv_path.expanduser().resolve() if nuclei_csv_path is not None else None,
        load_data_csv_path=load_data_csv_path.expanduser().resolve() if load_data_csv_path is not None else None,
        manifest_path=manifest_path.expanduser().resolve() if manifest_path is not None else None,
        object_table_path=object_table_path.expanduser().resolve() if object_table_path is not None else None,
        feature_selected_path=feature_selected_path.expanduser().resolve() if feature_selected_path is not None else None,
        single_cell_parquet_path=single_cell_parquet_path.expanduser().resolve() if single_cell_parquet_path is not None else None,
        well_aggregated_parquet_path=well_aggregated_parquet_path.expanduser().resolve() if well_aggregated_parquet_path is not None else None,
        object_table=object_table,
        crop_mode=crop_mode,
        gpu=gpu,
        experiment_name=experiment_name,
        config_filename=config_filename,
        metadata_filename=metadata_filename,
        workers=workers,
        chunk_size=chunk_size,
        overwrite=overwrite,
    )
    return SKILL_RUNNERS[skill_key](context)


def _run_download_cellpainting_data(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.data_access import (
        build_data_request,
        build_download_plan,
        execute_download_plan,
        write_download_plan,
    )

    request = context.data_request
    if context.download_plan is None:
        if request is None:
            request = build_data_request(
                dataset_id=context.config.data_access.default_dataset_id,
                source_id=context.config.data_access.default_source_id,
                dry_run=False,
                output_dir=context.run_root / 'downloads',
                manifest_path=context.run_root / 'downloads' / 'download_manifest.json',
            )
        elif request.output_dir is None or request.manifest_path is None:
            request = replace(
                request,
                output_dir=request.output_dir or (context.run_root / 'downloads'),
                manifest_path=request.manifest_path or (context.run_root / 'downloads' / 'download_manifest.json'),
            )
        plan = build_download_plan(context.config, request)
    else:
        plan = context.download_plan
    plan_path = write_download_plan(plan, context.run_root / 'download_plan.json')
    execution = execute_download_plan(context.config, plan)
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.data_access',
        primary_outputs={
            'download_plan_path': plan_path,
            'download_output_dir': execution.step_results[0].step.output_dir if execution.step_results else None,
            'download_manifest_path': execution.step_results[0].step.manifest_path if execution.step_results else None,
        },
        details=_json_ready(execution),
        ok=execution.ok,
    )


def _run_inspect_cellpainting_data(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.data_access import data_access_summary_to_dict, summarize_data_access

    summary = summarize_data_access(context.config)
    summary_payload = data_access_summary_to_dict(summary)
    summary_path = context.run_root / 'data_access_summary.json'
    summary_path.write_text(json.dumps(summary_payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.data_access',
        primary_outputs={'data_access_summary_path': summary_path},
        details=summary_payload,
        ok=bool(summary_payload.get('ok', True)),
    )


def _run_cellprofiler_profiling(context: SkillRuntimeContext) -> PipelineSkillResult:
    execution = run_profiling_script(context.config, 'run-official-cellprofiler')
    backend_payload = context.config.load_profiling_backend_payload()
    paths_payload = backend_payload['paths']
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.workflows.profiling',
        primary_outputs={
            'image_table_path': context.config.resolve_profiling_backend_path(paths_payload['image_table_csv']),
            'cells_table_path': context.config.resolve_profiling_backend_path(paths_payload['cells_table_csv']),
            'cytoplasm_table_path': context.config.resolve_profiling_backend_path(paths_payload['cytoplasm_table_csv']),
            'nuclei_table_path': context.config.resolve_profiling_backend_path(paths_payload['nuclei_table_csv']),
            'log_path': execution.log_path,
        },
        details=_execution_result_to_dict(execution),
        ok=execution.returncode == 0,
    )


def _run_export_single_cell_measurements(context: SkillRuntimeContext) -> PipelineSkillResult:
    export_result = export_cellprofiler_to_singlecell_native(
        context.config,
        object_table=context.object_table,
        image_table_path=context.image_csv_path,
        object_table_path=context.object_table_path,
        output_path=context.run_root / 'single_cell.csv.gz',
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.profiling_native',
        primary_outputs={'single_cell_path': export_result.output_path},
        details=_json_ready(export_result),
        ok=True,
    )


def _run_pycytominer(context: SkillRuntimeContext) -> PipelineSkillResult:
    result = run_pycytominer_native(context.config, output_dir=context.run_root / 'pycytominer')
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.profiling_native',
        primary_outputs={
            'aggregated_path': result.aggregated_path,
            'annotated_path': result.annotated_path,
            'normalized_path': result.normalized_path,
            'feature_selected_path': result.feature_selected_path,
        },
        details=_json_ready(result),
        ok=True,
    )


def _run_summarize_classical_profiles(context: SkillRuntimeContext) -> PipelineSkillResult:
    result = summarize_classical_profiles(
        context.config,
        output_dir=context.run_root,
        feature_selected_path=context.feature_selected_path,
        manifest_path=context.manifest_path,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.profile_summaries',
        primary_outputs={
            'summary_path': result.summary_path,
            'well_metadata_summary_path': result.well_metadata_summary_path,
            'top_variable_features_path': result.top_variable_features_path,
            'pca_coordinates_path': result.pca_coordinates_path,
            'pca_plot_path': result.pca_plot_path,
        },
        details=_json_ready(result),
        ok=True,
    )


def _run_segmentation_masks(context: SkillRuntimeContext) -> PipelineSkillResult:
    load_data_path = context.run_root / 'load_data_for_segmentation.csv'
    pipeline_path = context.run_root / 'CPJUMP1_analysis_mask_export.cppipe'
    load_data_result = prepare_segmentation_load_data_native(context.config, output_path=load_data_path)
    pipeline_result = build_mask_export_pipeline_native(context.config, output_path=pipeline_path)
    workflow_config = _build_isolated_segmentation_skill_config(
        context.config,
        workflow_root=context.run_root,
        load_data_path=load_data_path,
        pipeline_path=pipeline_path,
    )
    execution = run_segmentation_script(
        workflow_config,
        'run-mask-export',
        ['--config', str(workflow_config.segmentation_backend_config), '--reuse-load-data', '--reuse-pipeline'],
    )
    sample_previews_result = generate_sample_previews_native(workflow_config, overwrite=True)
    mask_output_dir = context.run_root / 'cellprofiler_masks'
    summary_path = context.run_root / 'segmentation_summary.json'
    summary_payload = {
        'implementation': 'cellpaint_pipeline.skills.run-segmentation-masks',
        'load_data_path': str(load_data_result.output_path),
        'pipeline_path': str(pipeline_result.output_path),
        'cellprofiler_output_dir': str(mask_output_dir),
        'image_table_path': str(mask_output_dir / 'Image.csv'),
        'cells_table_path': str(mask_output_dir / 'Cells.csv'),
        'nuclei_table_path': str(mask_output_dir / 'Nuclei.csv'),
        'labels_dir': str(mask_output_dir / 'labels'),
        'outlines_dir': str(mask_output_dir / 'outlines'),
        'sample_previews_dir': str(sample_previews_result.output_dir),
        'sample_preview_count': sample_previews_result.generated_count,
        'execution': _execution_result_to_dict(execution),
    }
    summary_path.write_text(json.dumps(summary_payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.workflows.segmentation',
        primary_outputs={
            'load_data_path': load_data_result.output_path,
            'pipeline_path': pipeline_result.output_path,
            'cellprofiler_output_dir': mask_output_dir,
            'image_table_path': mask_output_dir / 'Image.csv',
            'cells_table_path': mask_output_dir / 'Cells.csv',
            'nuclei_table_path': mask_output_dir / 'Nuclei.csv',
            'sample_previews_dir': sample_previews_result.output_dir,
            'summary_path': summary_path,
            'log_path': execution.log_path,
        },
        details={
            'load_data': _json_ready(load_data_result),
            'pipeline': _json_ready(pipeline_result),
            'execution': _execution_result_to_dict(execution),
            'sample_previews': _json_ready(sample_previews_result),
            'summary': summary_payload,
        },
        ok=execution.returncode == 0,
    )


def _run_generate_sample_previews(context: SkillRuntimeContext) -> PipelineSkillResult:
    source_config = _resolve_segmentation_source_config(context)
    result = generate_sample_previews_native(source_config, output_dir=context.run_root / 'sample_previews_png', overwrite=context.overwrite)
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.segmentation_native',
        primary_outputs={'sample_previews_dir': result.output_dir},
        details=_json_ready(result),
        ok=True,
    )


def _run_export_single_cell_crops(context: SkillRuntimeContext) -> PipelineSkillResult:
    mode = (context.crop_mode or 'masked').strip().lower()
    if mode not in {'masked', 'unmasked'}:
        raise ValueError(f'Unsupported crop_mode {context.crop_mode!r}. Expected masked or unmasked.')
    return _run_single_cell_crop_skill(context, mode=mode)


def _run_single_cell_crop_skill(context: SkillRuntimeContext, *, mode: str) -> PipelineSkillResult:
    source_config = _resolve_segmentation_source_config(context)
    crops_root = context.run_root / mode
    result = extract_single_cell_crops_native(
        source_config,
        mode=mode,
        output_dir=crops_root,
        manifest_path=crops_root / 'single_cell_manifest.csv',
        workers=context.workers,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.segmentation_native',
        primary_outputs={'crops_dir': result.crops_dir, 'manifest_path': result.manifest_path},
        details=_json_ready(result),
        ok=True,
    )


def _run_export_masked_single_cell_crops(context: SkillRuntimeContext) -> PipelineSkillResult:
    return _run_single_cell_crop_skill(context, mode='masked')


def _run_export_unmasked_single_cell_crops(context: SkillRuntimeContext) -> PipelineSkillResult:
    return _run_single_cell_crop_skill(context, mode='unmasked')


def _run_export_deepprofiler_inputs(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.adapters.deepprofiler import export_deepprofiler_input

    if context.workflow_root is not None:
        result = export_deepprofiler_input(
            context.config,
            output_dir=context.run_root,
            image_csv_path=context.workflow_root / 'cellprofiler_masks' / 'Image.csv',
            nuclei_csv_path=context.workflow_root / 'cellprofiler_masks' / 'Nuclei.csv',
            load_data_csv_path=context.workflow_root / 'load_data_for_segmentation.csv',
            source_label='workflow-local-mask-export',
        )
    else:
        result = export_deepprofiler_input(
            context.config,
            output_dir=context.run_root,
            image_csv_path=context.image_csv_path,
            nuclei_csv_path=context.nuclei_csv_path,
            load_data_csv_path=context.load_data_csv_path,
        )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.adapters.deepprofiler',
        primary_outputs={
            'export_root': result.export_root,
            'export_manifest_path': result.manifest_path,
            'field_metadata_path': result.field_metadata_path,
            'locations_root': result.locations_root,
        },
        details=_json_ready(result),
        ok=True,
    )


def _run_prepare_deepprofiler_project(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.adapters.deepprofiler import export_deepprofiler_input
    from cellpaint_pipeline.adapters.deepprofiler_project import build_deepprofiler_project

    export_result = None
    resolved_export_root = context.export_root
    if resolved_export_root is None:
        if context.workflow_root is not None:
            export_result = export_deepprofiler_input(
                context.config,
                output_dir=context.run_root / 'deepprofiler_export',
                image_csv_path=context.workflow_root / 'cellprofiler_masks' / 'Image.csv',
                nuclei_csv_path=context.workflow_root / 'cellprofiler_masks' / 'Nuclei.csv',
                load_data_csv_path=context.workflow_root / 'load_data_for_segmentation.csv',
                source_label='workflow-local-mask-export',
            )
        else:
            export_result = export_deepprofiler_input(
                context.config,
                output_dir=context.run_root / 'deepprofiler_export',
                image_csv_path=context.image_csv_path,
                nuclei_csv_path=context.nuclei_csv_path,
                load_data_csv_path=context.load_data_csv_path,
            )
        resolved_export_root = export_result.export_root

    project_result = build_deepprofiler_project(
        context.config,
        output_dir=context.run_root / 'deepprofiler_project',
        export_root=resolved_export_root,
        experiment_name=context.experiment_name,
        config_filename=context.config_filename,
        metadata_filename=context.metadata_filename,
    )
    details: dict[str, Any] = {
        'project': _json_ready(project_result),
    }
    if export_result is not None:
        details['export'] = _json_ready(export_result)
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.adapters.deepprofiler_project',
        primary_outputs={
            'project_root': project_result.project_root,
            'project_manifest_path': project_result.manifest_path,
            'config_path': project_result.config_path,
            'metadata_path': project_result.metadata_path,
            'locations_root': project_result.locations_root,
            'export_root': resolved_export_root,
            'export_manifest_path': export_result.manifest_path if export_result is not None else (resolved_export_root / 'manifest.json'),
        },
        details=details,
        ok=True,
    )


def _run_build_deepprofiler_project(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.adapters.deepprofiler_project import build_deepprofiler_project

    result = build_deepprofiler_project(
        context.config,
        output_dir=context.run_root,
        workflow_root=context.workflow_root,
        export_root=context.export_root,
        experiment_name=context.experiment_name,
        config_filename=context.config_filename,
        metadata_filename=context.metadata_filename,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.adapters.deepprofiler_project',
        primary_outputs={
            'project_root': result.project_root,
            'project_manifest_path': result.manifest_path,
            'config_path': result.config_path,
            'metadata_path': result.metadata_path,
            'locations_root': result.locations_root,
        },
        details=_json_ready(result),
        ok=True,
    )


def _run_deepprofiler(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.adapters.deepprofiler_features import collect_deepprofiler_features
    from cellpaint_pipeline.adapters.deepprofiler_project import run_deepprofiler_profile
    from cellpaint_pipeline.deepprofiler_pipeline import deepprofiler_pipeline_result_to_dict, run_deepprofiler_pipeline

    if context.project_root is not None:
        profile_result = run_deepprofiler_profile(
            context.config,
            project_root=context.project_root,
            experiment_name=context.experiment_name,
            config_filename=context.config_filename,
            metadata_filename=context.metadata_filename,
            gpu=context.gpu,
        )
        if profile_result.returncode != 0:
            return _finalize_skill_result(
                context,
                implementation='cellpaint_pipeline.adapters.deepprofiler_project',
                primary_outputs={
                    'project_root': profile_result.project_root,
                    'feature_dir': profile_result.feature_dir,
                    'log_path': profile_result.log_path,
                },
                details={'profile': _json_ready(profile_result)},
                ok=False,
            )
        collection_result = collect_deepprofiler_features(
            context.config,
            project_root=context.project_root,
            output_dir=context.run_root / 'deepprofiler_tables',
            experiment_name=context.experiment_name,
        )
        return _finalize_skill_result(
            context,
            implementation='cellpaint_pipeline.adapters.deepprofiler_features',
            primary_outputs={
                'project_root': profile_result.project_root,
                'feature_dir': profile_result.feature_dir,
                'single_cell_parquet_path': collection_result.single_cell_parquet_path,
                'single_cell_csv_gz_path': collection_result.single_cell_csv_gz_path,
                'well_aggregated_parquet_path': collection_result.well_aggregated_parquet_path,
                'well_aggregated_csv_gz_path': collection_result.well_aggregated_csv_gz_path,
                'feature_manifest_path': collection_result.manifest_path,
                'log_path': profile_result.log_path,
            },
            details={
                'profile': _json_ready(profile_result),
                'collection': _json_ready(collection_result),
            },
            ok=True,
        )

    result = run_deepprofiler_pipeline(
        context.config,
        output_dir=context.run_root,
        workflow_root=context.workflow_root,
        image_csv_path=context.image_csv_path,
        nuclei_csv_path=context.nuclei_csv_path,
        load_data_csv_path=context.load_data_csv_path,
        experiment_name=context.experiment_name,
        config_filename=context.config_filename,
        metadata_filename=context.metadata_filename,
        gpu=context.gpu,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.deepprofiler_pipeline',
        primary_outputs={
            'project_root': result.project_root,
            'feature_dir': result.feature_dir,
            'collection_output_dir': result.collection_output_dir,
            'pipeline_manifest_path': result.manifest_path,
            'collection_manifest_path': result.collection_manifest_path,
        },
        details=deepprofiler_pipeline_result_to_dict(result),
        ok=result.ok,
    )


def _run_summarize_deepprofiler_profiles(context: SkillRuntimeContext) -> PipelineSkillResult:
    result = summarize_deepprofiler_profiles(
        output_dir=context.run_root,
        single_cell_parquet_path=context.single_cell_parquet_path,
        well_aggregated_parquet_path=context.well_aggregated_parquet_path,
        manifest_path=context.manifest_path,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.profile_summaries',
        primary_outputs={
            'summary_path': result.summary_path,
            'well_metadata_summary_path': result.well_metadata_summary_path,
            'top_variable_features_path': result.top_variable_features_path,
            'pca_coordinates_path': result.pca_coordinates_path,
            'pca_plot_path': result.pca_plot_path,
        },
        details=_json_ready(result),
        ok=True,
    )


def _run_deepprofiler_profile(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.adapters.deepprofiler_project import run_deepprofiler_profile

    resolved_project_root = context.project_root or context.config.deepprofiler_project_root
    result = run_deepprofiler_profile(
        context.config,
        project_root=resolved_project_root,
        experiment_name=context.experiment_name,
        config_filename=context.config_filename,
        metadata_filename=context.metadata_filename,
        gpu=context.gpu,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.adapters.deepprofiler_project',
        primary_outputs={
            'project_root': result.project_root,
            'feature_dir': result.feature_dir,
            'checkpoint_dir': result.checkpoint_dir,
            'log_path': result.log_path,
        },
        details=_json_ready(result),
        ok=result.returncode == 0,
    )


def _run_collect_deepprofiler_features(context: SkillRuntimeContext) -> PipelineSkillResult:
    from cellpaint_pipeline.adapters.deepprofiler_features import collect_deepprofiler_features

    resolved_project_root = context.project_root or context.config.deepprofiler_project_root
    result = collect_deepprofiler_features(
        context.config,
        project_root=resolved_project_root,
        output_dir=context.run_root,
        experiment_name=context.experiment_name,
    )
    return _finalize_skill_result(
        context,
        implementation='cellpaint_pipeline.adapters.deepprofiler_features',
        primary_outputs={
            'single_cell_parquet_path': result.single_cell_parquet_path,
            'single_cell_csv_gz_path': result.single_cell_csv_gz_path,
            'well_aggregated_parquet_path': result.well_aggregated_parquet_path,
            'well_aggregated_csv_gz_path': result.well_aggregated_csv_gz_path,
            'field_summary_path': result.field_summary_path,
            'feature_manifest_path': result.manifest_path,
        },
        details=_json_ready(result),
        ok=True,
    )


SKILL_RUNNERS: dict[str, Callable[[SkillRuntimeContext], PipelineSkillResult]] = {
    'inspect-cellpainting-data': _run_inspect_cellpainting_data,
    'download-cellpainting-data': _run_download_cellpainting_data,
    'run-cellprofiler-profiling': _run_cellprofiler_profiling,
    'export-single-cell-measurements': _run_export_single_cell_measurements,
    'run-pycytominer': _run_pycytominer,
    'summarize-classical-profiles': _run_summarize_classical_profiles,
    'run-segmentation-masks': _run_segmentation_masks,
    'generate-sample-previews': _run_generate_sample_previews,
    'export-single-cell-crops': _run_export_single_cell_crops,
    'prepare-deepprofiler-project': _run_prepare_deepprofiler_project,
    'run-deepprofiler': _run_deepprofiler,
    'summarize-deepprofiler-profiles': _run_summarize_deepprofiler_profiles,
    'export-masked-single-cell-crops': _run_export_masked_single_cell_crops,
    'export-unmasked-single-cell-crops': _run_export_unmasked_single_cell_crops,
    'export-deepprofiler-inputs': _run_export_deepprofiler_inputs,
    'build-deepprofiler-project': _run_build_deepprofiler_project,
    'run-deepprofiler-profile': _run_deepprofiler_profile,
    'collect-deepprofiler-features': _run_collect_deepprofiler_features,
}


def _finalize_skill_result(
    context: SkillRuntimeContext,
    *,
    implementation: str,
    primary_outputs: dict[str, Path | None],
    details: dict[str, Any],
    ok: bool,
) -> PipelineSkillResult:
    manifest_path = context.run_root / 'pipeline_skill_manifest.json'
    manifest_payload = {
        'implementation': implementation,
        'generated_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'skill': pipeline_skill_definition_to_dict(context.definition),
        'output_dir': str(context.run_root),
        'primary_outputs': {key: str(value) if value is not None else None for key, value in primary_outputs.items()},
        'details': details,
        'ok': ok,
    }
    manifest_path.write_text(json.dumps(manifest_payload, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    return PipelineSkillResult(
        skill_key=context.definition.key,
        category=context.definition.category,
        implementation=implementation,
        output_dir=context.run_root,
        manifest_path=manifest_path,
        primary_outputs=primary_outputs,
        details=details,
        ok=ok,
    )


def _resolve_segmentation_source_config(context: SkillRuntimeContext) -> ProjectConfig:
    if context.workflow_root is None:
        return context.config
    payload = context.config.load_segmentation_backend_payload()
    payload['paths']['load_data_csv'] = str(context.workflow_root / 'load_data_for_segmentation.csv')
    payload['paths']['cellprofiler_output_dir'] = str(context.workflow_root / 'cellprofiler_masks')
    runtime_config_path = context.run_root / 'segmentation_source_config.json'
    runtime_config_path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    return replace(context.config, segmentation_backend_config=runtime_config_path)


def _build_isolated_segmentation_skill_config(
    config: ProjectConfig,
    *,
    workflow_root: Path,
    load_data_path: Path,
    pipeline_path: Path,
) -> ProjectConfig:
    payload = config.load_segmentation_backend_payload()
    payload['project_name'] = f'{config.project_name}_skill_mask_export'
    payload['paths']['load_data_csv'] = str(load_data_path)
    payload['paths']['mask_export_pipeline'] = str(pipeline_path)
    payload['paths']['cellprofiler_output_dir'] = str(workflow_root / 'cellprofiler_masks')
    payload['paths']['sample_previews_dir'] = str(workflow_root / 'sample_previews_png')
    payload['paths']['masked_crops_dir'] = str(workflow_root / 'masked')
    payload['paths']['masked_manifest_csv'] = str(workflow_root / 'masked' / 'single_cell_manifest.csv')
    payload['paths']['unmasked_crops_dir'] = str(workflow_root / 'unmasked')
    payload['paths']['unmasked_manifest_csv'] = str(workflow_root / 'unmasked' / 'single_cell_manifest.csv')
    runtime_payload = dict(config.mask_export_runtime)
    runtime_payload['work_root'] = str(workflow_root / '.mask_export_sharded_work')
    payload['mask_export_runtime'] = runtime_payload
    runtime_config_path = workflow_root / 'segmentation_workflow_config.json'
    runtime_config_path.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    return replace(config, segmentation_backend_config=runtime_config_path)


def _execution_result_to_dict(result: ExecutionResult) -> dict[str, Any]:
    return {
        'label': result.label,
        'command': list(result.command),
        'cwd': str(result.cwd) if result.cwd is not None else None,
        'log_path': str(result.log_path) if result.log_path is not None else None,
        'returncode': result.returncode,
    }


def _json_ready(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if is_dataclass(value):
        return _json_ready(asdict(value))
    if isinstance(value, dict):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    return value
