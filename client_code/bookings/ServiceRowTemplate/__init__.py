"""Scaffold Form for ServiceRowTemplate."""

from __future__ import annotations
from ._anvil_designer import ServiceRowTemplateTemplate
import anvil  # type: ignore


class ServiceRowTemplate(ServiceRowTemplateTemplate):
    """Material 3 ready scaffold for ServiceRowTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
