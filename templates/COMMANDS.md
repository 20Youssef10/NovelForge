# NovelForge Command Reference

Natural language is accepted; these are the canonical shorthands. Commands resolve through the orchestrator, which selects only the specialists the task actually needs.

## Project
`/novel create` — initialise a project
`/novel status` — inspect project health and open decisions
`/novel report` — produce an agent report
`/bible update` — update the Novel Bible
`/bible audit` — audit the Bible against domain files

## Workspace
`/workspace list` — list novels in the workspace
`/workspace use` — set the active project
`/workspace audit` — check project boundaries and registry
`/author profile` — view or amend author preferences

## Planning
`/plan story|saga|arc|chapter|scene` — plan before drafting

## Drafting
`/write chapter|scene` — draft approved scope

## Characters
`/character analyse|create|simulate|arc|voice`

## World and institutions
`/world analyse|expand`
`/faction simulate|audit`

## Mystery and information
`/mystery create|analyse|reveal|solve`
`/reader analyse|check`
`/foreshadow add|check|payoff`
`/payoff audit|show|resolve`

## Structure and causality
`/causality check`
`/consequences check`
`/pacing audit`
`/tension audit`

## Style, voice, originality
`/style analyse|drift|compare`
`/voice check`
`/generic check`
`/cliche check`
`/trope track|audit`
`/theme analyse`
`/motif track|audit`

## Power and action
`/power check|exploit|scale`
`/battle analyse`

## Consistency
`/continuity check`
`/timeline check`

## Canon and versions
`/canon impact|update|show`
`/branch create|compare|merge|rollback`
`/version snapshot|diff|compare|rollback`

## Research and language
`/research topic|audit|sources`
`/localise chapter`

## Memory and review
`/memory update|audit|show`
`/critique chapter|arc|story`

## Notes
- `/version` and `/branch` overlap deliberately: `/branch` operates on story alternatives, `/version` on snapshots and diffs.
- `/critique` is independent review and does not modify prose. Repairs are proposed, then applied on approval.
- Risk classification decides autonomy, not the command. LOW-risk work may proceed; HIGH-risk work always requires approval before execution.
