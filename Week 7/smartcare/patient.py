"""SmartCare domain layer - Patient (FR-01, FR-06, FR-07)."""

from ._validation import require_text


class Patient:
    """A person receiving care. ID and name are validated and read-only."""

    def __init__(self, patient_id: str, name: str) -> None:
        self._patient_id = require_text(patient_id, "Patient ID")
        self._name = require_text(name, "Patient name")

    @property
    def patient_id(self) -> str:
        return self._patient_id

    @property
    def name(self) -> str:
        return self._name

    def matches_id(self, patient_id: str) -> bool:
        """True if this patient has the given ID (FR-06)."""
        return self._patient_id == patient_id

    def matches_name(self, text: str) -> bool:
        """True if the name contains the text, ignoring case (FR-07, provisional)."""
        return text.strip().lower() in self._name.lower()
