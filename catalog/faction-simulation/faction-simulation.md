# Faction Simulation v2.1

Factions are not hive minds. Each is a collection of people with partial information, competing interests, and internal disagreement, and its response is the aggregate of those rather than a single institutional will.

## Record

Maintain each faction in `factions/FACTION.md`, with blocs, partial information, and a response log. The response log matters most: a faction that has never been asked how it would respond will be modelled from whatever the plot requires.

## Model

For each faction, record: goals, assets, constraints, leaders, internal blocs, public position, hidden agendas, relationships with other factions, and what it knows.

Internal blocs matter more than they first appear. A faction with three blocs and a single stated policy will surprise the reader, which is usually the wrong effect. Record where blocs disagree and what each would do if it prevailed.

## Response simulation

For a meaningful event:

1. Establish what each bloc knows and what it believes about the event's cause.
2. Determine what each bloc wants from the outcome.
3. Assess what each can do given its assets and constraints.
4. Predict the response, and the disagreement likely to follow it.
5. Propagate second-order effects — how the response changes the faction's position relative to others.

Factions respond to their interests and their information, not to the author's plot. A faction that acts suicidally because the story requires it should be able to explain its reasoning from its own position.

## Partial information

Never model a faction as omniscient. They know what they have observed, been told, or inferred — usually less than the reader, and sometimes less than the protagonist. Information asymmetry between factions is one of the most useful sources of political tension available.

Where a faction acts on false information, that information should have a traceable source, because the moment it is corrected the consequences should follow.

## Detection

Flag: instant unanimity, responses with no information basis, factions that ignore their own constraints, resources appearing when needed and vanishing when not, alliances with no mutual benefit, and institutions that act as plot devices rather than actors.

## Coordination

Use `worldbuilding` for the institutions' origins, `consequence-engine` for how faction moves propagate, `power-system` where institutional power depends on a system, `character-simulation` for leader behaviour, and `narrative-graph` for `MEMBER_OF` and `CONFLICTS_WITH` edges.
