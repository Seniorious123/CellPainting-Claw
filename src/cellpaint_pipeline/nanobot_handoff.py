from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class NanoBotTaskRoute:
    key: str
    user_goal: str
    preferred_tool: str
    preferred_target: str
    reason: str
    params_template: dict[str, Any]


@dataclass(frozen=True)
class NanoBotHandoffSummary:
    agent_name: str
    mcp_server_name: str
    recommended_tool_order: list[str]
    task_routes: list[NanoBotTaskRoute]
    start_commands: dict[str, str]
    local_files: dict[str, str]
    notes: list[str]


def nanobot_recommended_tool_order() -> list[str]:
    return [
        'list_mcp_tools',
        'show_nanobot_handoff',
        'list_pipeline_skills',
        'show_public_api_contract',
        'run_pipeline_skill',
        'run_public_api_entrypoint',
        'run_pipeline_preset',
    ]


def nanobot_task_routes() -> list[NanoBotTaskRoute]:
    return [
        NanoBotTaskRoute(
            key='discover-capabilities',
            user_goal='List what the Cell Painting agent can do before choosing a workflow.',
            preferred_tool='list_mcp_tools',
            preferred_target='MCP discovery catalog',
            reason='Start with the MCP-visible tool list when task intent is still broad or ambiguous.',
            params_template={},
        ),
        NanoBotTaskRoute(
            key='plan-gallery-data',
            user_goal='Inspect gallery data availability and build a reusable download plan.',
            preferred_tool='run_pipeline_skill',
            preferred_target='plan-gallery-data',
            reason='This is already a stable skill-level task and avoids forcing the agent to assemble planning parameters manually.',
            params_template={
                'skill_key': 'plan-gallery-data',
                'config_path': '/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json',
                'params_json': '{"data_request": {"mode": "gallery-prefix", "prefix": "cpg0016-jump/source_4/workspace/", "dry_run": true}}',
            },
        ),
        NanoBotTaskRoute(
            key='run-full-workflow',
            user_goal='Run the standard profiling plus segmentation workflow.',
            preferred_tool='run_pipeline_skill',
            preferred_target='run-full-workflow',
            reason='Skill-level routing is the default high-level path for agent-driven end-to-end execution.',
            params_template={
                'skill_key': 'run-full-workflow',
                'config_path': '/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json',
                'params_json': '{}',
            },
        ),
        NanoBotTaskRoute(
            key='run-deepprofiler-full',
            user_goal='Run the DeepProfiler full-stack branch from the standardized pipeline interface.',
            preferred_tool='run_pipeline_skill',
            preferred_target='run-deepprofiler-full',
            reason='The skill key already captures the intended DeepProfiler branch without exposing internal workflow names.',
            params_template={
                'skill_key': 'run-deepprofiler-full',
                'config_path': '/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json',
                'params_json': '{}',
            },
        ),
        NanoBotTaskRoute(
            key='direct-public-entrypoint',
            user_goal='Call one stable public API entrypoint when the exact operation is already known.',
            preferred_tool='run_public_api_entrypoint',
            preferred_target='run_end_to_end_pipeline or another public entrypoint',
            reason='Use this when the agent has already resolved the exact stable public API contract and does not need the task aliases from skills.',
            params_template={
                'entrypoint': 'run_end_to_end_pipeline',
                'params': {'include_validation_report': True},
                'config': '/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json',
            },
        ),
    ]


def nanobot_handoff_summary() -> NanoBotHandoffSummary:
    repo_root = Path(__file__).resolve().parents[2]
    integrations_root = repo_root / 'integrations' / 'nanobot'
    return NanoBotHandoffSummary(
        agent_name='Cell Painting Operator',
        mcp_server_name='cellpaint-pipeline',
        recommended_tool_order=nanobot_recommended_tool_order(),
        task_routes=nanobot_task_routes(),
        start_commands={
            'start_mcp_http': 'cd /root/pipeline/cellpaint_pipeline_lib/integrations/nanobot && ./start_cellpaint_mcp_http.sh',
            'run_nanobot_local': 'cd /root/pipeline/cellpaint_pipeline_lib/integrations/nanobot && ./run_nanobot_local.sh',
        },
        local_files={
            'quickstart': str(integrations_root / 'quickstart.md'),
            'single_file_example': str(integrations_root / 'nanobot.yaml.example'),
            'single_file_local_http': str(integrations_root / 'nanobot.local.http.yaml'),
            'directory_config': str(integrations_root / 'local_config'),
            'agent_instructions': str(integrations_root / 'local_config' / 'agents' / 'main.md'),
            'mcp_server_config': str(integrations_root / 'local_config' / 'mcp-servers.yaml'),
        },
        notes=[
            'Prefer skill-level execution for common goals such as full workflow runs and DeepProfiler runs.',
            'Prefer public API dispatch only when the exact stable entrypoint is already known.',
            'NanoBot still needs a model API key to complete natural-language conversations.',
        ],
    )


def nanobot_task_route_to_dict(route: NanoBotTaskRoute) -> dict[str, Any]:
    return {
        'key': route.key,
        'user_goal': route.user_goal,
        'preferred_tool': route.preferred_tool,
        'preferred_target': route.preferred_target,
        'reason': route.reason,
        'params_template': route.params_template,
    }


def nanobot_handoff_summary_to_dict(summary: NanoBotHandoffSummary | None = None) -> dict[str, Any]:
    resolved = summary or nanobot_handoff_summary()
    return {
        'agent_name': resolved.agent_name,
        'mcp_server_name': resolved.mcp_server_name,
        'recommended_tool_order': list(resolved.recommended_tool_order),
        'task_routes': [nanobot_task_route_to_dict(route) for route in resolved.task_routes],
        'start_commands': dict(resolved.start_commands),
        'local_files': dict(resolved.local_files),
        'notes': list(resolved.notes),
    }
