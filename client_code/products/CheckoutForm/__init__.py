"""Scaffold Form for CheckoutForm."""

from __future__ import annotations
from ._anvil_designer import CheckoutFormTemplate
import anvil  # type: ignore


class CheckoutForm(CheckoutFormTemplate):
    """Material 3 ready scaffold for CheckoutForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
