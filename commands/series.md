---
description: Manage series-level canon shared across novels
argument-hint: "<list|check|book> [name]"
---

Manage series canon.

1. Load `series-manager`, and `workspace-manager` for boundaries.
2. Resolve WORKSPACE, SERIES, NOVEL, BRANCH before any retrieval.
3. For `list`, report each book, its status, and what it inherits.
4. For `check`, test the book against the series bible: character status, ages, injuries, knowledge, and terminology. Report conflicts; do not choose a winner.
5. For `book`, record what a new volume inherits and what it changes locally.
6. Never promote novel-local canon to series canon without explicit approval and a migration note.
