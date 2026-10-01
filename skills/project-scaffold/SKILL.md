---
name: project-scaffold
description: Create or extend a NovelForge project by initialising the Novel Bible, copying only the domain templates the novel needs, and recording project configuration such as POV, tense, and approval strictness. Use when starting a new novel, adding a domain to an existing project, or running a novel create command.
---
# Project Scaffold v2.5

Create the structure a novel needs and nothing more. A scaffold with forty empty files teaches the author nothing and teaches the agent to ignore most of them.

## Principle

Scaffold from what the author has told you, not from what a template offers. If the author has not decided the tense, do not record one — record the field as `UNRESOLVED` and let the decision come from the writing.

## Phases

1. **Ask before building.** Get title, genre or subgenre, and whether this is greenfield or an existing manuscript. A manuscript goes to `manuscript-import`, not here.
2. **Copy the core.** `NOVEL_BIBLE.md`, `PROJECT_SETTINGS.md`, and the canon trio — `canon/facts.md`, `canon/retcons.md`, `canon/unresolved.md` — are always present. Everything else is conditional.
3. **Copy the conditional domains** the author's answers actually justify. Planning needs `chapters/`. A power system needs `power_system/`. Factions need `factions/`. A series needs a link in the workspace registry.
4. **Copy templates verbatim.** Never paraphrase a template during scaffolding; the templates are the contract and the validator checks their reachability.
5. **Record configuration** in `PROJECT_SETTINGS.md` where the author has decided it.
6. **Report** what was created, what was deliberately skipped, and what remains `UNRESOLVED`.

## Minimal default set

A novel with no stated genre needs only:

```
NOVEL_BIBLE.md
PROJECT_SETTINGS.md
canon/facts.md
canon/retcons.md
canon/unresolved.md
chapters/CHAPTER_PLAN.md
chapters/SCENE_PLAN.md
quality/FINDINGS.md
```

Everything beyond that is added on demand as the novel commits to it.

## Extending an existing project

When adding a domain later, copy the template, add the directory to the Novel Bible index, and record why it is now needed. Do not backfill domains the novel has not earned.

## Rules

- Never invent genre, POV, tense, or theme. Leave the field `UNRESOLVED` with a note that the author has not decided.
- Never create a domain directory without a template to populate it. An empty directory is noise.
- Scaffolding is MEDIUM risk: it creates files but establishes no canon, so it may proceed without approval. Filling in canon afterwards is not scaffolding and is gated normally.
- Do not scaffold inside another novel's directory; that is `series-manager` territory.
- If the project already exists, extend it rather than overwriting. Never clobber authored content.

## Output

Record the scaffold in the agent report: files created, domains skipped and why, and the `UNRESOLVED` fields awaiting the author. Register the project in `workspace/PROJECT.md` so the workspace knows it exists.

## Coordination

Use `manuscript-import` instead when prose exists, `workspace-manager` for registration and boundaries, `series-manager` for a series volume, and `context-manager` once there is enough project state to make retrieval meaningful.