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

## Small reusable example

For the illustrative equation $2x+3=11$, subtracting $3$ gives $2x=8$, hence $x=4$. Substitution gives $2(4)+3=11$. A variation $2x+3=12$ changes the answer to $4.5$; integer answers were not an assumption of the method.

Use exact values where practical and round only the final presentation. Label numerical approximations.

## Questions that reveal understanding

- Which assumption permits this step?
- What changes if one input, boundary condition, or query mode changes?
- Where is the first invalid step in this attempted solution?
- Which method applies here, and why does the alternative fail?
- How can you independently check this answer?

For core methods, include a normal case and a relevant boundary or failure case. For programs, examine actual outputs, ordering, multiplicity, termination, and applicable input modes; do not erase duplicate answers before checking whether they matter.

Answers are visible by default:

```markdown
> [!question] Does a small residual guarantee small solution error?

**Answer:** Only with suitable conditioning information; explain or demonstrate the relevant bound.
```

Use collapsed solutions only when the user explicitly requests hidden-answer practice. Keep the substantive explanation beside its concept rather than moving it into an unrequested study guide.
