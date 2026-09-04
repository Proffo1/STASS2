# Part A - Understand the Problem (AI OFF)

**What data must be stored?** Patient name, practitioner name, appointment time (date and time). Later it would also need a patient ID, contact details and appointment status.

**What functions might be useful?** `book_appointment()`, `display_appointments()`, `cancel_appointment()`, `find_appointments_by_patient()`, `check_availability()`.

**What could go wrong?** Blank or misspelled names, double bookings, invalid or past times, lost data when the program closes, and two patients with the same name.

**What requirements are unclear?** Appointment length, clinic opening hours, whether patients can book themselves or only receptionists, how records are stored, privacy rules for health data, and whether cancellations or reminders are needed.
