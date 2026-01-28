"""Scaffold Form for MessageRowTemplate."""

from __future__ import annotations
from ._anvil_designer import MessageRowTemplateTemplate
import anvil  # type: ignore


class MessageRowTemplate(MessageRowTemplateTemplate):
    """Material 3 ready scaffold for MessageRowTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
