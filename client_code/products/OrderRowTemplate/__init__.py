"""Scaffold Form for OrderRowTemplate."""

from __future__ import annotations
from ._anvil_designer import OrderRowTemplateTemplate
import anvil  # type: ignore


class OrderRowTemplate(OrderRowTemplateTemplate):
    """Material 3 ready scaffold for OrderRowTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
