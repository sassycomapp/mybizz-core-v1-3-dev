from __future__ import annotations
from anvil import *  # type: ignore


class PasswordResetFormTemplate(ColumnPanel):
    """Material 3 scaffold template for PasswordResetForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
