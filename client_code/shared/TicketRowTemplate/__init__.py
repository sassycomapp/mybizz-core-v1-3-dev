"""Scaffold Form for TicketRowTemplate."""

from __future__ import annotations
from ._anvil_designer import TicketRowTemplateTemplate
import anvil  # type: ignore


class TicketRowTemplate(TicketRowTemplateTemplate):
    """Material 3 ready scaffold for TicketRowTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
