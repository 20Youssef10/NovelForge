---
description: Run the quality gate and record a verdict
argument-hint: "[scope]"
---

Run the quality gate.

1. Load `quality-gate`. Run the checks that apply to this scope, not all of them.
2. Use `project/quality-check.md` for a single unit and `templates/QUALITY_GATE.md` for a project-wide audit.
3. Carry findings into `quality/FINDINGS.md` and check its regression watch list.
4. Record a verdict: PASS, PASS_WITH_ACCEPTED_ISSUES, or BLOCKED.
5. A gate does not invent fixes. It records evidence, safe repairs, and decisions needing the author.
6. Never declare completion solely because prose exists.
