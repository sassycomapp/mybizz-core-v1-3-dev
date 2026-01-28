"""Scaffold Form for FeaturesTab."""

from __future__ import annotations
from ._anvil_designer import FeaturesTabTemplate
import anvil  # type: ignore


class FeaturesTab(FeaturesTabTemplate):
    """Material 3 ready scaffold for FeaturesTab."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
