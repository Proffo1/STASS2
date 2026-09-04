"""SmartCare v0.1 - Human-written appointment prototype (Stage 1 Lab).

Part B code (task 1 + enhanced version) with ONE controlled improvement (Part G):
prevent two appointments for the same practitioner at the same time.
No database, no GUI.
"""

appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    """Record an appointment. Raises ValueError for blank patient names
    and for practitioner/time double bookings."""
    if not patient_name:
        raise ValueError("Patient name cannot be empty")

    # Part G improvement: no double booking of a practitioner at the same time
    for existing in appointments:
        if (existing["practitioner"] == practitioner_name
                and existing["time"] == appointment_time):
            raise ValueError(
                f"{practitioner_name} is already booked at {appointment_time}")

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time,
    }
    appointments.append(appointment)


def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | "
              f"Practitioner: {appointment['practitioner']} | "
              f"Time: {appointment['time']}")


if __name__ == "__main__":
    print("Welcome to SmartCare: The Clinical Appointment Booking System!")
    book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
    book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")
    display_appointments()
