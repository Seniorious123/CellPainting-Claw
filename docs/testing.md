# Testing

The repository test strategy is currently split into two tiers.

## `fast`

Purpose: quick regression coverage for routine changes.

Coverage focus:

- config contract
- public API catalog and dispatcher
- orchestration
- presets
- skills

Run:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline.test_suites fast
```

Or, after installation:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
cellpaint-pipeline-tests fast
```

## `extended`

Purpose: broader validation before a release or after changes to delivery, segmentation, or DeepProfiler integration.

Coverage focus:

- everything in `fast`
- delivery smoke tests
- minimal real profiling and segmentation branch checks
- current DeepProfiler branch smoke coverage

Run:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline.test_suites extended
```

Or, after installation:

```bash
cd /root/pipeline/cellpaint_pipeline_lib
cellpaint-pipeline-tests extended
```

## List Available Suites

```bash
cd /root/pipeline/cellpaint_pipeline_lib
PYTHONPATH=src /root/miniconda3/envs/lyx_env/bin/python -m cellpaint_pipeline.test_suites --list
```

## Recommended Practice

- run `fast` during normal development
- run `extended` before publication or after changes to delivery, DeepProfiler, or agent-facing integration
- documentation-only edits do not require `extended` every time
