"""Scaffold Form for ReviewSubmissionForm."""

from __future__ import annotations
from ._anvil_designer import ReviewSubmissionFormTemplate
import anvil  # type: ignore


class ReviewSubmissionForm(ReviewSubmissionFormTemplate):
    """Material 3 ready scaffold for ReviewSubmissionForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
