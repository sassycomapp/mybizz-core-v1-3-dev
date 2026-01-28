"""Scaffold Form for VariantManager."""

from __future__ import annotations
from ._anvil_designer import VariantManagerTemplate
import anvil  # type: ignore


class VariantManager(VariantManagerTemplate):
    """Material 3 ready scaffold for VariantManager."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
