# Series Manager v2.3

`workspace-manager` enforces isolation between novels by default. This skill is the deliberate, recorded exception: a series shares canon because the author said so, and shares nothing else.

## Namespace

WORKSPACE → SERIES → NOVEL → BRANCH

A novel may belong to exactly one series, or to none. The series sits above the novel and below the workspace, and the series bible is a distinct authority from any single novel's Novel Bible.

## Two tiers of canon

Keep these strictly separate, because conflating them is how sequels break:

- **Series canon** — true across every book. World rules, the shared timeline, magic or technology limits, house and faction history, recurring characters, the glossary.
- **Novel canon** — true only within one book. Local politics, book-specific antagonists, a character's state at the start of this volume.

When a book contradicts series canon, that is almost always a defect, not a subversion. A deliberate change requires a recorded author decision and a migration note in the series bible.

## Inheriting canon

A new novel in a series inherits the series bible at creation and records what it inherits. Everything inherited is `SERIES_CANON` until the book changes it, at which point the change is either local (book-only, recorded) or a series-level retcon requiring approval across every affected book.

## Cross-book continuity

Track the things that cannot be quietly contradicted: who is alive, who knows what, ages, injuries, alliances, and promises. A character who lost an arm in book one and uses it in book three is the most common series failure, and it is always a knowledge-state problem before it is a physical one.

Where a book could plausibly be read without the earlier ones, say so and let the author choose whether to enforce continuity or signal accessibility.

## Divergence control

When books deliberately diverge, record the divergence point, what each book does differently, and whether a later book is expected to reconcile it. Unexplained divergence reads as error to readers and as amnesia to agents.

## Rules

- Never retrieve a series bible as canon for a novel outside that series.
- Never promote novel-local canon to series canon without explicit author approval and a migration note.
- Shared style is not shared canon. Two books in a series may have deliberately different voices; the series Style DNA holds only what the author confirmed applies to all of them.
- Naming a character similarly across unrelated series grants no access.

## Output

Maintain `series/SERIES_BIBLE.md` for shared canon, `series/BOOK.md` per volume, and register the series in the workspace. Report unresolvable cross-book conflicts to the author rather than choosing a winner.

## Coordination

Use `workspace-manager` for boundaries and the project registry, `canon-manager` for classification and retcon approval, `timeline` for the shared chronology, `memory-manager` for series-scoped state, and `localisation` for terminology that must stay consistent across translated volumes.
