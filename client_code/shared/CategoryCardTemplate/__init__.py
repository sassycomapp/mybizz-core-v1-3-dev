"""Scaffold Form for CategoryCardTemplate."""

from __future__ import annotations
from ._anvil_designer import CategoryCardTemplateTemplate
import anvil  # type: ignore


class CategoryCardTemplate(CategoryCardTemplateTemplate):
    """Material 3 ready scaffold for CategoryCardTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
