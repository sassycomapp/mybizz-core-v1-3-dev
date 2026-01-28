"""Scaffold Form for KBArticleDetailForm."""

from __future__ import annotations
from ._anvil_designer import KBArticleDetailFormTemplate
import anvil  # type: ignore


class KBArticleDetailForm(KBArticleDetailFormTemplate):
    """Material 3 ready scaffold for KBArticleDetailForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
