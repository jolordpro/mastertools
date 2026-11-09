---
name: motion-evidence-audit
description: Audit a motion designer's portfolio, case study, resume bullet, LinkedIn section or website page against Staff/Principal motion-systems hiring standards, then say what evidence is missing and how to close it. Use whenever the user says "audit my portfolio", "is this case study Staff-level", "review my site/LinkedIn for motion roles", "what's missing for a principal motion role", "score this against the rubric", "rewrite this resume bullet", or pastes motion-systems resume bullets, a case study, a portfolio URL or a job posting and asks how it reads. Also use for Head of Creative or creative-leadership positioning checks (mode creative-leadership). Produces a plain-language verdict, what the material proves and fails to prove, hidden issues, ranked fixes and rewrites; a scorecard only when asked. Not for critiquing one animation (motion-critique) or designing a motion system (motion-system-architect).
---

# Motion evidence audit

as_of: 2026-10-04. Market facts drift: job postings, what Figma Motion or other tools can do, and which companies hire for which levels all change. Treat any such fact in this skill or in an audit as dated, and check live postings before advising on a specific role.

## What this skill is, and is not

Hiring panels for Staff and Principal motion roles look for evidence that a person made motion behavior repeatable for other people, not just excellent. This skill reads a surface (portfolio, case study, resume, LinkedIn, site) and reports what that surface proves, what it fails to prove, and the cheapest artifact that would prove it.

It is a synthesis of several assessment frameworks. The 14 dimensions, the weights and the score bands are this skill's own construction, not an industry standard and not a hiring prediction. They are working tools for you, not output for the reader: the person asked how their material reads to a hiring panel, and a panel never speaks in dimension codes or coverage percentages. The value is the evidence discipline, not the number. Show numbers only when the user asks for a score, and then say once that the scale is synthesis.

Measuring the motion itself (values in a codebase, an After Effects inventory or keyframe export) is not an evidence audit. Say so and hand it to motion-system-architect, which audits implementations.

Core idea: **unknown is not weak.** Most portfolios are packaged for craft and are silent on tokens, accessibility, governance and adoption. Silence becomes a "next probe", never a low score.

## Inputs

Accept any mix of: pasted text, a URL (fetch it if a web tool is available), PDF or screenshots, a job posting. Before scoring, note what you could actually see. Text cannot evidence craft or behavior (mark D1, D3, D4 as U unless media or prototypes were seen). A resume alone is claim-only (confidence D). Never pretend to have watched a reel you only read about.

## Modes

| Mode | When | What changes |
|---|---|---|
| `staff-product-motion` (default) | Product, design-systems or motion-systems IC roles, e.g. Staff Motion Designer in a design-innovation or platform team | Default weights and gates in `references/rubric.md` section 2 |
| `creative-leadership` | Head of Creative, creative director, studio leadership | Reweighted toward leverage, influence, governance and craft; own gates; in `references/rubric.md` section 2 |

If the user does not pick, infer from the target role and say in plain words which lens you used ("I read this as a product motion IC application") rather than naming the mode. In creative-leadership work, team size, hiring, talent development, budget and stakeholder management are the core of the role, not extras: assess them directly as claims (what is stated, what would prove it, what a panel will ask) even though the frameworks behind this skill are thin on them. Never set them aside as outside the audit.

## Workflow

1. **Intake.** Establish: target role and level, mode, surface(s) supplied, and what was and was not visible. Ask at most two questions, and only if the answer changes the audit (usually target role). Otherwise state assumptions and proceed. When a job posting is supplied, split it into must-haves, nice-to-haves and traits, give each an ID, and map each to the proof in the material or a named gap (`references/portfolio-architecture.md` section 4, "Read the posting"). Tag what the posting says apart from what you infer about the team.
2. **Inventory.** List the projects or claims in the material. For each, who did what (use the attribution ledger in `references/evidence-and-gates.md` section 5 when the text says "we").
3. **Review in halo-control order** (`references/portfolio-architecture.md` section 2): craft first, so a strong reel cannot inflate the systems dimensions scored afterwards, then interaction, then leverage and influence.
4. **Score each dimension** D1 to D14 on 1 to 5 using the signatures in `references/rubric.md`, and assign evidence confidence A/B/C/D/U separately (`references/evidence-and-gates.md` section 1). Respect the ceilings: C caps at 3, D caps at 2 and is shown as "claimed", U is not scored. Score a dimension only when the surface makes a claim or shows evidence *about that dimension*; adjacent hints (a re-skin feature is not a token architecture) stay U and become probes. An interactive prototype is B for behavior (D3, D4) and C for anything about shipping or adoption.
5. **Compute** axis scores, the evidenced-weight total and the coverage percentage (formula in `references/rubric.md` section 2). At 60 percent coverage or more, use the total internally to decide where to focus. Below 60 percent, treat any total as provisional and lead part (b) with what would need to be shown. A score built on thin evidence reads as a verdict the evidence cannot carry, which is why scores stay out of the output unless asked.
6. **Check gates** (`references/evidence-and-gates.md` section 4). Each is pass (evidence at A or B), provisional pass (C), fail, or not tested (U or claim-only D). Not tested blocks a level call as firmly as fail, but the remedy is to show evidence, not to build capability.
7. **Run the red-flag sweep** against RF-01 to RF-30 and inflation patterns I1 to I6 (internally; describe what you find in plain words). Also check: contradictions inside the material ("runs a tight ship" beside "teams love working with me"), mismatches across surfaces (job title, dates, team size different on resume and LinkedIn), outcomes borrowed from the platform or audience rather than earned by the person, employer ownership of tools or code, and gaps that matter more in this domain (accessibility for health, trust and error states for finance, likeness, league and music rights for AI work in sports media).
8. **Build work orders** from the 20-artifact library (`references/portfolio-architecture.md` section 6). Rank by gate impact (the gates the artifact itself moves once delivered), then by effort, then by how many role types care. Flag time-gated items (a release, an approval, data that takes weeks to accumulate) as "start now" whatever their rank. Retro-documenting real shipped work as a system is legitimate evidence-surfacing when it is labeled "retro-documented" and describes only what was actually built; hand that work to `motion-system-architect` (retro-document mode).
9. **Compress claims** (`references/claim-rewrites.md`): strip test, verb-to-evidence, rewrite with `[CONFIRM: ...]` slots.
10. **Write the output** in the template below. Lead with the verdict. Keep it as short as the evidence allows. Steps 4 to 8 are your working; their codes (D1 to D14, A/B/C/D/U, RF-xx, I1 to I6, A01 to A20, gate names, coverage percentages) never appear in the output unless the user asks for the rubric mapping.

## Output template

Write for the person who will act on it, in the words a hiring manager would use. Five parts, in this order: the answer first, the proof second, the fix last.

**(a) Verdict.** A short paragraph: the level the material supports today in plain words ("reads as a strong Senior product motion designer; the Staff case is not on the page yet"), the single biggest reason, and the single cheapest change that would move it. Say what you could and could not see (text only, no reel) in one clause.

**Credibility errors first.** If the material contains things a panel would catch as wrong (arithmetic that does not add up, dates or team sizes that contradict each other, broken code, a standard misquoted), list them right after the verdict, numbered, each with the fix. They cost more than any missing evidence, so they come before everything else.

**(b) What it proves, and what it doesn't.** Group by what a panel looks for: craft, product behavior, systems and leverage, influence and adoption, and for leadership roles, team, hiring, budget and direction. For each, one or two lines: what is **shown** (with the quote or artifact), what is only **claimed**, and what is **not shown** and what would show it. Silence is "not shown yet", never "weak". Tie the gaps to the target role and its domain.

**(c) Things a panel will notice.** Contradictions, cross-surface mismatches, borrowed outcomes, precise-looking numbers with no source, ownership or IP questions, title inflation, and the likely false alarms. Quote the line.

**(d) What to do, ranked.** A short table: rank, the gap, the artifact to make or surface (named plainly: "a one-page motion spec with tokens", "a before/after with the metric and its source"), effort (under a week / a few weeks / a quarter), and "start now" for anything that takes time to accumulate. At most 8 rows. Never advise manufacturing evidence: if the work was not done, the fix is to do it (small and real), not to describe it as done. Check whether an employer owns a tool before recommending the person publish it.

**(e) Rewrites.** For a short surface (an About section, a summary, a few bullets), give the whole rewritten version ready to paste, then a brief line-by-line note on what changed and why. For a long one, rewrite the lines that matter most. Every number, name or fact not in the material goes in a `[CONFIRM: what, from whom]` slot; never assert an unbracketed specific the user did not give. Prefer the smaller true claim to the larger unsupported one.

**Scorecard (only on request).** If the user asks to "score this" or for the rubric, add the three axes (craft, product interaction, org leverage) on 1 to 5 with targets, the evidenced total and its coverage, gate status, and the one-sentence note that the weights and bands are synthesis, not a standard or a prediction. Present scores as where to focus, always beside the fixes. Below 60 percent coverage, label the total provisional and do not give a band.

## Scoring discipline (why these rules exist)

- **Separate score from confidence.** A well-argued 4 with no artifact is a 4 at confidence C, which the cap turns into 3. Showing both lets the user see whether to build or to prove.
- **Do not let one artifact carry many dimensions.** A token file supports D5. It supports adoption only if usage evidence comes with it.
- **High craft cannot offset a missing systems gate**, and high leadership cannot offset an inability to reason precisely about behavior. Check D1 or D3 at 3 or above when the leadership dimensions are strong.
- **Staff has several valid shapes** (system architect, cross-team lead, hardest-problem solver, organizational steward). Do not require all. Do not read a missing management title as missing seniority, or a Principal title as Principal scope.
- **Anti-conflation:** beautiful animation is not a motion system; a handoff meeting is not engineering influence; publishing is not adoption; a tool existing is not infrastructure. Full list in `references/evidence-and-gates.md` section 7.
- **Broadcast and studio work translates, but only through a bridge** (`references/portfolio-architecture.md` section 5). Templates, rule sets and tools that let others produce the work count as leverage; the finished package, however good, counts as craft.
- **Never score on prestige** of employer or client, **or on terminology density**. "State machine", "tokens",
  "motion language" and "design system" are evidence only when an artifact, decision, adoption record or outcome
  backs them (KB-S 36.2). Score the separable personal contribution.

## When auditing the user's own work

Before starting, load this user's private overlay if one exists: the `motion-overlay` skill, or else `~/.claude/motion-skills-local/motion-evidence-audit.md`. It holds the user's private context and rules, which take precedence over the defaults here. It never ships with this skill.

- If the user keeps a verified facts file, read it first and take numbers and claims only from entries it marks as verified, respecting any venue limits it records. A fact in the material that the file does not hold is unverified: mark it `[CONFIRM]`.
- If they keep a decisions or rulings log, skim it newest-first before stating ownership, IP or framing rules; a later entry supersedes an earlier one.
- If the supplied copy has unresolved placeholders (`[LINK]`, `[BEFORE/AFTER]`), say the surface is a draft and audit it as text-only rather than hunting for the live site, unless the user gives a URL.
- Never invent a metric. If a claim needs a number nobody has supplied, write `[CONFIRM: ...]` and list it as a next probe.
- Rewrites follow the user's own voice and style rules when they state them.

## References (read when the step calls for it)

| File | Read for |
|---|---|
| `references/rubric.md` | Scale, weights, axis formulas, bands, creative-leadership weights, and for each of D1 to D14 the Senior/Staff/Principal signatures, proof to look for, and false positives |
| `references/evidence-and-gates.md` | Confidence A/B/C/D/U and ceilings, triangulation, leverage and adoption ladders, all gates, Staff versus Principal calibration, attribution ledger, inflation patterns, strip test, nine-link chain |
| `references/portfolio-architecture.md` | What each surface can prove, review order, 13-step case-study spine, above-the-fold rule, media balance, project mix, broadcast bridge, the 20-artifact library, RF-01 to RF-30 |
| `references/claim-rewrites.md` | Verb-to-evidence table, rewrite procedure, adjective-to-rule list, metric forensics, resume work-history questions, worked examples |

Load the rubric for every audit. Load the others on demand: gates when stating a level, portfolio-architecture when advising structure or choosing work orders, claim-rewrites in step 9.

## Hard edges

- No verdict on craft or behavior from text alone; say it is not shown in what you saw.
- No levelling from a total alone. A level call needs the gates.
- No work order that fabricates evidence, backdates, or claims others' work.
- If the surface is a single claim line (one bullet, one headline), do claim triage (a short verdict plus parts d and e) and ask for the artifact behind it.
