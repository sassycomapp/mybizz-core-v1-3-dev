"""Scaffold Form for GuestbookForm."""

from __future__ import annotations
from ._anvil_designer import GuestbookFormTemplate
import anvil  # type: ignore


class GuestbookForm(GuestbookFormTemplate):
    """Material 3 ready scaffold for GuestbookForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
