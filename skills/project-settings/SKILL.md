---
name: project-settings
description: Read and update project-level configuration for POV model, tense, approval strictness, autonomy level, and engine selection, so these are project settings rather than facts buried in a plan. Use when configuring a project, changing approval strictness, or when the orchestrator needs to resolve what may proceed without asking.
---
# Project Settings v2.5

Some decisions belong to the project rather than to a scene or a plan. POV, tense, and how much the agent may decide alone are configuration, not prose. Keeping them in a plan means they get re-litigated every session.

## Record

Configuration lives in `PROJECT_SETTINGS.md`. Every field the author has decided is authoritative; every field they have not is `UNRESOLVED`, and an unresolved setting is never guessed.

## Fields that change agent behaviour

**POV model and tense** — read by `narrative-voice` and `scene-writing`. An unset value means the narrator has not been chosen yet, which is different from third limited.

**Approval strictness** — the most consequential field, because it governs how much proceeds unattended:

| Level | MEDIUM risk | HIGH risk |
| --- | --- | --- |
| `strict` | Ask before acting | Ask before acting |
| `standard` | Proceed when clearly local and reversible | Ask before acting |
| `permissive` | Proceed | Ask before acting |

HIGH-risk work always requires approval at every level. Permissive relaxes only MEDIUM, and never below the guarantee that canon and structure are not changed unattended. There is no setting that waives the HIGH gate.

**Autonomy ceiling** — caps what may proceed even when a risk level would allow it. Useful when an author wants narrow scope for a while.

**Enabled engines** — restricts which engines may run. When an author wants canon frozen mid-draft, disabling `canon-manager` and `version-control` is clearer than relying on instructions not to use them.

## Rules

- Settings never override the author. A setting is a standing instruction that the author can change at any time, and a current instruction beats a stored one.
- A setting never overrides canon. `PERMANENT_CANON` outranks any configuration.
- Record why a setting changed. Approval strictness is usually changed because something nearly went wrong, and the reason is the useful part.
- Do not set a field to make a validation pass. Unresolved is a valid state.
- Settings are project-scoped. Cross-project behaviour belongs in `author-profile`.

## Coordination

Read by `novel-orchestrator` for every routing decision, by `canon-manager` for classification, by `narrative-voice` and `scene-writing` for POV and tense, and by `quality-gate` when judging whether an action was in scope. Report a setting that contradicts observed practice as a finding rather than silently reconciling it.