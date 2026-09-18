"""SmartCare domain model - Appointment and AppointmentStatus
(FR-03, FR-04, FR-05, FR-09, FR-10, FR-12).
Skeleton only: attributes and operation signatures, no full behaviour yet."""

from enum import Enum


class AppointmentStatus(Enum):
    """The fixed status list (FR-09). The list itself is an assumption to validate."""
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class Appointment:
    """One patient seeing one practitioner at a date and time."""

    def __init__(self, appointment_id, patient, practitioner, date, time):
        self.appointment_id = appointment_id
        self.patient = patient                       # Patient (exactly one)
        self.practitioner = practitioner             # Practitioner (exactly one)
        self.date = date
        self.time = time
        self.status = AppointmentStatus.SCHEDULED    # new bookings start Scheduled

    def is_active(self):
        """Return True unless the appointment is Cancelled (used by FR-04)."""
        raise NotImplementedError

    def conflicts_with(self, other):
        """Return True if same practitioner, date and time, both active (FR-04)."""
        raise NotImplementedError

    def change_status(self, new_status):
        """Change status if the change is allowed (FR-09, FR-12)."""
        raise NotImplementedError

    def cancel(self):
        """Set status to Cancelled; never delete the appointment (FR-10)."""
        raise NotImplementedError
