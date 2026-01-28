"""Scaffold Form for SignupForm."""

from __future__ import annotations
from ._anvil_designer import SignupFormTemplate
import anvil  # type: ignore


class SignupForm(SignupFormTemplate):
    """Material 3 ready scaffold for SignupForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
