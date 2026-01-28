from __future__ import annotations
from anvil import *  # type: ignore


class SocialShareComponentTemplate(ColumnPanel):
    """Material 3 scaffold template for SocialShareComponent."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
