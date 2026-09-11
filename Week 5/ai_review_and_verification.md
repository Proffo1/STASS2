# Parts F and G - AI Requirements Review and Verification

**Tool used:** Claude (Anthropic). Check your course policy. If you must use Microsoft Copilot, paste the prompt below into Copilot and replace the AI output with your own results.

## Part F - Prompt used
> Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation.

## Part F - AI output (summarised) and Part G - classification

| # | AI suggestion | Evidence or assumption? | Decision | Evidence used / explanation |
|---|---|---|---|---|
| 1 | FR-04 does not say what "same time" means. Should overlapping appointments also conflict? | Question requiring validation | **Modified** | The brief gives no appointment length. I kept exact date/time matching and added open question 4. |
| 2 | "Search should be fast" (draft NFR) cannot be tested. Add a number. | Based on the wording of the draft | **Accepted** | Replaced it with NFR-06: under 1 second at course scale, marked provisional because the numbers are an assumption. |
| 3 | FR-06/FR-07 do not say what searches the client wants. | Question requiring validation | **Accepted** | The brief says "difficulty finding patient information" only. FR-07 is provisional and open question 2 was added. |
| 4 | Status list is undefined, so "inconsistent status" cannot be tested. | Based on "inconsistent appointment status" | **Accepted** | FR-09 now fixes a status list (Scheduled, Completed, Cancelled) and FR-12 limits changes. Both are marked assumptions. |
| 5 | FR-10 and FR-11 conflict if cancelled appointments are deleted. | Based on "limited appointment history" | **Accepted** | FR-10 now says "set status to Cancelled, never delete". |
| 6 | NFR "easy to use" is vague. | Based on the draft wording | **Modified** | Replaced with "no more than 5 prompts", marked provisional. The number is my target, not the client's. |
| 7 | Add SMS reminders for patients. | No evidence | **Rejected** | Not in the brief, so it stays out of scope. |
| 8 | Add role-based login and audit logs. | No evidence | **Rejected** | The brief does not mention users, permissions or audit needs. |
| 9 | Require AES-256 encryption of records. | No evidence | **Rejected** | Over-specified and invented. Privacy is raised only as open question 6. |
| 10 | Ask about privacy and data retention rules. | Question requiring validation | **Unverified** (kept as a question) | Plausible for health data, but I cannot confirm rules without the client. |
| 11 | Patients may need to book online. | No evidence | **Rejected** | The brief says staff use the system. Patient portal is out of scope. |

**Pattern:** the AI was strongest at ambiguity and testability (items 1–6). It overreached when it added features and technical solutions (7–9, 11).
