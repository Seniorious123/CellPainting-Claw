from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / 'src'
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

project = 'CellPainting-Claw'
author = 'OpenAI Codex'
release = '0.1.0'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
]

source_suffix = {
    '.md': 'myst',
    '.rst': 'restructuredtext',
}
master_doc = 'index'
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'export/**',
    'skill_catalog_draft.md',
    'cppipe_customization_design.md',
]
templates_path = ['_templates']

autodoc_member_order = 'bysource'
autosummary_generate = False
autodoc_mock_imports = [
    'mcp',
    'boto3',
    'botocore',
    'cpgdata',
    'quilt3',
    'deepprofiler',
    'tensorflow',
    'tensorflow_addons',
]

myst_enable_extensions = [
    'colon_fence',
    'deflist',
    'fieldlist',
]
myst_heading_anchors = 3

html_theme = 'furo'
html_title = 'CellPainting-Claw'
html_static_path = []
