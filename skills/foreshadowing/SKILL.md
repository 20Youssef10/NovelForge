---
name: foreshadowing
description: Create, track, audit, and resolve layered narrative setups with stable IDs, visibility and strength assessment, spoiler-risk control, and explicit payoff status. Use for planting clues, auditing payoff debt, and checking reveal integrity.
---
# Foreshadowing v2.1

Assign stable IDs to every meaningful setup and track it from planning through payoff. A setup that is not registered is a setup that will be forgotten.

## Lifecycle

Statuses: `PLANNED`, `PLANTED`, `ACTIVE`, `PAID_OFF`, `ABANDONED`, `RECON_REQUIRED`.

- `PLANNED` — designed but not yet in prose.
- `PLANTED` — present in text, meaning not yet operative for the reader.
- `ACTIVE` — doing work the reader can respond to.
- `PAID_OFF` — resolved in a way that honours the setup.
- `ABANDONED` — deliberately dropped, with a recorded reason.
- `RECON_REQUIRED` — the setup now conflicts with canon and needs a decision.

Never delete an abandoned setup silently. Record the reason, because abandoned setups are where authorial memory diverges from the text.

## What to track

Setup, surface meaning, true meaning, intended payoff, visibility, strength, dependencies, affected chapters, and status. Record in `foreshadowing/FORESHADOW.md`.

## Layering

Prefer layered setups: a detail that reads innocently in context while also serving a deeper function. The surface reading must remain genuinely available, or the layer becomes a puzzle rather than a plant.

Layering depends on the reader not being told which meaning to prefer. That is a `reader-knowledge` question, not a writing one.

## Visibility and strength

- **Visibility** — how noticeable the setup is. Too visible telegraphs the payoff; too faint means the payoff arrives unearned.
- **Strength** — how much work the setup does: a hint, a strong implication, or a near-confirmation.

Match strength to payoff ambition. A major reveal needs a proportionate trail, not one symbolic object mentioned once.

## Audit

Detect forgotten setups, weak or missing payoffs, premature reveals, accidental spoilers, over-obvious signalling, contradictory clues, duplicate setups doing the same work, and setups that no longer serve the story.

Payoff distance matters: a setup resolved immediately is not foreshadowing, and a setup left across a very long span should be reinforced at least once.

## Coordination

Use `payoff-debt` for obligation tracking and overload, `mystery-engine` for clue integrity, `reader-knowledge` for spoiler risk, `theme-engine` and `symbolism-motif` for thematic plants, and `narrative-graph` to link setup to payoff edges.
