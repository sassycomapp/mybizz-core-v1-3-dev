"""Scaffold Form for InvoiceListForm."""

from __future__ import annotations
from ._anvil_designer import InvoiceListFormTemplate
import anvil  # type: ignore


class InvoiceListForm(InvoiceListFormTemplate):
    """Material 3 ready scaffold for InvoiceListForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
