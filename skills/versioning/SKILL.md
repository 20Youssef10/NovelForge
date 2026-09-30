---
name: versioning
description: Deprecated alias retained for backwards compatibility. Snapshots, branches, diffs, rollbacks, merges, and retcons now live in version-control; route all versioning work there.
---
# Versioning (deprecated alias)

This skill has been merged into `version-control`, which owns snapshots, diffs, comparisons, rollbacks, branches, experimental alternatives, merge proposals, conflict review, and approved retcons, together with the pre-merge check sequence.

**Route all versioning work to `version-control`.**

Kept in place so that existing projects, prompts, and command references that invoke `versioning` continue to resolve rather than failing. It carries no independent behaviour; the records in `versions/` are shared.

`version-control` retains the v1.x risk discipline: snapshot before a meaningful edit, keep branches isolated, and never merge silently.
