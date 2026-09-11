# Stage 2 Tutorial - From Problems to Requirements

## Activity 1 - Stakeholder Map
| Stakeholder | Need | Potential conflict |
|---|---|---|
| Reception staff | Fast booking and searching, no duplicates | Want speed, while management wants strict data checks that add steps |
| Practitioners | Reliable schedules and patient information | May want flexible bookings that conflict with the no-double-booking rule |
| Clinic management | Small, maintainable system, good history and low cost | Limited budget conflicts with extra features that staff or patients want |
| Patients | Correct appointments and privacy | Easy access (convenience) vs strict privacy and security |
| Maintainers / developers | Simple, testable code | Quick delivery vs clean structure |

## Activity 2 - Functional or Non-Functional?
| Requirement | Answer |
|---|---|
| The system shall allow staff to cancel an appointment. | **Functional** |
| The system should remain responsive for the course-scale dataset. | **Non-functional** (performance) |
| The system shall retain cancelled appointments. | **Functional** (an observable behaviour: they stay visible in history) |
| Core business logic should be independently testable. | **Non-functional** (testability) |
| The system shall search for a patient by ID. | **Functional** |

## Activity 3 - Repair Ambiguous Requirements
| Requirement | Problem | Clarification question |
|---|---|---|
| The system should be easy to use. | "Easy" cannot be measured and differs per user. | How many steps or how much training time is acceptable for a receptionist to book an appointment? |
| Patient search should be fast. | "Fast" has no number, and the data size is unknown. | How many patients are there, and what response time (for example, under 1 second) is acceptable? |
| The system should securely manage data. | "Securely" does not say which threats, rules or controls. | Which privacy laws apply, who may see which records, and must access be logged? |
| Appointments should normally be easy to cancel. | "Normally" and "easy" are vague, and the exceptions are not stated. | Who may cancel, when is cancelling not allowed, and what should happen to the cancelled record? |

## Activity 4 - AI Requirements Audit
| AI suggestion | Classification | Evidence / reason |
|---|---|---|
| Patients receive SMS reminders. | Unsupported (out of scope) | The brief does not mention reminders or patient communication. |
| Facial recognition login. | Unsupported (out of scope) | No login or security need is stated. It is also high-risk for privacy. |
| Receptionists create appointments. | Assumption requiring validation | The brief says "staff" report duplicate bookings, which implies staff book, but "receptionist" as the role needs to be confirmed. |
| Online payment. | Out of scope | The brief does not mention payments. |
| Practitioners view schedules. | Assumption requiring validation | Practitioners are part of the system, but the brief does not say they view schedules. |
| AI recommends treatments. | Out of scope | Clinical decision support is not requested. It is also a safety risk. |
| Cancelled appointments remain in history. | Confirmed | Supported by the brief's "limited appointment history" and "inconsistent appointment status" problems. |

## Exit question
**Why is "AI suggested it" not sufficient evidence for a requirement?**
AI does not know the clinic. It generates plausible features from general patterns and can invent needs, so a suggestion is only a hypothesis. A requirement needs evidence from the client or stakeholders (the brief, an interview, a confirmed answer). Otherwise we build, test and maintain things nobody wants, and the team is still accountable for the result.
