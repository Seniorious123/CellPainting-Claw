# Command-Line Interface

CellPainting-Claw provides two main public CLI surfaces:

- `cellpainting-claw`
- `cellpainting-skills`

## Main CLI

The main CLI is the broadest public command-line surface. Important commands include:

- `show-config`
- `smoke-test`
- `run-end-to-end-pipeline`
- `run-profiling-suite`
- `run-segmentation-suite`
- `run-workflow`
- `run-deepprofiler-pipeline`

## Skills CLI

The skills CLI is a narrower task-oriented layer. Its main commands are:

- `list`
- `describe`
- `run`

## Examples

```bash
cellpainting-claw --help
cellpainting-claw run-end-to-end-pipeline --config configs/project_config.portable.example.json
cellpainting-skills list
```

The command-line layer mirrors the workflow structure described in the earlier documentation sections.
