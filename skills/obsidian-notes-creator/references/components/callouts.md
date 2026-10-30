# Callouts and Visible Solutions

Use callouts to distinguish a warning, question, example, or optional aside. Core explanations and long derivations usually belong in normal Markdown.

```markdown
> [!warning] Check the assumptions
> A convergence guarantee applies only under its stated conditions.

> [!example] Worked calculation
> Give the data, reasoning, result, and check.

> [!question] Q1 · What changes at the boundary?
>
> > [!success] Answer
> > Explain directly here.
```

**Self-check format.** Put each question in a `[!question]` callout and its answer in a nested `[!success] Answer` callout, both without folding markers. The reader sees a question box with a green answer box inside it. Number questions `Q1 ·`, `Q2 ·` when a section has more than one. Keep this format identical across every note; do not mix it with plain `**Q1.**` / `**Answer:**` paragraphs.

Use `[!note]` for context, `[!tip]` for a useful shortcut, `[!summary]` for a compact recap, and `[!quote]` for an attributed quotation. Choose by meaning rather than colour; themes may style them differently.

For likely misconceptions, a short warning in the form "You might think X — actually Y" is easier to remember than a general caution. Collect the rest in a **Common mistakes** table (mistake, what happens, fix) rather than scattering warnings through the explanation.

A callout without a folding marker stays visible. `[!question]-` is collapsed and `[!question]+` starts expanded but is still foldable. **Do not use either folding marker for answers or solutions by default.** Use the nested non-folding answer callout above so the answer is directly readable. Hidden-answer practice is an explicit opt-in.

The one folded box by default is **Before you read** (`[!info]-`): it is a term lookup, not a solution, so folding keeps the note's opening short.

Keep blockquote prefixes on all lines belonging to a callout, including blank lines and any embedded code fences. Avoid deeply nested callouts and wrapping entire notes in them.
