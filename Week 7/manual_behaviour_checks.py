"""Part F - manual behaviour checks (prints what happens). Run: python manual_behaviour_checks.py"""
from datetime import date, time
from smartcare import Patient, Practitioner, Appointment, AppointmentStatus, InvalidStatusTransitionError

def show(label, fn):
    try:
        print(f"{label:48} -> {fn()}")
    except Exception as e:
        print(f"{label:48} -> {type(e).__name__}: {e}")

print("1. Valid objects")
p = Patient("P001", "Alice Smith"); d = Practitioner("D01", "Dr John Doe", "General Practice")
a = Appointment("A001", p, d, date(2026, 11, 2), time(10, 0))
print(f"   {p.name} / {d.name} ({d.specialty}) / status {a.status.value}")

print("2. Invalid input")
show("Patient with blank name", lambda: Patient("P002", ""))
show("Patient with name=None", lambda: Patient("P003", None))
show("Practitioner with blank specialty", lambda: Practitioner("D02", "Dr Roe", " "))
show("Appointment with patient=None", lambda: Appointment("A002", None, d, date(2026, 11, 2), time(9, 0)))
show("Appointment with date as a string", lambda: Appointment("A003", p, d, "2026-11-02", time(9, 0)))

print("3. Cancel a scheduled appointment")
a.cancel(); print(f"   status now {a.status.value}, still an object, active = {a.is_active()}")

print("4. Illegal repeated transition")
show("Cancel an already-cancelled appointment", a.cancel)
show("Change Cancelled to Completed", lambda: a.change_status(AppointmentStatus.COMPLETED))

print("5. Direct mutation is blocked")
def mutate(): a.status = AppointmentStatus.SCHEDULED
show("a.status = SCHEDULED", mutate)
