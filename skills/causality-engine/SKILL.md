---
name: causality-engine
description: Verify that major plot turns arise through coherent prior conditions, triggers, choices, actions, mechanisms, and consequences, distinguishing necessity from coincidence and coincidence from contrivance. Use when a turn feels unearned or arbitrary.
---
# Causality Engine v2.1

Verify that major turns arise rather than merely happen. A plot that moves is not the same as a plot that moves because of what came before.

## Chain model

For each major turn, model in order:

1. **Prior conditions** — the established state that made the turn possible.
2. **Trigger** — the immediate event that set it off.
3. **Character choice** — the decision, with the options it rejected.
4. **Action** — what was done.
5. **Mechanism** — how the action produced the result.
6. **Result** — the immediate outcome.
7. **Secondary effects** — what follows.

A chain missing its mechanism is the most common failure: the outcome simply happens to the action without a stated or implied route between them.

## Distinguishing the three

- **Causal necessity** — given the conditions and the character's established nature, the result was the only credible outcome.
- **Coincidence** — an uncaused event that helps the story. Acceptable when seeded, plausible, and in character.
- **Contrivance** — an uncaused event that exists to force a turn, and strains against established world or character logic.

Coincidence used as repair is not coincidence; it is a structural patch. When a turn needs coincidence to work, the real problem is upstream and should be fixed there.

## Flags

- Missing knowledge — a character acts on information never acquired.
- Impossible timing — events cannot occur in the order given.
- Unexplained resources — a character uses something they could not have obtained.
- Passive resolution — a conflict ends because a character stops acting, not because anything changed.
- Outcomes lacking a mechanism.
- Reversals that serve the author rather than the situation.

## Deliberate coincidence

Allow deliberate coincidence when the project supports it and mark it clearly in the plan, so a later reader knows it was a choice rather than an oversight. An unmarked coincidence is indistinguishable from a mistake.

## Output

Record chains in `causality/CAUSAL_CHAIN.md` with each link, the entity IDs involved, and any weak or missing links identified. Hand weak links to `plot-engineering` for repair and to `canon-manager` if repairing them changes canon.

## Coordination

Use `plot-engineering` to design turns, `consequence-engine` for what follows, `character-simulation` to verify the decision was in character, `mystery-engine` for withheld information, and `narrative-graph` to trace dependencies.
