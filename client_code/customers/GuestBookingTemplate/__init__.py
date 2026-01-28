"""Scaffold Form for GuestBookingTemplate."""

from __future__ import annotations
from ._anvil_designer import GuestBookingTemplateTemplate
import anvil  # type: ignore


class GuestBookingTemplate(GuestBookingTemplateTemplate):
    """Material 3 ready scaffold for GuestBookingTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
