---
name: obsidian-notes-creator
description: Create, improve, and audit Obsidian study notes from lectures, PDFs, textbooks, and existing notes. Use for single notes or whole subject folders, worked examples, rendered mathematics, ASCII and Mermaid diagrams, and SVG figures. Preserve existing organisation when improving a vault. Triggers - create study notes, improve notes, obsidian notes, organise notes, learning notes, note from lecture, note from PDF.
---

# Obsidian Notes Creator

Make notes accurate, understandable, and useful for solving unfamiliar problems. Match depth to the learner and the requested scope; decoration and length are not evidence of quality.

## 1. Inspect and choose the mode

- **Create:** identify the source, audience, prerequisites, and learning objectives before choosing a structure.
- **Improve:** read existing notes, neighbouring notes, assets, and relevant vault instructions. Repair and deepen those files in place. Preserve filenames, folders, links, original dates, and useful author wording. Do not create a parallel study guide, rename files, or impose a new folder tree unless requested or necessary to the task.
- **Audit:** report specific gaps with file references; do not silently rewrite an audit-only request.

For a folder-wide task, inventory every Markdown file first. Track each as unreviewed, reviewed unchanged, improved, or unresolved, with a short reason. A small selection of polished notes is a targeted pass, not a completed folder review. Keep this working record outside the notes unless requested.

Defaults: answers and solutions are directly visible; SVG figures have a white background. Explicit user preferences override these defaults.

## 2. Understand before expanding

Identify missing reasoning, prerequisites, assumptions, definitions, and misleading claims. Distinguish source statements from derived examples and uncertain material. Keep source citations near the claims they support; never invent page numbers, measurements, or experimental results.

Prioritise correctness, complete worked reasoning, and useful connections. Add a visual, analogy, table, or exercise only when it teaches something the existing explanation does not.

- [Single note](references/structure/single-note.md): adaptable content modules.
- [Multi-file notes](references/structure/multi-file.md): ownership, granularity, and preservation.
- [Index notes](references/structure/index-note.md): update existing navigation when needed.

## 3. Explain and demonstrate

For unfamiliar material, connect motivation and intuition to the formal statement. Reference notes may lead with a definition; worked problems may lead with the question. No mandatory analogy or diagram quota.

- [Intuition and mathematics](references/writing/intuition-first.md): symbols, assumptions, derivations, and limits.
- [Analogies](references/writing/analogies.md): explicit mapping and where it breaks.
- [Examples](references/writing/examples.md): complete solutions, independent checks, and diagnostic questions.
- [Comparisons](references/writing/comparisons.md): method choice, guarantees, and fair evidence.

## 4. Use the appropriate representation

Choose prose, a table, ASCII, Mermaid, or SVG according to what the reader needs to see. Keep equations in rendered LaTeX. Make visuals consistent with the surrounding worked example.

- [Diagrams and SVG](references/components/diagrams.md)
- [Callouts and visible answers](references/components/callouts.md)
- [Frontmatter](references/components/frontmatter.md)
- [Wikilinks and embeds](references/components/wikilinks.md)

## 5. Verify and report honestly

Use the [verification workflow](references/verification.md) and [quality checklist](references/quality-checklist.md). Verify calculations separately from rendering. Inspect generated figures at their intended embed size. Check changed links and assets.

Report coverage, substantive improvements, checks actually run, and unresolved issues. Distinguish reviewed, executed, and rendered. Never claim exhaustive validation from samples, syntax checks, or file counts alone.
