"""SmartCare domain model - Practitioner (FR-02, FR-08).
Skeleton only: attributes and operation signatures, no full behaviour yet."""


class Practitioner:
    """A clinician who sees patients."""

    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id   # unique ID (FR-02)
        self.name = name                         # practitioner's name (FR-02)

    def matches_id(self, practitioner_id):
        """Return True if this practitioner has the given ID (FR-02)."""
        raise NotImplementedError
