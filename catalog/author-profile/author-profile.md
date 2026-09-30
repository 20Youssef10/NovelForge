# Author Preference Profile v2.1

Store what the author has told you about how they want to work. This is the only part of NovelForge that crosses novels by design.

## What to store

- **Writing goals** — what they are trying to produce and why.
- **Dislikes and refusals** — tropes, devices, framings, and processes they have ruled out.
- **Workflow preferences** — plan-first or draft-first, approval expectations, how much autonomy to take.
- **Planning granularity** — how detailed they want plans before drafting begins.
- **Feedback preferences** — how much criticism they want, in what form, and how blunt.
- **Language and formatting** — variant, conventions, and house style.
- **Recurring stylistic preferences** — consistent tendencies they have established.
- **Autonomy boundaries** — what must always be asked about, and what need never be.

Store in `workspace/AUTHOR_PROFILE.md`.

## Precedence

Author preferences shape workflow and style, but they never override novel-specific authority:

1. Explicit current instruction from the author
2. This novel's canon and Style DNA
3. This novel's established workflow decisions
4. Stored author preferences
5. General defaults

A preference recorded for one novel does not automatically apply to another. Promote it here only when the author has stated it as generally true.

## Rules

- Store only stable preferences the author has explicitly established. Do not infer a preference from a single decision, and do not accumulate guesses.
- Separate stable preferences from temporary instructions. A note to change tone for one chapter is not an author preference.
- Never use a stored preference to justify ignoring an explicit instruction to the contrary. The current instruction wins.
- A preference that conflicts with the novel's own voice yields to the novel's voice. Authors are not always consistent with themselves across works.

## Maintenance

Review periodically and delete preferences that have not been confirmed in a long time. A profile that accumulates unverified assumptions will eventually override a live instruction, which is the worst failure this skill can produce.

## Coordination

Use `narrative-style` for the novel's actual prose voice — the profile is not the source of Style DNA. Use `workspace-manager` for cross-novel boundaries, and `memory-manager` for scoped persistence of these preferences.
