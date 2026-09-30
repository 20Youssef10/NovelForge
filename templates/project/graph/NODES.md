# Narrative Graph Nodes

Durable entities only. A node per passing character mention is a graph nobody maintains and nobody trusts.

- ID: (stable, never reused)
- Type: CHARACTER / LOCATION / FACTION / EVENT / MYSTERY / CLUE / PROMISE / POWER / THEME / MOTIF / OBJECT / CONCEPT
- Name:
- Canon state: PERMANENT_CANON / ARC_CANON / CHAPTER_CANON / SCENE_STATE / PROPOSAL / UNRESOLVED / RETCON
- Summary (one line):
- Source (where established):
- First appeared:

## Register

| ID | Type | Name | Canon state | Source |
| --- | --- | --- | --- | --- |
| | | | | |

## Integrity checks
Run after any structural edit.

| Check | Result |
| --- | --- |
| Orphan nodes (no relations)? | |
| Edges pointing at missing nodes? | |
| Canon state changed without a `canon-manager` record? | |
| Duplicate nodes for the same entity? | |
| Nodes added for trivial prose detail? | |
