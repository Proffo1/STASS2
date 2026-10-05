# SmartCare Case Study (Assignment 2)

A small patient, practitioner and appointment system for SmartCare Community Clinic, built in four stages from first prototype to domain layer.

## Structure

| Folder | Stage | Contents |
|---|---|---|
| `stage01/` | Why software engineering matters | Python prototype, human vs AI comparison, tutorial answers, reflection |
| `stage02/` | Requirements engineering | Requirements Specification v0.2, AI review, reflection |
| `stage03/` | Domain modelling | Domain model workbook, UML diagram, CRC cards, Python skeletons |
| `stage04/` | Domain implementation | `Patient`, `Practitioner`, `Appointment` classes, unit tests, AI engineering log |

## How to run (Python 3.9+, no extra packages)

```
cd stage01 && python smartcare_v01.py
cd stage01 && python test_behaviour.py
cd stage03/code && python check_consistency.py
cd stage04 && python -m unittest -v
cd stage04 && python manual_behaviour_checks.py
```

## AI use

AI use is documented in each stage: `stage01/ai_usage.md`, `stage02/ai_review_and_verification.md`, `stage03/domain_model_workbook_v0.3.md` and `stage04/ai_engineering_log.md`. Each stage also has a `reflection.md`.
