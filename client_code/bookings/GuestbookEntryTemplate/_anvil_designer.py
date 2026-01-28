from __future__ import annotations
from anvil import *  # type: ignore


class GuestbookEntryTemplateTemplate(ColumnPanel):
    """Material 3 scaffold template for GuestbookEntryTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
