# Installation

## Validated Environment

The reference environment file is:

- `environment/cellpainting-claw.environment.yml`

It includes the validated stack used for:

- CellProfiler execution
- pycytominer profiling
- DeepProfiler full-stack validation
- the test suite
- optional data-access helpers such as `boto3`, `quilt3`, `cpgdata`, and `awscli`

## Create the Environment

```bash
cd <repo-root>
conda env create -f environment/cellpainting-claw.environment.yml
conda activate cellpainting-claw
```

If you already have a working `cellpainting-claw`, you can reuse it.

## Install the Library

Editable installation:

```bash
cd <repo-root>
pip install -e .
```

Optional extras:

```bash
pip install -e .[test]
pip install -e .[deepprofiler,test]
pip install -e .[data-access,test]
pip install -e .[mcp]
```

Source-only execution without editable installation also works:

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw --help
```

## Minimal Post-Install Checks

Validate the example project config:

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw show-config \
  --config configs/project_config.example.json
```

Run the smoke test:

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw smoke-test \
  --config configs/project_config.example.json \
  --output-path outputs/smoke_test_report.json
```

A healthy smoke test confirms that:

- the project config parses successfully
- backend roots resolve correctly
- validation artifacts are readable
- workflow manifests are readable

## Recommended Test Commands

```bash
cd <repo-root>
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw.test_suites fast
PYTHONPATH=src $PYTHON_BIN -m cellpainting_claw.test_suites extended
```

## Data-Access Note

`awscli` is currently included in the validated environment because the data-access layer can use it together with `cpgdata`.

If you later observe environment friction around `docutils` or CellProfiler command-line behavior, split data-access utilities into a dedicated environment rather than weakening the main workflow contract.
