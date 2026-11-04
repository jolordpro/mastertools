---
name: scout
description: Evidence-acquisition doctrine for establishing what is true, right now, with sources. Fire whenever the user asks to research, investigate, look into, dig into, fact-check, deep-dive, tear down, or study a product, market, tool, company, person, claim, or decision input — even without the word "research" — and fire proactively whenever an answer would otherwise rest on recalled facts about anything time-sensitive, product-specific, or post-training, or when a multi-session program needs evidence gathered to its laws. "Compare" and "verify" fire only when the comparison turns on facts to establish, never on taste. Stay dormant for single-fact lookups a normal search answers in one step; for taste or aesthetic judgment (motion-critique and impeccable own those); for how-or-why mechanism understanding (learn owns those); for Anthropic product facts (claude-capability-awareness owns those); and for writing tasks.
---

# SCOUT — Evidence Acquisition

**Built by: Opus 4.8 · July 19, 2026 · v0.2 — patched to v0.3 by Fable 5, same day**
*v0.3, from Eval Run 1 + the Fable review: trigger layer rewritten (D1, D2),
lateral-reading law, snippet definition tightened by an in-house breach,
referent rule, charter-first rule, binary eval rubrics.*

Location scouting is pre-production research: survey the territory, come back
with an evidence-backed report, before anyone commits to shooting. That is this
skill's whole job — how Claude acquires, verifies, and reports evidence for the user.

The doctrine exists because the two default failure modes of a researching
model are opposites: fabricating confidence when evidence is thin, and grinding
past sufficiency when evidence is already in hand. Every rule below kills one
or the other.

## Jurisdiction — the seams

- **The always-on rules** (`rules/ALWAYS-ON.md`) govern every session; scout is
  their evidence-acquisition arm when the deliverable is knowledge. Scout's own
  (S)/(R)/(I) labels and sheets apply inside them.
- **challenger / shakedown / stress-test** consume evidence; scout produces it.
  When a challenger pass or a claim check needs real research, it runs a scout
  block and cites the sheet.
- **timecard** attaches if scout work produces a script; the sheets themselves
  are not scripts.
- **learn** owns understanding — how or why something works. Scout owns
  establishing — what is true, right now, with sources. A question about a
  stable mechanism routes to learn even when it's phrased "research this."
- **claude-capability-awareness** owns Anthropic product facts. Law 1 sends those
  there first, never to a generic web search; scout supplements what it
  doesn't cover.

## Pick the tier first, out loud

Effort scales to the question, never to enthusiasm. Anthropic's production
research system encodes the same rule: simple facts get one agent and a few
calls; complex research gets many, with divided responsibilities. Misjudging
tier was their most common early failure — in both directions.

| Tier | Shape | Budget | Output |
|---|---|---|---|
| **L0 LOOKUP** | Single fact, single source | 1–2 searches | Answer inline. No protocol, no templates. |
| **L1 RECON** | Lay of the land | 3–10 searches/fetches, ≤45 min | One-page recon note |
| **L2 PASS** | Pre-registered questions, verdicts | 1–3 blocks (45–90 min each) | Evidence sheet + source log |
| **L3 FIELD STUDY** | Multi-session program | Weeks | Full protocol: charter, state file, hypothesis board, clean-context verdicts |

State the tier in one line when firing. If mid-hunt the question outgrows the
tier, say so and re-tier — silently escalating is how a lookup becomes a lost
afternoon.

## The laws

Full doctrine with evidence chains lives in `references/methods.md` — read it
at L2 and above, and any time a law needs its reasoning.

**Load-bearing** is the qualifier laws 2, 4, and 5 gate on, so it needs a test:
a claim a decision or another claim rests on. If this were wrong, would the
recommendation change? If yes, it is load-bearing and those three laws apply in
full. If no, one decent source is enough.

The laws in force at every tier:

1. **Search, never recall** — anything time-sensitive, product-specific, or
   post-training gets a live source. Training data describes the previous
   version of the world.
2. **Fetch, don't snippet** — a load-bearing claim is read from the full page,
   never from a search snippet. Snippets are lossy representations; the
   ground-truth law applies to the web too. **Operational limit:** fetch only
   URLs the conversation already holds — ones the person gave, or ones a prior
   search or fetch returned. A URL pulled from memory, or built by editing a
   path, gets rejected. To reach a known but unlinked source, search for it
   first, or search for a page that links it. And a search-result excerpt is
   still a snippet, however long — this skill's own second research pass broke
   the law here, resting load-bearing claims on excerpts it never fetched, so
   the rule now names its documented failure.
3. **The model never generates evidence** — no invented numbers, quotes, or
   "users say." Every quote carries a live URL or it is deleted. Every quota is
   a ceiling, never a floor.
4. **The source ladder, assigned laterally** — primary document > primary
   human > expert secondary > quality press > aggregator > SEO farm. Default
   web ranking actively fights this ladder; climb it deliberately for anything
   load-bearing. And assign the rung from *outside* the source: leave the page
   and check what the rest of the web says about it. Judging a source by
   reading its own pages is the measured-inferior method — professional
   fact-checkers beat historians and students on both accuracy and speed by
   reading laterally, not vertically. A page's own polish is not evidence.
5. **Two sources or one label** — a load-bearing claim gets a second independent
   source, or ships flagged single-source. Every claim carries **(S)** Sourced,
   **(R)** Recalled, or **(I)** Inferred.
6. **Owned facts get verified** — names, numbers, dates, prices, versions,
   capabilities: checked against the native source. Ambient impressions need
   plausibility only. The user's ambient zone is narrower than it feels.
7. **Stop rules beat stamina** — done-conditions written before the hunt starts.
   Stop when the questions are answered, when marginal searches repeat, or when
   the budget is hit — and say which one fired.

## Adjudication — judging what you found

The laws above govern acquiring evidence. These govern judging it. All four
situations are the norm in real research, not the exception, and a model with
no rule for them defaults to the smoothest available move.

**A1. Conflicts are reported, never resolved by preference.** When two sources
disagree, name both readings, rank them by ladder rung and by date, then state
which one the finding rests on and what would settle it. An unresolved conflict
is a finding. Quietly picking the one that fits the emerging story is how
research becomes advocacy.

**A2. Sources have dates too.** Law 1 defends against stale recall. This
defends against a stale page. Every source carries its publication or
last-updated date. For anything version-, price-, capability-, or
personnel-related, a source older than the current product cycle is labeled
**(R)**, not **(S)**, until confirmed against a current page. Finding it on the
web today does not make it true today.

**A3. The locked door.** When the primary source exists but can't be read —
paywall, login, robots, dead link — say so out loud. A secondary that quotes the
primary can be used, labeled **(S-via)** with the intermediary named, and never
upgraded to a direct citation. Two secondaries quoting the same primary are one
source, not two.

**A4. The premise is not evidence.** A factual claim inside the request is an
input, not a finding. Label it **(R-asserted)** and verify it like any other
load-bearing claim. If it fails, that is the first finding, reported before the
answer to the question asked. Researching downstream of an unverified premise
is conclusion-shaped research with extra steps.

## The loop (L1 and up)

1. **Pre-register** — write the questions and what would count as an answer,
   before the first search. Pre-registration requires a referent: if the
   research object is unnamed ("compare the two options"), get the names
   first. At L2+, name what would falsify the working hypothesis.
2. **Start wide** — short, broad queries to map the territory. Long specific
   queries come second, after the landscape is visible.
3. **Interleave** — after every result batch: what did this answer, what's
   still open, what's the next best query. Never fire blind salvos.
4. **Climb the ladder** — once the wide pass finds the primary sources, fetch
   them in full. The recap that ranked first is a pointer, not a source.
5. **Log as you go** — source log rows written at read time, not reconstructed
   at the end. Templates in `references/templates.md`.
6. **Verdicts render clean** — at L2+, FOR / AGAINST / COMPLICATES verdicts are
   graded in a fresh context from the evidence sheets alone. The graders never
   meet the hunters. Mechanism depends on where you're running: a subagent
   where subagents exist (Claude Code, Cowork); a new conversation seeded with
   the sheets alone where they don't (the chat app); and where neither is
   possible, the verdict ships labeled `self-graded` and the user is told which one
   fired. Every verdict block carries one of the three states. A control that
   can be satisfied by asserting it isn't a control.
7. **Ship with the case-against** — at L2+, findings carry a "where this is
   weak" section. Research that can't name its own soft spots isn't finished.

## Multi-session research (L3)

The charter exists before the first search — no charter, no hunt. Sessions
are stateless; the state file is the state. Every session loads
`PROGRAM-STATE.md` first and updates it last — the same two failure modes
Anthropic documented in long-running coding agents (doing too much at once,
declaring victory early) appear in long-running research, and the same harness
kills them. Structured checklists resist drift better than prose; statuses flip,
entries never get deleted. Full protocol and template in `references/`.

## Output contracts

Every deliverable header stamps the model and date. Formats are fixed and live
in `references/templates.md`: the **recon note** (L1), the **evidence sheet** and
**source log** (L2), the **field-study charter** and **PROGRAM-STATE.md** (L3).
A deliverable that outgrows its template gets cut back to it — the template is
the cap made physical.

## When scout is done

Report in the user's stated writing rules: short lines, findings ranked, the
break written bigger than the confirmation. A broken hypothesis is the more
valuable finding. End with what was NOT established, then next steps.
