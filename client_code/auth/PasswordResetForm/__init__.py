"""Scaffold Form for PasswordResetForm."""

from __future__ import annotations
from ._anvil_designer import PasswordResetFormTemplate
import anvil  # type: ignore


class PasswordResetForm(PasswordResetFormTemplate):
    """Material 3 ready scaffold for PasswordResetForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
