---
description: Create or adopt a novel project, initialising the Novel Bible and domain structure
argument-hint: "[title] [genre]"
---

Create or adopt a novel project.

1. Load the `novel-orchestrator` skill and follow its state machine.
2. If the author names an existing manuscript or a directory, route to `manuscript-import` instead of scaffolding.
3. Otherwise initialise from `templates/project/`, creating only the domains the novel needs.
4. Fill `NOVEL_BIBLE.md` with identity, premise, and canon policy. Leave unknown fields blank rather than inventing them.
5. Register the project in `workspace/PROJECT.md` so the workspace knows it exists.
6. Report what was created and what was deliberately left empty, and why.
