---
name: memory-manager
description: Maintain long-term writing-agent memory across sessions using scoped durable notes, retrieval policies, expiry rules, and strict canon boundaries. Use when persisting state beyond a single task, resuming prior work, or preventing stale memory from contaminating a project.
---
# Long-Term Agent Memory v2.1

Memory accelerates retrieval. It never replaces project files, and it never outranks them.

## Layers

Classify every memory entry into exactly one layer, and attach scope and source:

`AUTHOR_PROFILE` → `NOVEL_CANON` → `CURRENT_ARC` → `CURRENT_CHAPTER` → `CURRENT_SCENE` → `BRANCH_STATE` → `RESEARCH` → `TEMPORARY_WORKING_CONTEXT`

Scope widens as durability increases. A scene-level observation that seems universally true is almost always wrong; promote it deliberately or let it expire.

## What to persist

Record entries in `memory/MEMORY_ENTRY.md`.

Persist only meaningful durable state: established decisions, author preferences, resolved canon questions, active obligations, and long-running project constraints. Do not persist prose, restatements of what the Novel Bible already says unambiguously, or speculation about future work.

Prefer project files as the canonical source. Memory holds pointers and working knowledge that would be expensive to re-derive.

## Retrieval

Retrieve by scope, narrowing from `AUTHOR_PROFILE` to the active layer. Memory is a candidate source: verify any recalled fact against the current file before relying on it, because memory may predate a retcon.

## Expiry and invalidation

- `TEMPORARY_WORKING_CONTEXT` expires when its scope ends. Do not carry it forward by default.
- Invalidate or downgrade entries after a retcon, a branch divergence, a merge, or project separation.
- Mark entries that depend on branch state with that branch, and never surface them outside it.
- Prefer a `REVIEW` date to an assumption that an entry is still true.

## Rules

- Never promote speculation to durable memory.
- Never let memory override an authoritative current file. When they disagree, the file wins and the memory entry is corrected.
- Never transfer canon, names, terminology, or style rules between novels on the basis of similarity. Cross-novel material requires explicit author instruction.
- Memory is disposable. Deleting an entry that is wrong is better than maintaining one that misleads.
