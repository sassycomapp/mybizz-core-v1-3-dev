"""Scaffold Form for BusinessProfileTab."""

from __future__ import annotations
from ._anvil_designer import BusinessProfileTabTemplate
import anvil  # type: ignore


class BusinessProfileTab(BusinessProfileTabTemplate):
    """Material 3 ready scaffold for BusinessProfileTab."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
