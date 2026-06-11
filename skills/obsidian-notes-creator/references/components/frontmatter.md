# Frontmatter Reference

Obsidian reads YAML frontmatter at the top of every note (between `---` delimiters).
It powers search, dataview queries, and the Properties panel.

---

## Standard Block

```yaml
---
tags:
  - subject/topic
  - concept
date: YYYY-MM-DD
---
```

Always include at minimum: `tags` and `date`.

---

## All Property Types

| Type | YAML syntax | Example |
|---|---|---|
| Text | `key: value` | `status: in-progress` |
| Number | `key: 4.5` | `difficulty: 3` |
| Checkbox | `key: true` | `reviewed: false` |
| Date | `key: 2024-01-15` | `date: 2024-06-11` |
| Date + Time | `key: 2024-01-15T14:30:00` | `due: 2024-06-30T23:59:00` |
| List (inline) | `key: [a, b, c]` | `tags: [cv, ssl, moco]` |
| List (block) | multiline under key | see below |
| Link | `key: "[[Other Note]]"` | `related: "[[18-repr]]"` |

### Block list syntax
```yaml
tags:
  - CV
  - contrastive-learning
  - MoCo
```

---

## Recommended Tags Pattern

Use **hierarchical tags** with `/` to namespace by subject:

```yaml
tags:
  - CV/concepts          # subject / folder-type
  - CV/contrastive       # subject / sub-topic
  - exam-prep            # cross-subject utility tag
```

---

## Full Example

```yaml
---
tags:
  - CV/concepts
  - self-supervised-learning
  - contrastive-learning
date: 2026-06-11
status: complete
difficulty: 3
prerequisites:
  - "[[18-representation-learning]]"
---
```

---

## Notes

- Frontmatter **must be the first thing** in the file — no blank lines before the opening `---`.
- Obsidian treats unknown keys as custom properties — they won't break anything.
- `aliases` lets other notes link using different names: `aliases: ["SSL", "Self-Supervised"]`
