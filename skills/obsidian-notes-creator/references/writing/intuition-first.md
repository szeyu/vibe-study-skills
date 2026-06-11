# Intuition-First Writing

The most common mistake in study notes is leading with the formula, definition, or algorithm — before the student knows *why it exists* or *what problem it solves*. This file defines the order to build understanding.

---

## The Golden Order

```
1. Problem           — What goes wrong without this?
2. Intuition         — What's the big-picture idea?
3. Analogy           — Make it concrete (see writing/analogies.md)
4. Formal definition — Now the formula/algorithm lands
5. Confirmation      — "This is why the formula looks this way"
```

Never open a concept with its definition. Open with its **motivation**.

---

## Practical Templates

### For a new concept

```markdown
## [Concept Name]

> **In a nutshell:** One sentence that gives the core idea without jargon.

### The Problem It Solves

[What goes wrong in the world without this concept? 2-3 sentences.]

### Intuition

[Big-picture explanation using plain language. No symbols yet.]

### How It Works

[Now introduce the mechanism, formula, or algorithm.]

**Why the formula looks this way:**
[Connect each part of the formula back to the intuition.]
```

### For a formula

```markdown
## [Formula Name]

Plain-text version first:
"[What the formula computes in plain English]"

Formal version:
$$[formula]$$

Breaking it down:
| Part | Meaning |
|---|---|
| [symbol] | [what it represents] |

Why minimising/maximising this achieves the goal:
[Step through the direction, e.g. "The -log flips the goal: minimising -log(x) = maximising x"]
```

---

## Specific Patterns

### "Why does this formula push X and pull Y?"

Walk through in three lines:
```
Minimising L
  = Maximising the fraction        (negative log flips direction)
  Fraction grows when:
    numerator ↑  →  positive pair gets closer
    denominator ↓  →  negative pairs get pushed away
```

### "Why does this design choice exist?"

Open with the world **without** the design choice:
```
Without [X], the problem is: [concrete failure mode].
With [X], [concrete improvement].
```
Then explain the mechanism.

### "Why this number / threshold?"

Show what happens at too-low and too-high values:
```
[Parameter] too low  →  [failure mode A]
[Parameter] at optimum  →  [good outcome]
[Parameter] too high →  [failure mode B]
```
This works for masking ratio, temperature, momentum, learning rate, etc.

---

## Signals That Notes Are Formula-First (Bad)

- The first thing after the heading is a LaTeX block
- There's no "problem" or "motivation" section before the algorithm
- Examples appear only at the end, as an afterthought
- The student would need to already understand the concept to read the note

## Signals That Notes Are Intuition-First (Good)

- The first paragraph explains what the concept is trying to do
- An analogy appears before any symbols
- The formal definition comes with a "why it looks this way" explanation
- A student with no background could read the first 3 paragraphs and get the gist
