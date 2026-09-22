# Callouts and Visible Solutions

Use callouts to distinguish a warning, question, example, or optional aside. Core explanations and long derivations usually belong in normal Markdown.

```markdown
> [!warning] Check the assumptions
> A convergence guarantee applies only under its stated conditions.

> [!example] Worked calculation
> Give the data, reasoning, result, and check.

> [!question] What changes at the boundary?

**Answer:** Explain directly here.
```

Use `[!note]` for context, `[!tip]` for a useful shortcut, `[!summary]` for a compact recap, and `[!quote]` for an attributed quotation. Choose by meaning rather than colour; themes may style them differently.

A callout without a folding marker stays visible. `[!question]-` is collapsed and `[!question]+` starts expanded but is still foldable. **Do not use either folding marker for answers or solutions by default.** Use normal text or a non-folding callout so the answer is directly readable. Hidden-answer practice is an explicit opt-in.

Keep blockquote prefixes on all lines belonging to a callout, including blank lines and any embedded code fences. Avoid deeply nested callouts and wrapping entire notes in them.
