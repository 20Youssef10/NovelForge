# Privacy

NovelForge is a set of instruction files. It collects nothing.

## What the plugin contains

Text only: `SKILL.md` files under `skills/`, templates under `templates/`,
commands under `commands/`, images under `assets/`, and the scripts under
`scripts/`. There is no runtime, no network call, and no telemetry in the plugin
itself.

## What runs when you install it

**A session hook.** `hooks/hooks.json` registers a `SessionStart` hook that runs
`hooks/session_start.py` when a supported agent opens a session.

It does this and nothing else:

1. Walks upward from the working directory looking for a `NOVEL_BIBLE.md`.
2. If it finds one, reads the title, status, canon branch, open Critical findings
   count, and open obligation count from that project.
3. Prints them as session context.

It does not read, write, or transmit any file. If it finds no project it prints
nothing and exits successfully. It never fails a session.

The script is in the repository and is readable in full: about 130 lines of
dependency-free Python.

## What your novel project contains

Whatever you put in it. NovelForge's conventions keep canon in project files rather
than in agent memory, so a novel you write stays on your disk, in your format, under
your control. Nothing is uploaded.

## Telemetry

NovelForge itself sends nothing. If you install skills through the [skills.sh](https://skills.sh)
CLI or another registry, that tool has its own telemetry, which is documented at
<https://skills.sh/docs/cli> and can be disabled with `DISABLE_TELEMETRY=1`. That
telemetry belongs to the installer, not to NovelForge.

## Third-party calls

None. The plugin makes no HTTP requests. The `research` and `research-provenance`
skills describe how an agent should record sources you look up yourself; the plugin
performs no lookups.

## Reporting a problem

Open an issue at <https://github.com/20Youssef10/NovelForge/issues>.