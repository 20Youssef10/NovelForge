---
name: consequence-engine
description: Propagate meaningful immediate, delayed, social, material, relational, strategic, political, and thematic consequences through the narrative graph and timeline. Use after any significant change to check that the story acknowledges what it caused.
---
# Consequence Engine v2.1

When something important happens, the world responds — eventually. This engine exists to find the places where the story forgot.

## Categories

For every meaningful action, inspect:

- **Immediate** — what changes on the page.
- **Delayed** — what surfaces later, once consequences have had time to compound.
- **Social** — how groups and individuals react.
- **Material** — resources, money, damage, capability loss.
- **Relational** — trust, alliance, dependence, resentment.
- **Strategic** — how plans and positions change.
- **Political** — how institutions and factions realign.
- **Thematic** — what the event means for the story's questions.

Not every action needs all eight. A small action with a large delayed consequence is more interesting than an action with eight immediate ones.

## Propagation

Propagate major changes through the `narrative-graph` and `timeline`. For each affected entity, ask what would plausibly now be different, and record it. Also ask what an interested observer would have noticed — consequences that leave no trace anywhere are inert.

## Record

Maintain each tracked consequence in `consequences/CONSEQUENCE.md`, with its category, expected window, and propagation set. A consequence with no recorded window never arrives, because nothing schedules it.

## Detection

- **Consequence amnesia** — a significant event produces no acknowledgement in later scenes.
- **Accidental world-state reset** — the story silently returns to a prior state, as though nothing happened.
- **Unearned recovery** — damage is forgotten faster than the world's logic permits.
- **Underweighted response** — factions and institutions react far more calmly than their motives would allow.
- **Consequence the story repeatedly ignores** — a pattern the author has stopped noticing.

## Timing

Consequences should not all land at once. Immediate, next-scene, next-arc, and late consequences are all useful, and the gap between cause and effect is a primary source of pacing tension. Record the expected window so a late consequence does not arrive unannounced.

## Rules

Do not invent consequences the story does not want. Report what should follow and let the author decide whether the story has room for it. A consequence declined deliberately is a decision; a consequence unnoticed is a bug.

## Coordination

Use `causality-engine` to verify the cause, `faction-simulation` for institutional response, `payoff-debt` to register the consequence as an obligation, `timeline` for scheduling, and `narrative-graph` to trace affected entities.
