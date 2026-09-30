# Worldbuilding v2.1

Build coherent worlds from geography, history, cultures, factions, politics, economics, religion and myth where relevant, technology, magic, social rules, and important locations.

## Coherence over accumulation

Prefer internally consistent systems with consequences over encyclopedic detail. Every world rule should imply something: a behaviour, a constraint, a resource, a conflict, or a reason someone would break it.

Avoid adding detail that never affects the story. A city needs a river and a toll if the toll shapes the plot; it does not need a census of its bakeries. If a detail cannot plausibly matter later, it is noise.

## Design from pressure

Build the world outward from what creates conflict. Start with the scarcity, the wrong, the border, the resource, or the inheritance that the story needs, and let institutions and customs grow from attempts to manage it. Worlds designed from pressures tend to feel inhabited; worlds designed from aesthetics tend to feel staged.

## Consequences

Distinguish permanent canon from proposals and unresolved questions. Record which world facts are load-bearing and which are decorative, because only load-bearing facts need impact analysis when they change.

New world facts are claims on canon. Register them through `canon-manager` and connect durable ones to `narrative-graph` with stable IDs so that later changes can be traced.

## Scale discipline

Build at the scale the story needs. Expand outward only when a character encounters the boundary; a novel set in one street should not require a fully mapped continent. Depth where it matters, silence elsewhere.

## Avoid the two failure modes

- **Exposition delivery** — the world is explained rather than encountered. Show rules through characters complying with, negotiating, or being broken by them.
- **Setting as wallpaper** — the world exists but nothing in it ever responds to the characters. If the world cannot lose anything, it is not generating tension.

## Coordination

Use `power-system` for magical or technological capability, `faction-simulation` for institutions and blocs, `research` for factual grounding, `consequence-engine` for how world events propagate, and `causality-engine` to verify that world conditions actually cause plot turns.
