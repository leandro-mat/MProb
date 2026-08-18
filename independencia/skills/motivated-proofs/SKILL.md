---
name: motivated-proofs
description: Use when the user asks you to write, rewrite, or revise mathematical proofs, paper drafts, lecture notes, or any mathematical exposition to be "motivated." Also use when the user asks you to diagnose why a proof feels unmotivated, puzzling, or contains "rabbit-out-of-a-hat" steps. Covers role motivation (what each step DOES), insight motivation (where each step CAME FROM), context-sensitivity, cognitive-load management, and the eight actionable strategy families for producing motivated mathematical writing. Do NOT use for non-mathematical prose or for proofs that only need logical verification without expositional improvement.
---

# Motivated Proofs: Writing Skill

Based on Rebecca Lea Morris, "Motivated proofs: What they are, why they
matter and how to write them," *The Review of Symbolic Logic* 13 (2020)
23--46.

## 1. Core Definition

A proof is **motivated** relative to a context *C* iff every step is both:

1. **Role-motivated** — a typical finite reader with access to *C* can
   identify the *task(s) each step is intended to perform* (what does this
   step *do*?).
2. **Insight-motivated** — a typical finite reader with access to *C* can
   identify *where each step could have reasonably come from* (why *this*
   step? how could a human have discovered it?).

A motivated proof contains **no "puzzling" steps**. Two distinct kinds of
puzzle are ruled out:

| Puzzle type | Reader's question | Violated condition |
|---|---|---|
| "What is this step *doing*?" | I see that it works, but what is its purpose? | Role motivation |
| "How could anyone *think* of this?" | The step is correct but feels like magic. | Insight motivation |

Motivation is **context-relative** — the same proof can be motivated for
an expert audience and unmotivated for an intermediate audience, depending
on what resources each context contains.

---

## 2. Theoretical Framework

### 2.1 Context

A context *C* is a mathematical "toolkit" containing:

- **Definitions, theorems, proofs** (standard mathematical knowledge)
- **Techniques** — precise, reusable approaches (completing the square,
  induction, double counting, rescaling variables, diagonalization)
- **Heuristics** — guidance about *how to try* solving problems (Steele's
  heuristic: "apply inequalities where they are nearly sharp"; "try a
  special case and reduce the general case to it"; "work backwards from
  the goal")

Each resource has a **range of application**:

| Range | Meaning |
|---|---|
| **Narrow** | Can only be reliably applied in very explicitly familiar settings |
| **Medium** | Can be applied in mildly non-standard settings, but not very unusual ones |
| **Wide** | Can be reliably applied even in new, non-standard, or highly unusual circumstances |

**Example**: A reader who knows "the min of *ax² + bx + c* is at *−b/2a*"
with medium range will NOT recognize this when the quadratic is written
as ⟨y,y⟩ − 2α⟨x,y⟩ + α²⟨x,x⟩ (variable named α, coefficients reversed,
coefficients expressed as inner products and written to the right). The
proof writer must explicitly point out "this is a quadratic in α" to
bring the expression within the resource's range.

### 2.2 Finite Agent Assumption

The reader is a **finite mathematical agent** with limited cognitive
resources. Even if all the right resources are in her context with wide
enough range, she may still fail to make connections if:

- The chain of reasoning needed is too long (many connections required)
- Individual connections are too difficult (cognitively expensive)
- The proof is poorly organized or cluttered with irrelevant information
  (raising the cost of *every* connection)

**Key principle**: The proof writer's job is to **minimize the cognitive
cost** of making the connections between the proof and the reader's
context.

---

## 3. The Eight Strategy Families

When writing or rewriting a proof to be motivated, deploy strategies from
these eight families. For every step in the proof, ask: (1) what is its
intended task? (2) where could it have reasonably come from? Then make
those answers visible to the reader.

### Strategy 1: Make Hidden Structure Explicit

Many steps become puzzling because their mathematical nature is obscured
by notation, ordering, or non-standard presentation.

**What to do**: Insert brief remarks that name the structure.

- "This is a quadratic in α."
- "The expression inside the sum is a telescoping series."
- "We are looking at a fixed-point equation."
- "The right-hand side factors as (x−y)(x+y)."

**Example** (Cauchy-Schwarz): The expression
⟨y,y⟩ − 2α⟨x,y⟩ + α²⟨x,x⟩ has its quadratic nature obscured by
non-standard variable name, reversed term order, and inner-product
coefficients written on the right. Adding "Notice that
⟨y,y⟩ − 2α⟨x,y⟩ + α²⟨x,x⟩ is a quadratic in α" brings it within range
of the reader's algebraic resources.

### Strategy 2: Supply Missing Heuristics

Often the insight behind a step is a *heuristic* that the target audience
lacks. The proof feels unmotivated because the reader cannot reconstruct
the reasoning that led to the step.

**What to do**: Explicitly state the heuristic and show how it applies.

- "To extract the most information from this inequality, we should apply
  it where it is as sharp as possible."
- "When stuck, try proving a special case first, then reduce the general
  case to it."
- "We work backwards: to prove P, it suffices to prove Q, and Q is easier
  because..."
- "Symmetry suggests trying..."

**Heuristic catalog** (include these explicitly when relevant):

| Heuristic | When to use |
|---|---|
| Steele's heuristic | Any inequality proof: apply inequalities where they are (nearly) sharp |
| Special-case reduction | Complex theorems: prove a special case, then reduce |
| Work backwards | Goal is clear but path isn't: start from conclusion |
| Symmetry exploitation | Problem has symmetric structure |
| "Fudge factor" / auxiliary sequence | Direct application of an inequality fails because terms are too unequal |
| Wishful thinking | Assume the hardest sub-problem is solved, then solve it later |
| Generalization | Prove a stronger statement that is easier to prove |

### Strategy 3: Provide Rational Reconstructions (Discovery Narratives)

For the hardest steps, the insight requires a chain of reasoning that is
too long or too subtle for a typical reader to reconstruct unaided.

**What to do**: Precede the formal proof with a sketch of how it could
have been discovered, OR interleave discovery reasoning with the formal
steps.

**Template for a discovery narrative**:

> "Let's see how one might discover this proof. A natural first attempt
> would be to [naive approach]. This fails because [reason]. The failure
> suggests that we need to [diagnosis]. One way to fix this is to
> [strategy], which leads us to introduce [key construction]."

**Example** (Carleman's inequality): Show that the naive application of
AM-GM to the aᵢ gives a divergent sum → diagnose that the terms are too
unequal → Steele's heuristic says apply inequalities where sharp → AM-GM
is sharp when terms are equal → introduce auxiliary sequence cᵢ to make
terms more equal. Then the cᵢ sequence is *motivated* rather than
"popping up from nowhere."

### Strategy 4: Show Failed Attempts

A step is often motivated by seeing what happens *without* it.

**What to do**: Briefly sketch the naive or "obvious" approach, show why
it fails, then introduce the actual step as the fix.

- "If we try to apply [Theorem X] directly, we get [dead end]. This
  happens because [reason]. To fix this, we first [step]."
- "A natural guess would be [guess], but this fails when [condition].
  This suggests we need to handle [condition] separately, leading to..."

**Why this works**: It reveals *both* the role (the step fixes a specific
problem) *and* the insight (the step comes from diagnosing that problem).

### Strategy 5: Modularize — Lemmas and Proof Sketches

Information management at the **global** level.

**What to do**:

- Break long proofs into named lemmas. Each lemma has a clear purpose
  stated in its name or a one-line summary.
- For complex proofs, provide a brief **proof sketch** or **roadmap**
  before the formal argument.
- Within a proof, use **signposting**: "We now establish Claim 1," "It
  remains to show that...," "The proof proceeds in three stages."

**Why this works**: When a reader encounters step S inside "Proof of
Lemma L," the lemma's stated purpose narrows the search space for
connections. She doesn't need to consider *all* possible roles for S, only
those relevant to L's goal. This reduces cognitive cost.

### Strategy 6: Hide Irrelevant Information (Local Information Management)

**What to do**: Do not introduce notation, variables, coefficients, or
expansions until the moment they are needed. Use compact notation to
suppress detail when it is not relevant.

**Example** (Wilson's Theorem — Lagrange's proof):

| Bad (too much info too early) | Good (info hidden until needed) |
|---|---|
| (x+1)...(x+p−1) = x^{p−1}+A₁x^{p−2}+...+A_{p−1} | Let L(x) = (x+1)(x+2)...(x+p−1) |
| (x+2)...(x+p) = (x+1)^{p−1}+A₁(x+1)^{p−2}+... | L(x+1) = (x+2)(x+3)...(x+p) |
| (x+p)(x^{p−1}+A₁x^{p−2}+...)= (x+1)^p + A₁(x+1)^{p−1}+... | (x+p)L(x) = (x+1)L(x+1) |

The second version hides the coefficients Aᵢ until they are actually
needed, making the algebraic manipulation much easier to parse.

**Checklist**: Before introducing any symbol or expansion, ask "Does the
reader need this right now to follow the argument?" If not, postpone it.

### Strategy 7: Signal Roles Proactively

For every non-obvious step, explicitly state its role *before* or *as* it
is introduced.

**What to do**: Use role-signaling phrases:

- "To bound this term, we introduce..."
- "The key is to rewrite the sum as..."
- "In order to apply Theorem X, we first need to put the hypothesis in
  the form..."
- "We want to show that [expression] is minimized when [value]. To find
  the minimizer, observe that [expression] is a quadratic in..."
- "The following choice of [parameter] makes the inequality sharp:..."

### Strategy 8: Compensate for Narrow Resource Ranges

When a required resource is in the context but has only narrow/medium
range, the proof writer must actively bridge the gap.

**What to do**: Make the connection between the proof step and the
resource explicit.

- If the resource is "completing the square" but the quadratic looks
  unusual → show the completing-the-square computation inline.
- If the resource is "telescoping series" but the pattern is obscured →
  write out the first few terms and show the cancellation.
- If the resource is "min of quadratic at −b/2a" but coefficients look
  strange → explicitly identify a, b, c in the current expression.

---

## 4. Diagnostic Protocol: Is This Proof Motivated?

For each step *S* in the proof, run this checklist **relative to the
intended audience's context C**:

### Step 4.1: Role Motivation Check

> Can a typical finite reader with access to C identify what task(s) *S*
> is intended to perform?

- If YES → role-motivated.
- If NO → diagnose *why*:
  - Missing resource? (e.g., reader doesn't know that this expression can
    be minimized)
  - Resource present but range too narrow? (e.g., reader knows about
    quadratics but doesn't recognize this as one)
  - Too many connections required? (role only clear after a long chain of
    reasoning)

### Step 4.2: Insight Motivation Check

> Can a typical finite reader with access to C identify where *S* could
> have reasonably come from?

- If YES → insight-motivated.
- If NO → diagnose *why*:
  - Missing heuristic? (e.g., reader doesn't know that applying
    inequalities where sharp is a good strategy)
  - Heuristic present but inapplicable? (e.g., preliminary reasoning
    looks like a dead end)
  - Chain of discovery reasoning too long/unguided? (too many inferential
    steps without prompts)

### Step 4.3: Cognitive Cost Check

Even if all resources are present with wide range, is the cognitive cost
of making the connections too high?

- Are there too many symbols defined at once?
- Is the structure of the proof unclear (no lemma boundaries, no
  signposting)?
- Are individual steps requiring very effortful algebraic manipulations
  to parse?

---

## 5. Rewriting Protocol: Making an Unmotivated Proof Motivated

Given an unmotivated proof P and a target context C:

### Phase 1: Analyze

For each puzzling step, classify the deficiency:

| Deficiency | Primary fix (see §3) |
|---|---|
| Step's role is unclear | Strategy 1 (make structure explicit) or Strategy 7 (signal roles) |
| Step's origin is mysterious | Strategy 2 (supply heuristic), Strategy 3 (discovery narrative), or Strategy 4 (show failed attempt) |
| Reader lacks a key heuristic | Strategy 2 (supply missing heuristic explicitly) |
| Key resource has too narrow range | Strategy 8 (bridge the gap: show the connection explicitly) |
| Chain of reasoning too long | Strategy 3 (discovery narrative) or Strategy 5 (modularize) |
| Proof is cluttered / hard to parse | Strategy 6 (hide irrelevant info), Strategy 5 (modularize) |

### Phase 2: Apply Fixes

Apply the strategies. Order them from least to most invasive:

1. **Minimal fix**: Add a one-line comment naming hidden structure
   (Strategy 1) or signaling a role (Strategy 7).
2. **Small fix**: Add a sentence supplying a missing heuristic (Strategy 2)
   or bridging a narrow resource range (Strategy 8).
3. **Moderate fix**: Add a brief sketch of a failed attempt (Strategy 4)
   or restructure notation to hide clutter (Strategy 6).
4. **Major fix**: Add a discovery narrative (Strategy 3) or break out
   lemmas / add a proof sketch (Strategy 5).

### Phase 3: Verify

After rewriting, re-run the diagnostic protocol (§4) on the new version.
A proof is fully motivated relative to C only if *every* step passes both
the role and insight motivation checks.

---

## 6. Prompt Templates

When asked to rewrite a proof, structure your response accordingly.

### Template A: Quick Fix (One Puzzling Step)

> The step [describe step] fails to be [role/insight] motivated relative
> to [context description] because [reason]. To fix it, [apply specific
> strategy]. Here is the revised passage: [revised text].

### Template B: Full Proof Rewrite

1. **State the target context** explicitly: "I'll rewrite this proof
   assuming the reader has access to [resources] with [narrow/medium/wide]
   range, and is familiar with [heuristics]."
2. **Present the proof**, incorporating strategies 1–8 as needed.
3. **Annotate key motivations** inline or as margin notes — but only when
   the motivation is non-obvious. Routine algebraic steps do not need
   annotation.

### Template C: Discovery Narrative

> Here is one way this proof could have been discovered:
>
> [Step 1: Naive attempt]
> [Step 2: Diagnosis of failure]
> [Step 3: Strategy to fix]
> [Step 4: Derivation of key construction]
> [Step 5: The formal proof follows naturally from this reasoning.]

---

## 7. Examples of Good Motivated Writing

### Example 1: Cauchy-Schwarz — Choice of α (from §4 of paper)

**Unmotivated version**:
> Now let α := ⟨x,y⟩/⟨x,x⟩. Substituting this in the above yields...

**Motivated version** (Strategies 1, 2, 7):
> To get the most information out of this inequality, we should apply it
> where it is as sharp as possible. Notice that
> ⟨y,y⟩ − 2α⟨x,y⟩ + α²⟨x,x⟩ is a quadratic in α. To make the inequality
> as sharp as possible, we should apply it where this quadratic takes its
> minimum value. The minimum of a quadratic occurs at −b/2a, which here
> gives α = ⟨x,y⟩/⟨x,x⟩. Substituting this back...

### Example 2: Carleman's Inequality — The cᵢ sequence (from §2 of paper)

**Role**: The cᵢ sequence makes the terms to which AM-GM is applied more
nearly equal, so that AM-GM is applied where it is nearly sharp.

**Insight**: Direct application of AM-GM fails (gives divergent series)
because the aᵢ terms are too unequal. Steele's heuristic says apply
inequalities where sharp; AM-GM is sharp when terms are equal; hence
introduce an auxiliary "fudge factor" sequence.

A motivated exposition would *tell the reader all of this* before (or as)
the cᵢ sequence is introduced.

### Example 3: General AGM Inequality — Rescaling (from §5 of paper)

**Role**: The rescaling αₖ = aₖ/A ensures Σ pₖαₖ = 1, reducing to the
special case A = 1.

**Insight**: Apply the bound eˣ⁻¹ to both aₖ and A to get a double bound
max{A,G} ≤ e^{A−1}. This proves the inequality for the special case A = 1.
Now reduce the general case to this special case by rescaling.

A motivated exposition would include the discovery narrative showing how
the double bound emerges and how it reveals the special case.

---

## 8. Relation to Other Virtues

When applicable, note these connections (they can strengthen the
exposition):

- **Beauty** (Cellucci): A proof is beautiful when it provides
  understanding, defined as "recognition of the fitness of the parts to
  each other and to the whole." Motivated proofs deliver exactly this —
  the reader grasps how each part fits.
- **Fit / Transparency** (Raman-Sundström & Öhman): A transparent proof
  is one where "it is easy to see what is going on" with no *deus ex
  machina*. Motivated proofs are transparent by construction.
- **Explanation**: Motivated proofs are not necessarily explanatory in
  Steiner's or Kitcher's sense, but they *do* promote understanding and
  reuse of resources.

---

## 9. Edge Cases and Caveats

- **Not every proof can be fully motivated** for every context. Some
  proofs require resources simply not available in a given context. In
  such cases, note what additional resources would be needed.
- **Over-motivating is possible**. Do not annotate routine algebraic
  manipulations, simple substitutions, or standard logical inferences.
  Motivation is for *non-obvious* steps.
- **Multiple discovery paths** may explain the same step. It suffices to
  present *one* reasonable path; it need not be historically accurate.
  What matters is that the reader can see *a* path.
- **Partial motivation is valuable**. Even if not every step can be made
  both role- and insight-motivated, improving *some* steps still yields
  epistemic benefits.
- **The context must be chosen**. Always decide (or ask the user) what
  the target audience's context is before rewriting. A proof motivated
  for graduate students may look very different from one motivated for
  advanced undergraduates.

---

## 10. Quick Reference Card

| Problem | Signal phrase | Strategy |
|---|---|---|
| Hidden structure | "Notice that X is a Y (quadratic, telescoping sum, fixed point...)" | S1 |
| Missing heuristic | "A useful heuristic: [heuristic]. Here's how it applies..." | S2 |
| Mysterious construction | "Let's see how one might discover this..." | S3 |
| Unexplained choice | "If we try the naive approach [X], it fails because [Y]. This suggests..." | S4 |
| Proof is a wall of text | Break into lemmas; add "The proof proceeds in three stages." | S5 |
| Too many symbols too soon | Use abbreviations; postpone expansion of coefficients | S6 |
| Step's purpose unclear | "To bound this term, we..." / "The key is to..." | S7 |
| Resource range too narrow | "Recall that [resource]. In our case, a = ..., b = ..., c = ..." | S8 |

---

## Codex Integration

When applying this skill in Codex:

1. Determine the target audience and mathematical context from the user's request and the surrounding file. State a reasonable assumption when the audience is not explicit.
2. Inspect enough surrounding material to preserve notation, terminology, level, and the author's existing voice.
3. Distinguish a request for diagnosis from a request for implementation. Review-only requests should produce analysis and suggested text without editing files.
4. For requested local edits, modify only the relevant scope, preserve unrelated user changes, and use the normal patch-based editing workflow.
5. For LaTeX or other compilable documents, run an appropriate validation when practical. Separate errors introduced by the change from pre-existing warnings or path/toolchain problems.
6. Match the language of the manuscript and explain the pedagogical choices at the user's level.
7. Report the edited file and location, the strategies applied, and any validation result.


