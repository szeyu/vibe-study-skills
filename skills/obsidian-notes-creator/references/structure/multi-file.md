# Multi-File Structure

Some topics are too large or too interconnected to fit in one note.
This file defines **when to split** and **how to organise** across multiple files.

---

## When to Split Into Multiple Files

Split when **any** of these apply:

1. **Length** — the note exceeds ~400 lines and still feels dense
2. **Reusability** — a sub-concept is referenced from multiple other notes (it deserves its own file so others can wikilink directly to it)
3. **Distinct audiences** — one part is conceptual theory, another is step-by-step technique, another is worked examples. Different readers want different parts.
4. **Natural subtopics** — the topic has 3+ major sub-concepts that each warrant their own diagram and examples

Do **not** split just because a topic is "big". Split when the parts are genuinely separable.

---

## Standard Folder Layout

```
topic-name/
├── README.md                  ← Hub/index note (see structure/index-note.md)
├── concepts/                  ← Theory and "what is X"
│   ├── 01-overview.md
│   ├── 02-concept-a.md
│   └── 03-concept-b.md
├── techniques/                ← "How to do X" — algorithms, methods, procedures
│   ├── 01-method-a.md
│   └── 02-method-b.md
├── examples/                  ← Worked problems and case studies
│   ├── 01-basic.md
│   └── 02-advanced.md
└── practice/                  ← Exercises, past exam questions
    └── 01-exercises.md
```

Not all folders are required. Use only what the topic needs:
- A pure theory topic might only need `concepts/`
- A procedural topic might only need `concepts/` + `techniques/`
- A problem-solving topic might only need `concepts/` + `examples/` + `practice/`

---

## File Naming Conventions

- **Prefix with numbers** for reading order: `01-`, `02-`, `03-`
- **Use kebab-case**: `self-supervised-learning.md` not `selfSupervisedLearning.md`
- **Name after the concept**, not after what it contains: `moco.md` not `momentum-encoder-notes.md`
- **Keep names short**: the folder provides context

---

## Cross-File Linking

Every file in a multi-file structure should:
1. Link back to the hub: `← [[README]]`
2. Link forward to the next logical file
3. Use `![[file#section]]` to embed shared content rather than copy-pasting

Example top-of-file navigation:
```markdown
**Topic:** [[README|Self-Supervised Learning]]
**Previous:** [[01-overview]]
**Next:** [[03-simclr]]
```

---

## Deciding File Granularity

| Situation | Decision |
|---|---|
| Two concepts are always explained together | Keep in one file, use `##` headings |
| One concept is referenced from 3+ other notes | Give it its own file |
| A concept has its own diagram, examples, and pitfalls | Give it its own file |
| A concept is just a definition (< 10 lines) | Keep in a parent file, use `###` heading |

---

## Example: Self-Supervised Learning

This topic naturally splits because contrastive and predictive learning are distinct families, and MoCo/SimCLR/MAE each have enough depth for their own files:

```
CV/
├── README.md
├── concepts/
│   ├── 01-classical-unsupervised.md    ← K-means, PCA, Autoencoder
│   ├── 02-contrastive-learning.md      ← Framework + InfoNCE loss
│   ├── 03-moco.md                      ← Queue + momentum encoder
│   ├── 04-simclr.md                    ← Single encoder, large batch
│   └── 05-mae.md                       ← Masking, ViT, 75% ratio
└── practice/
    └── 01-ssl-exercises.md
```
