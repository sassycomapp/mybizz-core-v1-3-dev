"""Scaffold Form for GuestNoteTemplate."""

from __future__ import annotations
from ._anvil_designer import GuestNoteTemplateTemplate
import anvil  # type: ignore


class GuestNoteTemplate(GuestNoteTemplateTemplate):
    """Material 3 ready scaffold for GuestNoteTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
