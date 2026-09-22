# Frontmatter

Follow the vault's existing property conventions. Preserve creation dates, aliases, tags, and user-maintained fields. Do not rewrite dates merely because a file was inspected or add metadata solely to make a note look finished.

For a new note, a small block may be sufficient:

```yaml
---
tags:
  - subject/topic
date: YYYY-MM-DD
---
```

Replace the example date with the actual creation date. Add an updated date only if the vault uses it and the content changed substantively. A review status must reflect checks actually performed; creating a file does not justify `status: complete`.

Use valid YAML at the start of the file. Quote wikilink property values, for example `prerequisites: ["[[Foundations]]"]`. Keep property types consistent across related notes. Add aliases only when they help find the note, and avoid introducing a competing tag taxonomy.

Cite sources beside the claims they support. Optional source metadata can complement those citations but does not replace page, section, or figure references when available.
