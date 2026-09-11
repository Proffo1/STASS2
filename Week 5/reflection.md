# Reflection - Stage 2 Lab

The AI noticed several ambiguities I missed. It pointed out that "same time" in the double-booking rule was undefined, that "search should be fast" and "easy to use" could not be tested, and that FR-10 (cancel) and FR-11 (history) would contradict each other if cancelled appointments were deleted. I had not defined the list of appointment statuses either.

The AI overreached when it proposed SMS reminders, role-based logins, audit logs, AES-256 encryption and online patient booking. None of these appear in the client brief, so I rejected them and kept them out of scope. It also tended to state design decisions as if they were client needs.

The requirement that changed most was FR-10. It now says a cancelled appointment is given the status Cancelled and is never deleted, so the history stays complete. The vague performance and usability wording was also replaced with measurable provisional targets (NFR-05 and NFR-06).

Requirements must have evidence because the software will be judged against them. A requirement that nobody asked for adds cost, risk and extra testing, and it may conflict with what the clinic really needs. "AI suggested it" is not evidence. Only the client brief or a confirmed answer from the client is.
