# Installed skills

This directory belongs to the **skills CLI** (`npx skills`) and to Codex CLI
bare-skill discovery, which both install here.

It is deliberately **not** a symlink to `../skills`. NovelForge's own 45 skills
live in `../skills` and are reached by the plugin manifests, the OpenCode
catalog, and the two other discovery links. Pointing this directory at the
canonical tree meant that any `npx skills add` wrote third-party skills straight
into NovelForge's source, where they were indistinguishable from real engines.

Keep foreign skills here. Keep NovelForge's own in `../skills`.
