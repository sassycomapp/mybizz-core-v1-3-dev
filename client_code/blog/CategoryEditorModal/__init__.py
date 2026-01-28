"""Scaffold Form for CategoryEditorModal."""

from __future__ import annotations
from ._anvil_designer import CategoryEditorModalTemplate
import anvil  # type: ignore


class CategoryEditorModal(CategoryEditorModalTemplate):
    """Material 3 ready scaffold for CategoryEditorModal."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
