# AI Engineering Log (Part H)

**Tool:** Claude (Anthropic). If your course requires Microsoft Copilot, rerun the prompt below there. The draft, review findings and log must then be replaced with your own results.

## Prompt
> Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML.
>
> Approved UML: Appointment(appointment_id, patient, practitioner, date, time, status); operations is_active(), conflicts_with(other), change_status(new_status), cancel(). Rules: new appointments are Scheduled; a practitioner cannot have two active appointments at the same date and time; cancelled appointments are kept.

## Generated contribution
The first draft is in `ai_evidence/ai_draft_appointment.py`. It included the class, enum, exception and transition table.

## Review checklist (Part E)
| Check | Finding |
|---|---|
| Model consistency | Matches all UML operations, but adds `complete()`. |
| Unsupported features | `complete()`, `__eq__`, `__hash__`, `__repr__`, and string input for status. |
| Public state mutation | None. Status is read-only (good). |
| Unnecessary inheritance | None. |
| Invented dependencies | None. Only imports the standard library and the two domain classes. |
| Error handling | Weak: `date` and `time` were accepted unchecked (a string date and `None` time were accepted when I ran the draft). A non-string appointment ID would raise `AttributeError`. |

## Decisions, with verification
See table 4 in `domain_implementation_workbook_v0.4.md`. In short, 4 parts were accepted, 4 modified and 3 rejected.

| Evidence | Where |
|---|---|
| 26 unit tests passing | `ai_evidence/unittest_output.txt` |
| Manual behaviour run | `ai_evidence/manual_check_output.txt` |
| Draft probe (string date accepted, string status accepted, equality by ID only) | Confirmed by running the draft in this session |

## Explanation of non-UML decisions
- **Transition table:** it makes the legal changes visible in one place. Only Scheduled can change.
- **Read-only properties:** the UML says status is protected, so the code gives no setter.
- **`InvalidStatusTransitionError`:** the lab prompt allows an agreed exception, and an error type is clearer than a boolean.
