"""Scaffold Form for CheckInOutForm."""

from __future__ import annotations
from ._anvil_designer import CheckInOutFormTemplate
import anvil  # type: ignore


class CheckInOutForm(CheckInOutFormTemplate):
    """Material 3 ready scaffold for CheckInOutForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
