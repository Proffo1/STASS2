# Reflection - Stage 3 Lab

The hardest decision was where to put the rules about many appointments, such as double-booking and history. One Appointment cannot see the others, but I did not want a Manager class for every concept. I settled on one small optional class, AppointmentBook, and kept cancellation and history as an operation and a query.

The AI over-designed in several places. It proposed PatientManager, PractitionerManager, NotificationManager, ClinicController and ScheduleEngine, a Person superclass, and subclasses for each status. None of these has a requirement behind it. NotificationManager would build SMS reminders that the client never asked for, and ClinicController would become a class that owns everything.

My final choices rest on evidence from SmartCare v0.2. Patient, Practitioner and Appointment come from FR-01 to FR-03. The multiplicities come from FR-03 and FR-11. AppointmentStatus comes from FR-09, and AppointmentBook comes from FR-04, FR-08 and FR-11. Anything without a requirement ID was rejected or left unverified. I also ran a consistency check to confirm the skeleton code matches the UML.
