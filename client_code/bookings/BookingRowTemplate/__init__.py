"""Scaffold Form for BookingRowTemplate."""

from __future__ import annotations
from ._anvil_designer import BookingRowTemplateTemplate
import anvil  # type: ignore


class BookingRowTemplate(BookingRowTemplateTemplate):
    """Material 3 ready scaffold for BookingRowTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
