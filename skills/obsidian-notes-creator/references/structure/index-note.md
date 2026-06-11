# Index Note Template

The index (or hub) note is the entry point for a multi-file topic.
It doesn't contain detailed content — it provides orientation and navigation.

---

## Template

```markdown
---
tags:
  - subject/topic
  - index
date: YYYY-MM-DD
---

# [Subject Name]

> [Brief 2-3 sentence description of what this topic covers and why it matters.]

---

## Quick Navigation

### Core Concepts
- [[concepts/01-overview|Overview]] — Big picture and motivation
- [[concepts/02-concept-a|Concept A]] — [One-line description]
- [[concepts/03-concept-b|Concept B]] — [One-line description]

### Techniques & Methods
- [[techniques/01-method-a|Method A]] — [One-line description]

### Worked Examples
- [[examples/01-basic|Basic Examples]] — Start here
- [[examples/02-advanced|Advanced Examples]] — After concepts

### Practice
- [[practice/01-exercises|Exercises]] — Self-test questions

---

## Concept Map

[Mermaid diagram showing how the sub-topics relate to each other]

---

## Prerequisites

- [[prior-subject-note]] — [what the reader needs first]

---

*Last updated: YYYY-MM-DD*
```

---

## Rules for a Good Index Note

1. **No detailed content** — the index sets direction, not substance. If you're explaining something at length, it belongs in a concept file.
2. **Every link has a one-line description** — bare wikilinks are useless for navigation.
3. **The concept map is mandatory** — it shows structure at a glance.
4. **Prerequisites are explicit** — don't assume the reader knows what to read first.
5. **Last-updated date** — so you know when to review.

---

## When to Write the Index Note

Write it **last**, after all the concept/technique/example notes exist.
The index is a map of what you built — you can't map it until it exists.

Exception: if the topic is large enough, write a skeleton index first to plan the file structure, then fill it in as you write each sub-note.
