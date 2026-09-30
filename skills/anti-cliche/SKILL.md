---
name: anti-cliche
description: Detect overused narrative, dialogue, imagery, character, and plot conventions and propose context-fitting alternatives, while preserving deliberate genre use. Use when prose or structure feels predictable, or when revising familiar beats.
---
# Anti-Cliché Engine v2.1

Identify whether a pattern is a cliché, an intentional convention, or merely familiar. These are three different things, and treating them as one produces novels that are neither surprising nor readable.

## Classification

- **Cliché** — a convention used without function, because it is the path of least resistance.
- **Intentional convention** — a genre move used deliberately, understood by the audience, and doing work.
- **Merely familiar** — recognisable but not yet exhausted, and appropriate here.

Genre conventions are infrastructure. Readers who choose a mystery expect a detective; removing the detective to be original removes the thing they wanted. The problem is never familiarity itself.

## What to examine

- **Narrative moves** — thetwist, the betrayal, the sacrifice, the last-minute arrival, the dying confession.
- **Description and imagery** — the metaphor that arrives pre-formed, imagery imported from a different genre.
- **Character roles** — the wise mentor, the reluctant hero, the loyal friend, the comic relief who knows nothing.
- **Solutions** — the genre-default answer to the problem the plot posed.
- **Emotional beats** — reactions arriving in the expected order and register.
- **Dialogue** — lines that exist because the scene needs them said.

## Record

Log each review in `cliches/CLICHE.md`, including the classification and the decision. A convention that was assessed and kept is a decision; one that was never assessed is a habit that happened to survive.

## Method

For each candidate, explain why the beat feels expected — which convention it draws on, and what prior expectation it confirms. Then propose alternatives that remain compatible with canon, character agency, and causality.

Alternatives must come from this story: its setting, its characters' psychology, its themes, its established world. A different cliché is not an alternative. An alternative that would require breaking canon or character is not an alternative.

## Where subversion fails

Subversion requires the reader to hold the expectation and then have it overturned for a reason. Subverting without establishing the expectation produces only confusion. Reversal for its own sake is a different cliché — the shock of the unexpected — and readers recognise it too.

## Rules

- Never rewrite merely to appear novel. If a convention is doing its work, the correct action is to leave it.
- Do not reject a familiar device for being familiar. Ask whether it is functioning.
- Report rather than replace, and let the author choose. Convention is frequently a deliberate commercial or genre decision.

## Coordination

Use `trope-manager` for the registry and expectation tracking, `theme-engine` for alternatives grounded in theme, `character-simulation` for whether a subverted moment is in character, and `generic-writing-detector` for prose-level stock language.
