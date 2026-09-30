---
name: memory-governance
description: Deprecated alias retained for backwards compatibility. Memory classification, scoping, retrieval policy, expiry, and invalidation now live in memory-manager; route all long-term memory work there.
---
# Long-Term Memory Governance (deprecated alias)

This skill has been merged into `memory-manager`, which owns memory layers, scope and source attachment, retrieval policy, expiry, invalidation after retcon or branch divergence, and the rule that memory never outranks an authoritative project file.

**Route all long-term memory work to `memory-manager`.**

Kept in place so that existing projects, prompts, and command references that invoke `memory-governance` continue to resolve rather than failing. It carries no independent behaviour; entries in `memory/` are shared.

The classification vocabulary (`AUTHOR_PREFERENCE`, `NOVEL_CANON`, `ARC_STATE`, `CHAPTER_STATE`, `SCENE_STATE`, `BRANCH_STATE`, `RESEARCH`, `TEMPORARY`) is unchanged and is defined in `memory-manager`.
