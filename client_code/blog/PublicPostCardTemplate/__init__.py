"""Scaffold Form for PublicPostCardTemplate."""

from __future__ import annotations
from ._anvil_designer import PublicPostCardTemplateTemplate
import anvil  # type: ignore


class PublicPostCardTemplate(PublicPostCardTemplateTemplate):
    """Material 3 ready scaffold for PublicPostCardTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
