---
name: workspace-manager
description: Manage multiple novel projects within one workspace using strict project boundaries, registry metadata, active-project selection, and cross-novel isolation. Use when more than one novel is present, when switching projects, or before any cross-project reference.
---
# Multi-Novel Workspace Manager v2.1

Treat each novel as an isolated narrative world with its own canon, narrative graph, memory, Style DNA, glossary, research, branches, and obligations. Isolation is a correctness property, not tidiness.

## Namespaces

Resolve scope as WORKSPACE → NOVEL → BRANCH before any retrieval or write. A file path without a resolved namespace is an unsafe path.

- **WORKSPACE** — `workspace/WORKSPACE.md`, the author profile, and the project registry.
- **NOVEL** — the project root, its `NOVEL_BIBLE.md`, and all domain files.
- **BRANCH** — `versions/BRANCH.md`, isolated state until an explicit merge.

## Registry

Maintain `workspace/PROJECT.md` with, per project: project ID, name, path, status, active flag, and isolation policy. Exactly one project should normally be active; if the active flag is ambiguous, ask rather than infer, because writing to the wrong novel is unrecoverable.

## Isolation rules

- Never retrieve another novel's canon, characters, terminology, plot, or research on the basis of similarity. Two novels sharing a name, a genre, or a trope share nothing else.
- Never leak style rules between novels. Style DNA is project-specific by definition.
- A cross-novel reference must be explicitly requested by the author, or explicitly marked as shared author knowledge in `author-profile`.
- Cross-novel reuse never promotes material into canon automatically. Reuse is a proposal until `canon-manager` records it.

## Switching projects

Before switching: flush temporary working context, verify no uncommitted branch state, and record the active project. After switching: re-derive namespace, re-read the target `NOVEL_BIBLE.md`, and discard assumptions carried from the previous novel.

## Authored exception

Isolation may be deliberately overridden for shared-world projects, but only with an explicit, recorded author decision naming the shared elements. Absent that record, isolation is absolute.
