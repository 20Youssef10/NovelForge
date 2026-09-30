---
name: timeline
description: Maintain coherent chronology across dates, durations, ages, sequencing, travel time, flashbacks, and simultaneous events, tracking branch-specific divergences separately. Use when planning, auditing, or changing when anything happens.
---
# Timeline v2.1

Maintain a coherent chronology without over-tracking irrelevant minutiae. A timeline that records every meal is a timeline nobody maintains, and an unmaintained timeline is worse than none.

## What to track

Dates, durations, ages, sequencing, travel time where it is consequential, flashbacks, simultaneous events, and branch-specific events. Prioritise anything a character could notice, a plot turn could depend on, or a contradiction could hide behind.

## Age and duration

Record ages explicitly. A character's age at the time of an event, not merely at the present, because age limits and maturation are easy to break silently across long novels.

Travel time is consequential when the story depends on arrival, pursuit, message timing, or resource decay. If it matters, record it; if it does not, leave it loose.

## Record

Maintain events in `timeline/EVENT.md` with date or range, duration, participants and their ages at the time, causal position, and the effects owed. Record chronology and presentation order separately — they are different facts, and conflating them produces false continuity errors.

## Ordering and dependency

Before accepting a timeline change, identify dependent chapters, character ages, travel constraints, causal ordering, and any event that becomes impossible if the change holds.

Events that were simultaneous in one plan and sequential in another create the hardest class of contradiction to find later, because nothing looks wrong in isolation.

## Branch divergence

Branch-specific events must be recorded against their branch. A branch that shifts a date does not change the main timeline, and merging branches requires reconciling both chronologies explicitly rather than assuming one supersedes the other.

## Flashbacks and non-linearity

Record non-linear presentation separately from chronology. The order in which the story presents events and the order in which they occur are different facts; conflating them produces false continuity errors.

## Rules

- Never move an event silently. A date change is a canon change and routes through `canon-manager`.
- Prefer a range over a false precision when the story is imprecise.
- Check ages and durations together; they fail as a pair.

## Coordination

Use `causality-engine` to verify that ordering is causally necessary, `consequence-engine` for downstream effects of a time change, `consequence` propagation through factions, and `version-control` for branch divergence and merges.
