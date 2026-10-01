# Changelog

All notable changes to NovelForge are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.5.0] — 2026-10-01

### Added

- **`context-budget`** — real token-budget discipline. Per-scope ceilings (scene
  8,000, chapter 20,000, arc 60,000, novel 120,000), a dependency-free estimation
  method, an eleven-rank relevance ordering, and a trim-by-deferral sequence that
  names what is never sacrificed. Rationale for deferral is recorded, because an
  unexplained omission is indistinguishable from a mistake.
- **`project-scaffold`** — the skill `/novel create` lacked. Eight phases from
  author questions to a minimal default set, with a rule that a domain is created
  only when a template exists to populate it. Scaffolding is MEDIUM risk and may
  proceed without approval; filling canon afterwards is not scaffolding.
- **`project-settings`** — POV, tense, approval strictness, autonomy ceiling, and
  engine selection as project configuration rather than plan prose. Strictness
  governs MEDIUM risk only; HIGH-risk work always asks, and no setting waives that.
- **`cross-engine-audit`** — one call that selects the right engine subset per scope,
  sequences them so later stages consume earlier findings, and consolidates output
  into stable finding IDs. Records skipped engines and why, and treats engine
  disagreement as an authorial question rather than reconciling it automatically.
- **`onboarding`** — first-time orientation. Opens with one question, delivers a
  first artefact rather than an architecture tour, explains only three concepts
  before the first draft, and routes to scaffold, import, or series setup.
- **`examples/salt-and-ember/`** — a complete worked project with 16 files, showing
  filled canon with dependencies, a power system with enforceable costs, a
  deliberately unsolved mystery, an accumulating findings ledger, a measured and
  trimmed context packet, and a chapter audit with an unresolved engine
  disagreement. Deliberately incomplete, with the omissions recorded.
- **`PROJECT_SETTINGS.md`** and **`audit/AUDIT_RUN.md`** templates.
- **3 new slash commands** — `audit`, `setup`, `budget`.
- **`extensions.com.openai.onboardingSkill`** wired to the onboarding skill in both
  OpenAI manifests.

### Changed

- `novel-orchestrator` gains Configuration and a context-budget routing rule, and
  reads approval strictness from settings. A duplicated Approval policy section was
  merged into one.
- `novel-create` routes through `project-scaffold` and records configuration.
- Validator checks the worked example: required files present, no stray `skills/`
  directory, all three strictness levels documented, and open questions genuinely
  marked `UNRESOLVED`.

## [2.4.0] — 2026-09-30

### Added

- **skills.sh support.** NovelForge installs through the open agent skills
  registry, which covers 20-plus agents in one command. Verified against
  `skills` CLI v1.7.0: all 45 skills are discovered, and a scoped install lands
  correctly with a working `skills-lock.json`.
- **skills.sh badge** and installation section in the README, including
  telemetry opt-out and the distinction between installing the plugin and
  installing individual skills.
- `gh skill install` documented in the compatibility table.

### Fixed

- **`.agents/skills` is no longer a symlink into the canonical `skills/` tree.**
  That path is the install target for both the skills CLI and Codex CLI, so
  `npx skills add <anything>` wrote third-party skills directly into
  NovelForge's source, where they were indistinguishable from real engines and
  were picked up by the orchestrator routing table and the OpenCode catalog.
  Verified by installing an unrelated skill into a clone: it added a
  46th engine to `skills/`. The directory is now real, git-ignored for
  installed skills, and documented in place.
- Validator now asserts `.agents/skills` is a real directory, so this cannot be
  reintroduced, and reports any third-party skills present there.

### Changed

- Validator layout section distinguishes the two symlinked discovery paths
  (`.opencode/skills`, `.gemini/skills`) from the skills CLI install target
  (`.agents/skills`).

## [2.3.1] — 2026-09-30

### Fixed

- **Invalid plugin category.** `category` was set to `Writing`, which is not a
  title in the OpenAI dashboard's category list, so the plugin would have been
  skipped in the marketplace picker. Now `Creativity`, in all three places the
  value appears: `plugin.json`, `.codex-plugin/plugin.json`, and
  `.agents/plugins/marketplace.json`.
- **Over-length `defaultPrompt` entries.** All three starter prompts exceeded
  the documented 128-character submission limit in both manifests, at 161, 140,
  and 277 characters. Rewritten to 105, 102, and 93.

### Added

- Validator now enforces the documented OpenAI listing limits: `displayName`
  and `shortDescription` at most 30 characters, `longDescription` at most 4000,
  `developerName` at most 80, at most three `defaultPrompt` entries of at most
  128 characters each, at most 20 `capabilities` of at most 120 characters,
  description at most 4000, a recognised `category`, and required
  `policy.installation`, `policy.authentication`, and `category` on every
  marketplace entry.

## [2.3.0] — 2026-09-30

### Added

- **`manuscript-import`** — phased intake for an existing draft: inventory,
  structure, entity and relationship extraction, timeline reconstruction,
  knowledge states, Style DNA inference, and canon classification. Approval is
  required between phases, every extraction carries a source citation, and
  nothing is classified as permanent canon until the author confirms it.
- **`series-manager`** — canon deliberately shared across a series, with
  `SERIES_CANON` and `NOVEL_CANON` kept strictly separate, explicit inheritance
  per volume, and recorded divergence points. This is the sanctioned exception
  to `workspace-manager`'s default isolation.
- **16 slash commands** in `commands/` for Claude Code: `novel-create`,
  `novel-import`, `novel-status`, `novel-report`, `plan`, `write`, `critique`,
  `gate`, `continuity`, `canon-impact`, `branch`, `payoff`, `mystery`, `power`,
  `style`, `series`.
- **`SessionStart` hook** shared by Codex and Claude Code. Detects a novel
  project, injects root, title, status, branch, open Critical findings, and open
  obligation count, and suppresses unfilled template placeholders rather than
  reporting them as values. Silent outside a project; never fails a session.
- **Findings ledger** (`project/quality/FINDINGS.md`) making critique stateful:
  stable finding IDs, resolved only once verified, author-accepted risks with
  reasons, and a regression watch list.
- **Progressive disclosure** — five engines gained a `references/` file holding
  depth that is not needed until the skill is working on a problem:
  `canon-manager/CHANGE_PROCEDURE.md`, `critique/CHECK_CATALOGUE.md`,
  `generic-writing-detector/PATTERNS.md`, `mystery-engine/FAIRNESS.md`, and
  `power-system/SCALING_AND_EXPLOITS.md`.
- **5 new templates** — import plan and extraction log, series bible and book
  entry, findings ledger.
- **OpenCode HTTP catalog** (`catalog/`) generated by `scripts/build_catalog.py`
  and kept current by a second workflow, allowing install without cloning.
- **`CONTRIBUTING.md`** and **`AGENTS.md`**.

### Changed

- Validator now verifies that `references/`, `scripts/`, and `assets/` paths
  named inside a skill resolve to real, non-empty files.
- Validator now checks catalog freshness against the canonical skills tree.
- CI additionally smoke-tests the session hook for silence outside a project and
  tolerance of malformed stdin.

### Removed

- **The five compatibility aliases** — `trope-management`, `versioning`,
  `memory-governance`, `workspace-isolation`, `prose-style`. They existed to
  protect installs that do not exist: the plugin had no users when they were
  added, and four of the five were referenced by nothing at all. Removing them
  takes the surface from 48 skills to 45 and eliminates a class of ambiguity
  where two skills claimed one job. Use `trope-manager`, `version-control`,
  `memory-manager`, `workspace-manager`, and `narrative-style`.

## [2.2.0] — 2026-09-30

### Added

- **`scripts/validate.py`** — repository validator covering skill spec
  compliance, skill substance floors, cross-reference integrity, orchestrator
  routing coverage, alias target validity, manifest version agreement, live
  Agent Plugins schema conformance, licence/author agreement, en-GB spelling,
  stale version labels, and discovery-symlink integrity.
- **`.github/workflows/validate.yml`** — runs the validator on every push and
  pull request with `--schema --strict`, plus a skills-tree integrity check
  that tolerates symlinks not materialising on Windows checkouts.
- **Substance checks for skills.** Format-valid-but-empty skills are now a
  build failure. Both historical regressions — the v1.5 one-line pointers and
  the v2.0.1 description restatements — were well-formed files carrying no
  instructions, so they passed every spec rule.

## [2.1.0] — 2026-09-30

### Added

- **Skill expansion.** All 43 working engines rewritten from 90–120 byte
  restatements into substantive procedure, failure modes, and guardrails.
  Average body 2,911 bytes, up from roughly 120.
- **Depth recovery.** Craft procedures lost in v1.0→v1.5 restored into the
  writing engines; v1.5 engine depth restored into the analysis engines;
  v2.0.0 phase-2 content extended.
- **Orchestrator state machine** and a routing table covering all 42 engines.
- **12 new templates** for engines that previously had no on-disk artefact:
  scenes, relationships, factions, battles, pacing, tension, causal chains,
  consequences, cliché reviews, voice profiles, glossary, reader state.
- **18 templates expanded**, including three still headed "v1.5" inside a
  v2.0.1 package and twelve restored as verbatim copies of older versions.
- **5 compatibility aliases** rewritten as real routing documents, replacing
  conflicting duplicate skill pairs.

## [2.0.1] — 2026-09-30

### Changed

- Restored the 12 skills deleted in v2.0.0 and the 25 missing templates, but at
  placeholder depth. Documented in 2.1.0.

## [2.0.0] — 2026-09-30

### Added

- Phase-2 engines: style drift, generic-writing detection, anti-cliché, trope
  management, theme and symbolism, research provenance, author profile, memory
  governance, workspace isolation, quality gate.

### Removed

- Twelve craft skills and six templates. This removed the writing half of the
  system and left only analysis engines; the omission was not documented at the
  time and was reverted in 2.0.1.

## [1.5.0] — 2026-09-30

### Added

- Twelve analysis engines: narrative graph, causality, consequence, pacing,
  tension, payoff debt, reader knowledge, character simulation and arcs, power
  exploit, battle choreography, faction simulation.

### Changed

- Twelve Phase-0 skills were replaced with one-line pointers to the v1.0
  specialists rather than extended. This was undetected until 2.1.0.

## [1.0.0] — 2026-09-30

### Added

- Initial system: 19 craft skills, 22 templates, Novel Bible source of truth,
  targeted context retrieval, risk-based autonomy, branching.
