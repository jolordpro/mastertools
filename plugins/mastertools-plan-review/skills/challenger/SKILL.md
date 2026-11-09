---
name: challenger
description: >-
  An adversarial "make it exceptional, not adequate" pass over any non-trivial
  plan or deliverable — creative, written, strategic, technical, operational, or
  design work. It challenges the plan, widens the solution space with real
  research, stress-tests how the result lands on whoever meets it, probes for
  high-upside moves that bend assumed (not real) constraints, then converges to a
  sharper plan and a short list of decisions for the human. Use this skill
  whenever the user says "challenge," "pressure-test," "critique," "evaluate,"
  "push this," "expand," "go deeper," "red-team," "raise the bar," "make this
  world-class/exceptional," "what am I missing," or "before I build/commit," or
  runs it on a project of any kind — and also fire it proactively, before
  committing to any foundational, hard-to-reverse, or pattern-setting decision,
  even when not asked by name. Skip it for trivial one-step tasks. This
  challenges a plan before it's built; to audit an artifact that already
  exists, use shakedown instead.
---

# Challenger

Take whatever plan is on the table and force it past "good enough" toward the
best version that's actually achievable. Not by being contrarian — by being
rigorous, wide, and specific. Default output is adequate. The job here is to
beat the default. This applies to any kind of work: software, design, writing,
strategy, research, operations, a document, a deck, a brand system, a video, a
decision. Translate every step below into the medium you're actually in.

**Where this sits.** Challenger works on the *plan* — the direction, before
it's built. Its sibling **shakedown** works on the *artifact* — the built
thing, hunting bugs and weak points. If what's in front of you is already
built and the ask is to find what's wrong with it ("make sure it all works
before we publish"), that's a shakedown job; say so in one line and hand it
over rather than challenging a plan that no longer exists. When a Challenger
pass converges on a plan that then gets built, shakedown is the audit before
it ships. Plan → build → audit → ship.

If the work is part-built, part-plan: shakedown audits what exists, and
anything implicating the plan itself rides its escalation packet back here.
Don't run both blind in parallel on the same state.

## 0. Calibrate first

Match effort to stakes. Over-applying this to a one-line fix is itself a
failure mode.

- **Light** — trivial, fully-specified, one-step. *(Fix a typo, rename one
  file, resize a single export.)* Skip the full pass. Note one improvement if an
  obvious one exists, then proceed.
- **Standard** — a real piece of work with a real audience. *(A feature's flow,
  a chapter, a campaign email, one deliverable inside a larger system.)* Run
  Challenge + Converge, plus Experience if anyone meets the result, plus a
  single Break-the-frame probe if an obvious high-upside move is in reach.
- **Full** — foundational, hard-to-reverse, sets the pattern for everything
  after. *(An architecture, a naming system, a legal structure, a design
  system's grid — anything downstream inherits.)* Run all five passes in full.

State the tier you picked in one line, then go.

**"Go deeper" means deeper, not bigger.** First say what a top professional in
the field would do here that the task doesn't ask for: their material, methods,
tools and outside proof. Then rewrite the task to ask for that, and run the
passes on the rewrite.

**Chained runs.** If this pass runs immediately after shakedown on the same
work, inherit its calibration — tier, milestone, audience, bar — rather than
re-deriving it. State the inheritance in one line.

**Name the bar in the same breath.** Before challenging anything, state the
reference class you're aiming at — the specific person, work, product, or
standard that represents "exceptional" here. Every pass then measures against
that target instead of discovering it at the end. A pass with no named bar
drifts toward "better than before," which is how adequate wins.

## The passes

**Steelman before you strike.** Restate the plan in its strongest form and name
what it gets right — *then* challenge it. The goal is a better outcome, not a
cleverer critique.

**Anchor every challenge.** Each challenge points at a specific claim,
commitment, or omission in the plan as written — quote it or locate it. A
challenge that can't be anchored to something actually on the table is a
challenge to a strawman: cut it, or reclassify it as a question for the owner.
A risk outside what the plan sets out to do is a question or an upgrade, not a
weakness of the plan, unless the plan claims to cover it.

**Always look; grade honestly.** Every run does the full search its tier calls
for, and this skill is built to be run again and again on maturing work. The
deliverable is the truth about where the work sits on the return curve,
including when it's near the top. A weakness counts as plan-changing only when
it is anchored, checked, and you can say what goes wrong if the plan runs as
written. An assumption you couldn't check is a question for the owner, never
"plan-changing until checked." A choice the plan makes on purpose (a small
pilot, a standard pattern, a stated tradeoff) is the owner's call: offer the
alternative as an option, don't grade it a flaw. A small gap with a one-line
fix is an upgrade. Report findings at their true altitude
and value. As work matures the gains get smaller and cost more; when that
happens, say it plainly — *"the remaining moves are marginal: here they are,
here's what they'd cost, and I'd stop here"* is an honest, useful verdict, not
a failure to find something. What's forbidden is faking the reading in either
direction: never invent a weakness to look rigorous, never rubber-stamp to look
done.

**On a repeat pass,** don't re-serve improvements already raised and declined —
the ledger tracks those (see Ledger). Note them in one line, then spend the pass
on what's changed, what's newly in reach, and what still matters. Repeating
yourself trains the owner to stop running the pass.

### 1. Challenge — interrogate the plan

- Restate the real job-to-be-done, not the stated task. What does success
  actually look like for the person who'll use, read, watch, or own this?
- List the load-bearing assumptions. Mark which are unexamined — those are the
  ones to bend later.
- Check the claims the plan stands on. Check every claim that can be checked
  (a number, a tool's output, "X is in file Y") and quote each rule it cites
  at its source, before building on it. Rank risks by what has actually
  broken in work like this, not by a checklist of features.
- Find the weakest link: what breaks first under scale, scrutiny, edge cases,
  real audiences, or six months of entropy?
- Premortem: it shipped and it underwhelmed. Write the single most likely reason.
- Ask why the obvious approach is merely adequate — or quietly wrong.

### 2. Widen — expand the solution space (with real research)

- Generate **at least 3 genuinely distinct approaches**, not three flavors of
  one. Label each. One line on what it optimizes for and what it costs.
  Distinctness test: if two options would fail for the same reason, they're
  the same option wearing two hats — replace one.
- **Before outside prior art, check what the user already has:** their own
  parts catalog, project search, or past projects. Reusing a proven part of
  theirs usually beats the best outside example.
- **Research prior art for real — use the tools, don't vibe from memory.** Who
  does this exceptionally well right now — which people, works, products,
  organizations, or precedents? Name them. Note what to steal and what to avoid.
  Verify current practice; assume your training data may be stale on anything
  fast-moving. Proportion the dig to the tier: a couple of solid reference
  points at Standard, a real survey of the field at Full. **Label every
  prior-art claim:** *Sourced* (looked up this run — cite where) or *Recalled*
  (from training memory — flag it as possibly stale on fast-moving topics). No
  research tools in this environment? Say so once, label everything Recalled,
  and never dress Recalled as Sourced.
- Look past the user's own examples: gold-standard comparable products,
  open-source libraries and published material such as textbooks. Use what you
  find, don't only cite it.
- Cross-pollinate: how would someone from a different field attack this?
- Run the **10x question**: what would the order-of-magnitude-better version
  look like — and which achievable 20% of it captures most of the gain?

On maturing work where the direction is already settled — logged in the ledger
or affirmed by the owner — don't re-widen the whole frame. Generate
within-direction alternatives instead, or close widening in one line and say
why.

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
  seconds, first paragraph, default state — is the highest-leverage choice. Make
  it right for the typical person.
- **Progressive disclosure:** graspable up front, depth on demand. Never make
  the newcomer pay the expert's complexity tax, or strand the expert at the
  beginner's ceiling.
- **Then translate to the medium.** Interactive software: sane defaults,
  command-palette/keyboard paths, optimistic instant-feeling actions, undo over
  "are you sure?", specific recoverable errors, perceived speed via streaming and
  skeletons, one coherent system over one-off styling. A document, deck, brand
  system, video, or body of code — apply the same principle (clarity, flow, the
  right default, depth on demand) in that medium's terms.

### 4. Break the frame — probe high-upside moves (with guardrails)

This is where exceptional separates from competent. Hunt for moves that could be
an **exponential** improvement, even if they bend a current parameter.

First, separate real constraints from assumed ones:

- **Real** (physics, security, privacy, legal, a hard dependency, the user's
  explicit non-negotiables) → respect. Do not route around these.
- **Assumed** (convention, a default setting or template, "that's how it's
  usually done," an inherited pattern, scope drawn by habit) → fair game to bend.
- **User-stated** (a deadline, a budget, a "must include X") → respect by
  default, but check each one once: load-bearing, or habitual? If a stated
  constraint is the single thing blocking the exponential version, neither
  route around it nor override it — surface the tradeoff plainly ("Friday
  costs you X; Monday buys you Y") and put the call in Decisions-for-you.

For each bold move, state four things:

1. The constraint you'd bend.
2. The payoff — and *why it could be exponential rather than incremental*.
3. The cost and blast radius.
4. Reversibility.

Then act by door type:

- **Two-way door** (reversible, contained): prototype or draft it, compare
  against the baseline, keep it if it wins. Show the diff, the draft, or the
  result — whatever the medium allows.
- **One-way door** (irreversible or high blast radius): **do not execute.**
  Surface it as a recommendation with the four-point framing and let the human
  decide.

A reversible bet with large upside is usually worth taking. An irreversible one
is a decision for the owner, not for you.

**The shape, worked once:**

- *Constraint bent:* "the report must cover all twelve findings equally"
  (assumed — inherited from last quarter's template).
- *Payoff:* leading with the two findings that drive the decision makes the
  report act on its reader instead of merely informing them. The multiplier is
  attention, not information — the same facts, aimed.
- *Cost / blast radius:* ten findings demoted to an appendix; one stakeholder
  may ask where theirs went.
- *Reversibility:* two-way door — the appendix keeps everything; restoring the
  old order is a re-sort.
- *Action:* reversible, so drafted both openings and attached the comparison.

### 5. Converge — synthesize, don't dump

Divergent thinking without convergence is just noise.

- **Cross-part pass before "done".** Before calling the plan finished, or saying
  more passes add little, push the person's real situation through every part at
  once: scenarios that touch several parts, conflicts between their goals, clocks
  that collide, and what one part assumes about another. Any plan-changing finding
  means it isn't finished.
- **Rounds tell you when to stop.** Across repeat passes, count the
  plan-changing findings each round. Stop when the count falls to marginal
  moves. If it holds or rises above marginal, the plan isn't converging: change the lens
  (sequence, who meets it, what one part assumes of another) rather than
  running the same pass again.
- **Carry every decision.** Each call the owner has made since the last plan
  shows up in the revised plan or its decisions list. A dropped ruling is a
  plan-changing finding.
- Pick the strongest synthesis across all passes. Justify it in a few lines.
- Produce a **revised, concrete, sequenced plan** — specific changes, not vibes.
  Replace every vague verb with a concrete, checkable change. Not "make it
  clearer" but the actual move — "cut the opening two paragraphs and lead with
  the result," or "replace the confirmation dialog with a 5-second undo." Tag
  each move **small/medium/large** for effort and the same scale for payoff.
  Start the longest waits (approvals, renders, other people) at once so they
  run while the rest gets built, then lead with the cheap wins. The top 5 moves
  are ranked by payoff.
- Name the reference class you're aiming at, and measure the result against it.

## Output

**Caps.** At most 3 options in full, at most 3 bold bets, and the revised plan
leads with its top 5 moves. Anything past a cap becomes a one-liner in a short
appendix. The reader must be able to see the two moves that matter without
digging them out of ten that don't.

Lead with a one-sentence **headline** — the single highest-value move, before
any detail; if the reader does nothing else, that's the one. If the work is
already near the top of the curve, the headline says exactly that. Then
produce, in this order:

1. **Tier** — the calibration call, one line.
2. **Verdict** — what in the original plan holds, what's weak (or "nothing
   material," when that's the truth: a sound plan often has zero or one
   plan-changing finding, with the rest listed as upgrades), and — on
   maturing work — an honest read on where it sits on the return curve and
   whether the remaining gains justify more passes.
3. **Options** — the distinct approaches, labeled, each with its why-it-matters
   and the research you actually found, every claim marked Sourced or Recalled.
4. **Experience** — *(if applicable)* who meets it, primary/edge paths, friction,
   the opening/default, and the depth-on-demand recommendation.
5. **Bold bets** — each with constraint / payoff / cost / reversibility /
   recommendation. Reversible ones you prototyped; one-way doors flagged, not
   executed.
6. **Revised plan** — concrete and sequenced.
7. **Decisions for you** — the calls that need the human, especially the one-way
   doors and anything that bends a stated parameter. Questions for the owner
   (risks outside the plan's scope, unanchored worries) go here, worded as
   questions.
8. **Appendix** — one-liners for anything past a cap.
9. **Lessons for other skills** — *(only when the pass taught something another
   skill should know)* one line each: the lesson, the skill it belongs to, and
   where to file it (the project's skill inbox or change queue). Don't edit the
   other skill from here.
10. **Handoff** — if the revised plan is headed for a build, this block, so a
   later shakedown run ingests it instead of re-deriving everything:

   ```
   HANDOFF → shakedown
   - Milestone: <what the build is heading toward, and when>
   - Audience: <who meets it, in what state>
   - Bar: <the named reference class>
   - Tier: <calibration tier used>
   - Bets taken: <reversible bets executed, one line each>
   - One-way doors approved: <owner-approved irreversible calls>
   - Accepted risks: <ledger ids>
   - Watch items: <the 1–3 places this plan most likely breaks in the
     build — shakedown probes these first>
   ```

11. **Ledger block** — only when there is no filesystem (see Ledger).

**When nobody can answer** (an overnight or unattended run): take the
recommended option on reversible calls, list every idea you skipped with a
one-line reason, and leave one-way doors and fixed calls listed for the owner,
never executed. Don't stop to wait for a reply.

## Ledger

Challenger and shakedown share one ledger per project: `.ledger/ledger.md`. No
filesystem in this environment? Emit the ledger block as the report's last item
and ask the owner to paste it into the next run. Read it during Calibrate;
append to it at Converge.

- **At calibration:** read prior entries from every skill. Anything with status
  `standing`, `closed`, `accepted-risk` or `deferred`, from any skill's prefix
  — a decision already made, a bet already declined, a risk already accepted
  or parked — is not re-raised unless its risk profile changed, and
  then you name what changed.
- **At converge:** open with a run line, then append what this pass settled —
  decisions made, bets declined, the named bar. Append-only; supersede prior
  entries by citing their id, never edit them away. Continue numbering from the
  highest `L-` id; write only `L-` entries.

```
- RUN · 2026-07-01 · challenger · tier: Full · anchor: plan v3
- L-014 · 2026-07-01 · challenger · bet-declined · "Kill the template gallery; ship one opinionated default" · closed
```

Fields: id · date · source · type · one-line summary · status. Types →
statuses: decision → standing|superseded(L-id); bet-declined →
closed|revisit-if(condition); accepted-risk → standing|escalated; bar →
standing|superseded(L-id). Other skills' entries (SD-, ST-, FT-) carry more
fields; read them, never rewrite them.

## Pre-flight (run silently; fix before emitting)

- Every recommendation names a concrete, checkable move — no "make it better."
- The bar is named, and the verdict measures against it.
- Every challenge is anchored to something actually in the plan; anything
  outside the plan's scope sits in Decisions as a question.
- Every plan-changing finding names what goes wrong and the check behind it.
  One that rests on an unchecked assumption, a deliberate choice or a nit
  moves down to a question or an upgrade.
- Every prior-art claim is labeled Sourced or Recalled.
- Caps respected; overflow went to one-liners.
- One-way doors surfaced, never executed.
- **Honest-broker check:** would any part of this verdict soften or sharpen if
  the plan were a stranger's instead of the owner's? If yes, rewrite that part.

## Anti-patterns (do not do these)

- **Generic advice.** "Be creative / think bigger / make it pop" with no
  concrete change attached is worthless. Every recommendation names a specific
  move.
- **Analysis paralysis.** The pass ends with a sharper plan and a decision list,
  not an endless menu.
- **Contrarianism.** Don't challenge to look smart. Steelman first; only strike
  where it improves the outcome.
- **Speculative alarms.** A worst case the plan never set out to handle, dressed
  up as a flaw. Ask it as a question or offer it as an upgrade.
- **Silent risky bets.** Never quietly rewrite scope, structure, dependencies, or
  anything irreversible. Surface it for a human call.
- **Scope-creep on trivial work.** Respect the calibration tier. A small task
  gets a small pass.
- **Research theater.** Describing how others solve this without having looked —
  a guess dressed as a fact. Label it Sourced or Recalled and mean it.
- **Auditing a build instead of challenging a plan.** If the thing is already
  made and the job is finding what's broken in it, that's shakedown's work.
- **Faking the reading — either direction.** Inventing weaknesses to look
  rigorous, *or* rubber-stamping to look finished. When the plan is strong, say
  so and name the marginal moves that remain; when it's weak, say that.
