---
name: reader-knowledge
description: Model plausible reader knowledge, inference, expectation, uncertainty, and misunderstanding at each narrative point, in order to test mystery fairness, reveal integrity, foreshadowing subtlety, and accidental spoilers. Use whenever information is revealed, withheld, or manipulated.
---
# Reader Knowledge Simulator v2.1

Maintain a model of what a careful reader plausibly knows, infers, suspects, misunderstands, and expects at each point. Use it to test fairness and subtlety — not to claim you can predict every reader.

## Information classes

Classify information as:

- **Explicit** — stated directly in the text.
- **Observable** — presented as evidence, though not explained.
- **Inferable** — supportable by reasoning from what is present.
- **Ambiguous** — supportable by more than one reading.
- **Hidden** — deliberately withheld, author-side only.
- **Misleading** — presented in a way that supports a false conclusion.

The distinction between inferable and ambiguous is where most fairness problems live. If a reasonable reader can reach the intended conclusion, the reveal is earned. If they can only reach it by assuming the author is steering them, it is not.

## Method

Maintain a reader-information ledger by chapter or scene where useful, recording at each point what has been established, what a reader would naturally conclude, and what they are now expecting. Test:

- **Mystery fairness** — could the reader have solved it from what they had?
- **Reveal timing** — has enough been planted, and not too much?
- **Foreshadowing subtlety** — is the plant available without being signposted?
- **Accidental spoilers** — has the text disclosed more than it intended?
- **Expectation management** — has the story set up a payoff it does not intend to deliver?

## Rules

- Model plausible information states, not a single deterministic one. Where a reasonable reader could hold two readings, record both and check that the intended one is supported.
- Never treat a reader's failure to notice a clue as a design success.
- Do not use this to make the text simpler. Controlling information is not the same as removing ambiguity that the story wants.

## Output

Record states in `reader/READER_STATE.md` with the position, what is established, likely inferences, and open expectations. Flag reveal points that are under-supported or over-signposted.

## Coordination

Use `mystery-engine` for clue integrity, `foreshadowing` for plant visibility, `payoff-debt` for expected payoffs, and `narrative-voice` for what the narration is permitted to know.
