---
name: research-provenance
description: Track research sources, claims, verification status, uncertainty, dates, and usage for factual material used in fiction, keeping traceable records of where externally derived facts enter the novel. Use for any claim the story depends on being accurate.
---
# Research Provenance v2.1

Maintain traceability from externally derived facts to the places in the novel that rely on them. A novel that depends on accuracy needs to know which facts are load-bearing and whether they are still true.

## Records

Record in `research/SOURCE.md` and `research/CLAIM.md`.

For each source: ID, title, type, date or access context, authority, and which claims it supports.

For each claim: ID, the claim, classification, source, verification state, scope, confidence, where it is used in the novel, and review date.

Verification states: `VERIFIED`, `UNCERTAIN`, `DISPUTED`, `CREATIVE_FICTION`.

## Load-bearing claims

Identify which claims the plot actually depends on. A novel that assumes a particular legal procedure, medical outcome, historical event, or technical process is relying on that claim; if it is wrong, the story breaks. These claims need verification, a review date, and a fallback.

Claims used only for colour need less rigour and rarely need a record at all. Distinguishing the two prevents the entire research apparatus being applied uniformly and pointlessly.

## Staleness

Mark claims for re-check when:

- the source is dated and the underlying facts may have changed,
- the claim concerns a fast-moving subject,
- sources disagree,
- the novel's use of the claim has been revised since verification,
- a significant amount of time has passed since last review.

A verified fact is verified as at a date. Recording that date is what makes the record honest.

## Rules

- Never fabricate citations. There is no such thing as a plausible placeholder source in a project record.
- Creative fiction must never masquerade as an external fact. An invented detail that later gets researched should have its classification changed explicitly, not silently.
- Flag outdated or unsupported factual assumptions when accuracy matters, even when nobody asked.
- Do not let research alter canon. Promotion runs through `canon-manager`.

## Coordination

Use `research` to gather and classify, `worldbuilding` to apply findings, `localisation` for cultural claims affecting adaptation, and `canon-manager` for promotion to canon.
