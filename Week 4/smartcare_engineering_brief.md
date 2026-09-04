# SmartCare v0.1 - Initial Engineering Brief

## 1. Problem summary (~100 words)
SmartCare Community Clinic currently manages patients and appointments using spreadsheets and paper records. This causes risks such as double bookings, slow searching, lost or inconsistent records and privacy concerns. The clinic wants software to manage patients, practitioners and appointments. However, the client statement is brief and not yet a complete specification. We do not know how many people will use the system, what data must be stored, what privacy rules apply, or what the budget and timeline are. Version 0.1 will be a small prototype that records appointments (patient, practitioner, time), while we ask the client questions to confirm the real requirements.

## 2. Initial stakeholders
| Stakeholder | Possible need |
|---|---|
| Receptionist | Quick booking and searching, no double bookings |
| Practitioners | See their schedule and patient details |
| Patients | Easy, private appointment handling |
| Clinic manager | Efficiency and reports |
| Privacy/compliance | Safe handling of health information |

## 3. Initial features
| Feature | Confirmed or provisional? | Why? |
|---|---|---|
| Appointment management | Confirmed | Stated in the client request |
| Patient records | Confirmed | "manage patients" |
| Practitioner records | Confirmed | "manage practitioners" |
| Patient search | Provisional | Implied but not stated |
| Practitioner schedule view | Provisional | Implied but not stated |
| Online payment, insurance | Provisional | No evidence yet; ask the client |
| Facial login, AI diagnosis, treatment plans | Not included | No evidence, high risk |

## 4. Questions for the client
1. How many patients, practitioners and daily appointments are there?
2. Who will use the software: staff only, or patients as well?
3. What patient details must be stored, and which privacy laws apply?
4. What are the appointment lengths, opening hours and practitioner rosters?
5. Are cancellations, reminders, payments or insurance needed, and what are the budget and deadline?

## 5. What we do not yet know
1. The exact data to store and how long it must be kept.
2. Whether the system must be accessible online or only inside the clinic.
3. Security, privacy and legal requirements, plus whether existing spreadsheet data must be migrated.
