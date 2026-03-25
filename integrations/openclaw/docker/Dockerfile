FROM condaforge/miniforge3:24.11.0-0

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    git \
    tini \
 && rm -rf /var/lib/apt/lists/*

RUN useradd --create-home --shell /bin/bash --uid 1000 cellpaint

WORKDIR /opt/cellpaint_pipeline_lib
COPY . /opt/cellpaint_pipeline_lib

RUN conda env create -f /opt/cellpaint_pipeline_lib/environment/lyx_env_reference.yml \
 && conda clean -afy

RUN /opt/conda/envs/lyx_env/bin/pip install -e /opt/cellpaint_pipeline_lib[mcp,data-access,test]

USER cellpaint
ENV HOME=/home/cellpaint
ENV PATH=/home/cellpaint/.local/bin:/opt/conda/envs/lyx_env/bin:/opt/conda/bin:$PATH

RUN curl -fsSL https://openclaw.ai/install-cli.sh | bash -s -- --no-onboard

WORKDIR /workspace/state/openclaw/workspace
ENTRYPOINT ["/usr/bin/tini", "--", "/opt/cellpaint_pipeline_lib/integrations/openclaw/docker/entrypoint.sh"]
CMD ["gateway"]
