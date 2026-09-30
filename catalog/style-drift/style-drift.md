# Style Drift Detector v2.1

Compare new or revised prose against this novel's own Style DNA and established representative passages — not against a generic genre standard. Prose that is unusual is not drifting if the novel has always been unusual.

## Dimensions

Check drift in:

diction and register, sentence rhythm and length, tense, narrative distance, POV handling, dialogue ratio, description density, imagery and metaphor density and sourcing, humour, emotional explicitness, and formatting.

## Intentional versus accidental

This is the whole judgement. Before flagging, ask whether the departure is:

- **Intentional evolution** — the story has moved somewhere, and the style moved with it. Chapter twelve can be terser than chapter three if something has changed.
- **Accidental drift** — a single scene written in a different register, most often because it was drafted in isolation or by a different pass.

Evidence for intention: sustained change across a span, correlated with a narrative development, and consistent in later chapters. Evidence for accident: isolated to one scene, uncorrelated with anything in the story, and reverting immediately afterwards.

## Record

Run audits against `style/STYLE_AUDIT.md`, which carries the dimension table, the intentional-versus-accidental judgement, generic-pattern findings, and any missing baselines.

## Method

Report: the dimensions that changed, the evidence with locations, the likely cause, the scope — single scene, chapter, arc, or whole novel — and the smallest corrective action that would restore consistency without flattening deliberate change.

Isolated drift in a single scene is usually a small local fix. Drift sustained across an arc is a structural question: either the style should be updated deliberately, or a batch of scenes needs work, and the author decides which.

## Rules

- Never flatten distinctive voice to achieve statistical consistency. The purpose is to find prose that has wandered from the book's voice, not to make every passage identical.
- Do not report a dimension that has no established baseline as drift. A novel with no consistent register has no register to drift from; that is a different finding, and a legitimate one.
- Preserve the author's voice even when it is inconsistent, unless asked otherwise. Report the inconsistency and let the author choose.

## Coordination

Use `narrative-style` to define or update the DNA, `generic-writing-detector` for prose that is styleless rather than misaligned, `narrative-voice` for POV and distance findings, and `critique` to route drift into a broader review.
