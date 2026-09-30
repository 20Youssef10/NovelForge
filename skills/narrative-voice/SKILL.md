---
name: narrative-voice
description: Analyse and preserve narrator identity, narrative distance, focalisation, reliability, and consistency across POV structures, detecting head-hopping, omniscient leakage, and impossible knowledge. Use for any POV design, revision, or audit.
---
# Narrative Voice Engine v2.1

Track who is speaking, how near they are, and what they are permitted to know. Voice is a structural property, not a decorative one: it determines what can be narrated at all.

## What to track

- **POV mode** — first, second, third limited, omniscient, multiple POV, or unreliable.
- **Narrator personality** — what the prose reveals about whoever is doing the narrating.
- **Distance** — how close the narration sits to the focal character, and whether it may move.
- **Focalisation** — whose experience filters the presentation.
- **Knowledge boundary** — what the narrator can and cannot know at each point.
- **Reliability** — where the narrator is partial, mistaken, or deliberately misleading.
- **Rhythm and interpretive language** — the permitted range of comment.

Record the project's POV conventions in `voice/VOICE_PROFILE.md`.

## Modes and their costs

Each mode buys something and costs something. Choose deliberately:

- **First person** — intimacy and restricted knowledge, at the cost of what the narrator cannot see.
- **Third limited** — interior access plus wider staging, with the obligation never to slip.
- **Omniscient** — scope and sweep, at the cost of suspense unless information is still withheld.
- **Multiple POV** — breadth and scale, at the cost of switching friction and voice consistency.
- **Unreliable** — dramatic irony and tension, at the cost of requiring detectable signals.

## Detection

- **Accidental head-hopping** — the narration moves to a different consciousness mid-scene without signal.
- **Omniscient leakage** — the narrator knows what a limited POV could not.
- **Impossible knowledge** — narration uses information no character has.
- **Inconsistent judgement** — the narrator evaluates with a stance belonging to a different character.
- **Voice shift** — the prose adopts a different register, dialect, or sensibility without a POV change to justify it.
- **Distance violation** — the narration moves closer or further than the established convention permits.

## Signals and transitions

Shifts require signals: a section break, a named character, an explicit time marker. Unsignalled shifts within a scene are almost always errors, because the reader cannot recover the intended focalisation.

Where a scene is deliberately head-hopped, the shift must be legible and consistently handled.

## Rules

Never silently convert a limited POV to omniscient to solve a convenience problem. If the narration needs information the POV character lacks, change the information, the POV, or the structure.

## Coordination

Use `narrative-style` for the broader prose contract, `dialogue` for character speech within the voice, `reader-knowledge` for what the reader may be told, and `continuity` for knowledge-state violations.
