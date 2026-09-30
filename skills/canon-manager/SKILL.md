---
name: canon-manager
description: Classify facts and changes into canon states, run dependency and impact analysis, and gate approved retcons. Use for any change to established canon, any promotion of a proposal to canon, and any decision that alters what has already been written.
---
# Canon Manager v2.1

Canon is the authority. Everything else — proposals, branch experiments, research hypotheses, memory — is a claim upon it, never a substitute for it.

## Classification

Classify every fact and every proposed change into exactly one state:

- `PERMANENT_CANON` — established and not to change without approval.
- `ARC_CANON` — true for the current arc, revisable at arc boundaries.
- `CHAPTER_CANON` — true for the current chapter.
- `SCENE_STATE` — true only within the current scene.
- `PROPOSAL` — proposed, not accepted; carries no authority.
- `UNRESOLVED` — canon is genuinely open; candidate answers recorded.
- `RECON` — superseded, with the supersession recorded and its reason.

Ambiguity between two states is itself a finding. Record it rather than silently choosing.

## Change procedure

1. State the proposed change in one sentence, in canon terms.
2. Locate every dependency: graph edges, obligations, chapter plans, character sheets, timeline events, mystery prerequisites, foreshadowing, and affected prose.
3. Produce an impact analysis using `CHANGE_IMPACT.md`, covering direct files, graph edges, characters and arcs, timeline, information states, obligations, causality, power, factions, themes, style, and branch interactions.
4. Classify risk against the orchestrator's LOW / MEDIUM / HIGH scale.
5. Apply LOW-risk local updates automatically. Route MEDIUM for confirmation. Route HIGH for explicit author approval before any edit.
6. Record the reason, the affected files, the approving authority, and the migration status.

## Rules

- Never silently overwrite established canon. There is no such thing as a quiet retcon.
- A change made in a branch does not alter main canon until an explicit, gated merge.
- Research findings do not become canon by being true. Promotion is a separate, recorded decision.
- Author truth, character knowledge, and reader knowledge are separate canon dimensions; changing one does not automatically change the others.
- If a change cannot be reversed cleanly, treat it as HIGH regardless of how small it appears.

## Output

Maintain `canon/facts.md`, `canon/retcons.md`, and `canon/unresolved.md` as the durable record. Every entry carries a stable ID, its establishing reference, its dependencies, and the date it was last reviewed. Stale canon that is never reviewed becomes a liability.
