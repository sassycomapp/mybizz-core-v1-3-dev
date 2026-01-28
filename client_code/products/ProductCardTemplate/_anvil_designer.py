from __future__ import annotations
from anvil import *  # type: ignore


class ProductCardTemplateTemplate(ColumnPanel):
    """Material 3 scaffold template for ProductCardTemplate."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self.init_components(**properties)
