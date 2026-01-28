"""Scaffold Form for PublicCategoryTemplate."""

from __future__ import annotations
from ._anvil_designer import PublicCategoryTemplateTemplate
import anvil  # type: ignore


class PublicCategoryTemplate(PublicCategoryTemplateTemplate):
    """Material 3 ready scaffold for PublicCategoryTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
