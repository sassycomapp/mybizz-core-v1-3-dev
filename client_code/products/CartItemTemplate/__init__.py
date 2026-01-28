"""Scaffold Form for CartItemTemplate."""

from __future__ import annotations
from ._anvil_designer import CartItemTemplateTemplate
import anvil  # type: ignore


class CartItemTemplate(CartItemTemplateTemplate):
    """Material 3 ready scaffold for CartItemTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
