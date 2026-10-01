# Audit Run

Worked example. A chapter-scope cross-engine audit, showing the composition and
consolidation.

Run: 2026-09-28
Scope: chapter
Author requested: mechanical check
Budget: 20,000 tokens allocated, 16,400 used

## Engines run
| Engine | Why it applied | Result | Findings raised |
| --- | --- | --- | --- |
| `context-manager` | Every audit starts by retrieving only what can affect the verdict | 10,200 tokens, trimmed per `context/BUDGET.md` | — |
| `continuity` | Cross-scene fact consistency | Two mechanical slips, both fixed | F-090, F-091 |
| `timeline` | Ch 3 depends on T-001 ordering | Coherent; the flashback ordering in T-004 is deliberate | — |
| `causality-engine` | The argument must arise from conditions | Sound; Maro's position follows R-001 | — |
| `consequence-engine` | The argument changes their alliance | Acknowledged in Ch 5 | — |
| `character-simulation` | Would Wenna say any of this under this pressure | Plausible; she is blunt under duress as specified | — |
| `reader-knowledge` | Reader knows more than Wenna about the stones | Intentional irony, not a leak | — |
| `foreshadowing` | F-002 is planted in this chapter | F-002 reaffirmed | — |
| `payoff-debt` | O-005 due this chapter | Carried, not paid | — |
| `pacing-engine` | Scene function against length | One Major finding | F-101 |
| `tension-engine` | The argument has stakes | Weak-but-present; the rope ladder holds it | — |
| `dialogue` | Maro's voice against profile | One Moderate finding | F-102 |
| `narrative-voice` | Close third, no head-hopping | Clean | — |
| `style-drift` | Against Style DNA | One Minor motif observation | F-103 |
| `quality-gate` | Closing verdict | PASS_WITH_ACCEPTED_ISSUES | — |

## Engines skipped
| Engine | Why it did not apply to this scope |
| --- | --- |
| `power-system`, `power-exploit`, `battle-choreography` | No power use or combat in Chapter 3 |
| `faction-simulation` | Disabled for this project; institutions not yet modelled |
| `theme-engine`, `symbolism-motif` (structural pass) | Thematic work is not this chapter's function; the motif check ran via `style-drift` |
| `trope-manager` | No genre-convention question arises here |
| `series-manager` | Standalone novel |
| `research-provenance` | No external factual claim depends on this chapter |

Recording the skips matters as much as the findings. `power-exploit` would have
produced confident output about a system this chapter never touches.

## Sequence used
Standard dependency order, with one deliberate exception: `critique` was run before
`quality-gate` as normal, but was restricted to an independent read rather than a
full review, since the author asked for a mechanical check.

## Findings
Merged with `quality/FINDINGS.md`. New findings only.

| ID | Severity | Finding | Location | Raised by | Notes |
| --- | --- | --- | --- | --- | --- |
| F-090 | Moderate | Rank stated as journeyman, contradicting C-001 context | Ch 3, Wenna's self-description | continuity | Mechanical; fixed |
| F-091 | Moderate | Manifest said 28 crew against 31 in C-004 | Ch 3, Maro's recount | continuity | Mechanical; fixed |
| F-101 | Major | Scene repeats known information instead of advancing R-001 | Ch 3, rope ladder | pacing-engine | Trimmed 40% |
| F-102 | Moderate | Maro's register more formal than `CHARACTER_VOICE.md` | Ch 3, his first four lines | dialogue | Left for revision pass |
| F-103 | Minor | "The sea did not care" recurs unreformed | Ch 1 and 3 | style-drift | Accepted risk |

## Engine disagreements
| Subject | Engine A says | Engine B says | Author decision |
| --- | --- | --- | --- |
| The rope ladder repetition | `pacing-engine`: scene is padded, trim it | `dialogue`: the repetition is deliberate, Maro is circling because he cannot say what he knows | Author: trim by 40%; the circling is preserved at a shorter length |

Neither engine was treated as authoritative. `pacing-engine` was measuring length,
`dialogue` was measuring character, and both were describing the same pages. The
author resolved it, which is the only correct outcome.

## Context budget
| Section | Loaded | Estimated tokens | Deferred | Reason |
| --- | --- | --- | --- | --- |
| Character and relationship | yes | 2,490 | no | both parties to the scene |
| Canon | yes | 190 | no | load-bearing facts |
| Timeline | yes | 280 | no | sets knowledge state |
| Style DNA | yes | 890 | no | auditing prose |
| Power system | no | 0 | 520 | not applicable to this chapter |
| Theme and motif | partial | 280 | 310 | motif checked, theme deferred |

## Risks carried forward
F-101 was repaired but not re-audited; the pacing consequence of the trim has not been
checked against Chapter 4's opening.

## Verdict
PASS_WITH_ACCEPTED_ISSUES

Chapter 3 may proceed. Next audit scope: Chapter 4 arc, which should resolve whether
the Chapter 3 trim left a hole and whether the Chapter 7 overload (F-104) is real.