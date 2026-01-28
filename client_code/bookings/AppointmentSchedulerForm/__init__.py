"""Scaffold Form for AppointmentSchedulerForm."""

from __future__ import annotations
from ._anvil_designer import AppointmentSchedulerFormTemplate
import anvil  # type: ignore


class AppointmentSchedulerForm(AppointmentSchedulerFormTemplate):
    """Material 3 ready scaffold for AppointmentSchedulerForm."""

    def __init__(self, **properties):
        super().__init__(**properties)
        # TODO: Implement UI bindings following M3 and coding standards.
