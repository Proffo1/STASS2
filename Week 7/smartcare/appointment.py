"""SmartCare domain layer - Appointment, AppointmentStatus and the transition error
(FR-03, FR-04, FR-09, FR-10, FR-12)."""

from datetime import date as Date, time as Time
from enum import Enum

from ._validation import require_text
from .patient import Patient
from .practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class InvalidStatusTransitionError(Exception):
    """Raised when a status change is not allowed (FR-12)."""


# Only a Scheduled appointment can move on. Completed and Cancelled are final.
_ALLOWED = {
    AppointmentStatus.SCHEDULED: {AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED},
    AppointmentStatus.COMPLETED: set(),
    AppointmentStatus.CANCELLED: set(),
}


class Appointment:
    """One patient seeing one practitioner at a date and time.

    Cancelled appointments stay as objects (FR-10). Status is read-only and can
    only change through change_status() or cancel().
    """

    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner, date: Date, time: Time) -> None:
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")
        if not isinstance(date, Date):
            raise TypeError("date must be a datetime.date")
        if not isinstance(time, Time):
            raise TypeError("time must be a datetime.time")

        self._appointment_id = require_text(appointment_id, "Appointment ID")
        self._patient = patient
        self._practitioner = practitioner
        self._date = date
        self._time = time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def date(self) -> Date:
        return self._date

    @property
    def time(self) -> Time:
        return self._time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def is_active(self) -> bool:
        """True unless the appointment is Cancelled (used by FR-04)."""
        return self._status != AppointmentStatus.CANCELLED

    def conflicts_with(self, other: "Appointment") -> bool:
        """True if both are active and share practitioner, date and time (FR-04)."""
        return (other is not self
                and self.is_active() and other.is_active()
                and self._practitioner.practitioner_id == other._practitioner.practitioner_id
                and self._date == other._date
                and self._time == other._time)

    def change_status(self, new_status: AppointmentStatus) -> None:
        """Change status if the transition is allowed (FR-09, FR-12)."""
        if not isinstance(new_status, AppointmentStatus):
            raise TypeError("new_status must be an AppointmentStatus")
        if new_status not in _ALLOWED[self._status]:
            raise InvalidStatusTransitionError(
                f"Cannot change status from {self._status.value} to {new_status.value}")
        self._status = new_status

    def cancel(self) -> None:
        """Cancel the appointment; it stays as an object (FR-10)."""
        self.change_status(AppointmentStatus.CANCELLED)
