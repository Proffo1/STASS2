"""FIRST DRAFT of Appointment as produced by the AI (Claude) for the Part D prompt.
Kept as evidence ONLY. The reviewed and refactored version is smartcare/appointment.py."""

from datetime import date as Date, time as Time
from enum import Enum

from smartcare.patient import Patient
from smartcare.practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class InvalidStatusTransitionError(Exception):
    pass


class Appointment:
    _ALLOWED = {
        AppointmentStatus.SCHEDULED: {AppointmentStatus.COMPLETED, AppointmentStatus.CANCELLED},
        AppointmentStatus.COMPLETED: set(),
        AppointmentStatus.CANCELLED: set(),
    }

    def __init__(self, appointment_id: str, patient: Patient,
                 practitioner: Practitioner, date: Date, time: Time) -> None:
        if not appointment_id or not appointment_id.strip():
            raise ValueError("Appointment ID cannot be empty")
        if not isinstance(patient, Patient):
            raise TypeError("patient must be a Patient")
        if not isinstance(practitioner, Practitioner):
            raise TypeError("practitioner must be a Practitioner")
        self._appointment_id = appointment_id
        self._patient = patient
        self._practitioner = practitioner
        self._date = date
        self._time = time
        self._status = AppointmentStatus.SCHEDULED

    appointment_id = property(lambda self: self._appointment_id)
    patient = property(lambda self: self._patient)
    practitioner = property(lambda self: self._practitioner)
    date = property(lambda self: self._date)
    time = property(lambda self: self._time)
    status = property(lambda self: self._status)

    def is_active(self) -> bool:
        return self._status != AppointmentStatus.CANCELLED

    def conflicts_with(self, other: "Appointment") -> bool:
        return (self.is_active() and other.is_active()
                and self._practitioner.practitioner_id == other._practitioner.practitioner_id
                and self._date == other._date and self._time == other._time)

    def change_status(self, new_status) -> None:
        if isinstance(new_status, str):          # convenience: accept "Cancelled"
            new_status = AppointmentStatus(new_status)
        if new_status not in self._ALLOWED[self._status]:
            raise InvalidStatusTransitionError(
                f"Cannot change from {self._status.value} to {new_status.value}")
        self._status = new_status

    def cancel(self) -> None:
        self.change_status(AppointmentStatus.CANCELLED)

    def complete(self) -> None:
        self.change_status(AppointmentStatus.COMPLETED)

    def __eq__(self, other) -> bool:
        return isinstance(other, Appointment) and self._appointment_id == other._appointment_id

    def __hash__(self) -> int:
        return hash(self._appointment_id)

    def __repr__(self) -> str:
        return (f"Appointment({self._appointment_id!r}, {self._patient.name!r}, "
                f"{self._practitioner.name!r}, {self._date}, {self._time}, {self._status.value})")
