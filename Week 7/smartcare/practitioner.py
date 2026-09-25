"""SmartCare domain layer - Practitioner (FR-02, FR-08)."""

from ._validation import require_text


class Practitioner:
    """A clinician who sees patients. No database logic. Fields are read-only."""

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        self._practitioner_id = require_text(practitioner_id, "Practitioner ID")
        self._name = require_text(name, "Practitioner name")
        self._specialty = require_text(specialty, "Specialty")

    @property
    def practitioner_id(self) -> str:
        return self._practitioner_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty

    def matches_id(self, practitioner_id: str) -> bool:
        """True if this practitioner has the given ID."""
        return self._practitioner_id == practitioner_id
