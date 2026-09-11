# SmartCare v0.2 - Requirements Specification

*Basis: client brief (Stage 2 Lab, Part A). "Evidence" always means a statement in the brief. Anything else is marked **provisional**.*

## 1. Problem and Scope

**Problem.** SmartCare Community Clinic manages patients and appointments with spreadsheets and paper records. Staff report **duplicate bookings**, **difficulty finding patient information**, **inconsistent appointment status** and **limited appointment history**. Management wants a **small, maintainable** patient, practitioner and appointment system.

**In scope (confirmed by the brief)**
- Patient records
- Practitioner records
- Appointment booking
- Prevention of duplicate bookings
- Finding patient information (search)
- Consistent appointment status
- Appointment history

**In scope (provisional, need client confirmation)**
- Practitioner schedule view
- Search by patient name
- Contact details stored on patient records

**Out of scope (no evidence in the brief)**
- SMS or email reminders
- Online payment and insurance processing
- Facial-recognition login
- AI diagnosis or treatment recommendations or plans
- Patient self-service portal
- Migration of existing spreadsheet or paper data (to be asked)

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Reception / administrative staff | Book appointments without duplicates, find patient information quickly, see a reliable appointment status | "Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status" |
| Practitioners | Accurate appointment and patient information for their own sessions | Practitioners are named in the requested system ("patient, practitioner and appointment system"); the schedule view is provisional |
| Clinic management | A small, maintainable system with trustworthy appointment history | "Management wants a small, maintainable... system"; "limited appointment history" |
| Patients (indirect) | Their appointments are recorded correctly and their information is handled properly | Implied by patient records; patients are not described as system users, so this is provisional |
| Future maintainers / developers | Code that is easy to understand, change and test | "maintainable" |

## 3. Functional Requirements

| ID | Requirement | Source | Status |
|---|---|---|---|
| FR-01 | The system shall allow staff to create a patient record containing a unique patient ID and the patient's name. | "manage patients" | Confirmed |
| FR-02 | The system shall allow staff to create a practitioner record containing a unique practitioner ID and the practitioner's name. | "manage practitioners" | Confirmed |
| FR-03 | The system shall allow staff to book an appointment by selecting an existing patient, an existing practitioner, a date and a time. | "manage appointments" | Confirmed |
| FR-04 | The system shall reject a booking if the practitioner already has a non-cancelled appointment at the same date and time, and shall display a message stating the conflict. | "duplicate bookings" | Confirmed |
| FR-05 | The system shall reject a booking if the patient or practitioner does not exist, or if the date or time is missing or invalid, and shall display the reason. | Data quality (follows FR-03) | Confirmed (derived) |
| FR-06 | The system shall allow staff to find a patient by patient ID and display that patient's record. | "difficulty finding patient information" | Confirmed |
| FR-07 | The system shall allow staff to find patients by (part of) name. | "difficulty finding patient information" | Provisional (the client has not said which search keys matter) |
| FR-08 | The system shall display all appointments for a chosen practitioner on a chosen date, ordered by time. | Practitioners are stakeholders | Provisional |
| FR-09 | The system shall give every appointment exactly one status from a fixed list: Scheduled, Completed, Cancelled. | "inconsistent appointment status" | Confirmed (the exact list is an assumption) |
| FR-10 | The system shall allow staff to cancel an appointment by setting its status to Cancelled; the appointment shall not be deleted. | "limited appointment history" | Confirmed |
| FR-11 | The system shall display the full appointment history of a patient, including Completed and Cancelled appointments, ordered by date and time. | "limited appointment history" | Confirmed |
| FR-12 | The system shall reject a status change that is not allowed (for example, changing a Cancelled appointment to Completed). | "inconsistent appointment status" | Provisional (the allowed transitions need validation) |

## 4. Non-Functional Requirements

| ID | Quality | Requirement | Status |
|---|---|---|---|
| NFR-01 | Data integrity | No appointment shall exist without a valid patient and practitioner, and no two non-cancelled appointments shall share a practitioner, date and time. | Confirmed (from the duplicate-booking problem) |
| NFR-02 | Reliability | Invalid user input shall produce a clear error message and shall never crash the program or change stored data. | Confirmed (derived) |
| NFR-03 | Maintainability | Business logic (booking, searching, status rules) shall be kept in functions separate from input/output code, with each function documented by a docstring. | Confirmed ("maintainable") |
| NFR-04 | Testability | Core logic shall be testable without user interaction, and every FR shall have at least one automated test. | Confirmed ("maintainable"; the tutorial requires independently testable logic) |
| NFR-05 | Usability | A trained receptionist shall be able to book an appointment using no more than 5 prompts or screens. | Provisional (the number 5 is a target to validate) |
| NFR-06 | Performance | Searches and bookings shall complete in under 1 second for up to 1,000 patients and 5,000 appointments. | Provisional (the course-scale size is an assumption) |

## 5. User Stories

- **US-01:** As a **receptionist**, I want to **book an appointment for a patient with a practitioner**, so that **the clinic's schedule is recorded in one place**.
- **US-02:** As a **receptionist**, I want to **be stopped from double-booking a practitioner**, so that **two patients are never given the same slot**.
- **US-03:** As a **receptionist**, I want to **find a patient by ID**, so that **I can quickly see their information**.
- **US-04:** As a **receptionist**, I want to **cancel an appointment but keep it on record**, so that **appointment status is consistent and the history is complete**.
- **US-05:** As a **practitioner**, I want to **see my appointments for a day**, so that **I know who I am seeing and when** *(provisional)*.
- **US-06:** As a **clinic manager**, I want to **view a patient's full appointment history**, so that **I can see past visits and cancellations**.

## 6. Acceptance Criteria

**AC-1 (US-01, normal)**
- GIVEN patient P001 and practitioner D01 exist and D01 is free on 2026-11-02 at 10:00
- WHEN the receptionist books P001 with D01 for 2026-11-02 at 10:00
- THEN the appointment is saved with status Scheduled and a confirmation is shown

**AC-2 (US-02, negative)**
- GIVEN D01 already has a Scheduled appointment on 2026-11-02 at 10:00
- WHEN the receptionist books another patient with D01 at that date and time
- THEN the booking is rejected, a message states that D01 is already booked, and no new appointment is stored

**AC-3 (US-03, normal)**
- GIVEN patient P001 exists
- WHEN the receptionist searches for patient ID P001
- THEN the record for P001 is displayed

**AC-4 (US-03, negative)**
- GIVEN no patient with ID P999 exists
- WHEN the receptionist searches for patient ID P999
- THEN the system displays "Patient not found" and does not crash

**AC-5 (US-04, normal)**
- GIVEN appointment A10 has status Scheduled
- WHEN the receptionist cancels A10
- THEN A10's status becomes Cancelled and A10 still appears in the patient's history

**AC-6 (US-04, negative)**
- GIVEN appointment A11 has status Cancelled
- WHEN the receptionist tries to mark A11 as Completed
- THEN the change is rejected and the status stays Cancelled

**AC-7 (US-01, negative)**
- GIVEN the patient ID entered does not exist
- WHEN the receptionist tries to book an appointment for it
- THEN the booking is rejected with the reason "patient not found"

## 7. Assumptions and Open Questions

**Assumptions (to be validated with the client)**
1. "Receptionist" and "staff" are the same group of users.
2. Appointment length is not needed, so a booking is identified by date and time only.
3. The status list Scheduled / Completed / Cancelled is sufficient.
4. The course-scale dataset is around 1,000 patients and 5,000 appointments.
5. A single user operates the system at a time.

**Open questions for the client**
1. Which patient details must be stored (contact details, date of birth, notes)?
2. How do staff usually look people up: ID, name, phone number or something else?
3. What statuses exist today in the spreadsheets, and which changes are allowed?
4. How long are appointments, and can a practitioner see overlapping appointments?
5. Do practitioners need to use the system, or only reception staff?
6. Are there privacy or retention rules for health records?
7. Must the existing spreadsheet and paper data be imported?

## 8. AI Requirements Review Record

*(Selected items. The full review is in `ai_review_and_verification.md`.)*

| AI suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| FR-04 should define "same time" (exact slot vs overlapping) | Question only | **Modified** | Valid ambiguity. Kept exact date/time matching and recorded the overlap issue as an open question (Q4). | Re-read the brief: no appointment length is given. |
| "Searches should be fast" in the draft is untestable | Based on the draft wording | **Accepted** | Replaced with NFR-06 and a measurable figure, marked provisional. | Checked NFR-06 can be measured with a timer. |
| Add FR-12 to control status changes | Based on "inconsistent appointment status" | **Accepted (provisional)** | Directly supports the stated problem, but the allowed transitions are not given. | Checked against the brief, listed as open question 3. |
| Add SMS reminders | No (invented) | **Rejected** | Not in the brief. Kept out of scope. | Searched the brief: no mention of reminders. |
| Add role-based login and audit logs | No (invented) | **Rejected** | The brief does not mention users or permissions. | Searched the brief. |
| Ask about privacy and retention rules | Question only | **Accepted as a question** | Reasonable for health records, but a question, not a requirement. | Added as open question 6. |
| Require encryption with AES-256 | No (invented) | **Rejected** | Over-specified and unsupported. | Not in the brief. |
