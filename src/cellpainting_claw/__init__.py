"""Public CellPainting-Claw compatibility layer."""

from cellpaint_pipeline import *  # noqa: F401,F403
from cellpaint_pipeline import __all__ as _legacy_all
from cellpaint_pipeline import __version__

__all__ = list(_legacy_all)
