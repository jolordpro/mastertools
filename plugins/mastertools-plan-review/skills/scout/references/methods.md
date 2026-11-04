# SCOUT — Methods: the doctrine with its evidence

**Built by: Opus 4.8 · July 19, 2026 · v0.1**
Sources labeled **(S)** Sourced this build, **(R)** Recalled from training,
**(I)** Inferred. Internal findings cite an internal measured corpus.

Primary sources for this build:
- Anthropic, "How we built our multi-agent research system," Jun 13 2025 —
  https://www.anthropic.com/engineering/multi-agent-research-system **(S — fetched in full)**
- Anthropic, "Effective harnesses for long-running agents," Nov 26 2025 —
  https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents **(S — fetched in full)**
- Anthropic, "Effective context engineering for AI agents," Sep 29 2025 —
  https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents **(S — key claims verified via excerpts)**
- "Deep Research: A Systematic Survey," arXiv:2512.02038, Dec 2025 **(S — existence and scope verified; field anchor)**
- An internal corpus: five research briefs, a review-program plan, a
  numbers-provenance rule, a ground-truth law, an owned-facts doctrine **(internal, measured)**

A build-time finding worth keeping: the July 2026 open-web sweep on "research
best practices" returned mostly SEO-tier recycling of the two Anthropic posts.
The ladder's bottom rung writes about research too. Primary engineering
sources plus the user's own measured corpus are the ore; everything else is echo.

---

## The thirteen principles

### 1. Tokens Are the Budget of Truth
Research quality tracks deliberate effort spent, and effort is measurable.
Anthropic found token usage alone explained 80% of performance variance on the
BrowseComp browsing benchmark, with tool-call count and model choice explaining
most of the rest **(S)**. The practical law: pick the effort tier consciously
(L0–L3), spend it where the question is hard, and never let effort be set by
enthusiasm or anxiety. Under-spending produces confident thinness;
over-spending produces research theater.

### 2. Start Wide, Then Drill
Expert human researchers map the landscape before drilling. Agents default to
the opposite — long, over-specific first queries that return few results —
and Anthropic corrected it by prompting short, broad openings, evaluate, then
progressively narrow **(S)**. The wide pass also surfaces which primary
sources exist, which is what the drill pass fetches.

### 3. Pre-Register the Questions
Write the questions, and what would count as an answer, before the first
search. Deciding afterward what counts as evidence is how observer bias
smuggles in the conclusion you wanted — the same reasoning behind a golden-fixture
checklist (internal). At L2+, also name what would falsify the
working hypothesis; a hypothesis with no death condition is a slogan
(internal law; rhymes with Heuer's Analysis of Competing Hypotheses
from intelligence tradecraft **(R)**).

### 4. The Source Ladder
Primary document > primary human > expert secondary > quality press >
aggregator > SEO farm. This ladder needs stating because default web ranking
fights it: Anthropic's human testers caught their research agents consistently
choosing SEO-optimized content farms over authoritative but lower-ranked
sources like academic PDFs and personal blogs; source-quality heuristics in
the prompt fixed it **(S)**. Corroborated by this build's own sweep: the 2026
"best practices" results were dominated by recycled listicles **(S)**. For
history and postmortems, dead products' primary artifacts (shutdown letters,
founder threads) outrank any retrospective.

### 5. Fetch, Don't Snippet
A load-bearing claim is read from the full page. Snippets are lossy
representations — an internal ground-truth law found three false findings in one
project from grepping flattened exports instead of raw structure (internal),
and the same failure shape applies to judging a source by its search snippet.
Search locates; fetch reads. Anthropic's system treats search results as
pointers for subagents to evaluate and pursue, not as answers **(S)**.

### 6. Search, Never Recall
Anything time-sensitive, product-specific, or plausibly post-training gets a
live source. Training data describes the previous version of the world — an
internal program pre-registered this exact trap: the training corpus is thick
with Frame.io V3, and recalled "facts" would silently describe the old product
(internal). Historical, settled claims are the only exception, and they still
get an (R) label.

### 7. The Model Never Generates Evidence
No invented numbers, no paraphrases wearing quotation marks, no "users say."
A numbers-provenance rule — the model never generates a number — generalizes to
all evidence classes (internal). Quotas are ceilings: a floor quota is a
fabrication pump, because a model told to hit 50 will pad with fakes before it
admits to 38 (internal). Every quote carries a live URL or it is
deleted. Acceptance spot-checks by the human are part of the contract.

### 8. Two Sources or One Label
A load-bearing claim gets a second independent source, or ships explicitly
flagged single-source. This is journalism's two-source rule imported whole
**(R)**, fused with the house confidence labels: **(S)** Sourced, **(R)**
Recalled, **(I)** Inferred, on every claim that carries weight. "Independent"
means independent — two outlets quoting the same press release are one source.

### 9. The Graders Never Met the Hunters
At L2+, verdicts on hypotheses render in a clean context that loads only the
evidence sheets, the board, and the pre-registered kill conditions — never the
hunt. A session grading its own harvest drifts toward FOR: it is invested in
the story its evidence tells, and internal research found personalization
fuels the flattery while structural separation, not prompting, is the
mitigation (internal). Journalism independently invented the same control —
the fact-check desk is not the reporter **(R)**. Anthropic's pipeline
separates roles the same way: a distinct CitationAgent processes the finished
report against sources **(S)**.

### 10. Write the State, Not the Vibe
Multi-session research runs on a state file loaded first and updated last.
Anthropic's long-running-agent work found exactly two dominant failure modes
across sessions — attempting too much at once and leaving undocumented
half-work, and later sessions declaring victory early — and the fix was an
initialized environment: a structured task list with pass/fail statuses, a
progress log, and a session-opening ritual of reading state before working
**(S)**. Two details worth stealing verbatim: statuses flip but entries never
get deleted, and structured formats (they used JSON) resist a model's urge to
"helpfully" rewrite them better than prose does **(S)**. Compaction alone is
not sufficient **(S)**. This is the PROGRAM-STATE.md pattern, independently
validated by Anthropic's production experience.

### 11. Interleave Thinking With Results
After every result batch: what did this answer, what remains open, what is the
next best query. Anthropic's subagents use interleaved thinking after tool
results to evaluate quality, identify gaps, and refine the next move, and it
measurably improved adaptation **(S)**. The anti-pattern is the blind salvo —
firing a fixed list of queries written before any results came back.

### 12. Stop Rules Beat Stamina
The two native failure modes are opposites: scouring endlessly for sources
that don't exist, and declaring victory before verification **(S — both
documented in Anthropic's systems)**. The countermeasure is the same for both:
done-conditions written before the hunt, and an explicit stop-reason at the
end — questions answered, marginal searches repeating, or budget hit. Saying
which one fired is part of the deliverable. "Further passes hit diminishing
returns" is a legal and valuable sentence (always-on rules), but it needs
evidence: it holds only when a fresh adversarial pass across the whole question
finds nothing that changes the answer.

### 13. The Case-Against Ships With the Findings
At L2+, every deliverable carries a "where this is weak" section: the
single-source claims, the unverified owned facts, the searches that came back
empty, the alternative reading of the evidence. Research that cannot name its
own soft spots isn't finished — it's advocacy (internal law;
rhymes with the intelligence community's key-assumptions check **(R)**).

### 14. Conflicts Are Findings
Corroboration usually produces partial disagreement, not clean confirmation.
The default failure is silent: a model picks the source that fits the story it
is already telling, or blends both into a sentence true of neither. Neither
move leaves a trace. So the rule is procedural — both readings named, ranked by
ladder rung and date, with the finding's dependency stated and the settling
evidence identified. This is the intelligence community's competing-hypotheses
discipline applied one level down, at the source rather than the conclusion
**(R)**. It also protects the case-against (13), which cannot cite a conflict
that was resolved before anyone saw it.

### 15. Sources Have Dates Too
Principle 6 stops the model quoting a stale memory. It does nothing about a
stale page, and search engines surface old pages without prejudice. The **(S)**
label conflates two different claims — *I found this on the web* and *this is
true now* — and for the questions asked most (what does this tool do, what
does it cost, who runs it, what version is current) the second is the one that
matters. Hence: every source carries its own date; anything version-, price-,
capability-, or personnel-related from before the current product cycle is
**(R)** until confirmed against a current page. An internal program pre-registered the same
trap from the other direction (internal) — the training corpus is
thick with Frame.io V3, and so is the open web.

### 16. The Locked Door
The primary source often exists and cannot be read: paywall, login wall,
robots, dead link. The tempting move is to cite the secondary that quotes it
and let the citation imply direct access. That is a quiet upgrade of evidence
quality, and it compounds — two outlets quoting one press release read as
corroboration while being a single source (8). So: say the door was locked,
label the workaround **(S-via)** with the intermediary named, never promote it
to a direct citation, and count all quotations of one primary as one source.

### 17. The Premise Is Not Evidence
Requests arrive with facts already inside them: *Frame.io does X, so research
whether Y.* Treating X as established and researching only Y is
conclusion-shaped research that never contradicts any other principle, which is
what makes it dangerous. The requester is a primary human source in their own
domain and also the person the system exists not to flatter — the internal finding
that personalization fuels sycophancy applies with full force to their own
assertions (internal). So an embedded claim is labeled **(R-asserted)** and
verified like any other load-bearing claim, and a failed premise is reported
first, ahead of the answer to the question as asked.

### 18. Read the Source Laterally
Assigning a ladder rung by reading the source's own pages is the method that
loses. Wineburg & McGrew compared professional fact-checkers, university
historians, and Stanford undergraduates evaluating live websites: the
historians and students read *vertically* — staying on the page, judging it by
its own contents and polish — while fact-checkers read *laterally*, leaving
after a quick scan to investigate the site from outside it. The fact-checkers
reached more accurate credibility judgments in less time (Teachers College
Record, 2019) **(S — corroborated across multiple independent sources)**.
Field experiments in high-school and university settings replicate the effect
when the strategy is taught **(S)**. Transfer to an agent's retrieval
affordances is argued, not measured **(I)** — but the underlying mechanism
(on-page cues are controlled by the source; off-page reputation is not) does
not depend on the reader being human. Scout's move: rung assignment is its own
small hunt. One lateral query per unfamiliar load-bearing source.

---

## Failure-mode table

Every rule above kills a documented failure. The map:

| Failure | Documented where | Killed by |
|---|---|---|
| Fabricated quotes/numbers under quota pressure | internal program (internal) | 7 |
| SEO-farm drift | Anthropic human testers **(S)** | 4 |
| Snippet-only reading | Ground-truth law (internal) | 5 |
| Stale recall presented as fact | internal program (internal) | 6 |
| Endless scouring for nonexistent sources | Anthropic **(S)** | 12 |
| Premature victory | Anthropic harnesses **(S)** | 10, 12 |
| One-shotting a multi-session program | Anthropic harnesses **(S)** | 10 |
| Self-grading flattery | internal research (internal) | 9 |
| Over-specific first queries | Anthropic **(S)** | 2 |
| Effort mismatched to question | Anthropic **(S)** | 1, tier ladder |
| Conclusion-shaped evidence gathering | internal doctrine (internal) | 3 |
| Findings without weaknesses | internal law (internal) | 13 |
| Conflict resolved by preference, silently | shakedown SD-002 | 14 |
| Stale page labeled as current fact | shakedown SD-003 | 15 |
| Secondary citation implying primary access | shakedown SD-013 | 16 |
| Researching downstream of an unverified premise | shakedown SD-005 | 17 |
| Self-graded verdicts asserted as clean | shakedown SD-007 | 9 + loop step 6 |
| Rung assigned by reading the page itself (vertical) | Wineburg & McGrew (S) | 18 |
| Load-bearing claims from search excerpts, unfetched | scout's own pass 2, July 19 (in-house) | 5 + law 2 |

## Depth and breadth — when to go parallel

Anthropic's headline result: a multi-agent system (lead + parallel subagents)
beat a single agent by 90.2% on their internal research eval, specifically on
breadth-first queries with many independent directions — at roughly 15× the
tokens of a chat **(S)**. The transfer for scout, which usually runs as one
agent: parallelism is a property of the plan, not just the architecture. At L2+,
decompose into independent lanes with an objective, an output format, source
guidance, and boundaries per lane — the exact delegation contract Anthropic
found necessary to stop subagents duplicating work **(S)**. One agent working
lane-by-lane against a written decomposition captures most of the benefit;
when true subagents are available (Cowork, Claude Code), the same lane specs
become their briefs unchanged.

## Evaluating research output

For grading research quality — scout's own evals, or any evidence sheet —
Anthropic's production rubric transfers whole: factual accuracy (claims match
sources), citation accuracy (cited sources match claims), completeness
(all pre-registered questions addressed), source quality (ladder position),
and tool efficiency (right effort for the tier) **(S)**. A single grading pass
with that rubric beat multiple specialized judges for consistency **(S)**.
Start evaluating with ~20 test queries, not hundreds — early changes have
effect sizes visible at small samples **(S)**. Judge end states, not paths:
two valid hunts can take different routes to the same finding **(S)**.
