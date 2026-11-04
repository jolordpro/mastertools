---
name: challenger
description: >-
  An adversarial "make it exceptional, not adequate" pass over any non-trivial
  plan or deliverable — creative, written, strategic, technical, operational, or
  design work. It challenges the plan, widens the solution space with real
  research, stress-tests how the result lands on whoever meets it, probes for
  high-upside moves that bend assumed (not real) constraints, then converges to a
  sharper plan and a short list of decisions for the human. Use this skill
  whenever the user says "challenge," "pressure-test," "push this," "expand," "go
  deeper," "red-team," "raise the bar," "make this world-class/exceptional," or
  runs it on a project of any kind — and also fire it proactively, before
  committing to any foundational, hard-to-reverse, or pattern-setting decision,
  even when not asked by name. Skip it only for genuinely trivial,
  fully-specified, one-step tasks.
---

# Challenger

Take whatever plan is on the table and force it past "good enough" toward the
best version that's actually achievable. Not by being contrarian — by being
rigorous, wide, and specific. Default output is adequate. The job here is to
beat the default. This applies to any kind of work: software, design, writing,
strategy, research, operations, a document, a deck, a brand system, a video, a
decision. Translate every step below into the medium you're actually in.

## 0. Calibrate first

Match effort to stakes. Over-applying this to a one-line fix is itself a
failure mode.

- **Trivial / fully-specified / one-step** → skip the full pass. Note one
  improvement if an obvious one exists, then proceed.
- **Moderate** → run Challenge + Converge, plus Experience if anyone meets the
  result.
- **High-stakes / foundational / hard-to-reverse / sets the pattern for
  everything after** → run all five passes in full.

State the tier you picked in one line, then go.

**"Go deeper" means deeper, not bigger.** First say what a top professional in
the field would do here that the task doesn't ask for: their material, methods,
tools and outside proof. Then rewrite the task to ask for that, and run the
passes on the rewrite.

## The passes

**Steelman before you strike.** Restate the plan in its strongest form and name
what it gets right — *then* challenge it. The goal is a better outcome, not a
cleverer critique.

### 1. Challenge — interrogate the plan

- Restate the real job-to-be-done, not the stated task. What does success
  actually look like for the person who'll use, read, watch, or own this?
- List the load-bearing assumptions. Mark which are unexamined — those are the
  ones to bend later.
- Find the weakest link: what breaks first under scale, scrutiny, edge cases,
  real audiences, or six months of entropy?
- Premortem: it shipped and it underwhelmed. Write the single most likely reason.
- Ask why the obvious approach is merely adequate — or quietly wrong.

### 2. Widen — expand the solution space (with real research)

- Generate **at least 3 genuinely distinct approaches**, not three flavors of
  one. Label each. One line on what it optimizes for and what it costs.
- **Before outside prior art, check what the user already has:** their own
  parts catalog, project search, or past projects. Reusing a proven part of
  theirs usually beats the best outside example.
- **Research prior art for real — use the tools, don't vibe from memory.** Who
  does this exceptionally well right now — which people, works, products,
  organizations, or precedents? Name them. Note what to steal and what to avoid.
  Verify current practice; assume your training data may be stale on anything
  fast-moving.
- Look past the user's own examples: gold-standard comparable products,
  open-source libraries and published material such as textbooks. Use what you
  find, don't only cite it.
- Cross-pollinate: how would someone from a different field attack this?
- Run the **10x question**: what would the order-of-magnitude-better version
  look like — and which achievable 20% of it captures most of the gain?

### 3. Stress the experience — how the result lands on whoever meets it *(only if someone or something will encounter the output)*

Almost everything is encountered by someone — a user, a reader, a viewer, an
audience, a client, a teammate, the next person who has to extend it. Run this
pass against *their* experience, in this medium's own terms. Skip it only for
pure internal machinery nobody interacts with.

- **Name who meets this, and in what state** — cold, skeptical, rushed, expert,
  first-timer. Design for the real one, not an idealized one.
- **Map the primary path** — what 80% of them will do, read, or follow. Make it
  as short, clear, and direct as the medium allows. Cut every step, sentence, or
  beat that can be inferred, defaulted, merged, or removed outright.
- **Map the power/edge path** — the 20% who need more. Make it reachable without
  burdening the common path.
- **Friction audit:** mark every point where the receiver has to work, wait,
  backtrack, re-read, decide, or get confused. Each is a tax — justify it or
  kill it.
- **First impression / defaults:** the opening — first screen, first ten
  seconds, first paragraph, default state — is the single highest-leverage
  choice. Make it the right one for the typical person.
- **Progressive disclosure:** graspable and uncluttered up front; depth
  available on demand. Never make the newcomer pay the expert's complexity tax,
  and never strand the expert at the beginner's ceiling.
- **Then translate to the medium.** If it's interactive software, hold it to
  current bars: sane defaults, command palette / keyboard paths for power users,
  optimistic and instant-feeling actions, undo over "are you sure?", specific
  recoverable errors, perceived speed via streaming and skeletons, one coherent
  system over one-off styling. If it's a document, a presentation, a brand
  system, a video, a body of code — apply the same underlying principle
  (clarity, flow, the right default, depth on demand) in that medium's terms.

### 4. Break the frame — probe high-upside moves (with guardrails)

This is where exceptional separates from competent. Hunt for moves that could be
an **exponential** improvement, even if they bend a current parameter.

First, separate real constraints from assumed ones:

- **Real** (physics, security, privacy, legal, a hard dependency, the user's
  explicit non-negotiables) → respect. Do not route around these.
- **Assumed** (convention, a default setting or template, "that's how it's
  usually done," an inherited pattern, scope drawn by habit) → fair game to bend.

For each bold move, state four things:

1. The constraint you'd bend.
2. The payoff — and *why it could be exponential rather than incremental*.
3. The cost and blast radius.
4. Reversibility.

Then act by door type:

- **Two-way door** (reversible, contained): prototype it, compare against the
  baseline, keep it if it wins. Show the diff or result.
- **One-way door** (irreversible or high blast radius): **do not execute.**
  Surface it as a recommendation with the four-point framing and let the human
  decide.

A reversible bet with large upside is usually worth taking. An irreversible one
is a decision for the owner, not for you.

### 5. Converge — synthesize, don't dump

Divergent thinking without convergence is just noise.

- **Cross-part pass before "done".** Before calling the plan finished, or saying
  more passes add little, push the person's real situation through every part at
  once: scenarios that touch several parts, conflicts between their goals, clocks
  that collide, and what one part assumes about another. Any plan-changing finding
  means it isn't finished.
- Pick the strongest synthesis across all passes. Justify it in a few lines.
- Produce a **revised, concrete, sequenced plan** — specific changes, not vibes.
  Replace every vague verb with a concrete, checkable change. Not "make it
  clearer" but the actual move — "cut the opening two paragraphs and lead with
  the result," or "replace the confirmation dialog with a 5-second undo."
- Name the reference class you're aiming at, and measure the result against it.

## Output

Produce, in this order:

1. **Tier** — the calibration call, one line.
2. **Verdict** — what in the original plan holds, what's weak.
3. **Options** — the distinct approaches, labeled, each with its why-it-matters
   and the research you actually found (with sources where you looked them up).
4. **Experience** — *(if applicable)* who meets it, primary/edge paths, friction,
   the opening/default, and the depth-on-demand recommendation.
5. **Bold bets** — each with constraint / payoff / cost / reversibility /
   recommendation. Reversible ones you prototyped; one-way doors flagged, not
   executed.
6. **Revised plan** — concrete and sequenced.
7. **Decisions for you** — the calls that need the human, especially the one-way
   doors and anything that bends a stated parameter.

## Anti-patterns (do not do these)

- **Generic advice.** "Be creative / think bigger / make it pop" with no concrete
  change attached is worthless. Every recommendation names a specific move.
- **Analysis paralysis.** The pass ends with a sharper plan and a decision list,
  not an endless menu.
- **Contrarianism.** Don't challenge to look smart. Steelman first; only strike
  where it improves the outcome.
- **Silent risky bets.** Never quietly rewrite scope, structure, dependencies, or
  anything irreversible. Surface it for a human call.
- **Scope-creep on trivial work.** Respect the calibration tier. A small task
  gets a small pass.
- **Research theater.** If you describe how others solve this, you actually
  looked — not a guess dressed as a fact.
