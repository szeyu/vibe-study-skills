# Analogies With Boundaries

Use an analogy when a familiar mechanism makes an unfamiliar one easier to reason about. A direct example, derivation, or small trace may be clearer. Analogies are optional and are not proofs.

## Three parts

1. Describe the familiar situation briefly.
2. Map its relevant objects and operations to the technical concept.
3. Name the point where the analogy stops being reliable, then return to the exact definition.

For a FIFO queue, a line of customers maps arrival to enqueue and serving the front customer to dequeue. Unlike people, stored values do not decide to leave or change order. An ASCII trace can then show the exact operations.

## Useful patterns

| Need | Pattern | Check |
|---|---|---|
| Explain a data structure | Familiar objects mapped to stored values and operations | Does ownership, order, or mutability differ? |
| Explain a mechanism | Same concrete case before and after applying it | Is the improvement conditional rather than guaranteed? |
| Introduce abstraction | Everyday case, mapping, formal version | Did the analogy import an unstated assumption? |

Avoid absolute claims such as “old representations are useless” or “slow updates guarantee comparability” when the actual effect is gradual or depends on conditions. Compression and learned representations can illustrate reconstruction, but they are not equivalent mechanisms.

## Bridges from what the reader already knows

Often the best "analogy" is not an everyday object but something the reader has already studied: a programming language they use, an earlier course, or familiar maths. Put the two side by side and name the difference explicitly, e.g. Python `list` vs NumPy array: one type per array, and `+` adds element by element. A useful format is: *habit you already have → what happens here → the right way here.* An unmarked difference makes a bridge misleading.

Walk through signs, logarithms, and inverses as mathematics, not as an analogy. Check their domains and dependencies explicitly.
