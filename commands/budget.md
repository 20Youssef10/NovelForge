---
description: Size and trim the current Context Packet against its token budget
argument-hint: "[scope]"
---

Size the context before loading it.

1. Load `context-budget`, and `context-manager` to assemble the candidate packet.
2. Set the budget from scope: scene 8,000 tokens, chapter 20,000, arc 60,000, novel
   120,000. Adjust downward for a small context window.
3. Estimate before loading: characters divided by four for prose, lines multiplied by
   twelve for tabular records. Treat these as a floor, since JSON, tables, and YAML
   inflate.
4. Rank every candidate section by decision relevance. Ranks 1 to 5 always load; ranks
   10 and 11 do not, unless explicitly requested.
5. If over budget, cut in order: thematic and relationship records, then prose in
   favour of facts and IDs, then narrow graph traversal to one hop, then summarise
   history, then split the task.
6. Never trim ranks 1 to 5. A packet missing the active scene or the canon it touches
   is worse than no packet.
7. Record what was deferred and why in the packet. An unexplained omission is
   indistinguishable from a mistake.