# Payoff Debt System v2.1

The story owes its reader things. This system tracks what is owed, when it was promised, and whether it has been paid — so that long novels do not quietly accumulate unkept promises.

## Types

Register every meaningful obligation with a stable ID:

`PROMISE`, `FORESHADOW`, `MYSTERY`, `CHARACTER_SETUP`, `RELATIONSHIP_SETUP`, `CONSEQUENCE`, `WORLD_SETUP`, `POWER_SETUP`

## What to record

For each obligation: stable ID, type, origin (where and when it was created), expected payoff window, dependencies, priority, status, and disposition rationale. Record in `obligations/OBLIGATION.md` and index it in `obligations/INDEX.md`.

Status: `OPEN`, `FULFILLED`, `TRANSFORMED`, `ABANDONED`, `BLOCKED`.

A `TRANSFORMED` obligation has been honoured in a different form — a promise answered with a different question, a setup paid off by reversal. This is legitimate and often better than a literal payoff, but it must be recorded as a decision, because nobody reviewing the novel later will be able to infer that a promise was consciously kept in altered form.

## Detection

- **Forgotten obligations** — never paid, and no longer in the plan.
- **Overloaded windows** — too many payoffs due at once, so each lands without weight.
- **Duplicate promises** — several obligations doing the same work.
- **Conflicting obligations** — two setups requiring incompatible outcomes.
- **Stale windows** — an obligation whose expected window has passed without resolution.
- **Abandonment without record** — setups dropped silently.

Overload is as damaging as neglect. A chapter that discharges six long-awaited payoffs gives the reader six moments of relief and no shape; a chapter that discharges one is a story.

## Window discipline

Payoffs should be spaced so that the reader experiences them as arrivals rather than as an inventory. When several windows overlap, choose deliberately which to move, and record the deferral so it is a decision rather than an oversight.

## Rules

- Never invent payoffs merely to clear debt. A payoff added to satisfy a ledger rather than serve the story is worse than the debt.
- Register obligations at the moment of planning, not retrospectively.
- An obligation may be deliberately abandoned with a recorded reason; that is a decision, not a failure.

## Coordination

Use `foreshadowing` for setup detail, `mystery-engine` for mystery obligations, `narrative-graph` to trace `PROMISES` and `PAYS_OFF` edges, `pacing-engine` to space resolutions, and `consequence-engine` when a payoff was also a consequence.
