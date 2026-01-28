"""Scaffold Form for UsersTab."""

from __future__ import annotations
from ._anvil_designer import UsersTabTemplate
import anvil  # type: ignore


class UsersTab(UsersTabTemplate):
    """Material 3 ready scaffold for UsersTab."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
