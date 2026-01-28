"""Scaffold Form for EmailSetupForm."""

from __future__ import annotations
from ._anvil_designer import EmailSetupFormTemplate
import anvil  # type: ignore


class EmailSetupForm(EmailSetupFormTemplate):
    """Material 3 ready scaffold for EmailSetupForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
