# Single Note Template

Use this template when a topic fits comfortably in one file (roughly under 400 lines).

---

## Full Template

```markdown
---
tags:
  - subject/topic
date: YYYY-MM-DD
---

# [Topic Title]

> **In a nutshell:** One sentence. What is this and why does it matter?

**Prerequisites:** [[prior-concept]] — what the reader needs to know first
**See also:** [[related-note]] — where this leads next

---

## Overview

[Mermaid or ASCII diagram showing the big picture of this topic]

---

## [Section 1: Main Concept]

[Problem / motivation — what goes wrong without this?]

[Intuition — plain language, no symbols]

> [!example] [Analogy title]
> [Concrete analogy using Pattern 1–5 from writing/analogies.md]

[Formal definition or formula]

**Breaking it down:**
| Symbol / Part | Meaning |
|---|---|
| ... | ... |

**Why it works:** [Connect the formula back to the intuition]

---

## [Section 2: Mechanism / Algorithm]

[Step-by-step with a diagram if helpful]

```
Step 1: [action]
Step 2: [action]
Result: [outcome]
```

---

## [Section 3: Comparison (if applicable)]

| Dimension | This | Alternative |
|---|---|---|
| ... | ... | ... |

**Key difference:** [One sentence summary]

---

## Summary Table

| Term | Definition | Example |
|---|---|---|
| [concept] | [brief] | [concrete] |

---

## Common Pitfalls

| Pitfall | Correct understanding |
|---|---|
| "[wrong belief]" | [correct explanation] |

---

## Practice

1. [Question]
   > [!question]- Answer
   > [Step-by-step answer]

2. [Question]
   > [!question]- Answer
   > [Answer]

---

## Related

- [[note-a]] — [why it's related]
- [[note-b]] — [why it's related]
```

---

## Notes on the Template

- The **overview diagram** is mandatory. If you can't draw it in Mermaid, use ASCII.
- The **in-a-nutshell** line forces you to understand the concept before writing about it.
- **Common Pitfalls** should reflect actual mistakes — don't fabricate them.
- **Practice** questions should use foldable callouts so the note can double as a study tool.
- **Related** links should always have a reason next to them, not just a bare wikilink.
