"""Tiny shared validation helper (a function, not a base class)."""


def require_text(value: object, field: str) -> str:
    """Return value stripped of surrounding spaces; reject non-strings and blanks."""
    if not isinstance(value, str):
        raise TypeError(f"{field} must be text, not {type(value).__name__}")
    value = value.strip()
    if not value:
        raise ValueError(f"{field} cannot be empty")
    return value
