"""Scaffold Form for TicketItemTemplate."""

from __future__ import annotations
from ._anvil_designer import TicketItemTemplateTemplate
import anvil  # type: ignore


class TicketItemTemplate(TicketItemTemplateTemplate):
    """Material 3 ready scaffold for TicketItemTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
