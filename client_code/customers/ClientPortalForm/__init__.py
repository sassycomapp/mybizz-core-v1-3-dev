"""Scaffold Form for ClientPortalForm."""

from __future__ import annotations
from ._anvil_designer import ClientPortalFormTemplate
import anvil  # type: ignore


class ClientPortalForm(ClientPortalFormTemplate):
    """Material 3 ready scaffold for ClientPortalForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
