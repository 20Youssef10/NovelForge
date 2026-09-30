# Plot Engineering v2.1

Engineer causality, escalation, stakes, reversals, choices, and consequences. Reject any event that exists only because something needed to happen.

## Event anatomy

For every major event, identify:

- **Cause** — the prior conditions that made the event possible.
- **Agent and decision** — who chose, and what they chose between.
- **Immediate effect** — what changed on the page.
- **Downstream consequence** — what changes later, and for whom.
- **Affected characters** — whose position, knowledge, or relationship moved.
- **Information change** — what the reader and each character now knows.
- **Future dependency** — what later work now depends on this event.

An event missing a cause is a coincidence. An event missing a decision is a happening. An event missing a downstream consequence is a reset.

## Causality and contrivance

Distinguish causal necessity from coincidence, and coincidence from contrivance. Coincidence is acceptable when it is seeded, plausible, and does the narrative work; contrivance is coincidence that exists to force a turn and strains against established world logic.

Coincidence used as repair — reaching for a random event to fix a structural problem — is the most common structural failure. Fix the cause instead.

## Predictability

Evaluate predictability by identifying the obvious route, then generating alternatives that are earned by the established world and characters. Predictability is not a fault; the absence of an earned alternative is. Offer the reader a choice between two legitimate routes and let the story take one.

## Trade-offs

Prefer irreversible consequences and meaningful trade-offs over spectacle without consequence. Every gain should cost something the story tracks. Escalation should raise stakes and reduce options, not merely increase volume.

## Rejecting events

When an event fails the test, say why and propose the smallest structural fix: add a cause, attach a decision, extend a consequence, or remove the event. Do not patch with additional events.

## Coordination

Use `causality-engine` for chain validation, `consequence-engine` for propagation, `tension-engine` for pressure, `pacing-engine` for tempo, and `payoff-debt` to register what the turn promises. Structural changes route through `canon-manager`.
