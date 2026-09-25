# Stage 4 Tutorial - Object-Oriented Design Decisions

## Activity 1 - Encapsulation Review
| Class | Protected state / invariant | Public operations |
|---|---|---|
| Patient | ID and name are non-blank text and cannot change after creation | `matches_id()`, `matches_name()`, read-only `patient_id` and `name` |
| Practitioner | ID, name and specialty are non-blank text and cannot change | `matches_id()`, read-only `practitioner_id`, `name`, `specialty` |
| Appointment | Status can only change through legal transitions. It always has a real patient, practitioner, date and time. It is never deleted. | `is_active()`, `conflicts_with()`, `change_status()`, `cancel()`, read-only properties |

## Activity 2 - Composition or Inheritance?
| Pair | Choice | Reason |
|---|---|---|
| Appointment and Patient | **Composition / association** | An appointment *has a* patient. It is not a kind of patient. |
| Appointment and Practitioner | **Composition / association** | An appointment *has a* practitioner. |
| Doctor and Practitioner (hypothetical) | **Inheritance** (a Doctor *is a* Practitioner) | The "is-a" test passes and a Doctor shares all the Practitioner behaviour. Use it only if doctors gain behaviour that other practitioners lack. Otherwise a `specialty` attribute is simpler. |
| Clinic and Appointment | **Composition / association** | A clinic *has* appointments. An appointment is not a clinic. Any such link should stay a reference, not ownership of everything. |

## Activity 3 - Responsibility Allocation
- **Who decides whether SCHEDULED can become CANCELLED?** The Appointment. It owns its status and the transition rules, so the rule lives in one place (`change_status`).
- **Who validates a patient name?** The Patient. It is the class that must always hold a valid name, so it checks in its constructor. A UI can also check for friendly messages, but it cannot be the only check.
- **Should Appointment execute SQL? Why?** No. Storage is a separate concern. SQL inside the domain class couples it to a database, makes it hard to test (NFR-04) and breaks the single-responsibility principle.
- **Should the UI decide whether a status transition is legal?** No. The rule belongs in the domain. A UI that decides can be bypassed or can disagree with other callers. The UI should call `cancel()` and report the error raised.

## Activity 4 - AI Code Critique
| # | Design problem | Correction |
|---|---|---|
| 1 | **Public status mutation** lets any code set an illegal status | Make status private and read-only. Change it only via `change_status()` / `cancel()`. |
| 2 | **SQL inside `cancel()`** mixes persistence with domain logic and makes testing hard | Remove SQL. `cancel()` only changes status. A separate storage layer saves it later. |
| 3 | **NotificationManager dependency** is out of scope (SMS reminders are not in the requirements) and couples the domain to something unneeded | Remove it. |
| 4 | **Inheriting from PatientRecord** fails the "is-a" test (an appointment is not a patient record) and exposes unrelated behaviour | Use an association to Patient instead. |
| 5 | **No transition protection**: nothing stops Cancelled to Scheduled | Add a transition table and raise `InvalidStatusTransitionError`. |
| 6 | **Hidden side effects in a simple method**: cancelling now also touches a database and sends messages | One responsibility per operation. Keep `cancel()` small and predictable. |
| 7 | **Invented dependencies** make the class impossible to use or test alone | Depend only on the domain classes it needs. |

## Exit question
**Why can code be object-oriented syntactically but still have poor object-oriented design?**
Using `class`, inheritance and methods only makes the *syntax* object-oriented. Good design depends on choosing the right responsibilities, keeping state encapsulated, using inheritance only for real "is-a" relationships, and keeping classes cohesive and loosely coupled. A class with public mutable state, SQL, notifications and an invalid inheritance chain is still valid Python OO syntax, but it is hard to test, change and trust.
