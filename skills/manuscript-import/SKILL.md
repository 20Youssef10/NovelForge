---
name: manuscript-import
description: Ingest an existing draft into a NovelForge project by inventorying chapters, detecting POV and tense, extracting characters and relationships, reconstructing the timeline and plot structure, inferring Style DNA, and classifying discovered canon. Use when adopting a manuscript already written, when a project has no Novel Bible, or when retrofitting structure onto finished prose.
---
# Manuscript Import v2.3

Import existing prose without damaging it. The prose is the artefact of record; the project files are a map of it. Never rewrite the author's sentences during intake.

## Principle

Import derives structure from what is already written. Nothing is invented, nothing is corrected, and nothing is silently normalised. Where the draft contradicts itself, record the contradiction as `UNRESOLVED` and let the author decide — a discovery phase that quietly fixes things is a rewrite in disguise.

## Phased, with approval between phases

1. **Inventory** — read the whole draft and count chapters, scenes, words, POV distribution, tense, and time span. Report before doing anything else.
2. **Structure** — map arcs, act or part structure, and the current narrative position.
3. **Entities** — extract characters, locations, factions, objects, and power-system terms, each with a stable ID and a source reference.
4. **Relationships** — build the relationship graph, marking asymmetry and unresolved tensions.
5. **Timeline** — reconstruct chronology, keeping presentation order and actual order distinct.
6. **Information** — record what the author knows, what each character knows, and what the reader has been told, per scene where feasible.
7. **Style** — infer Style DNA from the prose the author considers characteristic, and confirm it with them before treating it as canonical.
8. **Canon** — classify what is established versus unresolved. Everything discovered starts as `UNRESOLVED` until the author confirms it.

Present findings and get approval before writing project files. Intake is the largest structural operation NovelForge performs, so it carries the same approval discipline as any other HIGH-risk change.

## Extraction discipline

- **Cite everything.** Every extracted fact records the chapter or scene it came from. An unsourced extraction is a guess that will be trusted later.
- **Names are not identities.** A character appearing under two names may be one person, two people, or a deliberate reveal. Record the ambiguity; do not merge.
- **Infer Style DNA from a sample, then confirm.** Ask the author which passages feel characteristic rather than deriving it purely statistically, and record the answer as the baseline.
- **Distinguish author intent from artefact.** A dangling setup may be intentional, forgotten, or abandoned. Record all three possibilities rather than assuming one.
- **Preserve the author's terminology.** Import invented words into `glossary/GLOSSARY.md` exactly as written.

## Partial drafts

Incomplete manuscripts are the normal case. Mark the frontier explicitly: what is drafted, what is planned, and where the story currently stops. Everything after the frontier belongs in plans, never in canon.

## Output

Record the run in `import/IMPORT_PLAN.md` and every extraction decision in `import/EXTRACTION_LOG.md`, then populate the domain templates the draft actually supports. Do not create directories for domains the manuscript gives no evidence for.

## Coordination

Use `context-manager` to read without contaminating, `canon-manager` for classification, `narrative-voice` for POV detection, `timeline` for chronology, `narrative-style` for Style DNA, and `continuity` for the contradictions intake will inevitably surface. Follow with a `quality-gate` run, because import is when a draft's structural problems first become visible.
