---
description: Run a cross-engine audit over a scene, chapter, arc, novel, or series
argument-hint: "<scene|chapter|arc|novel|series> [id]"
---

Run a cross-engine audit.

1. Load `cross-engine-audit`, and `context-manager` plus `context-budget` to build a
   packet that fits the scope.
2. Select the engines the scope actually reaches, using the composition table in the
   skill. State the expected count before starting.
3. Run them in dependency order: establish what is true, then structure, then
   character, then information control, then tempo, then style, then thematics. Each
   stage consumes the last.
4. Record every run in `audit/AUDIT_RUN.md`, including the engines deliberately
   skipped and why. A skipped engine that should have run is the gap the record
   exists to expose.
5. Merge findings into `quality/FINDINGS.md` under stable IDs. Do not report the same
   issue once per engine that noticed it.
6. Where two engines disagree, record the disagreement and let the author decide. A
   scene that reads as intentional to one engine and accidental to another is a real
   authorial question.
7. Close with `quality-gate` and a verdict: PASS, PASS_WITH_ACCEPTED_ISSUES, or
   BLOCKED.

For a long novel, audit arc by arc rather than attempting one pass.