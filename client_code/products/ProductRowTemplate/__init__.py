"""Scaffold Form for ProductRowTemplate."""

from __future__ import annotations
from ._anvil_designer import ProductRowTemplateTemplate
import anvil  # type: ignore


class ProductRowTemplate(ProductRowTemplateTemplate):
    """Material 3 ready scaffold for ProductRowTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
