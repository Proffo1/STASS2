# Reflection - Stage 4 Lab

I modified four parts of the AI draft and rejected three. The draft accepted a string date and a `None` time, and its `change_status` accepted a plain string, so I added type checks and tightened the ID check. I rejected `complete()`, `__eq__`/`__hash__` and `__repr__` because none appears in the approved UML or the requirements. They would have added public behaviour and equality rules that nobody asked for.

The approved design constrained the AI strongly. The UML named every attribute and operation, and the prompt forbade databases, UI and notification classes, so the draft stayed small and had no Manager or service classes. The AI's extra additions were small and easy to spot because I could check each one against the UML.

The AI did well on the transition table and read-only status, but its error handling was weaker than the design required. I checked that by running the draft rather than trusting it.

I also added one thing the UML did not have: a Practitioner specialty, required by the lab. I flagged it for client confirmation and updated the UML to show it.
