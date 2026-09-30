# Mystery Engine v2.1

Treat mystery as controlled information, not surprise alone. Surprise without fairness is a trick; a mystery the reader could have solved and did not is a different kind of failure.

## Record

Maintain each mystery in `mysteries/MYSTERY.md`, and the underlying character and reader knowledge in `knowledge/LEDGER.md`. The four separations above are only maintainable if the knowledge states have somewhere to live.

## Four separations

Keep distinct, and never collapse them:

- **Author truth** — what actually happened.
- **Character knowledge** — what each character knows, suspects, and believes.
- **Reader knowledge** — what has been presented as explicit, observable, inferable, or ambiguous.
- **Evidence visibility** — what the reader has been shown, and with what reliability.

Most mystery failures are a collapse of one of these four.

## What to track

Central mysteries, sub-mysteries, suspects, motives, evidence, clues, red herrings, secrets, hypotheses, reveal prerequisites, reveal timing, and payoff state. Record each in `mysteries/MYSTERY.md` with a stable ID.

## Fair solvability

When a mystery is intended to be solvable, major conclusions must be supported by clues available before or at the reveal — unless the story deliberately establishes why evidence was hidden, destroyed, or unreliable. That exception must be visible in the text, not merely true in the author's head.

Test this directly: assemble the clue set available at the reveal point and check whether a careful reader could have reached the conclusion. If not, either add evidence earlier or change the intended solution. The step-by-step solvability test, the information-class table, and the failure taxonomy are in `references/FAIRNESS.md`.

## Red herrings

A red herring must be a real false lead, not a lie. It should be supported by evidence that a reasonable reader would follow, and it must be resolvable — either discarded or explained — rather than simply abandoned when inconvenient.

## Failure modes

Detect accidental withholding (evidence withheld to force a reveal), impossible knowledge (a character deducing what the text never gave them), arbitrary reveals (solutions arriving without mechanism), retroactively meaningless clues (details that only acquire meaning after the fact, revealed as though they had been planted), and clue chains that contradict each other.

## Post-reveal

Plan the aftermath. A reveal changes information state for every character and for the reader; track what each now knows, what they do about it, and which obligations it discharges. Reveals that produce no consequence are events, not resolutions.

## Output

Produce a compact mystery state, information map, clue map, the obvious reader expectation, alternative earned routes, risks, and unresolved questions.

## Coordination

Use `reader-knowledge` for what the reader plausibly holds, `foreshadowing` for clue planting, `payoff-debt` for reveal obligations, `causality-engine` for the solution's mechanism, and `narrative-graph` for clue and suspect relations.
