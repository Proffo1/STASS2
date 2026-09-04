# AI Activity Card - Ask, Check, Explain (applied to `book_appointment`)

**Before AI:** I think the code checks the name is not empty, builds a dictionary and appends it to a list. Problems I can already see: no duplicate check, the time is not validated, and data is not saved.

**AI request:** "Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me reason about the solution."

**Evaluate / Decide**
| Suggestion | Useful | Unclear | Incorrect | Out of scope | Decision |
|---|---|---|---|---|---|
| Check for double booking | ✔ | | | | Accept |
| Validate time format | | ✔ | | | Keep unverified |
| Save to database | | | | ✔ | Reject |

**Verify:** ran the code, tested normal and unusual input (`test_behaviour.py`), compared with requirements, checked Python truthiness docs.

**Explain:** I can explain the final code without the AI response. Still to understand: proper date/time handling with `datetime`.
