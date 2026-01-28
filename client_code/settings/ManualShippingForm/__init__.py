"""Scaffold Form for ManualShippingForm."""

from __future__ import annotations
from ._anvil_designer import ManualShippingFormTemplate
import anvil  # type: ignore


class ManualShippingForm(ManualShippingFormTemplate):
    """Material 3 ready scaffold for ManualShippingForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
