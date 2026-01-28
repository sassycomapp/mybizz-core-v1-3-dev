"""Scaffold Form for ThemeTab."""

from __future__ import annotations
from ._anvil_designer import ThemeTabTemplate
import anvil  # type: ignore


class ThemeTab(ThemeTabTemplate):
    """Material 3 ready scaffold for ThemeTab."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
