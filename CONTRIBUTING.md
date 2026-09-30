# Contributing to NovelForge

## Before you start

```bash
python3 scripts/validate.py                # fast, offline
python3 scripts/validate.py --schema       # also checks the live Agent Plugins schema
python3 scripts/validate.py --strict       # warnings fail too
```

CI runs `--schema --strict` on every push and pull request. Nothing merges with a failure.

## Adding a skill

1. Create `skills/<kebab-case-name>/SKILL.md`. The directory name **must** equal the frontmatter `name`, because OpenCode derives the skill ID from the path and other agents match on the name.
2. Write real instructions. A skill that only restates its own description is worse than no skill, and the validator will reject it — see *Substance* below.
3. Add the skill to the routing table in `skills/novel-orchestrator/SKILL.md`. The validator fails if you do not, because an unrouted engine is never selected.
4. If the skill needs a record on disk, add a template under `templates/project/` and reference it from the skill body. The validator fails on unreferenced domain templates.
5. If the skill has depth worth loading on demand, put it in `skills/<name>/references/` and point to it from the body. The validator checks the file exists and is not empty.
6. Run the validator.

### Writing a good skill

- **Lead with what the agent must do**, not with background. The body is loaded into context on activation, so every sentence costs.
- **Give the failure modes.** What this detects, what it refuses to do, and what it must never be used to justify.
- **State the boundaries with neighbouring skills** in a Coordination section, so two skills do not quietly overlap.
- **Name the records.** If the skill maintains state, say which file and which field.
- **Do not restate the description.** The description is what routes the skill; the body is what does the work.
- **Use en-GB spelling.** `analyse`, `behaviour`, `colour`, `focalisation`, `judgement`, `FULFILLED`. The validator scans for en-US forms and fails the build.

### Substance

Two regressions in this project's history were perfectly well-formed files that carried no instructions: in v1.5 twelve skills were replaced with one-line pointers, and in v2.0.1 forty-seven were replaced with a restatement of their own description. Both passed every format check and shipped through multiple releases.

The validator now enforces two floors, measured from the current tree where legitimate bodies run 632–5,620 bytes with 0.797–1.0 new vocabulary:

- body at least 400 bytes
- at least 35% of the body's vocabulary absent from its own description

These catch gutting without flagging a short-but-complete skill. A new skill that trips them is almost certainly a stub.

## Changing an existing skill

Do not silently reduce a skill's depth. If a skill is being merged into another, delete it in the same commit that updates the references to it — a half-finished merge leaves a dangling route.

## Changing the version

The version appears in four manifests and must agree:

- `plugin.json`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `.github/plugin.json`

Bump all four, or the validator fails. Additive changes take a minor bump; a removal or a behaviour change takes a major bump.

## Adding a template

Templates are records a skill maintains, not documentation. A good template:

- has a title and a short purpose line
- has empty fields for the skill to fill, not example values that look real
- has audit tables where a failure mode is expected
- is referenced from exactly one owning skill

## Regenerating the OpenCode catalog

```bash
python3 scripts/build_catalog.py          # writes catalog/
python3 scripts/build_catalog.py --check  # fails if catalog/ is stale
```

Run `--check` in CI. The catalog is generated, so never hand-edit it.

## Style

- en-GB spelling throughout
- Markdown tables for structured choices, prose for reasoning
- No emoji in skill content; they age badly and add noise to context
- Keep `SKILL.md` under 500 lines. Mine are under 90.
