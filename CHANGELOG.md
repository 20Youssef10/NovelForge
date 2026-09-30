# Changelog

All notable changes to NovelForge are recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
