# AGENTS.md

Instructions for agents working **on this repository**. For using NovelForge to
write a novel, load the `novel-orchestrator` skill instead.

## What this repository is

A skills-first agent plugin. 45 skills, 57 templates, 16 slash commands, and a
session hook. Installable as a plugin for Claude Code, Copilot, Codex, ChatGPT,
OpenCode, and Gemini CLI, or through the skills.sh registry for 20-plus agents.

## Run the validator before you claim anything works

```bash
python3 scripts/validate.py --schema --strict
```

It is fast and it is the project's contract. Do not report success on a change
without running it. It enforces, among other things: skill spec compliance,
a substance floor on every skill, routing coverage, reference integrity
(including that `references/` files actually exist), agreement across the four
manifests, licence/author agreement, and en-GB spelling.

## Things that have gone wrong here, so you do not repeat them

- **A gutted skill passed every format check.** v1.5 replaced twelve skills
  with one-line pointers; v2.0.1 replaced forty-seven with restatements of their
  own descriptions. Both were valid files. The substance floors exist because
  format validity is not usefulness.
- **Skills were deleted without updating anything.** v2.0.0 removed twelve
  skills and six templates and shipped as a "final release". The engine count is
  now guarded by the routing check.
- **Stale version labels survived inside content.** Templates headed "v1.5"
  shipped inside a 2.0.1 package. There is a check for this now.
- **Symlinked skill discovery was nearly lost.** `.opencode/skills` and
  `.gemini/skills` are relative symlinks to `skills/`. A plain `mv *` drops
  dotfiles; use `dotglob`. They are stored in git as mode `120000`, and a
  Windows checkout without symlink support will materialise them as plain text
  files.
- **A symlink in the install target corrupted the source tree.** `.agents/skills`
  used to be a symlink to `skills/`. It is the install target for both the
  skills CLI and Codex CLI, so `npx skills add` wrote third-party skills into
  NovelForge's own `skills/` directory, where the routing check and catalog
  generator then treated them as engines. It is now a real directory and the
  validator asserts that.

## Layout

```
skills/<name>/SKILL.md            the skill; name must equal the directory
skills/<name>/references/         depth, loaded on demand
templates/                        records skills maintain
templates/project/                per-novel project scaffolding
commands/*.md                     Claude Code slash commands
.agents/skills/                  install target for the skills CLI; NOT a symlink
hooks/hooks.json                  SessionStart, shared by Codex and Claude Code
scripts/validate.py               the contract
scripts/build_catalog.py          generates the OpenCode HTTP catalog
```

## Conventions

- en-GB spelling. `analyse`, `behaviour`, `colour`, `focalisation`, `FULFILLED`.
- Markdown tables for structured choices, prose for reasoning.
- Every finding cites a location. An unevidenced finding is an opinion.
- Record the reason, not just the change.
- Four manifests must agree on `name`, `version`, and `license`.

## Adding things

Adding a skill means: the `SKILL.md`, a row in the orchestrator routing table,
and any template it maintains. The validator enforces the first two. See
`CONTRIBUTING.md` for the substance floors and the reasoning behind them.
