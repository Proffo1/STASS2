# Reflection (Part H)

Before using AI, I wrote and ran the Part B programs. The first prints two hard-coded appointments. The second stores appointments in a list of dictionaries, with `book_appointment` and `display_appointments` functions and a blank-name check. Both ran, but I found limitations such as no saved data, no time validation and no protection against double bookings.

AI helped me understand why `not patient_name` also rejects `None`, and it pointed out the duplicate-booking problem that I had missed. It did make assumptions. The AI version treated all input as valid and returned a value I never asked for. It also suggested persistence and time validation, which the client has not requested.

I verified the output by running both versions in `test_behaviour.py` against a normal booking, a blank name, a duplicate practitioner/time, and `None` inputs. The AI version accepted every bad input, so it could not be used as-is.

The engineering work that remained for me was choosing what was in scope, deciding which suggestions to accept, modify or reject, testing unusual inputs, and picking exactly one improvement (the double-booking check). The AI could not decide what the clinic actually needs. Only the client can answer that.
