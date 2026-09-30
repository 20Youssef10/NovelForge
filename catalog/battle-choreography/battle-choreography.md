# Battle Choreography v2.1

Maintain a coherent tactical state throughout the sequence. Action is readable when the reader can reconstruct where everyone is, what each can see, and what it costs.

## Maintain the tactical state

Track throughout, not just at the start:

- **Positions** — where everyone is, and relative distances.
- **Visibility** — what each participant can see, and what blocks sight.
- **Terrain** — cover, elevation, hazards, escape routes, and destructible features.
- **Abilities** — what each can do, including current limitations and injuries.
- **Resources** — what has been spent, and what remains.
- **Costs** — what each action takes from the user.
- **Objectives** — what each side is actually trying to achieve.
- **Knowledge** — what each knows about the other's capabilities and intentions.

The state must be consistent between exchanges. A character who has lost an arm does not use it three exchanges later, and terrain that has been destroyed stops providing cover.

## Rules

- **Every reversal needs a cause.** Advantage changes because something changed — position, information, resource, condition — not because the scene needs it.
- **Major advantages must be earned or explained.** If a stronger character wins easily, either show why they cannot press the attack, or make the ease itself the point.
- **Prioritise decision and adaptation over attack exchanges.** A sequence reads well when participants respond to each other, not when blows are traded. Repeated attack-reaction cycles with no adaptation are the main failure of action writing.
- **Respect the power system's costs.** Using an ability incurs its cost now, and often later.
- **Knowledge constrains behaviour.** A character cannot respond to an opponent's ability if they have never seen it.

## Shape

Open with position, objective, and constraint rather than with an attack. Escalate by narrowing options: the terrain reduces, a resource runs out, an injury accumulates. Ensure the sequence ends with a changed state, not merely a victor.

Give the reader a moment to register reversals; a reversal that arrives faster than it can be perceived is not experienced.

## Record

Maintain the sequence in `battles/BATTLE.md`, including the reversal log. A battle with no recorded state cannot be audited, and unrecorded state is how sequences contradict their own earlier exchanges.

## Audit

Flag: unexplained position changes, abilities used beyond limits, attacks from impossible angles, terrain that changes without cause, injuries that vanish, victories without cause, participants who stop adapting, and sequences that resolve rather than end.

## Coordination

Use `power-system` for capabilities and costs, `character-simulation` for what participants would do, `tension-engine` for stakes and pressure, `pacing-engine` for sequence tempo, and `consequence-engine` for what the fight leaves behind.
