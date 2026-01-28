"""Scaffold Form for BookingCreateForm."""

from __future__ import annotations
from ._anvil_designer import BookingCreateFormTemplate
import anvil  # type: ignore


class BookingCreateForm(BookingCreateFormTemplate):
    """Material 3 ready scaffold for BookingCreateForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
