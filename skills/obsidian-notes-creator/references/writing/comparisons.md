# Comparison Patterns

When two or more things are related but different, comparisons prevent confusion and build deeper understanding. This file defines when and how to compare.

---

## Rule: Compare as Early as Possible

Don't wait until the end of a section to compare. If you're introducing B and A already exists in the notes, compare them immediately after introducing B.

---

## Pattern 1: Side-by-Side Table

The most common and readable format. Use whenever comparing 2+ things across multiple dimensions.

```markdown
| Dimension | Thing A | Thing B |
|---|---|---|
| [attribute 1] | ... | ... |
| [attribute 2] | ... | ... |
| [key difference] | ... | ... |
```

**Tips:**
- Put the **most important distinguishing row last** (it's what the student remembers)
- Use ✅ / ❌ for binary comparisons
- Keep cells short — one concept per cell

**Example:**
| | MoCo | SimCLR |
|---|---|---|
| Encoders | Two (query + key) | One (shared) |
| Key update | Momentum (no grad) | Backprop |
| Negative source | Queue of past keys | Current batch |
| Batch size needed | Moderate (256) | Large (4096+) |
| Memory cost | Queue | Large batch |

---

## Pattern 2: Hierarchy View

For things that are generalisations of each other. Show the progression from most constrained to most general.

```markdown
[Most specific / constrained]
  ↓  relaxes [constraint A]
[Middle]
  ↓  relaxes [constraint B]
[Most general]
```

**Example:**
```
K-means      encoder = hard assignment (one-hot),  decoder = lookup table
  ↓  relax: allow soft, continuous encoding
PCA          encoder = linear projection,           decoder = linear projection back,  + orthogonality constraint
  ↓  relax: allow nonlinear transforms + remove constraint
Autoencoder  encoder = deep NN,                    decoder = deep NN,                 no constraint
```

---

## Pattern 3: Similarities + Key Difference

After a table, always close with a plain-text summary of what they share and what truly separates them. The table shows details; this paragraph gives the mental model.

```markdown
**Similarities:** Both X and Y do [shared goal]. Both use [shared mechanism].

**Key difference:** X [does A] while Y [does B]. This matters because [consequence].
```

**Example:**
> **Similarities:** Both MoCo and SimCLR use the InfoNCE loss and data augmentation to create positive pairs.
>
> **Key difference:** MoCo decouples the number of negatives from batch size (via queue + momentum encoder), while SimCLR requires a huge batch to have enough negatives. This makes MoCo more memory-efficient for the same number of negatives.

---

## Pattern 4: Before / After (Same System, Different Config)

For comparing the same concept under different parameter settings.

```markdown
| Setting | What happens | Why |
|---|---|---|
| [param] too low | [failure mode] | [reason] |
| [param] optimal | [good outcome] | [reason] |
| [param] too high | [different failure] | [reason] |
```

**Example — Masking ratio in MAE:**
| Masking ratio | Transfer accuracy | Why |
|---|---|---|
| 10% (too low) | ~55% | Too easy — model copies neighbours |
| 75% (optimal) | ~75% | Forces global reasoning |
| 90% (too high) | ~66% | Too little context to reconstruct from |

---

## When Not to Use a Table

- When there's only **one** meaningful difference → use a sentence instead
- When the cells would be > 1 line each → split into separate sections with headers
- When the items are **not parallel** (different types of things) → tables imply they're comparable
