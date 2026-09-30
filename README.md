# NovelForge v2.4.0

[![skills.sh](https://skills.sh/b/20Youssef10/NovelForge)](https://skills.sh/20Youssef10/NovelForge)

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
| OpenCode | Skills directory | `.opencode/skills` → `skills/` |
| Copilot CLI / VS Code | Plugin | `.github/plugin.json` |
| Codex CLI, ChatGPT | Plugin (portable) | `plugin.json` (canonical), `.codex-plugin/plugin.json` (fallback) |
| Codex CLI, ChatGPT desktop | Marketplace | `.agents/plugins/marketplace.json` |
| Gemini CLI | Skills directory | `.gemini/skills` → `skills/` |
| OpenCode | Skills directory | `.opencode/skills` → `skills/` |
| Any of 20+ agents | skills.sh CLI | `npx skills add 20Youssef10/NovelForge` |
| GitHub CLI | `gh skill install` | `gh skill install 20Youssef10/NovelForge novel-orchestrator --agent claude-code` |

`skills/` is the single source of truth and sits at the standard discovery path every plugin host scans, so no manifest needs a skill list. The `.opencode/skills` and `.gemini/skills` entries are relative symlinks to it rather than copies, so those skills can never drift out of sync.

`.agents/skills/` is the one exception: it is a real directory, because the skills CLI and Codex CLI both install third-party skills there.

### OpenCode

Works out of the box — `.opencode/skills/` is OpenCode's native project discovery path and `.agents/skills/` is its compatibility path, so the same symlink serves both. Nothing to configure when the repo is your working directory.

To install globally instead, drop the skills into your config directory:

```bash
git clone https://github.com/20Youssef10/NovelForge.git ~/.config/opencode/skills/novelforge
```

OpenCode derives each skill ID from its path, so `skills/novel-orchestrator/SKILL.md` is loaded as `novel-orchestrator`. The frontmatter `name` is only a display label in V2, so the directory names are what you pass to the `skill` tool.

OpenCode loads skills through the `skill` tool rather than injecting them into every prompt, so skills are advertised by description and pulled in only when relevant. Its `license` and `compatibility` frontmatter fields are accepted for portability but not interpreted.

**Install from the HTTP catalog**, without cloning:

```jsonc
// opencode.jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "skills": [
    "https://raw.githubusercontent.com/20Youssef10/NovelForge/main/catalog"
  ]
}
```

The catalog in `catalog/` is generated from `skills/` by `scripts/build_catalog.py` and kept current by CI. It ships each skill as `<name>.md` rather than `SKILL.md` because a root-level `SKILL.md` in a catalog collapses every skill onto the single ID `SKILL` in V2.

### skills.sh

NovelForge is installable through [skills.sh](https://skills.sh), the open agent skills registry. The CLI detects installed agents and copies each skill into the right directory, covering 20-plus hosts at once.

```bash
# One skill
npx skills add 20Youssef10/NovelForge --skill novel-orchestrator

# The full system, into every detected agent
npx skills add 20Youssef10/NovelForge --all

# What is available, without installing
npx skills add 20Youssef10/NovelForge --list
```

Add `--global` for user scope instead of project scope, and set `DISABLE_TELEMETRY=1` to opt out of the anonymous install counts that feed the leaderboard.

Installed skills land in `.agents/skills/` and are recorded in `skills-lock.json`, so `npx skills check` and `npx skills update` work normally. That directory is a real directory, not a link to `skills/`: the CLI would otherwise write third-party skills straight into NovelForge's source, where they are indistinguishable from real engines.

If you use the plugin rather than individual skills, install it as a plugin instead — the plugin carries the orchestrator, the slash commands, and the session hook, which the skills CLI does not.

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

**Intake** — `manuscript-import`

45 skills in total: 44 engines plus the orchestrator. Five larger engines also ship a `references/` file holding the depth that is not needed until the skill is actually working on a problem.

## Commands

Claude Code users get 16 slash commands from `commands/`: `novel-create`, `novel-import`, `novel-status`, `novel-report`, `plan`, `write`, `critique`, `gate`, `continuity`, `canon-impact`, `branch`, `payoff`, `mystery`, `power`, `style`, `series`.

Other agents get the same workflows by asking in natural language; `templates/COMMANDS.md` is the full command reference.

## Session context

`hooks/hooks.json` registers a `SessionStart` hook shared by Codex and Claude Code. When a session opens inside a novel project, it injects the project root, title, status, branch, open Critical findings, and open obligation count — so cross-session continuity works without the agent being told where it is. It stays silent outside a project and never fails a session.

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

## Development

The repository validates itself. Run the checks before opening a pull request:

```bash
python3 scripts/validate.py                # offline checks
python3 scripts/validate.py --schema       # also fetch the live Agent Plugins schema
python3 scripts/validate.py --strict       # treat warnings as failures
```

CI runs the same validator on every push and pull request.

### What the validator enforces

| Area | Checks |
| --- | --- |
| Layout | Discovery symlinks present and resolving; `.agents/skills` is a real directory, not a link into `skills/`; `LICENSE` and `README` exist |
| Agent Skills spec | `name` pattern, length, matches directory; description present and within limits; line count; unknown frontmatter keys; body opens with a heading |
| **Skill substance** | Body above a byte floor, and adds vocabulary beyond its own description |
| Routing | Every engine appears in `novel-orchestrator` |
| Cross-references | No dangling skill or template references; every `references/` file exists and is non-empty; every domain template reachable |
| Manifests | Valid JSON; `name`, `version`, `license` identical across all four; required keys present |
| Schema | `plugin.json` has no fields the Agent Plugins schema forbids |
| OpenAI listing | `displayName`/`shortDescription` ≤ 30, `longDescription` ≤ 4000, `developerName` ≤ 80, ≤ 3 `defaultPrompt` of ≤ 128 chars, `capabilities` ≤ 20 of ≤ 120 chars, recognised `category`, required marketplace `policy` and `category` |
| Licence | MIT, copyright holder matches the manifest author |
| Language | No en-US spellings in skills or templates |
| Version labels | No pre-2.0 version labels left in content |
| OpenCode catalog | `catalog/` matches the canonical `skills/` tree |

The substance check exists because format validity is not usefulness. Two
regressions in this project's history were perfectly well-formed files that
carried no instructions at all, and both shipped through multiple releases
before anyone noticed. The floors are set from the measured distribution of
legitimate skills, so they catch gutting without flagging a short-but-complete
skill. See `CHANGELOG.md` for the full history.
