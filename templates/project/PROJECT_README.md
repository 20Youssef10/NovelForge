# Novel Project

This directory is NovelForge's working project root. Keep it beside your manuscript.

## Start here
1. Fill in `NOVEL_BIBLE.md` — identity, premise, and the domain index.
2. Populate only the domains this novel needs. A small project with three well-kept files beats a large one with fifty stale ones.
3. Set `workspace/PROJECT.md` so the workspace knows this project exists.

## Conventions
- **Project files are canonical.** Memory accelerates retrieval but never replaces them.
- **Stable IDs** connect the graph, obligations, canon impact, timeline, branches, research, and reports. Reuse an ID only if you mean the same thing.
- **Separate canon from proposal.** A proposal in `canon/facts.md` is canon; a proposal anywhere else is not.
- **Classify uncertainty.** Use `UNRESOLVED` rather than guessing — the system will otherwise invent an answer and later treat it as intentional.
- **Record what changes.** Retcons, transformations, and abandoned setups all need a recorded reason.

## Approval discipline
`LOW`-risk work may proceed automatically. `MEDIUM` needs confirmed scope. `HIGH` requires author approval **before** execution — canon and retcon, major character fate, ending, relationship structure, global timeline, power rules, major faction change, branch merge, cross-novel memory transfer, large-scale style change.

## Suggested structure
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

Create directories as needed. An empty template directory is harmless; a missing one that a skill expects is not.
