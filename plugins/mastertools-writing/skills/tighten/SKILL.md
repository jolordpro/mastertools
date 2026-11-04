---
name: tighten
description: >-
  Rewrite prose to be sharper, more concise, more fluent, more believable. A
  polish pass, not a first-draft generator -- it files existing text down
  against a documented ruleset. Fire whenever the user wants something to sound
  "more clear," sharper, tighter, punchier, or less like a LinkedIn post or
  default AI writing. Use on
  website copy, blog posts, newsletters, emails, taglines, headlines, bios, and
  anything meant to be sent or published. Built to run MANY TIMES on one piece:
  each run scores the text, fixes the weakest measured dimensions, and pushes it
  a notch sharper until it converges. Also triggers on "make this clearer,"
  "tighten this," "cut this down," "sharpen this copy," "polish this draft," or
  "run tighten on this." Default to it on any prose the user will send or publish,
  unless the piece is emotional or narrative Story-gear work (a brand film, a
  memorial, a founder story), which it protects rather than flattens.
---

If `~/.claude/overlays/tighten/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

# tighten

Make writing sharper, more concise, more believable. Not clever. Not decorated. Tight.

The whole skill rests on one move you repeat: **score the text, fix the weakest
measured thing, score again.** That is what lets it run five times without
sanding good prose into sawdust. A run does not "change something." It closes a
specific, named gap between the draft and the documented style, then
checks the number moved the right way.

The goal is not an impersonation of anyone. It is **a plain, disciplined spine
inside the writer's warmth.** Discipline that still sounds like a person.

---

## Prime directives (these outrank every rule below)

1. **Never invent a fact, number, name, or analogy to hit a target.** "Concrete
   over abstract" is a rule about *cutting vague adjectives*, not about
   fabricating specifics. Where the text needs a real number or name it does not
   have, mark `[NEEDS: ...]` and hand it back. A made-up statistic is the one
   failure that turns polish into a lie.
2. **Never polish bad thinking into a convincing wrong answer.** If the
   weakness is the argument, the logic, or the evidence -- not the words -- stop
   and say so. Route to the `challenger` skill. Fluent plus wrong is worse than
   clumsy plus wrong.
3. **The score is a transparent tally, never a vibe.** Objective dimensions come
   from `scripts/tighten.py`, which counts. Judgment dimensions are named and
   shown. If you cannot point to why a dimension passed, it did not.
4. **Protect the voice.** Cut what is weak, not what is distinctive. The output
   should read as the writer on their best day, not as generic polish.
5. **Obey the writer's standing rules.** The defaults are at most one em dash per
   paragraph (prefer periods), scrub the banned-word list, and reserve the
   fuller sensory voice for Story-gear work. The writer's own rules win.

A skill that only ever makes text shorter is a chainsaw. This one is a scalpel.

---

## When this fires

**On request:** "make this clearer / sharper / tighter," "cut this down,"
"polish this copy," "run tighten on it," "make this sound sharper and more
believable," or a re-run on a piece already passed through once.

**Default-on:** any prose the user will send or publish -- website copy, a blog
post, a newsletter, an email, a bio, a landing page, a headline. Offer the pass
even when unasked, because the writer's own standing rule is to default to tighten
mode on anything that leaves their hands.

**Stand down when:** the piece is Story-gear (a brand film script, a memorial, a
founder or brand narrative meant to move someone emotionally). Say so and offer
"Tighten-lite" instead (see Frame). Do not flatten warmth into bullet points.

---

## The workflow

Run these in order. Triage first, because it can stop the whole thing.

### Step 0 — Triage: words or thinking?

Read the draft once and ask: is the problem how it is *written*, or what it
*says*? If the argument is thin, the evidence is missing, or the logic is
broken, no amount of polish helps. Name the problem, recommend `challenger`, and
stop. Only proceed when the thinking is sound and the prose is what needs work.

### Step 1 — Frame: classify, then treat

Before a single edit, sort the input. This is what makes the skill work in every
context instead of applying one recipe to everything.

- **Pick the profile.** Read `references/profiles.md` and match the piece to a
  content type: website copy, blog post, newsletter, email, tagline, headline,
  bio, social post, or long-form. Each profile turns on the rules that fit and
  sets its own word budget and targets. A tagline is not an email. Do not treat
  them the same.
- **Confirm the gear.** Clarity gear (default) or Story gear (protect). If
  Story, stop-and-warn per above.
- **Name the one message.** Write the single sentence the piece exists to
  deliver. Everything downstream serves it. If you cannot name it, the draft has
  no spine yet -- that is a thinking problem (Step 0).
- **Set intensity.** Light (polish only), Medium (default), Full (ruthless
  compression; lowers the floor on the writer's say-so). Honor any preserve-list
  the user gives -- lines it must not touch.

### Steps 2-7 — The six passes

Walk them in order: **Frame, Strip, Sharpen, Sound, Stick, Ship.** (Frame is
Step 1 above.) Each pass cites the rule it serves; see `references/mechanics.md`
for the full move-list and worked before/afters.

**2. Strip — subtract.**
Open cold: delete throat-clearing so the first real sentence leads. Cut hedges
(often, I think, usually, arguably). Cut filler (really, very, just, actually,
basically). Collapse redundancy. Enforce one idea per line. This pass alone
often does half the work.

**3. Sharpen — sentence surgery.**
Build antithesis where it fits ("Not X. Y."). Drop a short load-bearing line
after a run of long ones. Force active voice. Replace a vague adjective with a
concrete specific -- and where the specific is missing, `[NEEDS: ...]`, never
invented. Prefer the plain word over the fancy one; keep the weight, lose the
jargon.

**4. Sound — rhythm and fluency.**
Read it aloud in your head. Fix the sentence you stumble on. Vary sentence
length so the prose has a pulse; monotone is the tell of a bot. Convert em
dashes to periods, holding the one-per-paragraph limit. This pass matters
because fluency is not decoration -- easy-to-read text is judged more true and
its author judged smarter. Clarity is a credibility move.

**5. Stick — make it land and travel.**
Give each abstract point one physical analogy the reader has already touched
(the door click, the signature with room around it). Name the core idea if it is
worth carrying into another room. Forge the key line so it survives being
screenshotted alone. See `references/aphorism-recipe.md` for compressing a line
into a maxim.

**6. Ship — finalize and check.**
Strip trends and dated references so it reads as timeless. Run the honesty
check: flag any line that sounds smooth but says nothing. Scrub the banned-word
list (`references/banned-words.md`). Then score and report.

---

## The scorecard

Every run ends with a score, built from two kinds of dimension. Run
`scripts/tighten.py metrics --file <text> --banned references/banned-words.md
--pretty` to get the objective half as real counts.

**Objective (measured by the script -- these drive convergence):**

- Word count is within the profile's budget.
- Average sentence length is in range for the profile.
- Sentence-length variance is high enough to have rhythm (not monotone).
- Reading grade fits the profile and audience (approximate; a guide, not a god).
- Hedges: zero, or only ones that carry real meaning.
- Filler words: zero.
- Em dashes: at most one per paragraph.
- Banned-word hits: zero.

**Judgment (you assess, and show your reasoning -- these do not converge to a
number, so they are flagged, not forced):**

- Opens cold, no throat-clearing.
- One idea per line.
- The key line survives out of context.
- Has a named or portable idea where the profile wants one.
- Abstract points have a concrete picture beside them.
- Meaning intact. Voice intact.

Report the objective dimensions as before/after numbers and the judgment
dimensions as pass/flag with a one-line reason. The score is the count of
dimensions passing. It is a checklist tally you can audit, not a rating you
invented.

---

## Re-run engine (the part that has to survive many passes)

The writer will run this again and again. Make repeated runs converge, not
drift.

- **Freeze what is maxed.** When a line hits every dimension it can, mark it
  frozen and leave it alone on later runs unless the user unlocks it. No
  undoing good work, no oscillation.
- **Monotonic only.** A run may only raise or hold each objective number, never
  lower it. If a proposed edit would drop variance or push word count back up
  without a clear gain, reject it.
- **Carry state between runs.** Log each pass to the ledger (below). On a
  re-run, read the last row for the piece and push the dimensions that are still
  short. Run three builds on run two.
- **Escalate, do not thrash.** Run 1 fixes the biggest, most obvious gaps
  (throat-clearing, hedges, word count). Later runs go after the subtler work
  (maxim quality, analogy, rhythm). Full intensity only when the writer asks.
- **Declare convergence honestly.** When every dimension is maxed, or the only
  gains left would breach the floor, say: "This is about as tight as it gets
  without losing meaning or voice." Then stop. Do not invent changes to look
  busy. **Converged is a valid, good result.**

**The floor (hard stops -- never cut below these, at any intensity):** the core
meaning, the writer's intended warmth, one sensory detail where the piece had
one, and audience-appropriate vocabulary. Full intensity lowers the floor on
length and plainness. It never lowers it on meaning.

---

## Anti-parody caps

Maxing every device produces a caricature, which is the opposite of sharp. Cap
them.

- No more than one antithesis ("Not X. Y.") per short run of sentences. It is a
  spice, not a base.
- Not every sentence short. The power of a short line comes from the long ones
  around it. Protect variance on purpose (the script measures it).
- Do not force a maxim where a plain statement is stronger. Most sentences are
  not trying to be quotable, and should not.
- Do not add an analogy to a point that is already concrete. One picture per
  abstract idea, not per sentence.

If the output reads like a wall of fortune cookies, it failed. Back off and
restore range.

---

## Voice lock

Before cutting, fingerprint the writer's voice from the draft and anything known
about them: their cadence, their specific (non-banned) word choices, their dry
humor, their sensory turns. Protect those while you cut. Remove what is weak, not
what is theirs. When a change would make the piece sound like anyone, it is the
wrong change. Where the writer's fuller sensory voice is the asset (Story-gear
work), Clarity gear tightens the structure without stripping their fingerprints.

---

## Protected regions (never rewrite these)

Detect and leave untouched: direct quotations, legal or compliance lines, code,
data and figures, proper names, and anything the user names in a preserve-list.
Tightening someone else's quote or a disclaimer is a bug, not a feature.
Handle lists and tables by their own logic; do not flatten them into prose or
prose into them.

---

## Output format (progressive disclosure -- lead with the result)

1. **The revised text.** First. It is what they came for.
2. **The single highest-impact change**, named in one line.
3. **Score: before -> after**, objective numbers plus judgment flags.
4. **One next action:** run again (and at what intensity), converged, or blocked
   on you.
5. **`[NEEDS: ...]` flags** up top if any real specific is missing.

Keep it tight by default. A `verbose` request unlocks the full pass-by-pass
reasoning and the per-line changelog.

---

## The ledger

One CSV per project: `.ledger/tighten-passes.csv` (sits beside the
Challenger/Shakedown/Timecard ledgers -- same directory, different file). Append
only; never edit prior rows. Override the path with the `TIGHTEN_LEDGER` env var.
Write rows through `scripts/tighten.py log` so free-text fields are sanitized
against spreadsheet-formula injection; never hand-append.

Schema (header written on init):

```
date,user,piece,pass_no,profile,intensity,words_before,words_after,grade_before,grade_after,score_before,score_after,frozen,needs,notes,schema_version
```

The ledger is what makes re-runs smart: it records how far a piece has traveled,
which lines are frozen, and what is still waiting on the writer.

**In plain chat (no persistent filesystem):** emit the CSV row in a code block
and tell the user to append it, and carry the frozen/score state inline in the
conversation. Same fallback pattern as the audit skills.

---

## Integration with the rest of the kit

- **challenger** — when Triage finds the thinking is thin, hand off. Polish
  cannot fix a weak idea.
- **shakedown** — runs cleanly on copy that Shakedown flagged as weak. Tighten is
  the fix pass for prose defects it surfaces.
- **timecard** — optional. If the user wants the ROI trail, log time saved per
  polish through Timecard; keep it off by default to stay lean.
- **Standing rules** — the banned-word list, the em-dash limit, and the
  Clarity/Story split are baked in, not optional.

---

## References

- `references/mechanics.md` — the full tightening move-list as rules, each with a
  worked before/after in the writer's domains. Read on every run.
- `references/profiles.md` — per-content-type rulesets, word budgets, and
  targets (website copy, blog, newsletter, email, tagline, headline, bio,
  social, long-form, Story-gear). Read at Frame.
- `references/aphorism-recipe.md` — how to compress a line into a maxim that
  survives out of context. Read at Stick.
- `references/banned-words.md` — the kill-list; also the input file for the
  metrics script. Read at Ship.
- `scripts/tighten.py` — objective metrics (`metrics`) and ledger logging
  (`log`, `init`). Stdlib Python 3; no installs.
- `evals/battery.md` — the test battery: fixtures, expected behavior per
  context, and the judging rubric. Run it to prove the skill behaves across
  contexts before relying on it.
