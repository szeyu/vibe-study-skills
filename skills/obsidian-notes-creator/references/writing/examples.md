# Examples and Diagnostic Practice

Choose examples around the learning objective. A brief illustration can clarify a definition; a worked problem needs enough detail to reproduce its answer. Do not impose a line limit on reasoning.

## Complete worked example

Include:

1. **Givens and goal:** all data, rules, initial values, units, and requested output.
2. **Assumptions:** distinguish supplied facts from explicitly chosen illustrative values.
3. **Method and applicability:** why this method applies and which conditions it needs.
4. **Steps:** substitutions, intermediate results, and explanations at difficult transitions.
5. **Result and interpretation:** precision, units, and what the answer means.
6. **Independent check:** substitution, a residual with its limitations, bounds, an alternative calculation, or an executable assertion.

Do not give a numeric fuzzy-system output without the rule base, membership functions, operators, and defuzzification convention needed to obtain it. Do not present an invented completion of a lecture problem as original source material.

### Narrate the thinking

Explain why each step is taken, not only what it is: "The error went up, so the step was too big; halve the learning rate." Point out where a learner is likely to go wrong at that step. A worked example that only lists operations teaches arithmetic, not method.

## Small reusable example

For the illustrative equation $2x+3=11$, subtracting $3$ gives $2x=8$, hence $x=4$. Substitution gives $2(4)+3=11$. A variation $2x+3=12$ changes the answer to $4.5$; integer answers were not an assumption of the method.

Use exact values where practical and round only the final presentation. Label numerical approximations.

## Say where every number comes from

A reader can't tell a measured figure from a guess unless the note says so. Tag numbers that aren't plain definitions:

| Tag | Use for | Example |
|---|---|---|
| (reported) | taken from a cited source | "~3 h halt (reported)" |
| (own calculation) | derived in the note or by code | "8 Gb/s (own calculation)" |
| (assumed) | an illustrative input chosen for the example | "200-byte messages (assumed)" |

When a number comes from code, run the code and paste its actual output. Never write the output you expect. A short "Check the numbers in code" block under a worked example lets the reader re-run it.

**When to add code.** Not every note needs code. Add it only when the reader gains something from running or changing it: real data to fetch, a calculation too long to do by hand, or a simulation. Concept notes (history, schools of thought, definitions, case studies) are better served by tables, worked numbers by hand, and diagrams. A "Work it by hand" table never needs code behind it. One firm exception: if the note quotes data you fetched (FRED, World Bank, an exchange API), include the code that fetches it and its real output, so the reader can rerun it.

**Code layout.** When a note does have code, lay out every runnable block in three parts so a reader can see what it does at a glance:

```python
import pandas as pd

# --- Constants ---
FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={}"
SERIES = "UNRATE"  # US unemployment rate, %


# --- Functions ---
def fred(series_id):
    """Download one FRED series, indexed by date."""
    url = FRED_CSV.format(series_id)
    return pd.read_csv(url, index_col=0, parse_dates=True)[series_id]


# --- Run ---
print(fred(SERIES).tail(3))
```

- Constants first: series IDs, URLs, windows, thresholds. No magic numbers in the run section.
- Small functions, each with a one-line docstring.
- Keep lines under about 80 characters: break long calls and f-strings over several lines.
- A tiny toy block (under ~10 lines) can skip the banners.
- In a multi-block note, define helpers once in the first block and start later blocks with `# Uses fred() from Step 2.`
- When refactoring existing code, run old and new and require identical output; keep the pasted output.
- Watch for gaps in data: dropping a missing month before `shift(12)` silently compares with 13 months ago.

**Code a reader can rerun.** The code is the source of truth, so it must give any reader the same result:

- Before the first code block, give a copyable run command that installs every library the code needs, e.g. `uv run --with <lib> --with <lib> python <note-name>.py`. If the note has several blocks, say to save them in order into one file.
- Fetch straight from the original source. No local caches, saved snapshots or machine-specific paths.
- Downloads have a timeout and fail with a plain message, not a traceback.
- Keep missing data visible: align by date rather than row position, and say "n/a" when a value is missing instead of printing NaN or silently skipping it.
- Data that keeps updating gets a fixed end date, so a rerun matches the pasted output.
- Keys and passwords come from environment variables, never written into the note.
- Label pasted output with its run date.

Currency in prose: Obsidian reads `$` as the start of maths. Write `\$40` or use the unit name (`USD 40`, `RM 5`); keep `$...$` for LaTeX only.

## Questions that reveal understanding

- Which assumption permits this step?
- What changes if one input, boundary condition, or query mode changes?
- Where is the first invalid step in this attempted solution?
- Which method applies here, and why does the alternative fail?
- How can you independently check this answer?

Prefer questions that make the reader think over recall questions: predict-then-check, spot the first wrong step, read notation aloud, change one input, or choose between two methods. Order practice from easy to hard. See [teaching style](teaching-style.md#12-practice-that-makes-the-reader-think).

For core methods, include a normal case and a relevant boundary or failure case. For programs, examine actual outputs, ordering, multiplicity, termination, and applicable input modes; do not erase duplicate answers before checking whether they matter.

Answers are visible by default:

```markdown
> [!question] Q1 · Does a small residual guarantee small solution error?
>
> > [!success] Answer
> > Only with suitable conditioning information; explain or demonstrate the relevant bound.
```

Keep each answer to about three short sentences. A longer answer usually means the question should be split, or the explanation belongs in the note body.

Use collapsed solutions only when the user explicitly requests hidden-answer practice. Keep the substantive explanation beside its concept rather than moving it into an unrequested study guide.
