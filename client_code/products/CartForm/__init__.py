"""Scaffold Form for CartForm."""

from __future__ import annotations
from ._anvil_designer import CartFormTemplate
import anvil  # type: ignore


class CartForm(CartFormTemplate):
    """Material 3 ready scaffold for CartForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
