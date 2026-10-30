# Scenario and Case Notes

Two note shapes for applied topics: system design, incident response, interviews, business cases. Each uses a fixed order, so the reader practises the same reasoning every time.

## Scenario note: "given this situation, how would you solve it?"

```markdown
# Scenario: <short name>

> [!question] The situation
> One paragraph, in the words an interviewer or manager would use.

## 1 · Clarify
| Ask | Why |            ← 3–4 questions that change the design

## 2 · Constraint
The one hard limit that shapes the answer, with a number if possible.

## 3 · Design
A flowchart or sequence diagram, then a table of parts and choices.

## 4 · Trade-off
"I'd choose X because Y. The cost is Z."  ← one quotable sentence

## 5 · Failure modes
| Risk | Guard |

## 6 · Measure
The metrics and alerts that show the design is working.

## Follow-ups
2–3 question callouts with nested answers.
```

| Rule | Why |
|---|---|
| Clarify before designing | most bad answers solve the wrong problem |
| Estimates show their arithmetic and tags | "8 Gb/s (own calculation, sizes assumed)" can be checked |
| The trade-off names a cost | an option with no cost hasn't been thought through |
| Link to related scenarios and real cases | the reader learns the pattern, not one answer |

## Case note: a real event, cause to lesson

```markdown
# Case: <event and year>

> [!abstract] In a nutshell
> Date, what happened, the scale (tagged "reported").

## Cause → effect chain
A flowchart from root cause to outcome. One arrow = one mechanism.

| What broke | Why | Fix in my design |

## Lesson for <reader's context>
How the same failure shape appears in the reader's own system.

## Q&A
2–3 question callouts, including "what single check would have caught it?"

## Sources
Primary sources first. Note where reports disagree (times, figures).
```

Keep cases factual: say "a study found" for unconfirmed claims, and never state a motive as fact.
