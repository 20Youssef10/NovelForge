# Quality Gate

Worked example. A real gate run on Chapter 3, showing a mixed verdict and why.

## Checks
- [x] Structure and narrative value
- [x] Causality
- [x] Consequences
- [x] Character agency and arc
- [x] Character consistency
- [x] Dialogue and character voice
- [x] Narrative voice and POV
- [x] Style DNA and style drift
- [x] Generic writing
- [x] Cliché and trope intent
- [x] Continuity
- [x] Timeline
- [x] Canon
- [x] Narrative graph integrity
- [x] Mystery and reader knowledge
- [x] Foreshadowing and payoff debt
- [x] Pacing and tension
- [x] Theme and motif
- [ ] Power and battle logic — not applicable, no power use in this chapter
- [ ] Faction plausibility — not applicable, `faction-simulation` disabled for this project
- [x] Research provenance
- [x] Version and branch integrity

## Findings
| # | Severity | Finding | Evidence (location) | Engine |
| --- | --- | --- | --- | --- |
| 1 | Major | The argument at the rope ladder repeats information the reader already has, without advancing either relationship | Chapter 3, the rope ladder scene | pacing-engine |
| 2 | Moderate | Maro's dialogue is noticeably more formal than his profile specifies | Chapter 3, his first four lines | dialogue |
| 3 | Minor | "The sea did not care" recurs from Chapter 1 and has not yet been made to mean anything different | Chapters 1 and 3 | symbolism-motif |

Severity describes consequence, not effort. Finding 1 is Major because it consumes a
whole scene on ground the reader has already covered, in the chapter where the
relationship actually changes.

## Safe automatic repairs
- Repeated exposition in the rope ladder scene trimmed by 40 per cent; the argument's
  substance is intact and the scene now ends 300 words earlier
- Two continuity slips corrected: Wenna's apprentice rank referenced as journeyman in
  one line, and the Cormoret's passenger count in another. Both now match C-004 and
  the power-system table

## High-impact approval items
| Item | Risk | Recommendation | Author decision |
| --- | --- | --- | --- |
| Restructure the Chapter 4 opening to give Maro a decision of his own | MEDIUM | Do it; the current opening has him react to Wenna for two pages | Approved 2026-09-28 |
| Move the reveal of C-002's speaker from Chapter 7 to Chapter 5 | HIGH | Do not; U-001 is deliberately unresolved | Declined |

## Unresolved risks
Finding 1 is repaired but not re-audied; the pacing consequence of the trim has not
been checked against Chapter 4's opening.

## Verdict
PASS_WITH_ACCEPTED_ISSUES

Chapter 3 may proceed. Finding 3 is a Minor motif observation, accepted for now on
the grounds that the motif may yet be transformed in a later chapter.