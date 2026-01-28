"""Scaffold Form for ReviewDisplayComponent."""

from __future__ import annotations
from ._anvil_designer import ReviewDisplayComponentTemplate
import anvil  # type: ignore


class ReviewDisplayComponent(ReviewDisplayComponentTemplate):
    """Material 3 ready scaffold for ReviewDisplayComponent."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
