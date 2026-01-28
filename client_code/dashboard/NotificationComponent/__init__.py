"""Scaffold Form for NotificationComponent."""

from __future__ import annotations
from ._anvil_designer import NotificationComponentTemplate
import anvil  # type: ignore


class NotificationComponent(NotificationComponentTemplate):
    """Material 3 ready scaffold for NotificationComponent."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
