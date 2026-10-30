# Teaching Style: Notes a Beginner Can Follow

A correct note can still be unreadable. This guide is about the reader's experience: how quickly they grasp the idea, whether they can follow each step, and whether they can use it afterwards. Apply it together with the rigour guides; when they pull in different directions, keep the content correct but move the fine print later rather than into the main explanation.

## 1. Know the reader first

Before writing, decide in one or two sentences who the reader is and what they already know. For example: "second-year student, comfortable with Python and high-school algebra, new to probability notation." Then build every explanation on that. Ask the user when it is unclear and it changes the writing.

- Reuse what they know as a bridge (Section 6).
- Define anything beyond that level the first time it appears.
- Pitch depth to the reader, not to the source. A textbook written for experts needs translating, not copying.

## 2. Write plainly

| Rule | Instead of | Write |
|---|---|---|
| One idea per sentence | "The kernel, which is learned during training and shared across positions, produces a feature map whose size depends on stride and padding." | "The kernel is a small grid of weights. It slides across the image. The same kernel is used at every position." |
| Define on first use | "Apply the defuzzification step." | "Defuzzification turns a fuzzy answer ('fairly hot') back into one number (31 °C)." |
| Plain verbs over stacked nouns | "Gradient magnitude attenuation occurs" | "The gradient gets smaller" |
| Example right after each claim | "Stemming may conflate distinct words." | "Stemming may merge different words: *university* and *universe* both become *univers*." |
| Bold a key term once, where it is defined | bolding every mention | **Learning rate** once, plain afterwards |

Flag for rewriting: sentences over about 25 words, three or more technical terms in one sentence, and paragraphs with no example. Aim for at most three short sentences per paragraph and per Q&A answer; when it runs longer, split it or turn the parallel parts into a table.

## 3. Concrete before abstract

Show two or three specific cases with real numbers. Let the reader notice what they share. Then name the pattern and give the general rule.

> Bisection on $f(x)=x^2-2$ over $[1,2]$: midpoint $1.5$, $f(1.5)=0.25>0$, so keep $[1,1.5]$. Midpoint $1.25$, $f(1.25)=-0.44<0$, so keep $[1.25,1.5]$. *Pattern:* keep the half where the sign changes. *Rule:* if $f(a)f(m)<0$ keep $[a,m]$, else keep $[m,b]$.

A formula met after the examples reads as a summary. Met first, it reads as a wall.

## 4. Build it before the shortcut

When a tool hides work (a library call, a closed-form formula, a named algorithm), let the reader do the work once by hand, then show the shortcut.

- Convolution on a 3×3 grid by hand → then `conv2d`.
- TF-IDF on three short sentences → then `TfidfVectorizer`.
- Summing a series term by term → then the closed form.

Afterwards the shortcut feels like a convenience, not magic. The reader can also check it.

## 5. Teach the reader to read the notation

Students often understand the idea but cannot read the symbols. Give a symbol decoder: the symbol, how to say it aloud, what it means, and a tiny example.

| Symbol | Say it | Means | Example |
|---|---|---|---|
| $\sum_{i=1}^{n} w_i x_i$ | "add up, for each $i$, weight times input" | weighted sum | $w=(2,1),\ x=(3,4) \Rightarrow 2\cdot3+1\cdot4=10$ |
| $\mu_A(x)$ | "membership of $x$ in $A$" | how much $x$ belongs to fuzzy set $A$, from 0 to 1 | $\mu_{\text{hot}}(31)=0.7$ |
| $\arg\max_c P(c\mid d)$ | "the class $c$ that makes the probability largest" | pick the best label | the label with the highest score wins |

Add "read it aloud" exercises: give a line of notation or code, and ask the reader to say it in plain words. Show the answer.

## 6. Bridge from what they know, and say where it breaks

Put the new thing next to something familiar: a language they already use, an earlier course, or everyday maths. Then state the difference explicitly, because a bridge with an unmarked gap is worse than no bridge.

| Familiar | New | Where it differs |
|---|---|---|
| Python `list` | NumPy array | One type per array; `+` adds element by element instead of joining lists |
| Classical set: in or out | Fuzzy set | Membership is a degree between 0 and 1, so "partly in" is allowed |
| Grading a test by counting wrong answers | Cross-entropy loss | Confident wrong answers cost far more than unsure ones |

A format that works well: **"Habit you already have → what happens here → the right way here."**

## 7. Make mistakes a first-class part of the note

Readers learn as much from what goes wrong as from what goes right. Every core note should have:

- **"You might think X — actually Y"** pairs for the most likely misconceptions.
- A **Common mistakes** table: mistake, what happens, fix.
- **Edge cases and limits**: what the method cannot do, inputs that break it, what it is *not* allowed to do.

| Mistake | What happens | Fix |
|---|---|---|
| Normalise test data with its own mean | Test scores look better than reality | Use the training mean and standard deviation |
| Forget to reset the gradient each step | Updates grow and training diverges | Zero the gradient before each backward pass |

## 8. Give every note the same shape

A predictable layout lets the reader spend effort on the content, not on finding their way around. A good default order:

1. **Before you read**: a folded table of the terms the note assumes, linked to where they are taught.
2. **In a nutshell**: one bold sentence, a small table of key results with real numbers, one closing sentence.
3. **Why it exists**: the problem it solves, ideally a failure of the naive approach.
4. **Core idea**: concrete case first, then the general statement.
5. **Work it by hand**: one real number walked through the arithmetic in a table, before any code (Section 10).
6. **Common mistakes**: a table, or one `[!caution] Common mistake` callout after the worked table.
7. **Check yourself**: questions with visible answers.
8. **Going deeper**: caveats, proofs, edge conditions, links onward.

Adapt the order for reference notes and exercise collections, but keep it the same across notes of the same kind.

## 9. Layer the depth

Not every reader needs every caveat on first read. Put the main path first and the fine print last.

- The main explanation covers the normal case cleanly.
- Conditions that **change the answer** in normal use stay in the main text.
- Rare edge conditions, proofs, historical notes and implementation subtleties go to **Going deeper**.

The simplified first pass must never contradict the precise version that follows.

**Split by number of new ideas, not by line count.** If a note introduces more than about three new concepts that each need their own example (for example precision, recall *and* F1, *and* ROC curves), give each a clearly separated part or its own note.

## 10. Narrate the thinking in worked examples

Show *why* each step is taken, not only *what* it is. The reader needs the decision, not just the arithmetic.

> **Step 2.** The error went *up* after this update, so the step was too big. → Halve the learning rate to 0.05 and try again.

Useful narration cues: "We do this because…", "Notice that…", "A common wrong move here is…", "Check: does this make sense? …".

## 11. Give each visual one job

- Draw only for the hardest idea in the note, or where a picture beats a paragraph (structure, flow, before/after).
- Use the **same values** as the worked example next to it, so the reader can cross-check.
- Add one sentence below it: "Notice that…".
- Prefer one clear figure to three decorative ones.

## 12. Practice that makes the reader think

Format every question the same way: a question callout with a nested green answer callout, never folded (see [callouts](../components/callouts.md)).

Recall questions ("What is X?") test memory. Better types:

| Type | Example |
|---|---|
| Predict, then check | "Before running: will accuracy go up or down if we remove the stop words? Why?" |
| Spot the bug | Give a short wrong solution; ask for the first wrong step. |
| Read it aloud | Translate notation or code into plain words. |
| Change one thing | "What changes if the threshold moves from 0.5 to 0.8?" |
| Choose the method | "Which of these two methods fits this problem, and why not the other?" |

Order the questions from easy to hard. Answers stay visible unless the user asks for hidden practice.

## 13. Give a folder a guided path

A pile of good notes is not yet a course. The index should open with a **Start here** table: the notes in reading order, each with "after this you will be able to…". Navigation lines (previous / next) inside each note should follow the same order. Number files in reading order when a sequence matters, and keep the numbering in step with the path.

## 14. Lay out the page so the eye can find things

Correct, plain sentences can still look messy on the page. The most common problem is cramming: one bullet holding a bold label, an explanation, inline code, a result and a link.

| Messy | Clean |
|---|---|
| `- **Infinite lists.** take 5 [1..] gives [1,2,3,4,5]; only what you ask for is computed. See [[Laziness]].` | A table row: Feature \| Example → result \| Python equivalent \| Learn more |
| Runs of `**Plain English:** …` / `**The fix:** …` paragraphs | The same small structure every time: code block, a one-line "What it means" callout, a "The fix" callout with code |
| A wall of bold bullets under "Going deeper" | A table (Topic \| In short \| Learn more) or short `###` sub-headings |
| One paragraph listing parallel ideas ("A recipe is…, a spreadsheet is…, a detective is…") | A table or a bullet per idea, so each can be compared at a glance |
| An "In a nutshell" box written as one dense paragraph | One bold sentence, then a small Measure/Result table (or 2–4 short bullets), then one closing sentence |

Rules:

- When items share the same parts, use a **table**; keep cells short (at most two lines with `<br>`).
- **One idea per bullet.** Put code and its result on their own line: `expr` → `result`, or a code block for definitions.
- **Links go last** — end of the item, a "Learn more" column, or the Related section — never mid-explanation.
- **Paragraphs of three or four short sentences** at most; numbered lists for steps.
- **Repeated sections look identical.** If a note has five "mistake" entries, each uses the same layout.
- **Bold** only the key term, never whole sentences.
- **Parallel ideas never share a paragraph.** Two or more items of the same kind (analogies, options, steps, cases) → bullets or a table.
- **Fine print stays short.** In Going deeper and other side sections, aim for about 15 words per table cell; cut background the reader does not need now.

## 15. Final pass: read it as the beginner

Before finishing, re-read each note as the reader from Section 1 and fix:

- sentences over about 25 words, or with three or more technical terms;
- any term used before it is defined;
- paragraphs with no example;
- any place where the reader must scroll back to understand;
- caveats interrupting the main explanation that could move to Going deeper;
- a missing "why should I care" in the first few lines;
- any cramped bullet or label-paragraph run that should be a table or a repeated mini-structure (Section 14).
