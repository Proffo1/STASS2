# AI Usage Log

**Tool used:** Claude (Anthropic). Check that this is permitted under your course policy. The lab says to use only the university-approved GenAI tool, such as Microsoft Copilot. If you must use Copilot, rerun the prompts below there and update this log with your own results.

| Stage | Prompt (summary) | What AI produced | Decision |
|---|---|---|---|
| Part B (AI OFF) | None | n/a | Human code taken from the lab brief. |
| Part C - tutor | "Act as a Python tutor. Explain the `book_appointment` function, identify three limitations, suggest improvements, do not rewrite the app, ask two questions." | Explanation of the code. Limitations: no duplicate check, no time validation, data not persisted. Suggestions: validate time, check duplicates. | **Accept** the duplicate-check idea (used in Part G). **Keep unverified** time-format validation (needs a requirement). **Reject** persistence for now (out of Stage 1 scope). |
| Part D - alternative | "Create a beginner-friendly function that stores patient name, practitioner name and appointment time. No database or GUI." | `ai_version.py` | **Modify**: used only for comparison. It has no validation, so it is not used as the final code. |
| Verification | n/a | n/a | Ran `smartcare_v01.py` and `test_behaviour.py`; results are in `comparison.md`. |

## Tutor questions I was asked (and my answers)

1. *Why does `not patient_name` also catch `None`?* Both `""` and `None` are falsy in Python.
2. *What happens if two patients are booked with the same practitioner at the same time?* In the original, both are saved, which is wrong. Part G fixes this.

## Evaluation of AI suggestions

| Suggestion | Useful | Unclear | Incorrect | Out of scope |
|---|---|---|---|---|
| Duplicate practitioner/time check | ✔ | | | |
| Validate time format | | ✔ (which format?) | | |
| Save to file/database | | | | ✔ |
| AI version omits validation | | | ✔ (as a final solution) | |
