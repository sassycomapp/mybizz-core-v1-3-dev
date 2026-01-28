"""Scaffold Form for ActivityItemTemplate."""

from __future__ import annotations
from ._anvil_designer import ActivityItemTemplateTemplate
import anvil  # type: ignore


class ActivityItemTemplate(ActivityItemTemplateTemplate):
    """Material 3 ready scaffold for ActivityItemTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
