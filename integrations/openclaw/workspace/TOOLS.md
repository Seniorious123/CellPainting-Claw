# Tools

Important local paths:

- repo root: `/root/pipeline/cellpaint_pipeline_lib`
- example config: `/root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json`
- Python interpreter: `/root/miniconda3/envs/lyx_env/bin/python`

Preferred CLI form:

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline <command> ...
```

Preferred discovery commands:

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline list-mcp-tools
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline show-public-api-contract
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline list-pipeline-skills
```

Preferred execution commands:

```bash
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-pipeline-skill --config /root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json --skill run-full-workflow
/root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline run-public-api-entrypoint --config /root/pipeline/cellpaint_pipeline_lib/configs/project_config.example.json --entrypoint run_end_to_end_pipeline
```

Optional MCP mode:

```bash
/root/pipeline/cellpaint_pipeline_lib/integrations/openclaw/start_cellpaint_mcp_http.sh
```
