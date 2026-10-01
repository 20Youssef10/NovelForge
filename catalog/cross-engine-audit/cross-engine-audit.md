# Cross-Engine Audit v2.5

A single audit that decides which engines matter for the scope in question, runs them in an order where later engines can use earlier findings, and returns one consolidated report.

## Why composition matters

Running all 45 engines on a single scene produces noise: a dialogue scene audited for power scaling and timeline produces forty "not applicable" rows and buries the two findings that matter. Composition is not about doing less work; it is about not manufacturing findings that cannot exist.

## Select by scope

| Scope | Engines |
| --- | --- |
| Scene | `dialogue`, `scene-writing`, `narrative-voice`, `tension-engine`, `continuity` |
| Chapter | Scene set plus `pacing-engine`, `payoff-debt`, `foreshadowing`, `reader-knowledge`, `style-drift` |
| Arc | Chapter set plus `character-arc-engine`, `causality-engine`, `consequence-engine`, `theme-engine`, `power-system` where applicable |
| Full novel | Arc set plus `narrative-graph`, `canon-manager`, `timeline`, `payoff-debt`, `generic-writing-detector`, `anti-cliche`, `research-provenance`, `version-control` |
| Series | Novel set plus `series-manager` |

Always include `quality-gate` as the closing step, and `critique` when the author asked for an honest assessment rather than a mechanical check.

## Sequence for dependency

Run in this order where the scope warrants it, because each stage can consume the last:

1. `context-manager` — retrieve only what can affect the audit
2. `continuity`, `timeline` — establish what is actually true
3. `causality-engine`, `consequence-engine` — structural validity
4. `character-simulation`, `character-arc-engine` — agency and change
5. `mystery-engine`, `reader-knowledge`, `foreshadowing`, `payoff-debt` — information control
6. `pacing-engine`, `tension-engine` — tempo and pressure
7. `narrative-style`, `style-drift`, `generic-writing-detector`, `anti-cliche` — voice and originality
8. `theme-engine`, `symbolism-motif`, `trope-manager` — thematics and convention
9. `power-system`, `battle-choreography`, `faction-simulation` — where applicable
10. `critique` — independent read of what the earlier stages found
11. `quality-gate` — verdict

Skipping a stage is fine when the scope does not reach it. Running stage 10 before stage 2 produces critique that flags structural problems the later engines then explain.

## Consolidate

Record every finding in `audit/AUDIT_RUN.md` with the engine that raised it, then merge into `quality/FINDINGS.md` under stable IDs. Do not report the same issue once per engine that noticed it.

Where two engines disagree, report the disagreement rather than picking a winner: a scene that reads as intentional foreshadowing to one engine and accidental symbolism to another is a genuine authorial question, and the author decides.

## Budget and cap

State the expected scope and engine count before starting, and confirm with the author if an audit would exceed a full novel pass. For a large novel, audit arc by arc rather than attempting one pass.

## Output

One report per run: scope, engines run, engines deliberately skipped and why, findings merged by ID, risks carried forward, and a verdict. Reference existing findings instead of restating findings already in the ledger.

## Coordination

Every engine is routed by `novel-orchestrator`. This skill decides the subset and the order; it does not replace any engine's own method.