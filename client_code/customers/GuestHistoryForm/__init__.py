"""Scaffold Form for GuestHistoryForm."""

from __future__ import annotations
from ._anvil_designer import GuestHistoryFormTemplate
import anvil  # type: ignore


class GuestHistoryForm(GuestHistoryFormTemplate):
    """Material 3 ready scaffold for GuestHistoryForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
