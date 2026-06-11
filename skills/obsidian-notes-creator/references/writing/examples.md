# Example Patterns

Concrete examples are non-negotiable. Every concept needs at least one.
This file defines the **structures** for writing good examples in study notes.

---

## Pattern 1: Concept → Example → Variation

The most versatile pattern. Show the concept, apply it to a specific case, then twist one variable to deepen understanding.

```markdown
## [Concept Name]

**Definition:** [Brief explanation]

**Example:**
[Specific, concrete scenario with real numbers or names]

**Variation:**
What if [one thing changes]? → [Different outcome and why]
```

**Real instance:**
```markdown
## Osmosis

**Definition:** Water moves from low to high solute concentration across a semipermeable membrane.

**Example:**
A red blood cell placed in salt water (high solute outside) → water leaves the cell → cell shrinks (crenation).

**Variation:**
What if the cell is placed in pure water? → Water floods in → cell swells → may burst (lysis).
```

---

## Pattern 2: Problem → Solution → Why It Works

For algorithm steps, derivations, or exam-style problems.

```markdown
**Problem:** [Specific question or scenario]

**Solution:**
Step 1: [action]
Step 2: [action]
Result: [answer]

**Why it works:** [The underlying principle that makes each step correct]
```

Use a foldable callout for solutions when the note doubles as practice material:
```markdown
> [!question]- Solution
> Step 1: ...
> Step 2: ...
> Result: ...
```

---

## Pattern 3: Cross-Discipline Example Table

For concepts that appear across subjects. Shows transferability.

| Subject | Concept | Concrete Example | Variation |
|---|---|---|---|
| Biology | Osmosis | RBC in salt water → shrinks | In pure water → swells |
| Physics | Momentum | Bowling ball vs tennis ball, same speed | Same mass, different speed? |
| Economics | Supply/Demand | OPEC cuts oil → price rises | New oil discovered → price falls |
| ML | Contrastive loss | Positive pair pulled closer | Negative pair pushed apart |

---

## Pattern 4: Named Worked Example

For complex derivations or multi-step proofs, give the example a title so it's referenceable.

```markdown
### Example: Why momentum encoder is needed

Suppose the encoder updates by 10% per step (no momentum).

After batch 1: encode image A → z_A (with encoder v1)
After batch 2: encoder changes → z_B encoded with v2
...
After batch 100: z_A was encoded with a completely different network.
z_A and z_100 are not comparable → the queue is useless.

Conclusion: large encoder updates invalidate the queue.
```

---

## What Makes an Example Good

- **Specific** — uses actual names, numbers, or concrete scenarios (not "some X")
- **Short** — 3-6 lines; if longer, it's a worked problem, not an example
- **Directly follows the concept** — not relegated to a later section
- **Teaches something you couldn't see from the definition alone**
- **Has a variation** that either confirms or surprises

## What Makes an Example Bad

- Circular: "For example, contrastive loss contrasts positives and negatives" (just restates the definition)
- Too abstract: "For example, consider two vectors A and B" (no context)
- Too long: becomes its own mini-lecture without a clear point
