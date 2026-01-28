"""Scaffold Form for DocumentTemplate."""

from __future__ import annotations
from ._anvil_designer import DocumentTemplateTemplate
import anvil  # type: ignore


class DocumentTemplate(DocumentTemplateTemplate):
    """Material 3 ready scaffold for DocumentTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
