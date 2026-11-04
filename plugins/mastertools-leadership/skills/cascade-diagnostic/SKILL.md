---
name: cascade-diagnostic
description: Run a structured cascade-health diagnosis across the seven leading-indicator domains from the Leadership RAG Library (BRIDGE-001). Use when a leader asks how healthy their organization, team, or leadership cascade is; when symptoms are vague or multiple ("something's off", "engagement is slipping", "skip-level signal has gone quiet", "people seem agreeable but nothing risky gets raised"); when they ask "where do I start" amid several problems at once; or when they want a periodic leadership health check or a client-facing health dashboard. Not for a single well-defined issue with an obvious owner — route those to the matching instrument skill.
---

# Cascade Diagnostic (BRIDGE-001)

Structured sensing pass that converts multi-layer observation into a calibrated intervention.

## Find the library

```
python3 -I <this skill>/../leadership-coach/scripts/library.py where
```

Exit 0: the first line printed is `<REPO>`. Exit 3: the library isn't on this machine. Say so once,
don't run this instrument from general knowledge, and give the fix from the `leadership-coach`
skill's "Find the library first" section.

```
<REPO> = the folder `library.py where` prints
PAGE   = <REPO>/Core_Canonical_Super_Pages/Observation_to_Coaching_Bridge_and_Cascade_Health_Dashboard.md
```

## Step 1 — Load

Read `<REPO>/CLAUDE.md` (binding governance — all of it applies here), then the **Binding rules**
section of `<this skill>/../leadership-coach/SKILL.md`. Every rule there binds this instrument;
the ones most often broken here are marking unsourced timeframes as your judgment, stating the
cultural assumption, and naming tensions from `<REPO>/05_Contradiction_and_Evidence_Log.md`.

Then `PAGE`. The sections you will use: §2.1 (four layers + live conversation structure), §2.3
(the seven domains with their Look/Listen/Ask lists), §2.5 (dosage), §2.6 (bite-sized action
criteria), §4 (question bank), §8 (multi-problem starter sequence).

This is Path B, so `PAGE` alone is not enough (`04_Retrieval_Playbook_and_Priority.md` §8). Before
you write the composite read, also read the page behind each domain you rate Yellow or Red:

| Domain | Page |
|---|---|
| Psychological Safety Climate | SAFE-001 (Artificial Harmony lives here) |
| Energy & Sustainable Capacity | ENERGY-001 |
| Enabling Leadership & Adaptive Space | CAP-001 + SYS-CAS-001 |
| Judgment Health & AI Co-Evolution | AI-001 |
| Multi-Layer Sensing & Cascade Integrity | SAFE-001 + SYS-CAS-001 |
| Capacity for Complexity & Mental Model Health | CAP-001 |
| Generativity & Pipeline Health | GEN-001 + PIPE-001 |

Read SYS-CAS-001 whenever the pattern spans more than one team or layer. If you can't reach a
page you need, say which one and what it leaves open.

## Step 2 — Walk the seven domains

1. Psychological Safety Climate
2. Energy & Sustainable Capacity
3. Enabling Leadership & Adaptive Space
4. Judgment Health & AI Co-Evolution
5. Multi-Layer Sensing & Cascade Integrity
6. Capacity for Complexity & Mental Model Health
7. Generativity & Pipeline Health

For each, use that domain's Look/Listen/Ask list in `PAGE` §2.3 as interview probes. **Select 2–3
probes per domain by relevance — do not dump the full list.** Ask about observable behavior and
specific recent incidents, not impressions.

**A domain with no data is Unknown, not green.** This rating is this instrument's rule, not a
rating the page defines; say so if you cite it. Never infer a rating from absence of complaint —
silence is itself an Artificial Harmony signal (SAFE-001), not evidence of health.

## Step 3 — Rate by direction of travel

Rate each domain **Green / Yellow / Red / Unknown**, judged on trajectory (improving / stable /
declining), not on a snapshot.

Apply the composite rule from the end of `PAGE` §2.3: **early yellows in Safety, Energy, or
Judgment Health outrank lagging greens elsewhere.** A cascade with strong delivery numbers and a
yellow safety trajectory is not healthy — say so plainly.

**No numeric scores: this instrument's rule.** BRIDGE-001 §2.3 tracks trajectory over absolute
scores and §5 names the Goodhart failure (the dashboard turns into a scorecard). Traffic-light plus
direction of travel only. If the user asks for a score out of ten, say it is this instrument's rule,
point to those two sections, and offer the trajectory read instead.

## Step 4 — Branch

- **Several domains degraded at once** → run the Multi-Problem / Cascade Overload Starter
  Sequence in `PAGE` §8. The page's trigger is "multiple cascade domains degraded
  simultaneously" and it sets no number; if you apply a cut-off, say it is your judgment. The
  sequence is *ordered* triage (stabilize sensing → protect capacity → surface safety → contain
  toxic patterns → then passage/AI/sponsorship work → cultural assumption check throughout).
  Deliver it as a sequence with reasons for the ordering, never as a parallel to-do list.
  Sensing comes before capacity. State the order the same way everywhere, short answer included.
- **One domain clearly degraded** → run the standard Bridge conversation structure (`PAGE` §2.1)
  on the highest-impact domain: observation share → second-order probe → sense-making and
  pattern test → person-vs-system decision → bite-sized action with dosage → follow-through
  contract.

If a specific instrument is clearly indicated, hand off: `containment-decision` (toxic patterns),
`capacity-audit` (People Leader overload, "do both"), `judgment-drift-check` (AI judgment risk).

## Step 5 — Output

Deliver:

1. **Dashboard table:** domain | rating | direction | evidence observed | what's missing.
2. **Composite read:** one paragraph on trajectory, naming which early warnings outrank which
   lagging greens.
3. **Intervention Mode block** in the format the library's `CLAUDE.md` requires.
4. **1–2 dosed actions** meeting the bite-sized criteria in `PAGE` §2.6 (specific and observable,
   small, linked to a success picture, owned and restated, followed by observation), with a
   review date marked as your judgment — the library sets no general review cadence.
5. **Named unknowns:** the domains where you have no data and what would produce it.

Then offer (do not force) a rendered dashboard artifact for client-facing use. If accepted,
apply the `lord-brand` skill for the visual system and publish via the Artifact tool.

## Path K override

If the leader is overwhelmed, depleted, or in crisis language, do **not** run the full seven-domain
walk. `04_Retrieval_Playbook_and_Priority.md` (§ Path K) forces extreme brevity: energy recovery
first, one micro diagnostic step only. Offer the full pass later. A complete dashboard delivered
to a drowning leader is over-dosage.

## Failure modes for this instrument

Passive sensing (waiting for data instead of designing observation) · treating agreeableness as
health · person-only reflex on recurring cross-layer patterns · over-coaching by acting on all
seven domains at once · Goodhart (turning the dashboard into scored targets) · rating Unknown as
Green. All are listed with detail in §5 of `PAGE`.
