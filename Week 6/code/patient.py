"""SmartCare domain model - Patient (FR-01, FR-06, FR-07).
Skeleton only: attributes and operation signatures, no full behaviour yet."""


class Patient:
    """A person receiving care at SmartCare."""

    def __init__(self, patient_id, name):
        self.patient_id = patient_id   # unique ID (FR-01)
        self.name = name               # patient's name (FR-01)

    def matches_id(self, patient_id):
        """Return True if this patient has the given ID (FR-06)."""
        raise NotImplementedError

    def matches_name(self, text):
        """Return True if the name contains the text (FR-07, provisional)."""
        raise NotImplementedError
