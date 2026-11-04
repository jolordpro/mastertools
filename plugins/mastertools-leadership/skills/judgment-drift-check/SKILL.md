---
name: judgment-drift-check
description: Check an organization for AI-era Decision Drift and judgment depreciation, and design Judgment Loops or Agent Manager capability, from the Leadership RAG Library's AI-001. Use when people justify decisions with "the model recommended it" or "the AI said so", when override or exception rates are falling without AI quality improving, when a leader asks whether their teams are losing judgment or how to govern an AI rollout beyond tooling and policy, when designing decision rights between humans and AI systems, or when building Agent Manager capability into a leadership pipeline. Not for AI tool selection, prompt engineering, or model/vendor comparisons — this is about human judgment health, not the technology stack.
---

# Judgment Drift Check (AI-001)

This is a judgment and safety instrument, not an AI-tooling one. The question is never which model
to use — it is whether human evaluative capacity is improving or silently depreciating.

## Find the library

```
python3 -I <this skill>/../leadership-coach/scripts/library.py where
```

Exit 0: the first line printed is `<REPO>`. Exit 3: the library isn't on this machine. Say so once,
don't run this instrument from general knowledge, and give the fix from the `leadership-coach`
skill's "Find the library first" section.

```
<REPO> = the folder `library.py where` prints
PAGE   = <REPO>/Core_Canonical_Super_Pages/AI_Transformation_Leadership.md
SAFE   = <REPO>/Core_Canonical_Super_Pages/Psychological_Safety_Multi_Layer.md
ENERGY = <REPO>/Core_Canonical_Super_Pages/Resilience_Energy_Management.md
```

## Step 1 — Lead with the evidence band

Read `<REPO>/CLAUDE.md`, then the **Binding rules** section of
`<this skill>/../leadership-coach/SKILL.md`. Every rule there binds this instrument; the ones most
often broken here are marking your own review cadences as judgment and stating the cultural
assumption behind any read of override behavior.

Then `PAGE`. Check §9 of `PAGE` for the per-claim bands before you write anything. If a band in
the page header and a band in §9 disagree for the same claim, use the lower one and say so.

Much of this domain is **Moderate–Emerging**, some Thin. Say so **up front**, not in a footnote,
using the communication language in `<REPO>/00_START_HERE.md` §4 — "this is emerging; treat it as
a working hypothesis." Confident tone here violates the library's evidence discipline. Never
upgrade a band because a recommendation would land better.

Finish this path's minimum set (Path D, `04_Retrieval_Playbook_and_Priority.md` §8): `SAFE` for
voice about AI errors and overrides, and `ENERGY` for the cognitive load that drift feeds on. When
the ask reaches capability building or the pipeline, also read CAP-001, PIPE-001 and SPONSOR-001;
when it reaches governance, BOARD-001. If you can't reach a page you need, say which and what it
leaves open.

## Step 2 — Screen for Decision Drift

Work through the six-signal early-warning cluster in §2.2 of `PAGE`. For each signal, capture
**concrete evidence:** incidents, rates, actual language used in meetings — not impressions.
Signals include overrides becoming rarer or costlier without AI quality improving, edge cases
forced into standard paths, the language shift to "the model recommended it," speed metrics
rising while qualitative review declines, and reduced human fluency when AI is unavailable.

Then check §2.3 of `PAGE` for judgment depreciation trajectory: **can people still articulate why
a decision is good or bad?** That question is the core test.

Also check the AI-era safety requirements in `SAFE` §2.5 — is it safe here to override the model,
to document the reasoning, to report an AI error, to refuse "the model said so"? Drift and silence
travel together; a team that cannot safely override has no judgment loop regardless of policy.

## Step 3 — Check hybrid alignment

Run the four misalignment modes in §2.6 of `PAGE`: **Substitution** (AI replacing judgment that
should stay human), **Conflict** (human and AI pulling against each other unproductively),
**Under-use** (human effort on work AI does better), **Over-trust** (accepting output without
evaluation). Name which are present with evidence.

## Step 4 — Design the response

**If drift signals are present** → install a healthy Judgment Loop using the six tactics in §2.1
of `PAGE`: explicit override rights with low-friction rationale capture; a periodic override and
exception review; adaptive space protected for evaluative work; periodic standard recalibration;
leader modeling; and cascade amplification one layer down. Add the anti-Goodhart sensing kit from
§2.2 of `PAGE` — sample override *quality*, and run periodic **"AI-off" evaluative exercises on
real cases**.

**If the ask is capability building** → the six-step Minimum Viable Agent Manager Development
Sequence in §2.5 of `PAGE`, work-embedded, with the dosage as written (step 1 is 2–4 weeks of
judgment-loop fluency; do not compress the sequence into a workshop). Connect it to the pipeline
and sponsorship systems — Agent Manager capability belongs in selection criteria and passage
requirements (PIPE-001), in who gets sponsored (SPONSOR-001), and in capacity for complexity
(CAP-001), not only in a training catalogue.

**If decision rights are unclear** → the six-question regime design set in §2.7 of `PAGE`: which
decisions are AI-primary, human-primary, or fully human; who holds override rights; how
escalation works; how edge cases route.

**If the org has nothing in place** → Minimum Viable AI Judgment Protection (§2.8 of `PAGE`),
including the simple principle that AI outputs are inputs and human evaluation remains
accountable.

## Step 5 — Output

1. **Findings per drift signal**, with evidence and the gaps where evidence is missing.
2. **Hybrid alignment read:** which of the four modes are active.
3. **Evidence bands stated** on every recommendation.
4. **Intervention Mode block** per the library's `CLAUDE.md`. Run the person-vs-system test
   in full: this is usually decision-rights, incentive, and adaptive-space design rather than
   individual AI skill.
5. **Dosed actions:** 1–2, with a named owner for the override review and a review cadence
   marked as your judgment (the library sets none).
6. If governance-level, note what belongs in front of the board (`Board_Fluency_and_Governance.md`
   §2.3 carries the AI governance question set and §2.5 the standing override item).

## Path K override

`AI_Transformation_Leadership.md` §8 is explicit: with an overwhelmed leader, do **not** open heavy
AI transformation work. Protect energy and safety first, and offer one micro judgment-protection
step only if relevant. Defer the full drift screen.

## Failure modes for this instrument

Efficiency-only adoption · silent decision drift · Agent Manager role neglect · opacity as power ·
governance lag · cultural or trust polarization · **Goodhart on judgment metrics** (override rate
becomes a target and gets gamed — watch for this specifically, since your own recommendations
create it). Detail in §5 of `PAGE`.
