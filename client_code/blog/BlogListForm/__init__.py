"""Scaffold Form for BlogListForm."""

from __future__ import annotations
from ._anvil_designer import BlogListFormTemplate
import anvil  # type: ignore


class BlogListForm(BlogListFormTemplate):
    """Material 3 ready scaffold for BlogListForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
