# Analogy Patterns

Analogies are the most powerful tool for making abstract concepts click.
This file defines the **types** of analogies and **when to use each**.

---

## Rule: Analogy Before Formula

Always introduce the intuition with an analogy **before** showing the math or formal definition.
The analogy gives the student a mental hook; the formula gives it precision.

```
WRONG order:  Formula → Example → Analogy (analogy feels like an afterthought)
RIGHT order:  Analogy → Intuition → Formula → Confirmation
```

---

## Pattern 1: Step-Down Analogy

Start with a very everyday scenario, then progressively map each element to the technical concept.

**Structure:**
```
1. Everyday version (no jargon)
2. "This maps to X in our context"
3. Technical version (with jargon)
```

**Example — InfoNCE loss:**
> You're in a room with 1 friend and 99 strangers.
> Someone asks: "What fraction of the crowd's attention belongs to your friend?"
>
> - Loss is LOW when your friend clearly stands out (close to you, strangers are far).
> - Loss is HIGH when strangers crowd you equally — your friend is lost in the noise.
>
> The model is trained to maximise this fraction. That's exactly what the InfoNCE numerator/denominator does.

---

## Pattern 2: Before / After Contrast

Show what happens **without** the mechanism, then **with** it.
This makes the problem vivid before the solution lands.

**Structure:**
```
WITHOUT [mechanism]:
  [show the broken state — concrete steps]

WITH [mechanism]:
  [show the fixed state — same concrete steps, different outcome]
```

**Example — MoCo momentum encoder:**
```
WITHOUT momentum encoder:
  Step 1: Measure Alice with ruler v1 → 170 cm → save
          [Encoder updates — ruler changes a LOT]
  Step 2: Measure Bob with ruler v2  → 175 cm → save
  Q: Is Bob taller than Alice?
  A: Can't tell. Different rulers. Old data is USELESS.

WITH momentum encoder:
  Step 1: Measure Alice with ruler v1.000 → 170 cm → save
          [Ruler adjusts by 0.001 — almost nothing]
  Step 2: Measure Bob with ruler v1.001  → 175 cm → save
  Q: Is Bob taller than Alice?
  A: Yes — the ruler barely changed. Data is STILL VALID.
```

Use this pattern when: a mechanism exists to **solve a problem that only arises with scale or over time**.

---

## Pattern 3: Object Analogy

Map the abstract system to a physical object with a clear, visualisable structure.

**Structure:**
```
[Object] = [Technical thing]
[Part of object] = [Component of technical thing]
[Action on object] = [Operation in the system]
```

**Example — MoCo queue:**
> **The shoebox of ID cards**
>
> - The shoebox = the queue (stores past representations)
> - The ID card = the encoded representation vector of one image
> - Taking a photo = running an image through the key encoder
> - Removing the oldest card = FIFO dequeue
> - The camera settings = the momentum encoder (changes slowly so cards stay comparable)

Pairs well with Pattern 2 — use Pattern 3 to name the analogy, then Pattern 2 to show it in action.

---

## Pattern 4: Process-as-Pseudocode Analogy

When the concept is a sequential process, write it as pseudocode but using everyday words.
This bridges the gap between narrative and technical.

**Structure:**
```
Step 1: [everyday action]  →  [what this maps to technically]
Step 2: [everyday action]  →  [technical]
Result: [everyday outcome] →  [technical outcome]
```

**Example — Why autoencoder ≠ semantic understanding:**
```
ZIP two photos of the same person:
  compress(photo_A) → bits_A
  compress(photo_B) → bits_B

  bits_A ≠ bits_B   ← completely different compressed output
  decompress(bits_A) → photo_A   ✓ perfect reconstruction
  decompress(bits_B) → photo_B   ✓ perfect reconstruction

Conclusion: ZIP never learned they're the same person.
            It only learned to copy bytes efficiently.
            An autoencoder has exactly the same weakness.
```

---

## Pattern 5: Fraction / Direction Flip

For mathematical concepts involving a negative sign, log, or inverse, walk through the direction change explicitly.

**Structure:**
```
Minimize [expression]
  = Minimize -log(fraction)    ← negative sign flips goal
  = Maximize  log(fraction)    ← log is monotone, so...
  = Maximize      fraction     ← this is the real goal
```

Then explain what makes the fraction bigger (numerator ↑, denominator ↓).

---

## Choosing the Right Pattern

| Situation | Best pattern |
|---|---|
| Introducing a new formula | Pattern 5 (direction flip) or Pattern 1 (step-down) |
| Explaining why a mechanism exists | Pattern 2 (before/after contrast) |
| Describing a data structure / system component | Pattern 3 (object analogy) |
| Showing a process step-by-step | Pattern 4 (process-as-pseudocode) |
| General concept intuition | Pattern 1 (step-down) |

---

## Quality Signals for a Good Analogy

- A student with no domain knowledge can follow the analogy
- Every component of the analogy maps to something real in the system
- The analogy doesn't break down halfway through
- After reading it, the formula or definition feels "obvious" rather than arbitrary
