"""Scaffold Form for NavigationComponent."""

from __future__ import annotations
from ._anvil_designer import NavigationComponentTemplate
import anvil  # type: ignore


class NavigationComponent(NavigationComponentTemplate):
    """Material 3 ready scaffold for NavigationComponent."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
