"""Scaffold Form for ManualTimeEntryModal."""

from __future__ import annotations
from ._anvil_designer import ManualTimeEntryModalTemplate
import anvil  # type: ignore


class ManualTimeEntryModal(ManualTimeEntryModalTemplate):
    """Material 3 ready scaffold for ManualTimeEntryModal."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
