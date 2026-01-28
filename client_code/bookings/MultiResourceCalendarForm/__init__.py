"""Scaffold Form for MultiResourceCalendarForm."""

from __future__ import annotations
from ._anvil_designer import MultiResourceCalendarFormTemplate
import anvil  # type: ignore


class MultiResourceCalendarForm(MultiResourceCalendarFormTemplate):
    """Material 3 ready scaffold for MultiResourceCalendarForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
