"""Scaffold Form for OrderDetailModal."""

from __future__ import annotations
from ._anvil_designer import OrderDetailModalTemplate
import anvil  # type: ignore


class OrderDetailModal(OrderDetailModalTemplate):
    """Material 3 ready scaffold for OrderDetailModal."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
