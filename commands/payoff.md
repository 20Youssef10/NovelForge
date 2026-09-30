---
description: Audit unresolved narrative obligations and payoff windows
argument-hint: "[audit|show|resolve] [id]"
---

Audit narrative obligations.

1. Load `payoff-debt`, and `foreshadowing` for setup detail.
2. Read `obligations/INDEX.md` and report what is open, due soon, stale, and overdue.
3. Flag overloaded windows, where resolving several obligations in one chapter gives the reader several moments of relief and no shape.
4. Never invent a payoff to clear a row. A payoff added to satisfy the ledger is worse than the debt.
5. `ABANDONED` with a recorded reason is a legitimate resolution; propose it where a payoff is clearly never coming.
6. Log any newly created obligation with a stable ID.
