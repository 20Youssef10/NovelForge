# Advanced Version Control v2.1

Every meaningful change should be attributable and reversible. History exists so that a bad structural decision costs an afternoon rather than the novel.

## Operations

`SNAPSHOT` · `DIFF` · `COMPARE` · `RESTORE` · `BRANCH` · `EXPERIMENT` · `MERGE` · `RECON` · `CANONIZE`

Represent major story states as snapshots or branches recording parent, purpose, scope, and canon status in `versions/SNAPSHOT.md` and `versions/BRANCH.md`.

## Before editing

Snapshot first. A structural change without a recorded parent cannot be evaluated, because there is nothing to compare it against, and a change that turns out wrong cannot be undone without guessing what came before.

Snapshot scope should match the change: a single scene repair needs a scoped snapshot, a restructure needs a full one. Snapshotting everything indiscriminately makes the history unreadable and the storage meaningless.

## Branches

A branch is isolated from main canon until explicitly merged. Branches are for genuine alternatives and experiments: what happens if this character survives, what if the reveal happens here instead, what if the faction sides differently.

Within a branch, track branch-specific canon, timeline, dependencies, affected files, unresolved conflicts, and quality-gate results. A branch that quietly edits main canon is not a branch.

## Merge

Never merge silently. Before merging:

1. Run canon impact analysis via `canon-manager` and `CHANGE_IMPACT.md`.
2. Run continuity, timeline, narrative-graph, obligation, mystery, and character-dependency checks.
3. Resolve conflicts explicitly, one at a time, recording each decision.
4. Confirm HIGH-risk items with the author.
5. Reconcile both chronologies and both canon sets; do not assume one supersedes the other.

After a merge, run orphan and dead-edge checks on the graph, re-verify open obligations, and invalidate branch-scoped memory.

## Retcons

A retcon is a version operation with a reason. Record previous canon, new canon, reason, affected files, impact level, and author approval. Never erase history to make a change look clean — the record of what was previously true is how later readers of the project understand why the text is as it is.

## Rules

- Do not merge branches into canon silently, ever.
- Do not use `RESTORE` to undo an approved decision without recording that you did.
- Keep branch count low. Branches that are abandoned without merging are pure cost; close them explicitly.

## Coordination

Use `canon-manager` for classification and approval, `continuity` and `timeline` for pre-merge checks, `payoff-debt` for obligation reconciliation, and `memory-manager` for post-merge invalidation.
