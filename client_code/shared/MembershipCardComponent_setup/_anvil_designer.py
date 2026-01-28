from __future__ import annotations
from anvil import *  # type: ignore


class MembershipCardComponent_setupTemplate(ColumnPanel):
    """Material 3 scaffold template for MembershipCardComponent_setup."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
