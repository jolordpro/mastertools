# 03 · Resume lane

**Prompt:** `prompts/resume-challenge-v2.md` (ready)
**Evidence:** `01-how-screening-works.md`, `02-company-dossier-netflix.md`

---

## What the resume has to do

1. **Get surfaced.** Survive parsing, meet the filters (skills, title, education, certifications, years, location), and score well on a learned matcher like Eightfold's.
2. **Survive the skim.** Titles, employers, dates, and the first words of each bullet carry a roughly 7-second first pass.
3. **Win the deep read.** Specific, quantified, clearly owned outcomes at the level the posting signals.
4. **Hold up later.** Every line must survive the interview and the background check.

## Method (the v2 passes)

**Stage 1: diagnose**

| Pass | What it does |
|---|---|
| 1. Decode the posting | Must-haves, preferred, the problem behind the hire, exact vocabulary (acronym and full form), culture signals. With several postings, rank fit and plan the scarce application slots. Read seniority from level numbers and pay ranges. |
| 2a. Parse test | Render as plain text; flag anything that scrambles, drops, or misorders fields. |
| 2b. Signal audit | Rate each matcher signal MOVABLE or FIXED and strong/medium/weak: skills overall, recent skills, current title, title history, company/industry, comparison-profile similarity, location/work type. Fix weak movable signals; send weak fixed signals to warm-path notes. |
| 2c. Coverage | Each requirement marked EXACT / CLOSE / MISSING. Every must-have is named and shown in a bullet, ideally in the most recent role. |
| 2d. Comparison profiles | Profiles of 2–5 people now in the role (names removed). Adopt shared vocabulary and structure only where true; never copy phrasing. |
| 2e. Sector translation | Translate only true equivalents; flag anything that would overstate. |
| 3. 7-second skim | One-sentence recruiter conclusion; fix the top third and the bullet openings. |
| 4. Blind pool test | Cold read from the page alone, plus 3 SYNTHETIC competitors ranked twice (matcher view, hiring-manager view). Run on the draft and again on the revision. |
| 5. Line audit | KEEP / SHARPEN / MERGE / CUT for every line; X-Y-Z bullets where the source supports numbers; reorder by relevance. |
| 6. Stand-out and authenticity | 2–3 differentiators in the top third; AI-tell sweep. |

**Stage 2: rewrite**
- Revised resume, with a re-run cold read.
- Top 10 changes.
- Post-apply checklist (check the parsed profile; file format).
- LinkedIn alignment.
- Warm-path notes.
- Change log.

**Fast lane:** if the posting is 4 days old or newer, skip the gate for non-blocking gaps and ship verified facts now.

## Rules specific to the resume

- Mirror only filterable nouns. The target title appears verbatim in the headline or summary *only as the target*, never as a past title.
- Must-have skills go in the most recent role wherever that's truthful. Eightfold computes a separate score on recent skills.
- Length: one page or two depending on seniority and how much evidence there is. Any line on page two must outrank what it displaces.
- No hidden text, ever.

## v1 → v2: what changed and why

| v1 | v2 | Why |
|---|---|---|
| Modeled the ATS as keyword search | Signal audit built on Eightfold's actual features | Netflix uses a learned matcher |
| Exact-term coverage as the core | Mirror budget; specifics over mirroring | Tailoring lost its signal (Galdin & Silbert); title-match data is still strong (Jobscan) |
| Only humans penalize AI text | Dual-reader rule | AI evaluators prefer AI-written text (Xu et al.) |
| One-shot output | Two stages with a gate; fast lane | Avoids rewrites full of placeholders; timing data |
| No portal mechanics | Parsed-profile check, application-limit awareness, file format | Netflix portal configuration |
| Grades itself | Blind cold read and synthetic pool | Removes self-grading bias |
| Level numbers unhandled | Stripped from search terms; used to calibrate seniority | Netflix title conventions |
