# Apply Craft — Build Plan

**Status:** Draft for approval · 2026-11-05
**Owner:** Jo
**Evidence current as of:** November 2026

---

## 1. What this is

A suite of Claude Code skills that guides a creative professional through the whole application journey: choosing targets, preparing a public footprint, tailoring each application, choosing the channel, following up, and interviewing.

- **First lane:** motion design (brand and launch motion, product and UI motion, 3D and broadcast motion).
- **First company:** Netflix. It has a researched dossier.

The suite turns this thread's four challenger-tested prompts and its evidence base into reusable, maintainable skills. Every skill can serve any user, because person-specific facts live in a profile file, not in the skill logic.

## 2. The honest promise

**No skill can guarantee an interview.** Some deciding factors are outside any document:
- fixed signals such as past employers, actual titles, and tenure (Eightfold's match model weighs these directly);
- the competing pool, internal candidates, and requisition freezes;
- timing.

A suite that claims a guarantee will push users to overstate, and overstatement gets caught in interviews and background checks.

**What the suite promises instead:**

1. **Zero avoidable failures.** Before an application ships, it clears every gate:
   - safe to parse;
   - every must-have covered;
   - titles and dates consistent everywhere;
   - no AI tells;
   - no confidentiality leaks;
   - working links and passwords.
2. **The best available channel.** Priority roles get a warm-path attempt (a referral or a direct note) in addition to the portal.
3. **Speed when it matters.** Postings 4 days old or newer go through the fast lane.
4. **A learning loop.** Every application is logged. After about 10, the funnel shows where the losses happen:

| Symptom | Likely cause | Skill to re-run |
|---|---|---|
| No response, portfolio link never opened | Not surfaced by screening | resume, target |
| Portfolio opened, no screen | Proof or level mismatch | portfolio, proof-piece |
| Recruiter screen, no next round | Positioning, level, or pay expectations | target, interview |
| Late-stage losses | Interview performance | interview |

**Metrics, tracked in the ledger** (targets are proposals to recalibrate after a baseline of 10 applications):

| Metric | Proposed target |
|---|---|
| Gate pass rate before submitting | 100% |
| Warm-path attempt rate on priority roles | ≥ 80% |
| Portfolio open rate (tracked links) | Track it; investigate if under 50% |
| Interview rate per application, by channel | Baseline the first 10, then improve |

**Context benchmarks.** These are directional, labeled in `knowledge/12-evidence-library.md`, and never shown to users as promises:
- ResumeGo field experiment: callback rates of 10.7–16.4% depending on cover letter.
- TalentWorks: about 2% interview odds for a typical applicant.
- Jobvite (reported secondhand): referred candidates hired at about 30% vs about 7% from job boards.

## 3. Architecture

```
                         ┌───────────────────────────────┐
                         │      apply-craft  (router)    │
                         │  reads profile + ledger,      │
                         │  detects journey stage,       │
                         │  routes, enforces shared gates│
                         └───────────────┬───────────────┘
        ┌──────────────┬────────────────┼────────────────┬──────────────┐
   apply-target   apply-company-intel  apply-resume   apply-cover-letter  apply-linkedin
        │                                                                     │
   apply-portfolio   apply-reel (motion)   apply-proof-piece   apply-warm-path
        │
   apply-interview   apply-followup

  Shared:  knowledge/  (rules + evidence)     templates/ → data/ (profile, ledger, dossiers)

  Existing skills the suite hands off to (no duplication):
    motion-design-career-strategist  → pay, leveling, offers, negotiation, tool choices
    challenger                       → plan QA; whole-suite review every quarter
    clear                            → prose polish (cover letters, About pages)
    composition                      → critique of reel key frames and thumbnails
    design-taste / frontend-design   → portfolio site UI
    deep-research                    → research sprints for backlog lanes
    skill-creator                    → evals and benchmarking
```

## 4. The journey and which skill runs

| # | Stage | Skill | Main output |
|---|---|---|---|
| 1 | Decide where to aim | apply-target (+ motion-design-career-strategist) | Ranked roles, role family, plan for limited application slots |
| 2 | Learn the company | apply-company-intel | Dossier: ATS and front-end stack, portal quirks, levels, pay ranges, process, portfolio rules |
| 3 | Get the public footprint ready | apply-linkedin, apply-portfolio, apply-reel | Search-safe profile and site, reel, proof map |
| 4 | Tailor each application | apply-resume → apply-cover-letter → apply-proof-piece | Tailored resume, letter, unlisted proof page, tracked link |
| 5 | Choose the channel | apply-warm-path | Referral ask, recruiter or hiring-manager note, connection note |
| 6 | Submit and log | apply-craft (router) | Ledger entry; checklist for the profile the portal builds after you apply |
| 7 | After applying | apply-followup | Follow-ups, ghosting handling, rejection learning, funnel stats |
| 8 | Interviews | apply-interview | Screen prep, portfolio presentation, craft deep dive, culture prep |
| 9 | Offer | motion-design-career-strategist (existing) | Offer evaluation and negotiation |

## 5. Skills: scope sheet

> **Status (2026-11-05):** this 12-skill sheet is the original proposal. §11c proposes slimming it to 3 new skills plus modes of the existing career skills. Until the owner rules, treat this sheet as the full scope inventory, not the build list.

Each skill's `SKILL.md` stays short. Detail lives in `references/`, which loads only when needed.

### 0. `apply-craft` — router (NEW)
- **Purpose:** the single entry point.
  - Detects the stage from the request and the ledger, then routes.
  - Enforces shared conventions.
  - Writes ledger entries.
  - Never submits an application on its own.
- **Triggers:** a pasted job posting; "apply to…", "help me get an interview", "where am I losing?"
- **Inputs:** `data/profile.md`, `data/ledger.md`, the request.
- **Status:** design only.

### 1. `apply-target` — choose where to aim (SEEDED)
- **Scope:**
  - decode the role family across 2–5 postings;
  - rank fit;
  - read level signals (Netflix level-numbered titles, posted pay ranges);
  - check posting age and decide on the fast lane;
  - plan around application limits (Netflix's portal has a limit setting of 2, scope unknown);
  - set the location and work-type stance (most Netflix roles are onsite).
- **Seeded from:** resume v2 Pass 1, LinkedIn v2 Pass 1, `knowledge/02`, `knowledge/08`.
- **Open research:** ghost-job prevalence and repost signals; how to detect posting age on Eightfold portals; what the application-limit setting actually covers.

### 2. `apply-company-intel` — dossiers (SEEDED)
- **Scope:** build and refresh one dossier per company using `templates/company-dossier-template.md`. Portal facts are re-verified for every application.
- **Seeded from:** `knowledge/02-company-dossier-netflix.md`.
- **Open research:** dossiers for Apple, Google, Meta, Amazon, Disney, Spotify, Pixar/Lucasfilm, the major AI labs, top motion studios (Buck, Gunner, Oddfellows, etc.), and agencies.

### 3. `apply-resume` (READY)
- **Source:** `prompts/resume-challenge-v2.md` and `knowledge/03-resume.md`.
- **Key mechanics:**
  - two stages with a stop gate, plus the fast lane;
  - a "movable vs. fixed" signal audit;
  - a blind cold read and a ranking against synthetic competing applicants;
  - a "mirror budget" (match the posting's exact words only for searchable nouns);
  - level-number handling;
  - checking the profile the portal builds after you apply.

### 4. `apply-cover-letter` (DRAFT)
- **Source:** `prompts/cover-letter-challenge-v2-draft.md` and `knowledge/04-cover-letter.md`.
- **Key mechanics:**
  - swap test (would the sentence still work with a competitor's name?);
  - costly-signal test (could an AI have written this sentence for anyone?);
  - fit with the resume;
  - warm-path notes;
  - a recommendation on whether a proof piece is worth it.
- **To do:** one challenger pass before it's marked ready.

### 5. `apply-linkedin` (READY)
- **Source:** `prompts/linkedin-challenge-v2.md` and `knowledge/05-linkedin.md`.
- **Key mechanics:**
  - headline names truthful work (AC-L-003);
  - target titles go in Open to Work preferences;
  - edits made with network sharing turned off;
  - Spotlights behaviors;
  - scam screen.

### 6. `apply-portfolio` (READY)
- **Source:** `prompts/portfolio-challenge-v2.md` and `knowledge/06-portfolio-and-site.md`.
- **Key mechanics:**
  - checks tagged by who does them: [AI], [AI+WEB], [ME];
  - creative vs. work-sample mode;
  - About page safe for a confidential search;
  - verification kit;
  - presentation outline.

### 7. `apply-reel` — motion lane (SEEDED; RECOMMENDED SPLIT)
- **Scope:**
  - review from key frames plus a shot list (the model cannot watch video);
  - edit list with timecodes;
  - variants by sub-lane (brand/launch, product/UI, 3D/CG, broadcast/title);
  - a hook to the `composition` skill for frame critique;
  - the "first 20 seconds" test on real people;
  - hosting and privacy settings.
- **Seeded from:** `knowledge/07-reel-and-motion-lane.md`.
- **Open research:** reel norms by sub-lane in 2026; Vimeo vs. YouTube privacy and quality; interactive pieces (Rive, Lottie) inside portfolios.

### 8. `apply-proof-piece` (SEEDED)
- **Scope:**
  - an unlisted proof page per priority posting (requirements mapped to deep links);
  - a tracked link per application;
  - the LinkedIn Featured pick;
  - a targeted work sample for top roles;
  - a confidentiality scrub.
- **Seeded from:** portfolio v2 #10, LinkedIn v2 #10, the cover letter "proof-piece call."

### 9. `apply-warm-path` (SEEDED; RESEARCH SPRINT)
- **Scope:**
  - referral asks, plus notes to recruiters and hiring managers (each under 600 characters);
  - connection notes (300-character limit);
  - Spotlights behaviors (Open to Work, engaging with the company's page, connections at the company);
  - InMail reply habits;
  - Netflix's referral flow (the referred person must still apply);
  - scam screen.
- **Open research:** referral etiquette at big tech; outreach that actually gets replies; motion-community channels (to verify); alumni networks.

### 10. `apply-interview` (NEW; RESEARCH SPRINT)
- **Scope:** recruiter screen; hiring-manager screen; portfolio presentation; craft deep dive; app critique; take-home or live exercise; culture round (Netflix culture memo, keeper test); AI interviewers.
- **Seeded from:** portfolio v2 #11 (presentation outline); the strategist reference §9.3 (EST); Netflix culture values in `knowledge/02`.
- **Open research:** the current Netflix design interview loop; use of AI interviewers (Eightfold launched one in 2025); take-home norms and spec-work ethics.

### 11. `apply-followup` (NEW; RESEARCH SPRINT)
- **Scope:** follow-up timing; handling ghosting; asking for rejection feedback; ledger analytics; a whole-suite challenger review every 10 applications.
- **Open research:** follow-up timing data; ghosting rates; recruiter norms for rejection feedback.

### Offers and negotiation
Handled by the existing **`motion-design-career-strategist`**. Don't duplicate it; the router hands off.

## 6. Shared conventions (every skill inherits these)

Defined in `knowledge/00-principles-and-guardrails.md`. In brief:
- truth is the ceiling; never rename titles;
- confidentiality rules come from the user's profile;
- AI disclosure; no hidden text;
- mirror budget; dual-reader rule (clean structure for machines, specifics for humans);
- voice rules;
- VERIFIED/ASSUMED labels and A–D evidence strength;
- actor tags; two-stage gate; fast lane; time budget;
- consistency table; change log; ledger write-back;
- never auto-submit.

## 7. Claude Code layout (proposed)

```
apply-craft/                     # plugin root, or ~/.claude/skills/
  skills/
    apply-craft/SKILL.md
    apply-target/SKILL.md
    apply-company-intel/SKILL.md
    apply-resume/
      SKILL.md                   # short: when to use, inputs, stages, outputs
      references/
        method.md                # passes, from prompts/resume-challenge-v2.md
        evidence.md              # slice of knowledge/01, 03, 12
    apply-cover-letter/…
    apply-linkedin/…
    apply-portfolio/…
    apply-reel/…
    apply-proof-piece/…
    apply-warm-path/…
    apply-interview/…
    apply-followup/…
  shared/
    knowledge/                   # this folder's knowledge/ files
    templates/
  data/                          # per-person, gitignored, never shared
    profile.md
    ledger.md
    dossiers/netflix.md
```

**Build rules:**
- Keep each `SKILL.md` lean and push detail into `references/`. The skill-creator skill has the current sizing guidance; check it when building.
- Keep user data out of skill folders, so the suite can serve anyone and no one's job search leaks.
- Skill names never contain "claude" or "anthropic."
- Each skill's description states what it maximizes ("interview odds"), never a guarantee.

## 8. Freshness protocol (keeping it current)

- Every evidence claim carries a date, a strength (A–D), and a `recheck-by` date.
- **At run time:** if a claim behind a decision is past its `recheck-by`, the skill re-verifies it with web search, or labels it ASSUMED and says so.
- **Company dossiers:** portal facts are re-verified for every application. They change; Netflix's own postings have shifted wording between 2024 and 2026.
- **Quarterly:** run `deep-research` on backlog items, then a `challenger` pass on the whole suite.
- **Baseline:** compiled November 2026. Fast-moving items should be rechecked by February 2027.

## 9. Build phases

| Phase | Build | Done when |
|---|---|---|
| 0. Foundation | Profile template, ledger, guardrails reference, evidence library, router skeleton | The router reads profile and ledger and routes a pasted posting to the right skill |
| 1. Port ready prompts | apply-resume, apply-linkedin, apply-portfolio | Each passes its eval fixtures (§10) |
| 2. Complete the application kit | apply-target, apply-company-intel, apply-cover-letter (after a challenger pass), apply-proof-piece | The Netflix dossier refreshes per application; the cover letter passes the challenger |
| 3. Motion depth | apply-reel, apply-warm-path (research sprint first) | Reel review works from key frames; warm-path notes pass the swap test |
| 4. Late funnel | apply-interview, apply-followup (research sprint first) | Presentation outline and mock panel work; ledger analytics produce the funnel diagnosis |
| 5. Pilot and recalibrate | Whole-suite challenger pass; 10 real applications | Metrics baselined; targets reset from real data |

## 10. Evals: how we know each skill works

Build fixtures with **planted defects**. Each skill must catch its own.

| Skill | Planted defects |
|---|---|
| Resume | Hidden white text; a renamed past title; a must-have that appears only in the skills list; dates that don't match LinkedIn; AI-tell bullets; a table or column layout; a client-identifying metric; a level number copied into the headline |
| Cover letter | Fails the swap test; restates the resume; stock opener; 650 words; tone that doesn't match the resume |
| LinkedIn | Headline claims a title never held; public Open to Work during a confidential search; level numbers in Open to Work titles; must-have skills not attached to the current role |
| Portfolio | No summary blocks; About page announces the job search; client imagery in a case study; broken password page; reel shot list without roles; undisclosed AI work |

**Pass bar:**
- catches 100% of critical defects (confidentiality, fabrication, hidden text);
- catches at least 90% of the rest;
- invents zero facts;
- labels every check it couldn't perform.

Run with `skill-creator`.

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Overpromising | The honest promise above; metrics in the ledger |
| Stale evidence | `recheck-by` dates; verification at run time; quarterly refresh |
| Bias from vendor-run studies | A–D labels; decisions anchored on A/B evidence where possible |
| The AI grading its own work | Blind cold read; synthetic pool ranking; optional review in a fresh chat |
| Confidentiality leak | Rule driven by the profile in every skill; critical eval fixtures |
| One-way doors (submitting; limited Netflix slots) | The router asks before anything is marked submitted; never auto-submits |
| Limits on what the AI can do (can't watch video, can't log in) | Actor tags; key-frame workflow |
| Scams during a search | Scam screen in warm-path and LinkedIn |

## 11b. Changes from challenger pass 4 (2026-11-05)

- **New gate:** `prompts/preflight-gate-v1.md` runs before every submission (stage 6), and the router enforces it (AC-L-008). It covers:
  - the application form;
  - parser output;
  - versions already sent to the same company;
  - the red-flag catalog (`knowledge/13`);
  - the objection map;
  - a blind panel with non-Claude models (AC-L-006).
- **Phase 0.5, before Phase 1 is "done":** run resume → LinkedIn → portfolio → gate on one real application. Every defect found becomes an eval fixture (AC-L-005).
- **AI posture:** disclosure plus proof of AI fluency when the posting asks for it (AC-L-007).
- **Lanes:** a "late lane" (posting more than 21 days old: warm path first) joins the fast lane.
- **Backlog additions:**
  - other ATS behavior (Greenhouse, Ashby, Lever, iCIMS);
  - sourcing tools that index public portfolios (to verify);
  - a references-and-verification plan for executives in a confidential search.

## 11c. Research plan and integration (2026-11-05, later)

- **The research program** is in `RESEARCH-PLAN.md`:
  - companies, including Pinterest, Meta, Google/YouTube and Buck;
  - the machine lane (ATS and AI tools);
  - the review lane (insider testimony);
  - phases R0–R6, with rule R-0: research never blocks a live posting.
- **Integration before building more skills.** A candidate's existing career system may already hold a source of truth, claim gates and job state. For the first user it does, so the proposed architecture slims from 12 new skills to **3 new skills**:
  - `apply-preflight`: the merged gate, which calls the existing claim tools;
  - `apply-intel`: company dossiers plus the review lane;
  - `apply-followup`: outcomes and the learning loop.

  The other lanes become modes or references of the existing career skills. Owner decides.
- **New lessons:** AC-L-009 (read the existing system first), AC-L-010 (latency), AC-L-011 (log outcomes). New flags J1–J12 in `knowledge/13`.

## 12. Decisions needed (approval checklist)

1. **Names:** suite `apply-craft`, skills prefixed `apply-`? Or your naming.
2. **Lanes:** motion first. Which lanes come next: brand/graphic, product/UI, 3D/CG, editorial/video, art direction?
3. **Reel:** a separate `apply-reel` skill (recommended), or keep it inside portfolio?
4. **Offers:** route to the existing `motion-design-career-strategist` (recommended) rather than duplicating it?
5. **User data:** a `data/` folder per person, gitignored (recommended)?
6. **Build order:** phases 0–5 as above?
7. **Research sprints:** run them now with `deep-research` before phases 3–4, or as each phase starts?
8. **Promise wording:** skill descriptions say "maximizes interview odds," never "guarantees"?
