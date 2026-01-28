from __future__ import annotations
from anvil import *  # type: ignore


class BookingCalendarComponentTemplate(ColumnPanel):
    """Material 3 scaffold template for BookingCalendarComponent."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
