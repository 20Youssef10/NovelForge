# Context Budget

Worked example. Showing what a measured, trimmed Context Packet looks like for a
single scene. The estimate method is `characters / 4` for prose and `lines × 12` for
tabular records, treated as a floor.

Task: draft Chapter 3, the rope-ladder argument
Scope: scene 3.2 only
Budget: 8,000 tokens (scene scope)
Used: 6,180 tokens

## Loaded
| Rank | Section | Source | Tokens | Why |
| --- | --- | --- | --- | --- |
| 1 | Scene 3.2 plan | `chapters/SCENE_PLAN.md` | 420 | the unit being drafted |
| 1 | Wenna's state | `characters/CHARACTER.md` | 1,150 | POV, and her choice drives the scene |
| 2 | C-003, C-004 | `canon/facts.md` | 190 | Maro aboard; the manifest count |
| 3 | R-001 neighbours | `characters/RELATIONSHIP.md` | 1,340 | the relationship this scene moves |
| 4 | O-005 | `obligations/INDEX.md` | 90 | due this chapter |
| 5 | T-001 boundary | `timeline/EVENT.md` | 280 | sets what she knows tonight |
| 6 | Knowledge: Wenna vs reader | `knowledge/LEDGER.md` | 520 | she must not know U-001 |
| 8 | Style DNA | `style/style-dna.md` | 890 | close third, clipped under stress |
| 9 | Reader state | `reader/READER_STATE.md` | 640 | the reader knows more than she does |
| — | Style audit | `style/STYLE_AUDIT.md` | 660 | for revision, not drafting |

Total loaded: 6,180

## Deferred
| Section | Tokens saved | Reason |
| --- | --- | --- |
| `obligations/OBLIGATION.md` full record for O-005 | 240 | The index carries enough to draft; the full record only matters at resolution |
| `themes/THEME.md` | 310 | This scene is relational, not thematic; the theme emerges in Chapter 6 |
| `themes/MOTIF.md` | 280 | "The sea did not care" is flagged in F-103 but is not being planted here |
| `power_system/POWER_SYSTEM.md` | 520 | No power use in this scene; loading it would invite the scene to use it |
| `mysteries/MYSTERY.md` | 480 | U-001 is unresolved; there is nothing to enforce |
| Chapters 1 and 2 summaries | 900 | Retrieved as event IDs, not prose |
| `graph/` node and edge tables | 660 | One-hop neighbours already resolved through the records above |

Total deferred: 3,390

## Why these deferrals
The power system is the clearest case. Loading `POWER_SYSTEM.md` would not have
prevented an error, because no capability is in play — but it would have put the
ability in front of the model, and a model with a fire-drawer's limits described at
it is more likely to write a scene with fire-drawing in it. Deferral is not only about
tokens; it is about not putting the wrong material in front of the decision.

The motif table was deferred because F-103 concerns a motif the chapter does not
develop. Loading it risks the scene quietly trying to pay off a symbol it was not
asked to plant.

## Over budget handling
Not reached here. Were the packet to exceed 8,000, the order of sacrifice would be:
theme and motif records first, then replace relationship prose with its IDs and
summary, then narrow graph traversal to the two entities actually on stage, then
split the scene into two drafting passes.

Ranks 1 to 5 are never trimmed. A packet missing the active scene or the canon it
touches is worse than no packet.