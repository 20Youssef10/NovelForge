# Context Budget v2.5

Retrieval discipline is an arithmetic problem, not a judgement problem. Agents over-retrieve because more context feels safer; it is not, and the cost is dilution.

## Budget

Default ceilings for a single Context Packet:

| Scope | Budget | Rationale |
| --- | --- | --- |
| Single scene | 8,000 tokens | One POV, one location, one turn |
| Chapter | 20,000 tokens | Several scenes plus their consequences |
| Arc | 60,000 tokens | Multiple chapters and their debts |
| Full novel | 120,000 tokens | Whole-project audit |

Adjust downward when the model has a small context window. Overrun is a finding, not a shrug.

## Measure before loading

Estimate tokens before committing to a packet. A rough method that needs no dependency:

```
tokens ≈ characters / 4        for prose and markdown
tokens ≈ lines × 12            for tabular records
```

Treat these as a floor, not an estimate, since JSON, tables, and YAML frontmatter inflate. When a figure lands within 20% of the budget, measure more carefully rather than proceeding.

Rank every candidate section before loading anything:

| Rank | Content | Load when |
| --- | --- | --- |
| 1 | Active scene, POV character, immediate constraints | Always |
| 2 | Canon facts the scene touches | Always |
| 3 | Graph neighbours within one hop | Always |
| 4 | Open obligations due in this scope | Always |
| 5 | Timeline entries bounding the scene | Usually |
| 6 | Character relationships in play | Usually |
| 7 | Power rules in force | If the scene uses power |
| 8 | Style DNA | If drafting or revising prose |
| 9 | Reader knowledge at this position | If information control matters |
| 10 | Themes, motifs, tropes | If the scene is thematic |
| 11 | Other branches, other novels | Never without explicit request |

## Trim by deferral

When over budget, cut in this order, because the last items are the most expensive and least decision-relevant:

1. Drop ranks 10 to 6 first. Thematic and relationship context rarely changes a decision.
2. Replace long prose with the specific facts and IDs needed. Cite the record rather than quoting it.
3. Narrow graph traversal from two hops to one.
4. Summarise history and read the full record only if the summary proves insufficient.
5. Split the task. Two bounded packets beat one oversized one.

Never trim rank 1 to 5. A packet missing the active scene or the canon it touches is worse than no packet.

## Record the trim

State in the packet what was deferred and why. An unexplained omission looks like an oversight, and the author cannot tell the difference between a deliberate cut and a mistake.

## Rules

- Do not load a domain because it exists. `factions/FACTION.md` is irrelevant to a scene in an empty room.
- Do not retrieve for reassurance. A packet is built from what can change the decision.
- Never retrieve another novel's canon, even when the names match.
- If the task genuinely cannot be done inside the budget, say so and propose a split rather than silently overrunning.

## Coordination

`context-manager` builds the packet, `context-budget` sizes and trims it, and `novel-orchestrator` decides the scope that sets the budget.