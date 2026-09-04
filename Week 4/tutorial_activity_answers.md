# Stage 1 Tutorial Activity - Why Software Engineering Still Matters

## Activity 1 - Think-Pair-Share
What does a software engineer still need to know if AI can produce a 100-line app quickly?
1. **Requirements and problem understanding:** knowing what the right thing to build is, and asking the client the right questions.
2. **Verification and testing:** judging whether code is correct, safe and handles unusual input, because AI output can be wrong or incomplete.
3. **Design, maintenance, ethics and accountability:** structure, security, privacy, teamwork, and taking responsibility for what is delivered.

## Activity 2 - Is This Software Engineering?
| Scenario | Programming? | Software engineering? | Why? |
|---|---|---|---|
| A: 50-line calculator by a student | Yes | Not really | Small, one person, no real users, no long-term maintenance, no stakeholders or requirements process. |
| B: Payroll system for 5,000 employees | Yes | **Yes** | Many stakeholders, accuracy and legal requirements, security, testing, teamwork, maintenance and change management. |
| C: AI generates an appointment app from one prompt | Code was generated (not written by a person) | Only if humans do the engineering | Without requirements, review, testing and ownership, it is just generated code. Engineering is the checking and decision making around it. |

## Activity 3 - SmartCare Problem Analysis
**Task 1 - Stakeholders**
| Stakeholder | What do they need? |
|---|---|
| Receptionist | Fast booking, easy search, fewer errors and double bookings |
| Practitioners (doctors, nurses) | Clear schedule view, accurate patient information |
| Patients | Easy booking and changing, privacy, reminders |
| Clinic manager / owner | Efficiency, reporting, cost control, compliance |
| IT / maintainers | Simple, supportable and secure system |
| Regulators / privacy officers | Compliance with health-data privacy law |

**Task 2 - Current problems**
1. Spreadsheets and paper allow double bookings and conflicting versions.
2. Searching for patients or appointments is slow.
3. Paper records can be lost, damaged or seen by the wrong people (privacy risk).
4. There are no automatic reminders, so there are more no-shows. Reporting is also manual.

**Task 3 - Questions for the client**
1. How many patients, practitioners and appointments per day does the clinic handle?
2. Who will use the system (receptionists only, or patients too)?
3. What patient information must be recorded, and what privacy rules apply?
4. How long are appointments, and what are the opening hours and practitioner rosters?
5. Do you need cancellation, rescheduling and reminders, and what is the budget and deadline?

## Activity 4 - Critique an AI Response
Only the client statement counts as evidence: "manage patients, practitioners and appointments."
| Suggestion | Client evidence? | In scope? | Decision |
|---|---|---|---|
| Appointment management | Yes, stated directly | Yes | **Accept** |
| Facial recognition login | None | No | **Reject** (privacy and cost, and no need shown) |
| AI diagnosis recommendations | None | No | **Reject** (clinical and legal risk; the clinic did not ask) |
| Patient search | Implied (managing patients) | Yes | **Accept** (confirm with client) |
| Online payment | None | Unclear | **Keep unverified** (ask the client) |
| Practitioner schedule view | Implied (managing practitioners) | Yes | **Accept** (confirm with client) |
| Insurance processing | None | Unclear | **Keep unverified** (ask the client) |
| Treatment-plan generation | None | No | **Reject** (clinical risk, beyond brief) |

## Exit question
Eliciting and clarifying requirements with the client, and deciding what is in scope. AI cannot be accountable to the client or know their real needs. (Verifying and testing against those requirements is another example.)
