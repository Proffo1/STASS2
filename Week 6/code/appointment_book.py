"""SmartCare domain model - AppointmentBook (OPTIONAL class).
Needed because FR-04, FR-08 and FR-11 involve *many* appointments, which no single
Appointment can know about. Skeleton only."""


class AppointmentBook:
    """Holds the appointments and answers questions about all of them."""

    def __init__(self):
        self.appointments = []   # list of Appointment objects

    def book(self, appointment):
        """Add an appointment, rejecting conflicts and invalid data (FR-03, FR-04, FR-05)."""
        raise NotImplementedError

    def schedule_for(self, practitioner, date):
        """Return a practitioner's appointments on a date, ordered by time (FR-08)."""
        raise NotImplementedError

    def history_for(self, patient):
        """Return all of a patient's appointments including Cancelled (FR-11)."""
        raise NotImplementedError
