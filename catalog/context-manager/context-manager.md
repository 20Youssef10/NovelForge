# Context Manager v2.1

Retrieve only what can affect the present decision. Assembling the largest possible context is a failure mode, not diligence: irrelevant material dilutes attention and invites contradiction.

## Isolation levels

Resolve scope before retrieval: WORKSPACE → NOVEL → BRANCH. Never leak content from another novel or branch unless an approved cross-project workflow explicitly requests it. Branch state and main canon are separate truths; mixing them produces the worst class of error.

## Layers

Retrieve in this order and stop as soon as the decision is supported:

1. `AUTHOR_PROFILE` — workflow and style preferences that shape how you work.
2. `PERMANENT_CANON` — facts that cannot change without approval.
3. `CURRENT_SAGA` → `CURRENT_ARC` → `CURRENT_CHAPTER` → `CURRENT_SCENE` — the active narrative position.
4. `GRAPH_NEIGHBOURS` — typed edges within one or two hops of the current entities.
5. `OBLIGATIONS` — open promises, setups, and consequences awaiting resolution.
6. `RELEVANT_ENTITIES` — only those characters, locations, factions, and objects the task actually touches.
7. `RESEARCH_PROVENANCE` — verification state for any factual claim in scope.
8. `WORKING_CONTEXT` — temporary notes for this task only.

Prefer durable relationships and active dependencies over incidental prose. A character sheet matters if the character acts; it does not matter because the character is prominent.

## Packets

Produce a `CONTEXT_PACKET.md` for multi-step work: task, scope, current narrative position, canon state, graph neighbourhood, characters and arcs, world and factions, timeline, knowledge states, mysteries, obligations, causality and consequences, power and battle state, Style DNA and voice, themes and motifs, research provenance, active branch, and unresolved issues.

## Rules

- Always separate canon, proposal, branch state, author truth, character knowledge, and reader knowledge. Collapsing these is the single most common source of hallucinated continuity.
- A proposal never becomes canon merely because it was retrieved. Promotion requires `canon-manager` and, for HIGH-risk changes, author approval.
- Respect `author-profile` for workflow and style preferences, but the novel's own Style DNA remains authoritative for prose.
- Exclude information the current POV character cannot know unless the task is explicitly authorial.
- If a retrieval is ambiguous, retrieve one layer wider rather than guessing, and flag the ambiguity in the packet.
