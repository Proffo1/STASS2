"""Part H - model/code consistency check.
Compares the classes, attributes and operations in the UML model against the code.
Run: python check_consistency.py"""
import inspect
from patient import Patient
from practitioner import Practitioner
from appointment import Appointment, AppointmentStatus
from appointment_book import AppointmentBook

MODEL = {
    Patient:         {"attrs": ["patient_id", "name"],
                      "ops": ["matches_id", "matches_name"]},
    Practitioner:    {"attrs": ["practitioner_id", "name"],
                      "ops": ["matches_id"]},
    Appointment:     {"attrs": ["appointment_id", "patient", "practitioner", "date", "time", "status"],
                      "ops": ["is_active", "conflicts_with", "change_status", "cancel"]},
    AppointmentBook: {"attrs": ["appointments"],
                      "ops": ["book", "schedule_for", "history_for"]},
}

def make(cls):
    p, d = Patient("P001", "Alice"), Practitioner("D01", "Dr Doe")
    return {Patient: lambda: p, Practitioner: lambda: d,
            Appointment: lambda: Appointment("A1", p, d, "2026-11-02", "10:00"),
            AppointmentBook: lambda: AppointmentBook()}[cls]()

ok = True
for cls, spec in MODEL.items():
    obj = make(cls)
    for a in spec["attrs"]:
        found = hasattr(obj, a)
        ok &= found
        print(f"{'PASS' if found else 'FAIL'}  {cls.__name__}.{a} attribute")
    for op in spec["ops"]:
        found = callable(getattr(cls, op, None))
        ok &= found
        print(f"{'PASS' if found else 'FAIL'}  {cls.__name__}.{op}() operation")

# model says: association is by object reference, status is an enum, new = Scheduled
a = make(Appointment)
checks = [
    ("Appointment.patient is a Patient", isinstance(a.patient, Patient)),
    ("Appointment.practitioner is a Practitioner", isinstance(a.practitioner, Practitioner)),
    ("Appointment.status starts Scheduled", a.status == AppointmentStatus.SCHEDULED),
    ("Status enum has exactly 3 values", len(AppointmentStatus) == 3),
    ("Appointment does not inherit from Patient", not issubclass(Appointment, Patient)),
]
for label, res in checks:
    ok &= res
    print(f"{'PASS' if res else 'FAIL'}  {label}")

# behaviour must NOT be implemented yet
for cls, spec in MODEL.items():
    for op in spec["ops"]:
        src = inspect.getsource(getattr(cls, op))
        stub = "NotImplementedError" in src
        ok &= stub
        print(f"{'PASS' if stub else 'FAIL'}  {cls.__name__}.{op}() is still a stub")

print("\nRESULT:", "model and code are consistent" if ok else "INCONSISTENCIES FOUND")
