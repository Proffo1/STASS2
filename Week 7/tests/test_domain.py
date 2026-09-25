"""Part F - behaviour checks as repeatable unit tests. Run: python -m unittest -v"""
import unittest
from datetime import date, time

from smartcare import (Patient, Practitioner, Appointment,
                       AppointmentStatus, InvalidStatusTransitionError)


def make_appt(aid="A1", pid="P1", did="D1", d=date(2026, 11, 2), t=time(10, 0)):
    return Appointment(aid, Patient(pid, "Alice Smith"),
                       Practitioner(did, "Dr Doe", "GP"), d, t)


class PatientTests(unittest.TestCase):
    def test_valid(self):
        p = Patient("P1", "  Alice Smith ")
        self.assertEqual((p.patient_id, p.name), ("P1", "Alice Smith"))
    def test_blank_name(self):
        with self.assertRaises(ValueError): Patient("P1", "   ")
    def test_none_name(self):
        with self.assertRaises(TypeError): Patient("P1", None)
    def test_blank_id(self):
        with self.assertRaises(ValueError): Patient("", "Alice")
    def test_read_only(self):
        with self.assertRaises(AttributeError): Patient("P1", "A").name = "B"
    def test_matching(self):
        p = Patient("P1", "Alice Smith")
        self.assertTrue(p.matches_id("P1")); self.assertFalse(p.matches_id("P2"))
        self.assertTrue(p.matches_name("alice")); self.assertFalse(p.matches_name("bob"))


class PractitionerTests(unittest.TestCase):
    def test_valid(self):
        d = Practitioner("D1", "Dr Doe", "Cardiology")
        self.assertEqual((d.practitioner_id, d.name, d.specialty), ("D1", "Dr Doe", "Cardiology"))
    def test_blank_specialty(self):
        with self.assertRaises(ValueError): Practitioner("D1", "Dr Doe", "")
    def test_blank_name(self):
        with self.assertRaises(ValueError): Practitioner("D1", " ", "GP")
    def test_none_id(self):
        with self.assertRaises(TypeError): Practitioner(None, "Dr Doe", "GP")
    def test_matches_id(self):
        d = Practitioner("D1", "Dr Doe", "GP")
        self.assertTrue(d.matches_id("D1")); self.assertFalse(d.matches_id("D2"))


class AppointmentTests(unittest.TestCase):
    def test_new_is_scheduled_and_active(self):
        a = make_appt()
        self.assertEqual(a.status, AppointmentStatus.SCHEDULED); self.assertTrue(a.is_active())
    def test_bad_patient(self):
        with self.assertRaises(TypeError):
            Appointment("A1", "Alice", Practitioner("D1", "Dr", "GP"), date(2026, 1, 1), time(9))
    def test_bad_practitioner(self):
        with self.assertRaises(TypeError):
            Appointment("A1", Patient("P1", "A"), None, date(2026, 1, 1), time(9))
    def test_bad_date_and_time(self):
        p, d = Patient("P1", "A"), Practitioner("D1", "Dr", "GP")
        with self.assertRaises(TypeError): Appointment("A1", p, d, "2026-11-02", time(9))
        with self.assertRaises(TypeError): Appointment("A1", p, d, date(2026, 1, 1), None)
    def test_blank_id(self):
        with self.assertRaises(ValueError): make_appt(aid=" ")
    def test_status_is_read_only(self):
        with self.assertRaises(AttributeError): make_appt().status = AppointmentStatus.COMPLETED
    def test_cancel_scheduled(self):
        a = make_appt(); a.cancel()
        self.assertEqual(a.status, AppointmentStatus.CANCELLED); self.assertFalse(a.is_active())
    def test_repeated_cancel_is_illegal(self):
        a = make_appt(); a.cancel()
        with self.assertRaises(InvalidStatusTransitionError): a.cancel()
        self.assertEqual(a.status, AppointmentStatus.CANCELLED)
    def test_cancelled_cannot_be_completed(self):
        a = make_appt(); a.cancel()
        with self.assertRaises(InvalidStatusTransitionError):
            a.change_status(AppointmentStatus.COMPLETED)
    def test_complete_then_cancel_illegal(self):
        a = make_appt(); a.change_status(AppointmentStatus.COMPLETED)
        with self.assertRaises(InvalidStatusTransitionError): a.cancel()
    def test_string_status_rejected(self):
        with self.assertRaises(TypeError): make_appt().change_status("Cancelled")
    def test_conflict_same_practitioner_date_time(self):
        self.assertTrue(make_appt("A1", "P1").conflicts_with(make_appt("A2", "P2")))
    def test_no_conflict_different_time_or_practitioner(self):
        a = make_appt()
        self.assertFalse(a.conflicts_with(make_appt("A2", t=time(11, 0))))
        self.assertFalse(a.conflicts_with(make_appt("A3", did="D2")))
    def test_cancelled_does_not_conflict(self):
        a, b = make_appt("A1"), make_appt("A2"); b.cancel()
        self.assertFalse(a.conflicts_with(b)); self.assertFalse(b.conflicts_with(a))
    def test_no_conflict_with_itself(self):
        a = make_appt(); self.assertFalse(a.conflicts_with(a))


if __name__ == "__main__":
    unittest.main()
