# Part E - Human vs AI comparison

| Question | Human version (`smartcare_v01.py`) | AI version (`ai_version.py`) |
|---|---|---|
| Easy to understand? | Yes. Two short functions, clear names, and the dictionary keys (`patient`, `practitioner`, `time`) match the brief. | Yes. Very short and well commented, but it has only one function and no way to display records. |
| Runs successfully? | Yes. Prints both sample appointments with no errors. | Yes. Runs and prints the list of dictionaries. |
| Uses only required features? | Yes, plus one chosen improvement (double-booking check, Part G). | Yes. No database or GUI, as instructed. |
| Adds assumptions? | Time is a plain string. Practitioner names are unique. Same name means same person. | Same string assumption. It also assumes any input is valid, and it returns the dictionary, which was never requested. |
| Handles errors? | Blank or `None` patient name raises `ValueError`. Same practitioner/time is rejected. Still unhandled: whitespace-only names, `None` time, bad time formats. | No. Blank names, `None` and duplicates are all accepted silently. |
| Could I explain it? | Yes, line by line, because I wrote it and tested it. | Yes after reading it, but I would need to be able to explain why it leaves out validation. |

## Test results (Part F, from `test_behaviour.py`)

| Test | Original Part B | Improved (Part G) | AI version |
|---|---|---|---|
| Normal appointment | accepted | accepted | accepted |
| Blank patient name | rejected (ValueError) | rejected | **accepted** |
| Same practitioner/time twice | **accepted** | rejected | **accepted** |
| `patient_name=None` | rejected | rejected | **accepted** |
| `appointment_time=None` | **accepted** | **accepted** | **accepted** |

## Part B - Limitations found in the human programs (at least five)

1. Data is lost when the program ends: nothing is saved to a file or database.
2. Task 1 hard-codes appointments. A receptionist cannot enter new ones.
3. Task 1 repeats code for every appointment, so it does not scale.
4. Time is a free-text string with no format check. It cannot be sorted or compared, and `None` is accepted.
5. Double bookings are allowed (fixed in Part G).
6. There is no way to search, cancel or edit appointments.
7. Whitespace-only names such as `"   "` pass the blank-name check.
8. There is no patient ID, so two patients named "Alice Smith" cannot be told apart.
9. Practitioners are not validated against a real list, and past dates are accepted.

## Conclusion

The AI version is shorter and tidy, but it does less checking. The human version is closer to the requirements because it has validation. Neither is complete. Deciding what "correct" means still requires client requirements.
