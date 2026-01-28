from __future__ import annotations
from anvil import *  # type: ignore


class CartItemTemplateTemplate(ColumnPanel):
    """Material 3 scaffold template for CartItemTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
