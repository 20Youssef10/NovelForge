---
description: Create or adopt a novel project, initialising the Novel Bible and domain structure
argument-hint: "[title] [genre]"
---

Create or adopt a novel project.

1. Load `project-scaffold` and `novel-orchestrator`, and follow the state machine.
2. If the author names an existing manuscript or a directory, route to `manuscript-import` instead of scaffolding.
3. Otherwise scaffold from `templates/project/`, creating only the domains the novel
   actually needs, and record configuration in `PROJECT_SETTINGS.md`.
4. Fill `NOVEL_BIBLE.md` with identity, premise, and canon policy. Record POV, tense,
   and approval strictness in `PROJECT_SETTINGS.md`. Leave any undecided field
   `UNRESOLVED` rather than inventing it.
5. Register the project in `workspace/PROJECT.md` so the workspace knows it exists.
6. Report what was created and what was deliberately left empty, and why.
