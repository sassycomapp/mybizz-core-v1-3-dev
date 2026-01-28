"""Scaffold Form for LoginForm."""

from __future__ import annotations
from ._anvil_designer import LoginFormTemplate
import anvil  # type: ignore


class LoginForm(LoginFormTemplate):
    """Material 3 ready scaffold for LoginForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
