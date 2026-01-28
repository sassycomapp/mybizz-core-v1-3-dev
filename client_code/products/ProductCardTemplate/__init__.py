"""Scaffold Form for ProductCardTemplate."""

from __future__ import annotations
from ._anvil_designer import ProductCardTemplateTemplate
import anvil  # type: ignore


class ProductCardTemplate(ProductCardTemplateTemplate):
    """Material 3 ready scaffold for ProductCardTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
