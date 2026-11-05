# 02 · Company dossier: Netflix

**Last verified:** November 2026
**Recheck-by:** February 2027. Re-verify portal facts for every application.

Format: **fact** — status (VERIFIED or ASSUMED) — source type.

---

## 1. Application stack

- **Careers flow:** `explore.jobs.netflix.net`, built on Eightfold (portal links to `netflix.eightfold.ai`). jobs.netflix.com routes there. — VERIFIED — live portal configuration.
- **Back end:** Netflix's own posting for an ATS configuration architect names Eightfold and Workday. — VERIFIED — Netflix job posting. Requisition IDs look like "JR43433" — ASSUMED to be Workday-style.
- **Resume matching:** uploading a resume matches the candidate to positions, and the match score is hidden from candidates (`hide_match_score: true`). The candidate-side recommendation threshold is 4.0 stars. — VERIFIED — portal configuration.
- **Required fields:** first name, last name, resume. The profile also has a LinkedIn URL field. — VERIFIED — portal configuration.
- **After applying:** candidates are asked to review the profile built from their resume and add any missing work or education. — VERIFIED — portal configuration. **Action:** check parsed titles, employers, dates, and skills; re-upload as DOCX if anything is wrong.
- **Application limit:** the configuration sets `max_applications_apply: 2`. — VERIFIED that the setting exists; ASSUMED meaning (the scope and time window aren't stated). **Action:** treat application slots as scarce until a recruiter confirms otherwise. Choosing which roles to spend them on is a one-way door.
- **Referral flow:** a referral sends the candidate an email asking them to apply; they aren't considered until they do. — VERIFIED — portal configuration.
- **Supporting documents:** the portal reportedly lets candidates upload extra documents such as a cover letter or portfolio. — ASSUMED — third-party walkthrough.
- **Onsite vs. remote:** 313 of 397 listed roles were onsite and 84 remote when checked. — VERIFIED — portal snapshot, Nov 2026.

## 2. Titles and levels

- Many Netflix titles carry level numbers: "AI Engineer 6," "Software Development Engineer in Test 5," "Technical Program Manager 5," "TPM (L5)." Some use traditional names: "Senior Motion Designer," "Production Designer." — VERIFIED — portal and postings.
- Netflix introduced five engineering levels, Engineer 3 through Engineer 7. — B — Levels.fyi community.
- Levels.fyi maps L5 TPM to "Senior TPM." — C — self-reported data.
- **Rules:**
  - Search terms use the title without the number.
  - The level number plus the posted pay range calibrates how senior claims should sound.
  - Never put a level number in a headline or in Open to Work titles.

## 3. Pay ranges seen in postings (directional; mostly mirror sites)

| Role | Range | Source |
|---|---|---|
| Technical Program Manager 5 (various) | $290k–$460k | Multiple mirrors |
| Senior Motion Designer, Live | $310k–$420k | Job mirror, 2026 |
| Manager, Motion Design, Brand Creative Studio | $198k–$310k | Ladders listing. **FILLED:** removed by the employer on 7/30/2026 (Entertainment Careers) |
| Production Designer, Brand Creative Studio | $139k–$221k | Mirrors, June 2026 |
| Senior Product / Visual Designer, Emerging Creative | $350k–$520k | Mirrors, 2026 |
| Designer, Global Consumer Products Creative | $147k–$242k + equity | Mirror, June 2026 |

For pay strategy and leveling, hand off to `motion-design-career-strategist`.

**Rule:** before using a slot, re-run the portal check (current roles, work-location field, posted pay). The portal API is at `explore.jobs.netflix.net/api/apply/v2/jobs?domain=netflix.com&query=<term>`.

## 4. Portfolio expectations (creative roles)

- **Earlier postings asked for the portfolio together with its password:**
  - Senior Motion Designer (2024): strongly recommended submitting a portfolio and password.
  - Product Design Manager: required an updated portfolio link and password.
  - Staff Product Designer, Ads Platform: strongly recommended including the portfolio with its password.
  - — VERIFIED from mirrors (older postings).
- **Current Brand Creative Studio postings** (2026) say a strong portfolio is required:
  - Production Designer: solid fundamentals and work inside brand systems.
  - Senior Manager, Production Design Lead: systems thinking and high-volume execution.
  - Manager, Motion Design: motion across campaigns, systems thinking, and multi-format work.
  - — VERIFIED — mirrors.
- **Product Brand Designer posting:** link the portfolio, reel, or work samples in the resume or on LinkedIn. — VERIFIED — mirror.
- **Netflix Animation early-career guidelines** (Netflix-hosted page) — VERIFIED:
  - Name, contact info, and portfolio URL (with password if protected) always visible.
  - Tailor the work to the role.
  - The first minute of a reel must catch the reviewer's eye.
  - Include breakdowns, with software noted on screen.
  - Contact info at the start and end of the reel.
- **Rules:**
  - Quote the current posting's exact portfolio instructions; never assume.
  - Gate only what needs gating.
  - Test the password in a private window.
  - Tell reviewers which case study to open first.

## 5. Culture memo (June 2024, "The Best Work of Our Lives")

- **Four principles:** the Dream Team; people over process; uncomfortably exciting; great and always better.
- **Eight values:** selflessness, judgment, candor, creativity, courage, inclusion, curiosity, resilience.
- **Keeper test:** would a manager fight to keep this person?
- New under Judgment: "You spend our members' money wisely."
- **How to use it:** show the values through outcomes and stories. Never list them as adjectives, and never recycle the memo's vocabulary.

## 6. Hiring process

- Generally described as manager-led and decentralized. — ASSUMED, from a third-party guide.
- Interviews reportedly test candor live, and include culture-memo questions ("What did you take from our culture memo? What do you disagree with?"). — C, prep sites.
- A portfolio presentation round of about 45–60 minutes is typical at big tech (EST, from the strategist reference). — ASSUMED for Netflix; ask the recruiter.
- **Open research:** see `11-research-backlog.md` (interview loop).

## 7. Unknowns to resolve

- Scope and time window of the 2-application limit.
- Whether Eightfold scores cover-letter text.
- Whether Netflix uses Eightfold's AI Interviewer.
- Current design interview loop by team (Brand Creative Studio, Product, Animation, Games).
- Whether postings link from LinkedIn (making LinkedIn's Skills Match usable as a free check).
