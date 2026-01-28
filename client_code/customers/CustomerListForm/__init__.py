"""Scaffold Form for CustomerListForm."""

from __future__ import annotations
from ._anvil_designer import CustomerListFormTemplate
import anvil  # type: ignore


class CustomerListForm(CustomerListFormTemplate):
    """Material 3 ready scaffold for CustomerListForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
