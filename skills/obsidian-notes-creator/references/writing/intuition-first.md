# Intuition and Formal Reasoning

For a new concept, a useful order is purpose → intuition → precise statement → worked application → limits. Adapt to the note: a formula reference can start with the formula; an exercise can start with its givens. Avoid repetitive introductory headings and forced analogies.

## Mathematics that explains

- Use `$...$` inline and `$$...$$` for display mathematics, outside code fences. Use `aligned` for connected derivation steps where supported by the vault renderer.
- Define symbols, domains, units, indexing, and conventions before they become ambiguous. Keep notation consistent across linked notes and figures.
- State assumptions next to the result: continuity, differentiability, nonzero denominators, independence, or input modes as applicable.
- Explain the non-obvious transition in a derivation. Distinguish equality, approximation, implication, and equivalence.
- Separate an algorithm's stopping rule from a guarantee about the true answer. A small residual alone need not imply small solution error.
- State what a theorem guarantees and what it does not. Provide a counterexample when it prevents a likely misconception.

For example, $-\log p$ is decreasing for $p>0$, since its derivative is $-1/p$. Minimising it maximises $p$ over the same feasible set. If $p$ is a ratio whose numerator also appears in the denominator, do not treat those quantities as independently adjustable.

Explain parameter changes under explicit conditions. Call a setting “optimal” only with an objective, domain, and supporting derivation or evidence. Otherwise describe the tradeoff.

An introductory explanation may omit technical detail temporarily, but must not contradict the formal statement that follows it.
