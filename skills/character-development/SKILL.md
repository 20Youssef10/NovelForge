---
name: character-development
description: Design characters as autonomous agents rather than plot tools, tracking identity, psychology, behaviour, relationships, voice, and arc. Use when creating, deepening, auditing, or maintaining any significant character.
---
# Character Development v2.1

Design characters as autonomous agents, not plot tools. A character exists whether or not the plot is watching, and their choices should be explicable from their own internal state.

## Core model

Track identity, backstory, beliefs, desires, fears, goals, flaws, secrets, knowledge, decision patterns, stress responses, moral boundaries, contradictions, relationships, voice, and arc. Contradictions are the most valuable field: a character who is generous and yet ruthless is more interesting than one who is merely consistent.

Record the character in `characters/CHARACTER.md` and voice in `style/CHARACTER_VOICE.md`.

## Agency test

Before a major action, ask whether it follows from the character's goals, beliefs, knowledge, situation, and established behaviour. If it does not, identify precisely what must change for the action to become credible — a new piece of information, a shifted priority, a broken boundary, or a deliberate exception the story acknowledges.

Do not invent knowledge the character has not acquired. A decision made on information the character lacks is the most frequent cause of implausible agency.

## Behavioural consistency

Define decision patterns and stress responses so behaviour is predictable in principle and surprising in detail. Characters should be recognisable under pressure. A crisis that produces entirely uncharacteristic behaviour needs a cause: a changed belief, a broken secret, exhaustion, or an explicit break.

Moral boundaries matter more than preferences. Boundaries are what make a character's crossings land.

## Arcs

Track arcs for major characters where useful: initial state → governing belief → pressure and conflict → key dilemmas → key choices → consequences → reversals → realisation → final state.

Arc belongs to `character-arc-engine`; this skill defines the character the arc operates on. Do not plan transformation without first establishing the belief the transformation revises.

## Relationships

Record each significant bond in `characters/RELATIONSHIP.md`. Relationships are two-way and asymmetric: what A wants from B is rarely what B wants from A, and a one-sided record is a character description rather than a relationship.

## Voice

Voice is character, not decoration. Derive it from background, education, status, and personality rather than assigning a quirk. See `dialogue` and `narrative-voice`.

## Coordination

Use `character-simulation` to stress-test decisions, `character-arc-engine` for transformation, `mystery-engine` for secrets and knowledge, and `causality-engine` where a character's choice drives a plot turn. Flag any character who exists only to deliver information or enable a plot beat.
