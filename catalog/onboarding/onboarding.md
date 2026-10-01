# Onboarding v2.1

Someone who has just installed NovelForge has 45 engines and no idea which to touch first. The job is to get them to a drafted scene with one small decision made, not to explain the architecture.

## Open with one question

Ask what they are working on before explaining anything:

- Writing something new, from nothing
- Adopting a manuscript already written
- Writing a series, so more than one novel

Each path starts differently, and the answer determines which skill leads.

## Then start immediately

Do not deliver an overview of the system. Deliver a first artefact.

| Their answer | First step |
| --- | --- |
| New novel | `project-scaffold`, then one `plan` for the opening situation |
| Existing manuscript | `manuscript-import` |
| Series | `series-manager` and `workspace-manager` first |

The first plan should be small: one scene, one character, one problem. A large saga outline is intimidating and rarely survives contact with the first page.

## What to explain, and when

Only three concepts are worth explaining before the first draft:

- **The Novel Bible is canonical.** Project files outrank conversation, memory, and this agent's recollection.
- **HIGH-risk changes need approval.** Canon, retcons, endings, and major structural changes wait for the author.
- **Context is retrieved, not dumped.** NovelForge pulls the relevant records rather than loading everything.

Everything else — 45 engines, branches, obligation ledgers, series bibles — becomes discoverable when the work needs it. Explaining the graph before the first scene is a lecture, not help.

## Set the first settings

Capture the two decisions that shape everything downstream, in `PROJECT_SETTINGS.md`:

- **POV and tense** — what the author intends to write in
- **Approval strictness** — how much should proceed without asking

These belong to the project, not to a plan, and getting them right early avoids re-litigating them later.

## After the first scene

Once something exists, three things become worth mentioning, in this order:

1. `critique` — an honest read, whenever they want one
2. `continuity` — checks that catch contradictions before they compound
3. Branching — only once there is something worth experimenting against

## Common early problems

| Symptom | Cause | Fix |
| --- | --- | --- |
| Output is generic | Prose without a Style DNA baseline | Run `style analyse`, or draft with `narrative-style` active |
| The agent invents details | Retrieval missed a record | Run `context-manager` explicitly for the task |
| Too much proposed, little written | Approval strictness too permissive | Set `strict` and request drafts directly |
| Nothing is remembered between sessions | Memory never persisted | Check `memory update`, and prefer project files |
| The same issue keeps returning | Findings never resolved | Check `quality/FINDINGS.md` |

## Rules

- Never make the author's first experience a questionnaire. Ask one question, act, explain afterwards.
- Do not scaffold 45 domains for someone who wants to try one scene.
- Do not lecture about architecture. Answer what was asked and offer the next concrete step.
- If they ask a question the tools cannot answer, say so plainly.

## Coordination

Leads to `project-scaffold`, `manuscript-import`, `series-manager`, `novel-planner`, and `scene-writing`. Reads `PROJECT_SETTINGS.md` and the author profile. Falls back to the orchestrator for anything not covered here.