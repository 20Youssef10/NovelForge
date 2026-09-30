# Narrative Graph v2.1

Represent durable narrative state as entities plus typed relationships. The graph is the dependency and index layer: it answers "what does this touch?" quickly. It is not a replacement for authoritative domain records, and it must never become the source of truth for canon.

## Entities

Give every durable entity a stable ID and record its type, name, canon state, summary, and source in `graph/NODES.md`. Characters, locations, factions, events, mysteries, clues, promises, powers, themes, and motifs qualify. A passing description of scenery does not.

## Relations

Record typed edges in `graph/EDGES.md` with the relation, evidence or source, and status. Core relations include:

`CAUSED_BY`, `AFFECTS`, `KNOWS`, `SUSPECTS`, `LOCATED_AT`, `MEMBER_OF`, `CONFLICTS_WITH`, `FORESHADOWS`, `PAYS_OFF`, `DEPENDS_ON`, `CHANGES`, `PROMISES`, `FULFILS`, `CONTRADICTS`, `CONSTRAINS`, `SYMBOLISES`, `THEMATICALLY_ECHOES`, `BRANCHES_FROM`

Use the narrowest relation that is true. Precision in edges is what makes the graph useful; vague edges produce noise that retrieval then has to work around.

## Use

- **Targeted retrieval** — pull one or two hops of neighbours rather than whole files.
- **Canon impact** — before a change, walk the edges outward to find everything affected.
- **Obligation tracing** — follow `PROMISES` and `PAYS_OFF` to find unpaid debt.
- **Contradiction detection** — `CONTRADICTS` edges should be rare and always intentional; an unexpected one is a finding.

`graph/README.md` documents the model and the boundary between the graph and canon. Read it before extending the relation vocabulary.

## Discipline

Do not create graph noise for trivial prose details. A node per passing character mention is a graph nobody maintains and nobody trusts. Add edges where a dependency genuinely exists and would matter if the entity changed.

After any structural edit, run orphan and dead-edge checks: entities with no relations, relations pointing at missing entities, and edges that no longer reflect the text.

## Coordination

`canon-manager` owns canon state; the graph records it. `context-manager` queries the graph for retrieval. `consequence-engine` propagates through it. `payoff-debt` uses it to trace obligations. Never let a graph edit change canon; route that through `canon-manager`.
