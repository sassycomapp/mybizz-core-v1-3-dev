"""Scaffold Form for BookingListForm."""

from __future__ import annotations
from ._anvil_designer import BookingListFormTemplate
import anvil  # type: ignore


class BookingListForm(BookingListFormTemplate):
    """Material 3 ready scaffold for BookingListForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
