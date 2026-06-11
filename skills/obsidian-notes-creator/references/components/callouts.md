# Callouts Reference

Obsidian callouts are blockquotes with a type tag. They render with a coloured border, icon, and title.

## Syntax

```markdown
> [!type] Optional custom title
> Content line 1
> Content line 2
```

Foldable — add `-` (collapsed by default) or `+` (expanded, collapsible):
```markdown
> [!faq]- Click to expand
> Hidden until clicked.
```

Nested:
```markdown
> [!note] Outer
> > [!warning] Inner
> > Nested content
```

---

## All 13 Types — When to Use Each

| Type | Aliases | Colour | Use when… |
|---|---|---|---|
| `note` | — | Blue | Background context, extra info, "by the way" facts |
| `info` | — | Blue | Defining terms, clarifying scope |
| `abstract` | `summary`, `tldr` | Teal | Opening 1-sentence summary of a long section |
| `tip` | `hint`, `important` | Cyan | Best practices, shortcuts, "remember this" |
| `success` | `check`, `done` | Green | Confirming correct understanding, "this is the right way" |
| `question` | `help`, `faq` | Yellow | Posing exam-style questions inside the note |
| `warning` | `caution`, `attention` | Orange | Common mistakes, subtle gotchas, "don't confuse with…" |
| `failure` | `fail`, `missing` | Red | What breaks, what doesn't work, anti-patterns |
| `danger` | `error` | Red | Critical misunderstandings that cause wrong answers |
| `bug` | — | Red | Known edge cases or counterintuitive behaviours |
| `example` | — | Purple | Analogies, worked examples, concrete illustrations |
| `quote` | `cite` | Grey | Direct quotes from papers, textbooks |
| `todo` | — | Blue | Study tasks, things to revisit |

---

## Decision Guide

```
Is this a mistake students commonly make?       → [!warning] or [!danger]
Is this a concrete example or analogy?          → [!example]
Is this a "remember this" shortcut?             → [!tip]
Is this background context, not core content?   → [!note]
Is this a self-check question?                  → [!question]
Is this a paper quote?                          → [!quote]
Is this confirming correct reasoning?           → [!success]
```

---

## Anti-patterns to Avoid

- **Don't wrap normal paragraphs in callouts** just to add colour. Callouts should signal something special.
- **Don't use `[!note]` for everything** — it dilutes meaning. Pick the most specific type.
- **Don't make callouts too long.** If it's more than ~6 lines, it's probably main content, not a callout.

---

## Examples

### Marking a common mistake
```markdown
> [!warning] Don't confuse these
> The **key encoder** in MoCo is NOT updated by backprop.
> Only the query encoder is. The key encoder uses momentum averaging.
```

### Analogy block
```markdown
> [!example] Shoebox analogy
> Think of the queue as a shoebox of ID cards.
> Each batch adds new cards. Old cards stay until the box is full.
> The momentum encoder ensures all cards were taken with the same camera.
```

### Foldable practice question
```markdown
> [!question]- Why does MAE use 75% masking instead of 15%?
> Images are spatially redundant — neighbours are highly correlated.
> 15% masking is too easy; the model just copies adjacent pixels.
> 75% forces reasoning about global object structure.
```
