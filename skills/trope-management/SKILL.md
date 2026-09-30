---
name: trope-management
description: Deprecated alias retained for backwards compatibility. The full trope registry, expectation tracking, and subversion analysis now live in trope-manager; route all trope work there.
---
# Trope Management (deprecated alias)

This skill has been merged into `trope-manager`, which owns the trope ledger, reader-expectation modelling, subversion analysis, stacking detection, and convention preservation.

**Route all trope work to `trope-manager`.**

Kept in place so that existing projects, prompts, and command references that invoke `trope-management` continue to resolve rather than failing. It carries no independent behaviour and writes to no separate records — the ledger in `themes/TROPE.md` is shared.

If you are migrating an older project, no data conversion is required: both names refer to the same ledger.
