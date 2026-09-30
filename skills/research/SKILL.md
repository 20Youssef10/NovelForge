---
name: research
description: Research factual and creative material for fiction, separating verified fact, interpretation, speculation, and creative invention, and translating findings into story-useful constraints and detail. Use when a novel depends on real-world accuracy.
---
# Research Engine v2.1

Research serves the story. Findings that do not change anything the novel does are not research, they are accumulation.

## Classification

Classify every finding as exactly one of:

- `VERIFIED_FACT` — supported by an authoritative source.
- `INTERPRETATION` — a defensible reading of evidence, not the evidence itself.
- `SPECULATIVE` — plausible but unconfirmed.
- `CREATIVE_FICTION` — invented for the novel, and labelled as such.

The distinction between fact and interpretation is where fiction goes wrong quietly. A claim presented as established fact when it is actually one reading of contested evidence misleads both the author and, eventually, the reader.

## Method

- For real-world facts, use appropriate current or authoritative sources, and record them through `research-provenance` with verification state and date context.
- Prefer primary and specialist sources over general summaries. Secondary summaries inherit their sources' errors without inheriting their currency.
- Note where sources disagree, and how old they are. Facts decay, and a novel set in the near future inherits the decay of whatever it assumes.
- For fictional invention, preserve internal consistency and mark invented material clearly. An invented element is a design decision, not an error.

## Apply

Translate research into story-useful constraints, options, or sensory detail only when relevant to the requested scene or world element. Research should change what a character can do, what they must fear, what costs money, or what they notice.

Discard findings that do not bear on the narrative, and say that you have discarded them. A research note nobody can use is a note nobody maintains.

## For invention

Where the novel deliberately departs from reality, record what was changed and why, so that internal consistency can be checked against the invented rule rather than against the world. An invented system must be internally coherent even when it is not possible.

## Rules

Never fabricate a citation or a source. An invented reference is worse than an admitted gap. If accuracy matters and cannot be verified, say so and let the author decide whether the scene needs it.

## Coordination

Use `research-provenance` for the source record, `worldbuilding` to apply findings to the setting, `power-system` where the subject is capability, and `canon-manager` for promoting a researched fact into canon.
