# Visuals That Explain

Choose the representation that reveals the relationship. No note needs a diagram merely to satisfy a quota.

| Need | Representation |
|---|---|
| Short distinction or definition | Prose or table |
| Queue, stack, substitution, small before/after trace | Fenced ASCII/text |
| Branching process, state transitions, actor messages | Mermaid |
| Precise geometry, annotated mechanism, mathematical curve | SVG |
| Formula or derivation | Rendered LaTeX in the note |

## One job per visual

Draw for the hardest idea in a note, or where a picture beats a paragraph (structure, flow, before/after). Use the same values as the worked example beside it so the reader can cross-check, and add one sentence: "Notice that…". One clear figure teaches more than several decorative ones.

## Semantic checks before styling

Decide what the figure teaches and what evidence supports it. Match names, symbols, colours, and values to the note. For numerical figures, derive geometry from the same equations or data as the worked example. Label axes, units, domain, scale, and important points. Distinguish discrete samples from a continuous curve; distinguish a schematic from a calculated plot. Do not imply a guarantee through an arrow or a smooth curve unsupported by the method.

## ASCII

Prefer a small readable trace when alignment carries the explanation. Use a `text` fence, explicit operation labels, and short lines that fit the note pane.

```text
front       back
[A][B][C]          dequeue -> A
   [B][C]          enqueue D
   [B][C][D]       next dequeue -> B
```

## Mermaid

Use flowcharts for decisions, sequence diagrams for actor exchanges, and state diagrams for lifecycle transitions. Keep nodes short; put lengthy mathematics in the surrounding prose. Use stable identifiers and quote labels containing syntax-sensitive characters.

In flowcharts, write a two-line label as a backtick string inside the quotes, with a real line break. It reads like the rendered node and also allows **bold** inside the label.

```mermaid
flowchart TD
    A["`Check method
    assumptions`"] --> B{"`Conditions
    satisfied?`"}
    B -->|Yes| C["Apply the method"]
    B -->|No| D["Choose another method"]
    C --> E["Check the result"]
```

### Mermaid mistakes that break or distort a diagram

Each of these either stops the diagram rendering or changes what it shows. Avoid them while writing; the renderer only catches some of them.

| Mistake | What happens | Fix |
|---|---|---|
| A participant or node named `end`, `opt`, `alt`, `loop`, `par`, `off` (any capitalisation) | parsed as a keyword: the diagram fails or a block closes early | rename: `OffPeak`, `Optimizer`, `EndUser` |
| `$` in a label | Obsidian may read it as inline maths | write the unit: `USD 40`, `RM 5` |
| `;` inside a sequence-diagram `Note` | the note text is cut at the `;` | use a comma |
| `_` inside a backtick label, such as `min_cluster_size` | renders as *italics* | use a plain quoted label, or write it with spaces |
| backtick labels outside flowcharts | support varies by Mermaid version; often shown as raw text | plain text in sequence and state diagrams |
| a `mermaid` block inside a callout | every line needs the `> ` prefix, including the fences | keep diagrams outside callouts when possible |

Broken and fixed:

```text
sequenceDiagram                     sequenceDiagram
    participant Off as Off-peak         participant OffPeak as Off-peak
    Off->>Grid: charge                  OffPeak->>Grid: charge
```

Render using an available compatible Mermaid renderer, preferably the target Obsidian version. A successful external render does not establish compatibility with every Obsidian version. Inspect arrow direction, branch labels, crossings, and readability. Do not rely on syntax checking alone.

**A diagram that renders can still be impossible.** Replay it step by step against the text: a git graph that cherry-picks a commit before it is created renders fine but teaches the wrong order. Check that every number, actor, and outcome in the diagram matches the note's own worked answer.

## Recipe: "How it works, step by step"

For a mechanism (an algorithm, a protocol, a data structure under change), one section with three views teaches more than scattered figures:

| Part | Shows | Example (Raft leader election) |
|---|---|---|
| 1. Flowchart | the rule each actor follows | "timeout → become candidate → request votes → majority?" |
| 2. Sequence or state diagram | who talks to whom over time, or the lifecycle | follower → candidate → leader states |
| 3. Step table | the same run with the note's own toy numbers | term 1, node B times out first, gets 3 of 5 votes |

Use one small example throughout the three parts, so the reader can trace a single run. When the mechanism is computable, run a toy version and paste its real trace into the table.

## SVG defaults

**Use a white background by default**, including an explicit white rectangle covering the viewBox. Use dark text and axes, restrained accent colours, and light grid lines. This preserves the figure's own contrast in both light and dark vault themes. Change this only for an explicit user preference or a specific output requirement.

- Give the figure a `viewBox` and enough margins for labels and arrowheads.
- Use a consistent type scale; inspect text at the intended embed width, not just at full canvas size.
- Use labels or line styles as well as colour. Avoid tiny legends and overlapping annotations.
- Include a meaningful `<title>` and `<desc>`, and a nearby Markdown sentence explaining what to notice. Do not rely on embedded accessibility metadata alone.
- Keep SVG self-contained: no scripts, external fonts, or remotely loaded images. Escape generated XML text and attributes.
- Reuse the existing asset folder and descriptive filenames. Embed with a resolvable path, for example `![[assets/queue.svg|640]]`, adjusted to the vault layout.
- Use one embed width across a vault or folder. Read the width from neighbouring notes before adding an embed, and match it.

Minimal static skeleton:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 360"
     role="img" aria-labelledby="title desc">
  <title id="title">Figure title</title>
  <desc id="desc">Describe the relationship illustrated here.</desc>
  <rect width="640" height="360" fill="#ffffff"/>
  <g font-family="sans-serif" font-size="20" fill="#172033">
    <text x="32" y="48">Replace with the actual figure</text>
  </g>
</svg>
```

Use an already available plotting library for calculated curves and charts when it reduces coordinate mistakes; use direct SVG for small geometric diagrams. Retain a generator when reproducing a complex figure would otherwise be difficult. Do not add a new graphics framework for a simple drawing.

## Render and inspect

Parse SVG XML, then render and visually inspect the actual output. Check clipping, whitespace, contrast, labels, scale, and consistency with the calculation. Inspect at the intended embed size on a representative note background. Fix defects and inspect again. If rendering is unavailable, report that limitation rather than calling the visual validated.
