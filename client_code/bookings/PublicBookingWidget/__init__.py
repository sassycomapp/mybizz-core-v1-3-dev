"""Scaffold Form for PublicBookingWidget."""

from __future__ import annotations
from ._anvil_designer import PublicBookingWidgetTemplate
import anvil  # type: ignore


class PublicBookingWidget(PublicBookingWidgetTemplate):
    """Material 3 ready scaffold for PublicBookingWidget."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
