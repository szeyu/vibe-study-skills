# Verification Workflow

Use existing vault tooling first. Keep temporary reports and extracted render inputs outside the notes. Do not add a parser, test framework, or dependencies merely to audit a Markdown folder.

## 1. Inventory and inspect

List all in-scope Markdown files and referenced assets. Read each note for a comprehensive review; keyword hits and file counts are insufficient. Track coverage and unresolved issues. Record existing problems separately from regressions introduced by the edit.

## 2. Structural checks

Check frontmatter, closed code fences, display-math delimiters, wikilinks, regular Markdown links, heading/block references, and embeds. Respect fenced examples, aliases, escaped characters, relative paths, duplicate basenames, and same-note anchors. A regular-expression search can flag candidates but cannot prove Markdown or mathematics correct.

Inspect changed headings for incoming anchor links. Parse generated SVGs as XML. For example, with actual asset paths:

```python
from pathlib import Path
from xml.etree import ElementTree

for path in changed_svg_paths:
    root = ElementTree.parse(Path(path)).getroot()
    assert root.tag == "{http://www.w3.org/2000/svg}svg", path
```

This checks XML structure only, not appearance or semantic accuracy.

## 3. Mathematics and program behaviour

Recompute changed numeric examples with a small runnable check. Prefer exact fractions or symbolic evaluation when appropriate; otherwise use justified tolerances. Check bounds, units, signs, boundary cases, and stated guarantees. Compare against an independent result rather than repeating the same unchecked expression.

For an illustrative worked solution to $2x+3=11$:

```python
from fractions import Fraction

x = Fraction(11 - 3, 2)
assert x == 4
assert 2 * x + 3 == 11
```

Adapt checks to the actual note: evaluate a claimed root in the original equation, integrate the specified membership function, or check that a plotted critical point lies on its curve. A residual is not an error bound without conditioning information.

Run executable examples with the relevant runtime when available. Test meaningful input modes and failure cases. Report “reviewed, not executed” if a runtime is unavailable; do not imply that pseudocode inspection was execution.

## 4. Render checks

- **LaTeX:** use the target Obsidian renderer when available. An installed compatible math renderer can flag syntax errors, but distinguish that from target-app validation and mathematical proof. Do not silently suppress unsupported-command errors.
- **Mermaid:** render changed blocks with an available renderer and inspect the outputs. Keep an input-to-note mapping so failures can be fixed at their source. Report whether all blocks or only a sample were checked.
- **SVG:** render and inspect each changed figure at its intended embed size. Confirm labels, contrast, clipping, arrows, axes, and plotted values. XML parsing alone is insufficient.

Use portable tool discovery and existing dependencies. Do not bake one machine's runtime paths into a reusable workflow. When a required tool is unavailable, use an available alternative and describe its limits; never invent a passing result.

## 5. Finish

Review the diff for accidental deletions, unsolicited reorganisation, hidden answers, duplicate explanations, and unsupported claims. Run the repository's whitespace/diff checks if available. Report reviewed/improved/unchanged/unresolved counts when useful, backed by the inventory, alongside checks actually performed.
