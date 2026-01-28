"""Scaffold Form for CurrencyTab."""

from __future__ import annotations
from ._anvil_designer import CurrencyTabTemplate
import anvil  # type: ignore


class CurrencyTab(CurrencyTabTemplate):
    """Material 3 ready scaffold for CurrencyTab."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
