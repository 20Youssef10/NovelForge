# Narrative Graph Edges

Use the narrowest relation that is true. Precision in edges is what makes the graph useful; vague edges create noise that retrieval must work around.

- ID:
- From (node):
- Relation:
- To (node):
- Status: ACTIVE / RETIRED / CONTRADICTED
- Evidence or source:
- Established at:
- Branch: MAIN / branch name

## Relations
`CAUSED_BY` · `AFFECTS` · `KNOWS` · `SUSPECTS` · `LOCATED_AT` · `MEMBER_OF` · `CONFLICTS_WITH` · `FORESHADOWS` · `PAYS_OFF` · `DEPENDS_ON` · `CHANGES` · `PROMISES` · `FULFILS` · `CONTRADICTS` · `CONSTRAINS` · `SYMBOLISES` · `THEMATICALLY_ECHOES` · `BRANCHES_FROM`

## Register

| From | Relation | To | Status | Evidence |
| --- | --- | --- | --- | --- |
| | | | | |

## Useful traversals
Walk these for specific questions.

- Canon impact of a change — `CAUSED_BY`, `AFFECTS`, `CONSTRAINS`, `DEPENDS_ON`
- Unpaid obligations — `PROMISES` without a matching `FULFILS`
- Who could know a fact — `KNOWS`
- Clue to suspect — `SUSPECTS`, `CAUSED_BY`
- Setup to payoff — `FORESHADOWS`, `PAYS_OFF`
- Thematic coherence — `THEMATICALLY_ECHOES`, `SYMBOLISES`

## Integrity checks
| Check | Result |
| --- | --- |
| Dead edges (referring to retired or missing nodes)? | |
| `CONTRADICTS` edges present, and each intentional? | |
| Branch edges leaking into main? | |
| Promises with no fulfil edge and no recorded decision? | |
