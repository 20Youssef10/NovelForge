# NovelForge Workspace

Workspace ID:
Created:
Isolation policy: STRICT

## Author profile
Path: `AUTHOR_PROFILE.md`
Scope: the only material that crosses novels by design.

## Novel registry
| Project ID | Name | Path | Status | Active |
| --- | --- | --- | --- | --- |
| | | | | |

Exactly one project should normally be active. If the active flag is ambiguous, ask rather than infer — writing to the wrong novel is unrecoverable.

## Namespaces
WORKSPACE → NOVEL → BRANCH. Resolve this before any retrieval or write. A file path without a resolved namespace is an unsafe path.

Each novel owns its own canon, narrative graph, memory, Style DNA, glossary, research, branches, and obligations. Nothing is shared by default.

## Isolation rules
- Never retrieve another novel's canon, characters, terminology, plot, or research on the basis of similarity. A shared name, genre, or trope shares nothing else.
- Never leak style rules between novels. Style DNA is project-specific by definition.
- A cross-novel reference must be explicitly requested by the author, or explicitly marked as shared author knowledge in `AUTHOR_PROFILE.md`.
- Cross-novel reuse never promotes material into canon automatically. Reuse is a proposal until `canon-manager` records it.

## Cross-novel reuse
| Source novel | Target novel | Element | Shared as | Author instruction | Canon status in target |
| --- | --- | --- | --- | --- | --- |
| | | | shared author knowledge / project-specific | | PROPOSAL / CANON |

Absent an explicit recorded author decision, isolation is absolute.

## Switching projects
Before switching: flush temporary working context, confirm no uncommitted branch state, record the active project.
After switching: re-derive namespace, re-read the target `NOVEL_BIBLE.md`, discard assumptions carried from the previous novel.
