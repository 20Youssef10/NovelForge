# NovelForge v2.1.0

A skills-first, agentic novel-writing system for long-form fiction. Supports fantasy, dark fantasy, mystery, thriller, psychological fiction, isekai, cultivation, murim, and hybrid projects.

Every skill is a plain `SKILL.md` following the [Agent Skills](https://agentskills.io/specification) open standard, so the same 48 files work across agents without modification. Per-agent manifests are included for the major plugin hosts.

## Install

**As a plugin** (Claude Code, Copilot CLI, Copilot in VS Code, Codex, ChatGPT):

```bash
# Claude Code
claude plugin marketplace add 20Youssef10/NovelForge
claude plugin install novelforge@novelforge

# Codex / ChatGPT
codex plugin marketplace add 20Youssef10/NovelForge
```

**As a skill directory** (any Agent Skills-compatible agent):

```bash
git clone https://github.com/20Youssef10/NovelForge.git ~/.claude/skills/novelforge
```

Copy rather than symlink if your agent will not follow symlinks (notably Windows without Developer Mode):

```bash
cp -R NovelForge/skills <your-agent-skills-dir>/novelforge
```

## Compatibility

| Agent | Mechanism | Manifest or path in this repo |
| --- | --- | --- |
| Claude Code | Plugin | `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json` |
| Copilot CLI / VS Code | Plugin | `.github/plugin.json` |
| Codex CLI, ChatGPT | Plugin (portable) | `plugin.json` (canonical), `.codex-plugin/plugin.json` (fallback) |
| Codex, ChatGPT desktop | Marketplace | `.agents/plugins/marketplace.json` |
| Agents with no plugin layer | Skills directory | `.agents/skills` → `skills/`, `.gemini/skills` → `skills/` |

`skills/` is the single source of truth and sits at the standard discovery path every one of these agents scans, so no manifest needs a skill list. The `.agents/skills` and `.gemini/skills` entries are relative symlinks to it rather than copies, so the skills can never drift out of sync.

## Core design
- File-based Novel Bible as the project source of truth
- Targeted context retrieval instead of loading the whole novel
- Risk-based autonomy with author approval for high-impact changes
- Plan-first, discuss, then draft workflows
- Narrative graph with stable IDs connecting every domain
- Narrative obligations tracked as an indexed ledger
- Main-canon and isolated branch support
- Multi-novel workspace isolation

## Architecture
43 specialist engines plus 5 retained compatibility aliases, routed by `novel-orchestrator`. The system remains skills-first: the Bible is canonical, the graph stores durable dependencies, memory accelerates retrieval but never overrides project files, branches stay isolated until an explicit merge, and high-impact changes sit behind approval gates.

## Engines

**Orchestration and state** — `novel-orchestrator`, `context-manager`, `quality-gate`, `canon-manager`, `workspace-manager`, `author-profile`, `memory-manager`, `version-control`

**Planning and structure** — `novel-planner`, `plot-engineering`, `pacing-engine`, `tension-engine`, `theme-engine`, `symbolism-motif`

**Craft** — `scene-writing`, `dialogue`, `character-development`, `worldbuilding`, `localisation`

**Character** — `character-simulation`, `character-arc-engine`, `narrative-voice`

**Style and originality** — `narrative-style`, `style-drift`, `generic-writing-detector`, `anti-cliche`, `trope-manager`

**Information and continuity** — `mystery-engine`, `reader-knowledge`, `foreshadowing`, `payoff-debt`, `continuity`, `timeline`, `narrative-graph`

**Causality** — `causality-engine`, `consequence-engine`

**Power, world, and action** — `power-system`, `power-exploit`, `battle-choreography`, `faction-simulation`

**Research and review** — `research`, `research-provenance`, `critique`

**Compatibility aliases** — `trope-management`, `versioning`, `memory-governance`, `workspace-isolation`, `prose-style`. These resolve to their canonical engine and share its records.

## Governance
Canon states: `PERMANENT_CANON`, `ARC_CANON`, `CHAPTER_CANON`, `SCENE_STATE`, `PROPOSAL`, `UNRESOLVED`, `RECON`.

Risk levels: `LOW` (proceeds automatically), `MEDIUM` (confirm scope), `HIGH` (author approval required *before* execution). HIGH covers canon and retcon, major character fate, ending, relationship structure, global timeline, power rules, major faction change, branch merge, cross-novel memory transfer, and large-scale style change.

There is no quiet retcon, and similarity never grants cross-novel access.

## Suggested project structure
```text
novel-project/
├── NOVEL_BIBLE.md
├── canon/            facts, retcons, unresolved
├── chapters/         chapter and scene plans
├── scenes/           scene records
├── plot/             arcs
├── characters/       profiles and relationships
├── factions/         institutions and blocs
├── power_system/     rules, costs, ranks, exploits
├── battles/          action sequences
├── timeline/         events
├── mysteries/        mysteries and reveals
├── reader/           reader knowledge states
├── knowledge/        who knows what, and when
├── foreshadowing/    setups
├── obligations/      promises awaiting payoff
├── causality/        causal chains
├── consequences/     owed effects
├── graph/            nodes and edges
├── style/            Style DNA, voices, audits
├── voice/            narration and POV
├── cliches/          cliché reviews
├── themes/           themes, motifs, tropes
├── pacing/           pacing audits
├── tension/          tension audits
├── research/         claims and sources
├── glossary/         canonical terminology
├── versions/         snapshots and branches
├── memory/           scoped agent memory
├── workspace/        project registry
└── quality-check.md
```

## Full-agent loop
DISCOVER → CONTEXTUALISE → PLAN → PROPOSE → APPROVE_IF_NEEDED → EXECUTE → AUDIT → REPAIR_SAFE → IMPACT_ANALYSE → UPDATE_STATE → QUALITY_GATE → REPORT

## Final principle
Never optimise for more prose. Optimise for meaningful narrative, and report unresolved risks rather than hiding them.

## Licence
MIT — see [LICENSE](LICENSE). Copyright (c) 2026 ShinZero.
