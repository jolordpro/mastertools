# 10 · Challenger lessons and ledger

Every prompt in this kit went through at least one `challenger` pass. This file records what those passes changed and why, so the skills don't repeat the mistakes. New lessons get the next ID (AC-L-012, …) and a one-line rule.

**ID namespace:** this kit's lessons use the `AC-L-` prefix. A project that already runs a `challenger` / `shakedown` ledger (`.ledger/ledger.md`) has its own `L-` numbers, and an unprefixed L-number there means that project's entry, not this kit's. When kit lessons are copied into a project ledger, keep the `AC-` prefix.

---

## Ledger

### AC-L-011 · Outcomes logged in defined words
- **Rule:** each application row records:
  - submitted date and posting age at submit;
  - channel, and whether there was a referral;
  - furthest stage, outcome, outcome date, and the exact wording.

  Status words are fixed: sent / closed by employer / rejected / withdrawn / never sent / offer.
- **Why:** field post-mortems of real applications found no submit dates and no rejection reasons, plus an ambiguous "all gone" status. Every cause could only be a hypothesis.

### AC-L-010 · Latency is a first-order failure mode
- **Rule:**
  - Ship-by: a reachable posting gets an application within 7 days of discovery, on current truthful proof.
  - Proof pieces improve the next application.
  - Referral asks go out in parallel with the submit.
  - Research never blocks a live posting (RESEARCH-PLAN R-0).
- **Why:** in those post-mortems, most losses involved packages finished weeks or months after posting, or never sent before the posting closed.

### AC-L-009 · Read the person's existing system before building or challenging
- **Rule:** before drafting or challenging anything for a real candidate, look for their existing records:
  - repos;
  - source-of-truth files;
  - prior audits;
  - the application ledger.

  Build on those, not on assumptions.
- **Why:** a challenger pass assumed a career change that the candidate's existing records contradicted. Those records also held stronger claim checks than this kit.

### AC-L-008 · Pre-flight gate before every submission
- **Rule:** before any slot is spent, run `prompts/preflight-gate-v1.md`. It covers:
  - posting status and lane;
  - literal must-haves;
  - the form and knockouts;
  - the parser;
  - company-level consistency;
  - the red-flag catalog (`13`);
  - the objection map;
  - AI posture;
  - confidential-search exposure;
  - the blind panel.
- **Why:** the lane prompts polish documents. None of them checks the application form, the extracted text, versions already sent to the company, or what each reader will doubt.

### AC-L-007 · AI fluency is proof when asked for
- **Rule:** disclosure stays mandatory. When a posting lists AI use as a requirement, show a specific, honest AI workflow as evidence.
- **Why:** the kit treated AI only as a risk. A live 2026 motion posting at a major streamer lists "proven use of AI tools to speed up asset creation or exploration" as a must-have.

### AC-L-006 · No self-grading
- **Rule:** blind reads and pool rankings must include at least one non-Claude model and, where possible, one human from the target field. Where they disagree with Claude, they win unless Claude can point to a specific line on the page.
- **Why:** AI evaluators prefer AI-written text 67–82% of the time (E16). In this thread, Claude drafted the resume and Claude challenged it.

### AC-L-005 · Validate on real inputs before expanding
- **Rule:**
  - No new lane gets built until the existing pipeline has run end to end on at least one real application: real resume, live posting, real form.
  - Every defect found becomes an eval fixture.
  - Every outcome goes in the ledger.
- **Why:** four prompts and 13 knowledge files were built without ever seeing the candidate's actual resume or a live posting. One target role in the dossier (Manager, Motion Design) had already been filled.

### AC-L-001 · The bar
- **Rule:** the standard is a review on par with an ex-Netflix recruiter turned top resume writer.
  - It invents nothing.
  - It says where the application should go in (channel, timing, which posting gets a scarce slot), not just what it should say.
- **Why:**
  - v1 prompts optimized documents only.
  - Research showed channel and timing move the base rate more than polish (referrals, the 96-hour window, application limits).

### AC-L-002 · Fold every fix into the prompt; diagnose before rewriting
- **Rule:** each new version absorbs all prior challenger findings into the prompt itself, so nothing lives as a separate patch list. Every prompt runs in two stages:
  - Stage 1 diagnoses and asks questions;
  - a STOP gate blocks Stage 2 if a question touches a must-have requirement, a confidentiality issue, or an NDA permission.
- **Why:**
  - v1 rewrote immediately, so it filled gaps with guesses.
  - A rewrite built on a wrong assumption costs more than a question.

### AC-L-003 · Headlines name truthful work; level numbers are stripped
- **Rule:**
  - The LinkedIn headline, hero text, and resume title line name what the person actually does.
  - Target titles go in Open to Work preferences, Skills, the About closing line, and proof pages.
  - Level-numbered titles ("Technical Program Manager 5") are searched and mirrored without the number. The number and pay range only calibrate seniority.
- **Why:**
  - LinkedIn v1 told the user to lead the headline with the target title, which implies a title never held. That is a credibility failure for career changers, and it surfaces in background checks.
  - Mirroring "Technical Program Manager 5" verbatim also matches no recruiter search.

### AC-L-004 · Tag who does each check; public pages stay search-safe
- **Rule:**
  - Every check is tagged `[AI]`, `[AI+WEB]`, or `[ME]`.
  - The model never pretends to watch video, open password pages, run a name search, or test site speed. It asks for key frames, shot lists, and pasted results instead.
  - Public pages (About, hero, headline) never signal a job search when the search is confidential. Availability lives on unlisted proof pages.
- **Why:**
  - Portfolio v1 asked the AI to "watch the reel" and "search your name." Those outputs would have been fabricated.
  - It also wrote an About page announcing the search, which could be seen by the current employer.

## Other mistakes caught (and the fix now in the prompts)

| # | Mistake in an earlier version | Fix |
|---|---|---|
| 1 | Modeled the ATS as keyword matching | Signal audit built on Eightfold's documented features (embeddings, skill recency, title similarity, ideal-candidate calibration) |
| 2 | Told users to mirror posting language heavily | **Mirror budget:** exact terms for filterable nouns only; never copy sentences |
| 3 | Treated "AI-proof" writing as avoiding structure | **Dual-reader rule:** standard structure plus specifics only the person has |
| 4 | Content Credentials recommended without caveats | Limits added (stripping; absence proves nothing; icon misread as "AI"); always paired with a visible credits line |
| 5 | Netflix portfolio-password evidence came from 2024 postings | Marked dated; **VERIFY the current posting** |
| 6 | Treated "Open to Work" public frame as clearly good or clearly bad | Two modes, chosen by confidentiality; the "desperate" view labeled as opinion |
| 7 | Confidentiality rules hard-coded to one person | Generalized to a profile-driven rule; personal details never written into shared files |
| 8 | No path for postings already days old | **Fast lane** for postings ≤4 days old: ship verified facts now, questions later |
| 9 | Fixes listed without effort cost | **Time budget** and per-fix time tags |
| 10 | No check that the rewrite actually reads as intended | **Blind cold read** plus a 3-profile **synthetic pool**, ranked as the matcher and as the hiring manager would |
| 11 | Identity facts drifted between documents | **Consistency table** required in every output |
| 12 | Cuts made silently | **Change log**, one line per cut, with the reason |
| 13 | Critiques without rewrites | **Every flag ships with its fix** |
| 14 | Cover letter treated as always read, or never read | Readership is split; the letter must stand on its own, and no must-have may live only in the letter |
| 15 | "Guarantee" framing | **Honest promise:** zero avoidable failures; best channel; learning loop |

## How to add a lesson

```
### AC-L-0XX · [short name]
- **Rule:** [one or two sentences the skill must follow]
- **Why:** [what went wrong, with the evidence that showed it]
- **Applied in:** [which prompt or skill files changed]
```
