# Tools

Important local paths:

- repo root: `/root/pipeline/CellPainting-Claw`
- example config: `/root/pipeline/CellPainting-Claw/configs/project_config.example.json`
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
$PYTHON_BIN -m cellpainting_claw run-pipeline-skill --config /root/pipeline/CellPainting-Claw/configs/project_config.example.json --skill run-full-workflow
$PYTHON_BIN -m cellpainting_claw run-public-api-entrypoint --config /root/pipeline/CellPainting-Claw/configs/project_config.example.json --entrypoint run_end_to_end_pipeline
```

Optional MCP mode:

```bash
/root/pipeline/CellPainting-Claw/integrations/openclaw/start_cellpaint_mcp_http.sh
```
