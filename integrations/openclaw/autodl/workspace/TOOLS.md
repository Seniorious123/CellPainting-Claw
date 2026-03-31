# Tools

Important local paths:

- repo root: `$REPO_ROOT`
- example config: `$REPO_ROOT/configs/project_config.example.json`
- Python interpreter: `$PYTHON_BIN`

Preferred CLI form:

```bash
$PYTHON_BIN -m cellpainting_claw <command> ...
```

Preferred discovery commands:

```bash
$PYTHON_BIN -m cellpainting_claw list-mcp-tools
$PYTHON_BIN -m cellpainting_claw show-public-api-contract
$PYTHON_BIN -m cellpainting_claw list-pipeline-skills
```

Preferred execution commands:

```bash
$PYTHON_BIN -m cellpainting_claw run-pipeline-skill --config $REPO_ROOT/configs/project_config.example.json --skill run-full-workflow
$PYTHON_BIN -m cellpainting_claw run-public-api-entrypoint --config $REPO_ROOT/configs/project_config.example.json --entrypoint run_end_to_end_pipeline
```

Optional MCP mode:

```bash
$REPO_ROOT/integrations/openclaw/start_cellpaint_mcp_http.sh
```
