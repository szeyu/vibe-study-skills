# Single Notes

Keep one coherent learning objective in a note. Length alone does not justify a split; the number of new ideas does. If a note introduces more than about three new concepts that each need their own example, give each a clearly separated part or its own note. Improve the existing headings when revising rather than forcing this template onto every file.

## Adaptable outline

**Before you read** lists the 3–5 terms the note uses but does not teach, each linked to where it is taught. It is folded (`[!info]-`) on purpose: it is a lookup table, not an answer. Skip it when the note assumes nothing new.

**In a nutshell** opens with one bold sentence, then a small table of the key results with real numbers, then one closing sentence. The table lets a reader get the note in ten seconds.

**Work it by hand** comes before any code (and most notes need no code at all): one table that walks a real number from the note through the arithmetic, so the reader can do it on paper. Follow it with one `[!caution] Common mistake` callout. If the note already has a Common mistakes table, add only the worked table.

Use the same shape for notes of the same kind, so readers know where to look.

```markdown
# Topic

> [!info]- Before you read: terms used here
> | Term | Meaning | More |
> |---|---|---|
> | basis point | 0.01 percentage point | [[toolkit-note#Heading\|toolkit]] |

> [!abstract] In a nutshell
> **One bold sentence: what it is and why it matters.**
>
> | Measure | Result |
> |---|---|
> | the key finding | a real number with its date |
> | the main exception | a real number with its date |
>
> One closing sentence on what to take away.

## Why it exists

The problem it solves, ideally where the naive approach fails.

## Core idea

A concrete case with real values first, then the general statement
with symbols defined and read aloud in words.

## Worked example

Givens and goal, steps with the reasoning narrated, result,
and an independent check.

## Work it by hand

| Step | Working | Result |
|---|---|---|
| one real input from the note | the arithmetic written out | **the answer** |

One or two sentences on what the numbers show, tagged by source.

> [!caution] Common mistake
> The likely misreading, then the correction with one real number.

## Common mistakes

| Mistake | What happens | Fix |
|---|---|---|

## Check yourself

> [!question] A question that tests reasoning, not recall.
> **Answer:** The explanation, visible.

## Going deeper

Rare conditions, proofs, and subtleties moved out of the main path.
```

Use only applicable sections. Add prerequisites, comparisons, a useful visual, or related links where they help. Omit empty headings and generic summaries. An analogy, diagram, summary table, and practice section are not mandatory in every note.

A reference note can lead with definitions; a proof can lead with its claim and assumptions; a worked exercise can lead with its problem. Preserve that purpose while making the reasoning complete.
