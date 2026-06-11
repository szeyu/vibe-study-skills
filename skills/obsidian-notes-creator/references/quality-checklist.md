# Quality Checklist

Run through this before closing a note or note set.

---

## Content Quality

- [ ] Every concept opens with **motivation** (what problem does it solve?) before the definition
- [ ] Every hard concept has an **analogy** — check `writing/analogies.md` for patterns
- [ ] Every concept has **at least one concrete example** — check `writing/examples.md`
- [ ] Formulas are accompanied by a **plain-English breakdown** (what each symbol means)
- [ ] Mathematical direction changes (negative signs, logs, inverses) are **explicitly walked through**
- [ ] Comparisons between similar concepts are **in a table**, not buried in prose

## Visual Quality

- [ ] Every note has **at least one Mermaid diagram** (flowchart, sequence, mindmap, etc.)
- [ ] Complex processes have an **ASCII before/after** or **queue/buffer diagram** if Mermaid can't express it
- [ ] Diagrams have labels that a reader can understand without reading the surrounding text

## Obsidian Components

- [ ] Callouts are used for: warnings, tips, analogies, practice questions — **not for decoration**
- [ ] Each callout type is used correctly (see `components/callouts.md` decision guide)
- [ ] Frontmatter is filled: `tags` and `date` at minimum
- [ ] At least **one wikilink** to a related or prerequisite note
- [ ] The **Related** section at the bottom has descriptions, not bare wikilinks

## Structure

- [ ] If the note is > ~400 lines, consider whether it should be **split** (see `structure/multi-file.md`)
- [ ] If split across files: a **hub/index note** exists and links to all sub-files
- [ ] Files are **numbered** for reading order if order matters
- [ ] The note opens with a **one-sentence summary** ("In a nutshell: …")

## Study Utility

- [ ] A **Common Pitfalls** or **Exam Pitfalls** table is included for exam-relevant topics
- [ ] Practice questions use **foldable callouts** (`> [!question]-`) so answers are hidden by default
- [ ] A **Summary Table** exists for topics with multiple terms or methods

---

## Minimum Viable Note

If time is short, at minimum a note must have:

1. One-sentence summary
2. One diagram (Mermaid)
3. One analogy or concrete example per major concept
4. Frontmatter with tags + date
5. At least one wikilink
