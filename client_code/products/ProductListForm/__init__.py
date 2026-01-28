"""Scaffold Form for ProductListForm."""

from __future__ import annotations
from ._anvil_designer import ProductListFormTemplate
import anvil  # type: ignore


class ProductListForm(ProductListFormTemplate):
    """Material 3 ready scaffold for ProductListForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
