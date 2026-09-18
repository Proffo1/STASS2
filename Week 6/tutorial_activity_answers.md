# Stage 3 Tutorial - From Requirements to Domain Models

## Candidate Concepts
| Candidate | Class? | Reason |
|---|---|---|
| Patient | **Yes** | Has an ID, name and its own behaviour (FR-01, FR-06). |
| Practitioner | **Yes** | Has an ID, name and behaviour (FR-02). |
| Appointment | **Yes** | Has state (date, time, status) and rules (FR-03, FR-04, FR-10). |
| Name | **No (attribute)** | A simple value belonging to Patient or Practitioner. |
| Clinic | **No (not needed yet)** | It is the context, not mentioned in any requirement as something with state or behaviour. |
| Database | **No** | A storage and implementation choice, not a domain concept. |
| Cancellation | **No (operation)** | An action that changes status (FR-10). Its result is a status, not an object. |
| Status | **No (attribute / enumeration)** | A fixed list of values with no behaviour (FR-09). |

## CRC Cards
**Patient** - Responsibilities: know ID and name; match by ID or name. Collaborators: none.

**Practitioner** - Responsibilities: know ID and name; match by ID. Collaborators: none.

**Appointment** - Responsibilities: know its patient, practitioner, date, time and status; say if it conflicts with another; change status when allowed; cancel without being deleted. Collaborators: Patient, Practitioner, AppointmentStatus.

## Relationship Reasoning
- **Patient to Appointment: which relationship and why?** An association, 1 to 0..*. One patient can have many appointments (history), and each appointment is for exactly one patient. It is not inheritance or composition, since appointments are separate records that outlive a visit.
- **Practitioner to Appointment: what multiplicity?** 1 to 0..*. A practitioner has many appointments and each appointment has exactly one practitioner.
- **Should Appointment inherit from Patient?** No. An appointment *is not* a patient (the "is-a" test fails). It *has* a patient, so use an association.
- **Does Clinic need to own every object?** No. Owning everything creates a "god object", increases coupling and hurts testability (NFR-03, NFR-04). The domain model shows relationships between objects. Nothing in the requirements asks for a Clinic that owns them, so leave it out until a requirement needs it.

## AI Model Critique
| AI proposal | Verdict | Reason |
|---|---|---|
| PatientManager | **Reject** | A wrapper with no requirement. Patient already knows how to match itself. |
| PractitionerManager | **Reject** | Same reason as PatientManager. |
| AppointmentManager | **Modify** | A holder is needed for rules across many appointments (FR-04, FR-08, FR-11), so keep one, named AppointmentBook, with narrow responsibilities. |
| ClinicController | **Reject (for now)** | A god class. Control and UI come in a later stage and no requirement asks for it. |
| NotificationManager | **Reject** | Reminders are out of scope. There is no evidence for it in the brief. |
| ScheduleEngine | **Reject** | Over-design. A schedule is a query on appointments (`schedule_for`). FR-08 is also provisional. |
