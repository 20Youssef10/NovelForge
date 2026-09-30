# Canon Change Procedure

Step-by-step detail for `canon-manager`. Load when a change is HIGH risk, when a retcon is proposed, or when a merge may affect canon. The skill body carries the classification vocabulary and the rules; this file carries the full procedure and the migration discipline.

## Full change procedure

1. **State the change** in one sentence, in canon terms. "Serra dies" is a statement; "adjust the death scene" is not.
2. **Classify what is being changed** — the current canon state, and the proposed state.
3. **Trace dependencies** across every domain:
   - graph edges touching the entity
   - open obligations that assumed the old fact
   - chapter and scene plans resting on it
   - character sheets, arcs, and relationships
   - timeline events and their ordering
   - mystery prerequisites and reveal timing
   - foreshadowing and payoff windows
   - faction positions and knowledge states
   - world facts and power-system rules
4. **Classify risk** as LOW, MEDIUM, or HIGH against the orchestrator's scale.
5. **Decide execution** — LOW may apply automatically, MEDIUM confirms scope, HIGH requires author approval **before** any edit.
6. **Snapshot** before applying, via `version-control`.
7. **Apply**, updating every domain in the same pass.
8. **Record** the reason, affected files, approving authority, and migration status.
9. **Verify** by re-running continuity, timeline, obligation, and graph checks.

## Risk classification

| Level | Applies to | Execution |
| --- | --- | --- |
| LOW | Local wording, formatting, obvious local continuity repairs | Automatic |
| MEDIUM | Bounded restructuring, limited behavioural change, one obligation with no ripple | Confirm scope |
| HIGH | Canon or retcon, major character fate, ending, relationship structure, global timeline, power rules, major faction state, cross-arc dependency, research promoted to canon, branch merge, cross-novel memory transfer, large-scale style change | Author approval before execution |

A change that cannot be reversed cleanly is HIGH regardless of how small it appears.

## Migration discipline

The most common post-retcon defect is not the change itself but its **partial application**: the new fact in the Bible, the old fact still in three chapters and two character sheets.

- Record migration status: PENDING, IN_PROGRESS, COMPLETE.
- List the specific locations that must change, not a general area.
- A HIGH-risk retcon is not complete until migration is COMPLETE.
- Until then, flag the project as mid-migration in the agent report.

## Canon states

| State | Meaning | May change without approval? |
| --- | --- | --- |
| `PERMANENT_CANON` | Established and binding | No |
| `ARC_CANON` | True for the current arc | At arc boundaries |
| `CHAPTER_CANON` | True for the current chapter | Within the chapter |
| `SCENE_STATE` | True only within the scene | Freely |
| `PROPOSAL` | Proposed, not accepted | It has no authority at all |
| `UNRESOLVED` | Genuinely open | Yes, by resolving it |
| `RECON` | Superseded, with reason and record | No, but it is already retired |

Ambiguity between two states is itself a finding. Record it rather than choosing silently.

## Dimension independence

Author truth, character knowledge, and reader knowledge are **separate** canon dimensions. Changing one does not change the others. A character can learn a fact without the reader learning it, and a reveal can change what the reader knows while the author's underlying truth is untouched. Most continuity errors are dimension collapses rather than factual contradictions.

## Branch interaction

- A change on a branch does not alter main canon until an explicit, gated merge.
- Before merge: canon impact analysis, continuity, timeline reconciliation of **both** chronologies, graph checks, obligation reconciliation.
- After merge: invalidate branch-scoped memory, re-run the gate on main.

## Rules that do not bend

- There is no quiet retcon.
- Research findings do not become canon by being true; promotion is a separate recorded decision.
- A proposal in working context is not canon because it was retrieved.
- Never delete a superseded fact. Record what it was, what replaced it, and why.
