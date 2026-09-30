# Narrative Graph

The graph is the dependency and index layer. It answers "what does this touch?" quickly. It is **not** the source of truth for canon — `canon/` and the domain files are.

## Files
- `NODES.md` — durable entities with stable IDs and canon state.
- `EDGES.md` — typed relationships with evidence and status.

## Working rules
1. Give every durable entity a stable ID. Never reuse an ID.
2. Use the narrowest relation that is true.
3. Add edges only where a dependency genuinely exists and would matter if the entity changed.
4. Do not create nodes for trivial prose detail.
5. After any structural edit, run orphan and dead-edge checks.

## Why it exists
- **Targeted retrieval** — pull one or two hops of neighbours rather than whole files.
- **Canon impact** — walk edges outward before a change to find everything affected.
- **Obligation tracing** — follow `PROMISES` to `FULFILS` to find unpaid debt.
- **Contradiction detection** — an unexpected `CONTRADICTS` edge is a finding.

## Boundary
A graph edit never changes canon. If an edge implies a canon change, route it through `canon-manager` and record the change in `canon/` first.
