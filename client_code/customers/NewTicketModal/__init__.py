"""Scaffold Form for NewTicketModal."""

from __future__ import annotations
from ._anvil_designer import NewTicketModalTemplate
import anvil  # type: ignore


class NewTicketModal(NewTicketModalTemplate):
    """Material 3 ready scaffold for NewTicketModal."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
