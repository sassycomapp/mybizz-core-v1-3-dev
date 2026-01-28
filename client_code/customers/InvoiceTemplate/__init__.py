"""Scaffold Form for InvoiceTemplate."""

from __future__ import annotations
from ._anvil_designer import InvoiceTemplateTemplate
import anvil  # type: ignore


class InvoiceTemplate(InvoiceTemplateTemplate):
    """Material 3 ready scaffold for InvoiceTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
