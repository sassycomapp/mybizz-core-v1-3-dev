"""Scaffold Form for MetricsPanel."""

from __future__ import annotations
from ._anvil_designer import MetricsPanelTemplate
import anvil  # type: ignore


class MetricsPanel(MetricsPanelTemplate):
    """Material 3 ready scaffold for MetricsPanel."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
