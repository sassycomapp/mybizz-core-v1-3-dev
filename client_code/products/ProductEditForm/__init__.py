"""Scaffold Form for ProductEditForm."""

from __future__ import annotations
from ._anvil_designer import ProductEditFormTemplate
import anvil  # type: ignore


class ProductEditForm(ProductEditFormTemplate):
    """Material 3 ready scaffold for ProductEditForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
