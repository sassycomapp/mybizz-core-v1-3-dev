"""Scaffold Form for ReviewModerationForm."""

from __future__ import annotations
from ._anvil_designer import ReviewModerationFormTemplate
import anvil  # type: ignore


class ReviewModerationForm(ReviewModerationFormTemplate):
    """Material 3 ready scaffold for ReviewModerationForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
