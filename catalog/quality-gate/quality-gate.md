# Quality Gate v2.1

Run the checks that apply to the work in front of you. The gate is a verification instrument, not a critic with opinions: it records evidence, not verdicts on taste.

## Principles

- Run applicable checks. A dialogue scene does not require a power-scaling audit; a battle does.
- A gate does not invent fixes. It records what is wrong, what can be safely repaired, and what needs the author.
- Every finding needs concrete evidence — a location, a quote, an ID, a contradiction. A finding without evidence is an opinion.
- Report unresolved risks plainly. Suppressing a known problem to reach a green gate is the worst outcome this gate can produce.

## Dimensions

1. **Structure and narrative value** — does the unit change something? Any beat that could be deleted without loss is filler.
2. **Causality** — does each major turn arise from conditions, trigger, choice, and mechanism rather than convenience?
3. **Consequences** — do downstream effects of meaningful actions appear where they should?
4. **Character agency and arc** — are decisions earned from goals, beliefs, and knowledge? Is transformation earned through choices rather than exposition?
5. **Dialogue, voice, and POV** — distinct voices, respected knowledge limits, no accidental head-hopping, subtext where it earns its place.
6. **Style DNA and style drift** — consistent with the project's established voice, with deviations that are intentional.
7. **Continuity, timeline, and canon** — no contradictions, coherent chronology, changes classified and approved.
8. **Narrative graph integrity** — stable IDs intact, no orphaned or contradictory edges after structural edits.
9. **Mystery and reader knowledge** — fair clues, no accidental spoilers, reveals earned.
10. **Foreshadowing and payoff debt** — setups live, payoffs arriving in plausible windows, no silently abandoned promises.
11. **Pacing and tension** — tempo serves function; stakes are real rather than announced.
12. **Originality** — generic writing, cliché, and trope-intent checks, distinguishing deliberate convention from unexamined habit.
13. **Theme and motif** — themes emerge through choices and consequences rather than being asserted.
14. **Power, battle, and faction logic** — rules respected, reversals caused, factions respond plausibly with partial information.
15. **Research provenance** — externally derived claims verified or marked uncertain.
16. **Version and branch integrity** — work attributable, reversible, and on the intended branch.

## Record

Single units use `project/quality-check.md`; project-wide audits use `templates/QUALITY_GATE.md`. Record the verdict with findings, safe repairs, and approval items listed separately.

Carry every finding into the project's `quality/FINDINGS.md` ledger so a gate run adds to the accumulated state rather than re-reporting the same problem indefinitely. Before running, check the ledger for previously accepted risks and regression watch entries so neither is silently re-raised.

## Verdict

- **PASS** — applicable checks pass, no outstanding HIGH-risk items.
- **PASS_WITH_ACCEPTED_ISSUES** — remaining findings are recorded, understood, and explicitly accepted by the author.
- **BLOCKED** — a HIGH-risk finding or unresolved approval gate prevents completion.

Record each verdict in the `QUALITY_GATE.md` instance for the unit, with findings, safe automatic repairs, and high-impact approval items listed separately.
