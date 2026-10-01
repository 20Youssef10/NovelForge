# Salt and Ember — worked example

A small, complete, fictional NovelForge project. It exists so the shape of a *filled*
project is visible rather than described, and so the templates have a reference to be
checked against.

Nothing here is a novel. There is no prose, only the records an agent would maintain
while writing one.

## What this demonstrates

| File | Shows |
| --- | --- |
| `NOVEL_BIBLE.md` | A filled identity block, and a domain index that marks what exists and what was deliberately skipped |
| `PROJECT_SETTINGS.md` | POV and tense as configuration, approval strictness with the reason it was raised |
| `canon/facts.md` | Four entries with dependencies, one demoted from permanent to arc canon, and the review note explaining why |
| `canon/retcons.md` | One completed high-impact retcon, and why the incomplete-migration section is empty |
| `canon/unresolved.md` | Two open questions, one deliberately deferred forever, and a collision warning between them |
| `characters/CHARACTER.md` | A full profile including contradictions, simulation notes, and an unresolved final state |
| `characters/RELATIONSHIP.md` | Asymmetric wants, divergent beliefs, and what each would have to sacrifice |
| `power_system/POWER_SYSTEM.md` | One ability with hard limits, three ranks, and two exploits left `UNRESOLVED` rather than patched |
| `obligations/INDEX.md` | Seven obligations, a due-soon table, and one overloaded window left open as a risk |
| `mysteries/MYSTERY.md` | A central mystery the author has deliberately not solved, with the audit rows still filled in |
| `timeline/EVENT.md` | Two events, one with chronology and presentation order deliberately reversed |
| `quality/FINDINGS.md` | Five open findings, two resolved, one accepted risk, one on regression watch |
| `quality-check.md` | A real gate run with a mixed verdict and one declined high-impact item |
| `context/BUDGET.md` | A measured scene-scope packet, what was deferred, and why deferring the power system mattered |
| `audit/AUDIT_RUN.md` | A chapter audit with the engines run, the engines skipped and why, and an engine disagreement the author resolved |

## Things worth noticing

**Not every engine ran.** The chapter audit skipped `power-system`,
`battle-choreography`, and `faction-simulation` because Chapter 3 has no combat and
no institutional politics. Recording the skips is as important as the findings: a
skipped engine that should have run is the gap the record exists to expose.

**Two engines disagreed and the author decided.** `pacing-engine` read the rope-ladder
scene as padding; `dialogue` read the repetition as a character circling something he
cannot say. Both were right about different things, and neither was authoritative.

**Unresolved is a valid state.** U-001, U-002, both power exploits, and the final
character state are all open on purpose. None of them is an oversight, and each says
so where a reader or agent would otherwise assume otherwise.

**The project is deliberately incomplete.** `factions/` is absent because the Guild
and Salt Compact are not yet modelled, and `faction-simulation` is disabled in
settings so it cannot confidently describe institutions that do not exist yet.
Chapters 1 to 3 are planned; 4 to 9 are not. An example that was complete in every
domain would misrepresent how a real project is maintained.

## Trying the engines against it

Copy the directory and point an agent at it:

```bash
cp -R examples/salt-and-ember /tmp/my-novel-project
cd /tmp/my-novel-project
```

Then ask for something the records already constrain, such as:

- "Draft Chapter 4, Maro's opening" — should respect `dialogue` F-102, the disabled
  `faction-simulation`, and the R-001 trajectory
- "Audit Chapter 5" — should notice F-090 on regression watch, because Chapter 5 was
  drafted before the rank correction
- "What does Chapter 7 owe the reader?" — should surface the overloaded window and
  F-104 rather than reassuring you that it is fine

The interesting test is the third. An agent that reports Chapter 7 as manageable has
not read `obligations/INDEX.md`.