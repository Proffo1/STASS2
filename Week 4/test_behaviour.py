"""Part F - verify behaviour of the human original, AI version, and improved version.
Run: python test_behaviour.py"""
import importlib

# ---- Original Part B enhanced code (before Part G improvement) ----
orig = []
def orig_book(p, d, t):
    if not p:
        raise ValueError("Patient name cannot be empty")
    orig.append({"patient": p, "practitioner": d, "time": t})

import smartcare_v01 as human_improved
import ai_version as ai

def attempt(label, fn, *args):
    try:
        fn(*args)
        return "accepted"
    except Exception as e:
        return f"REJECTED ({type(e).__name__}: {e})"

cases = [
    ("Normal appointment",           ("Alice Smith", "Dr. Doe", "10:00")),
    ("Blank patient name",           ("", "Dr. Doe", "11:00")),
    ("Same practitioner/time again", ("Bob Lee", "Dr. Doe", "10:00")),
    ("patient_name=None",            (None, "Dr. Doe", "12:00")),
    ("appointment_time=None",        ("Cara Fox", "Dr. Doe", None)),
]

print(f"{'Test':32}| {'Original (Part B)':46}| {'Improved (Part G)':58}| AI version")
for label, args in cases:
    r1 = attempt(f"o", orig_book, *args)
    r2 = attempt("h", human_improved.book_appointment, *args)
    r3 = attempt("a", ai.add_appointment, *args)
    print(f"{label:32}| {r1:46}| {r2:58}| {r3}")
