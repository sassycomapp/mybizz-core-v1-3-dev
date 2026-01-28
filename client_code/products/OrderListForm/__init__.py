"""Scaffold Form for OrderListForm."""

from __future__ import annotations
from ._anvil_designer import OrderListFormTemplate
import anvil  # type: ignore


class OrderListForm(OrderListFormTemplate):
    """Material 3 ready scaffold for OrderListForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
