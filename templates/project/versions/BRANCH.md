# Story Branch

- ID:
- Name:
- Parent snapshot:
- Created:
- Status: EXPERIMENTAL / REVIEW / APPROVED / MERGED / ABANDONED
- Canon branch: this branch

## Purpose
The question the branch exists to answer (what happens if...):
Scope of experimentation:
What it must not change:

## Isolation
Canon state: fully isolated from main until an explicit merge.
Branch-specific canon:
Branch-specific timeline:
Affected graph edges (branch-local):
Branch-specific memory scope (see `memory/MEMORY_ENTRY.md`):

## State
| Aspect | Main | Branch |
| --- | --- | --- |
| Key fact | | |
| Character state | | |
| Timeline | | |
| Open obligations | | |
| Faction positions | | |

## Findings
What the experiment revealed, whether or not it is merged:
What was better in the branch:
What was worse:
What should be carried into main regardless of merge outcome:

## Merge requirements
All must be satisfied before merge is proposed.

- [ ] Canon impact analysis (`CHANGE_IMPACT.md`)
- [ ] Continuity check
- [ ] Timeline reconciliation — both chronologies, not one superseding the other
- [ ] Narrative graph check (orphans, dead edges)
- [ ] Obligation reconciliation (opened, discharged, conflicting)
- [ ] Mystery and reader-knowledge state reconciled
- [ ] Character dependency check
- [ ] Style and voice check
- [ ] Quality gate run on the branch
- [ ] HIGH-risk items confirmed with the author
- [ ] Conflict resolutions recorded one at a time

## Merge
Merged on:
Approved by:
Conflicts and how each was resolved:
Post-merge memory invalidation completed:
Quality gate re-run on main:

## Rules
- A branch that quietly edits main canon is not a branch.
- Never merge silently.
- Close branches explicitly, including abandoned ones. Unclosed branches are pure cost.
