# Comparisons That Support Decisions

Compare methods when a learner might confuse them or needs to choose between them. Use a sentence for one distinction and a table for multiple comparable dimensions.

Useful dimensions include purpose, assumptions, inputs, output, guarantee, failure mode, and cost under a stated model. Prioritise the distinction that affects the learner's decision. Avoid unconditional checkmarks where the answer depends on conditions.

For example, bisection maintains a sign-changing bracket for a continuous function, whereas Newton iteration requires a usable derivative at each step and can fail from an unsuitable starting point. State Newton's local convergence assumptions before describing its convergence rate. “Faster” without these conditions is misleading.

When possible, apply both methods to the same problem and stopping criterion. Explain why their behaviour differs. Separate measured runtime from asymptotic work and iteration counts.

## Evidence discipline

- Cite empirical numbers with the source and relevant setup, including dataset, metric, and configuration.
- Label invented numbers as hypothetical; never present them as reported measurements.
- Do not declare a universal best parameter from one experiment.
- Draw a generalisation arrow only when the claimed inclusion is valid under stated constraints. Related methods need not form a hierarchy.
- Summarise the practical decision if the table alone does not make it clear; avoid repeating every cell in prose.
