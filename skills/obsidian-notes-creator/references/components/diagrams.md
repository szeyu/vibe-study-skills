# Diagrams Reference

Two tools: **Mermaid** (preferred) and **ASCII** (for cases Mermaid can't handle).

---

## Mermaid — Which Type to Use

| Diagram type | Use when… | Avoid when… |
|---|---|---|
| `flowchart LR/TB` | Process flow, decision trees, cause → effect | Showing time order between actors |
| `sequenceDiagram` | Two or more actors exchanging messages over time | Simple one-actor process |
| `stateDiagram-v2` | Lifecycles, phases, state machines | Things without clear states |
| `mindmap` | Topic overview, brainstorming, classification trees | Processes with order |
| `timeline` | Historical events, evolution of a concept | Non-time-ordered things |
| `flowchart TB` (tree) | Hierarchies, taxonomies, "A is a type of B" | Cyclic relationships |

---

## Mermaid Templates

### Flowchart — Process / Decision
```mermaid
flowchart LR
    A[Start] --> B{Decision?}
    B -->|Yes| C[Path A]
    B -->|No| D[Path B]
    C --> E[End]
    D --> E
```

### Flowchart TB — Hierarchy / Taxonomy
```mermaid
flowchart TB
    A[Parent] --> B[Child A]
    A --> C[Child B]
    B --> D[Leaf 1]
    B --> E[Leaf 2]
```

### Sequence Diagram — Actors Exchanging Messages
```mermaid
sequenceDiagram
    participant Q as Query Encoder
    participant K as Key Encoder
    participant L as Loss
    Q->>L: query vector
    K->>L: key vectors (from queue)
    L-->>Q: gradient (backprop)
    L-..->K: no gradient (momentum only)
```

### State Diagram — Lifecycle / Phases
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Training : start
    Training --> Converged : loss stable
    Training --> Failed : diverged
    Converged --> [*]
```

### Mind Map — Topic Overview
```mermaid
mindmap
  root((Topic))
    Branch A
      Detail 1
      Detail 2
    Branch B
      Detail 3
```

### Timeline — Historical / Evolution
```mermaid
timeline
    title Evolution of SSL
    2016 : Context Encoders
    2018 : BERT (NLP)
    2020 : MoCo · SimCLR
    2022 : MAE
```

---

## Multi-line Node Labels

Use backtick strings for multi-line text inside nodes:

```mermaid
flowchart LR
    A["`key encoder
    slow update`"] --> B["`queue
    65k negatives`"]
```

---

## ASCII Diagrams — When to Use

Use ASCII **only** when:
- You need a **custom layout** that Mermaid can't express (e.g., showing a fraction, a queue buffer, a training loop state)
- You want to show **before vs. after** side by side
- You need to annotate specific parts of a diagram with arrows mid-content

### Box Characters Reference
```
Corners:   ┌ ┐ └ ┘
Lines:     ─ (horizontal)   │ (vertical)
T-joints:  ├ ┤ ┬ ┴   Cross: ┼
Arrows:    → ← ↑ ↓   ▶ ◀ ▲ ▼
Double:    ═ ║ ╔ ╗ ╚ ╝
```

### Overview Box
```
┌─────────────────────────────────────────┐
│              TOPIC TITLE                │
├─────────────────────────────────────────┤
│  Concept A     Concept B     Concept C  │
│     │              │             │      │
│  [detail]       [detail]      [detail]  │
└─────────────────────────────────────────┘
```

### Layer / Stack
```
┌─────────────────────────────────────────┐
│              Top Layer                  │
├─────────────────────────────────────────┤
│              Middle Layer               │
├─────────────────────────────────────────┤
│              Bottom Layer               │
└─────────────────────────────────────────┘
```

### Queue / Buffer
```
Front                                  Back
  ↓                                     ↓
[k_1][k_2][k_3][ ... ][k_N]   ← FIFO queue
  ↑ dequeue                    enqueue ↑
(oldest removed)              (newest added)
```

### Before / After Contrast
```
WITHOUT momentum:                WITH momentum:
  Encoder v1  →  z_A (valid)      Encoder v1.000 → z_A (valid)
  [big update]                    [tiny update: Δ=0.001]
  Encoder v2  →  z_B              Encoder v1.001 → z_B (still ~valid)
  z_A vs z_B: INCOMPARABLE        z_A vs z_B: COMPARABLE
```

---

## Embedded Visuals — SVG / PNG (data Mermaid can't draw)

Mermaid and ASCII show **structure**. For **data with values** — heatmaps, charts,
confusion matrices, annotated figures — generate a self-contained **SVG** (or PNG)
and embed it. Renders natively in Obsidian, no plugin.

```
![[my-figure.svg|580]]      ← the |580 sets display width in px
```

Save figures to an assets folder (e.g. `99-assets/`). **Interactive JS does not
render** in Obsidian — always export a static image.

### Which tool for which visual
| Need | Tool |
|---|---|
| Process / hierarchy / lifecycle | Mermaid |
| Custom layout, before/after | ASCII or SVG |
| **Values + colour** (heatmap, chart, matrix) | **SVG / PNG** |
| Equations | LaTeX `$...$`, `$$...$$` |

### Dark/light-mode rules (Obsidian won't recolour your SVG)
- Transparent background — never paint a white/black rect.
- Labels/axes in **mid-grey `#8a8a8a`** — readable on any theme (never `#333` or `#fff`).
- Text on a coloured shape: white on dark tiles, near-black on light —
  `'#fff' if 0.299*r+0.587*g+0.114*b < 140 else '#1f1f1f'`.

### Generator skeleton
```python
W, H = 640, 400
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="sans-serif">']
# append <rect>/<text>/<line>/<path> elements …
svg.append('</svg>')
open("99-assets/figure.svg", "w").write("\n".join(svg))
```

Pair every embedded figure with one sentence of prose naming **what to notice**.

---

## Mermaid Pitfalls — what breaks rendering

| Mistake | Why it breaks | Fix |
|---|---|---|
| `\n` in a label | Mermaid prints `\n` literally — no line break | keep the label on one line, or use the backtick multiline form |
| Numbered prefix `A[1. Step]` | the `1.` confuses the parser → error or blank diagram | drop the dot (`Step 1`), or quote it: `A["1. Step"]` |
| Special chars `( ) : ; # ,` in a label | unbalanced/illegal tokens | quote the whole label: `A["f(x): cost"]` |
| Brackets/quotes inside a label | parser sees them as syntax | quote the label, escape inner quotes |

> Rule of thumb: if a node label has anything beyond **letters, spaces, and a
> hyphen**, wrap it in `"…"` — and never number nodes with `1.` / `2.`.
