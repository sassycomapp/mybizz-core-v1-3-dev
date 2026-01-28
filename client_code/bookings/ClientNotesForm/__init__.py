"""Scaffold Form for ClientNotesForm."""

from __future__ import annotations
from ._anvil_designer import ClientNotesFormTemplate
import anvil  # type: ignore


class ClientNotesForm(ClientNotesFormTemplate):
    """Material 3 ready scaffold for ClientNotesForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
