---
name: continuity
description: Check and maintain relevant continuity across characters, chronology, locations, objects, knowledge, relationships, world rules, abilities, injuries, terminology, and events, without over-tracking detail that cannot affect the story. Use before and after writing whenever consistency matters.
---
# Continuity v2.1

Use relevance-based checking. Do not exhaustively track details that cannot affect narrative decisions — a comprehensive record of every character's shirt colour is a waste of effort that buries the real contradictions.

## What to check

Identity, chronology, location, possessions, capabilities, injuries, relationships, knowledge, prior events, world rules, terminology, and meaningful state changes.

Prioritise by consequence: knowledge states, physical capability, and broken promises cause the most damaging contradictions because characters then act on false information.

## State separation

Keep these distinct and never let one silently overwrite another:

- Permanent canon
- Current arc
- Current chapter
- Current scene
- Temporary working context

A temporary note that quietly becomes permanent canon is how contradictions enter a project.

## Classification of conflicts

For each conflict, identify the exact conflicting facts, then classify:

- **Likely error** — a mistake; repair automatically if LOW risk.
- **Intentional change** — a deliberate retcon; record it through `canon-manager`.
- **Unresolved ambiguity** — the canon genuinely does not decide; record as `UNRESOLVED`.
- **Retcon candidate** — a change with broad impact; route for author approval.

State both facts and the location of each. A contradiction without two cited locations is a suspicion, not a finding.

## Knowledge checking

The most common serious continuity error is a character acting on information they never acquired. Cross-check every significant decision against `knowledge/LEDGER.md`: who knows this, when they learned it, and whether they could reasonably have inferred it. Acquisition points are mandatory — knowledge without a stated origin is where contradictions come from.

## Rules

Never silently rewrite canon. Report the conflict, classify it, propose the smallest repair, and let the risk level decide who approves it.

## Coordination

Use `timeline` for chronological contradictions, `mystery-engine` for knowledge and reveal states, `narrative-graph` for dependency tracing, `power-system` for capability limits, and `canon-manager` for anything classified as a retcon.
