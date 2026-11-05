# Portfolio + Personal Site Challenge v2

**Status:** ready. Challenger-tested (this pass produced AC-L-004).
**Feeds skills:** `apply-portfolio`, `apply-reel` (Pass 4 and output 9), and `apply-proof-piece` (outputs 10 and 14).
**Knowledge:** `00`, `06`, `07`, `08`, `09`, `12`.

## Changes from the version in the thread

- The confidentiality rule now comes from the user's profile instead of one person's background.
- **Kistler line corrected:** the lawsuit is against Eightfold, the platform behind Netflix's portal, not against Netflix.

## Before porting

- If `apply-reel` becomes its own skill (PLAN decision 3), move Pass 4 and output 9 there. Keep a one-line handoff in the portfolio skill.
- **Proof pages** (output 10) and **application packaging** (output 14) belong to `apply-proof-piece`.

## Prompt

```text
PORTFOLIO + PERSONAL SITE CHALLENGE v2
(Evidence current as of Nov 2026)

ROLE
Review my portfolio site (Home, About, case studies or work samples, reel, Contact) and any outside portfolio pages. Don't defend them. Judge them the way they are actually judged:
- a recruiter with about 3 minutes,
- a hiring manager with 5-10 minutes,
- a panel watching me present,
- search engines and AI tools assembling a picture of me,
- anyone checking that the work is mine.
Stage 1 diagnoses and asks. Stage 2 rewrites.

PRINCIPLE
The resume claims; the portfolio proves. Every major claim on my resume and LinkedIn needs proof here. Every piece here must be clearly mine, clearly scoped, and checkable.

WHO DOES WHAT
Every check is tagged:
[AI] = you do it from what I paste.
[AI+WEB] = you do it only if you can browse the web; if you can't, say so and give me the exact steps instead.
[ME] = I do it and paste the result back.
Never guess a result you couldn't observe. You can't watch video, so judge the reel only from my shot list and key frames.

MODE (I pick one)
CREATIVE: design, motion, brand, product. Proof = case studies + reel.
WORK SAMPLES: program, operations, strategy, leadership. Proof = one-page case studies, writing samples, plans, decks, dashboards, talks.

TIME BUDGET (I pick one): 2 hours / 1 day / 1 week. Rank every fix to fit it.

INPUTS (* = required)
1.* TARGET: role family, target companies, and 2-5 postings in full, including their exact wording about portfolio links, passwords, reels, or samples.
2.* MY SITE: URL(s); pasted text of Home, About, Contact, and every case study or sample; phone screenshots of Home and one case study.
3. REEL (Creative mode): link; a shot list with timecodes and my role on each shot; key frames at 0, 5, 10, 20, and 30 seconds, plus the final frame.
4.* MY FINAL RESUME and LINKEDIN (or the LinkedIn PDF export).
5.* SOURCE OF TRUTH + CREDITS SHEET, for each project: who else worked on it (by role), my exact role, dates, whether it shipped, results, any AI use, and permission or NDA status.
6.* MY SITUATION: Is my job search confidential? Who from my current organization might visit my site (by role, e.g., board, staff, funders)?
7. [ME] RESULTS: mobile PageSpeed Insights scores for Home and one case study; what happened when I opened my password-protected pages in a private browser window; the first page of results when I search my name; any AI-assistant summary of me; site analytics.
8. COMPARISON: 2-3 public portfolios from people in my target role family at target companies. Compare structure only; never copy.

GROUND RULES
- Authorship: every piece states my exact role. Team work names the team and spells out my part. Never imply sole authorship. Every credit must match what a collaborator would say if someone asked them.
- Confidentiality: follow the confidentiality rules in my profile. If my work involves regulated client data (for example, mental health services, healthcare, legal, or youth services), nothing that could identify a client appears anywhere, including page copy, images, video, captions, alt text, and file metadata. That means no names, faces, voices, initials, towns, schools, dates, case details, testimonials, quotes, or stories, even "anonymized" ones whose details could point to a person. Aggregate, de-identified numbers only.
- NDA or employer work: use it only with permission. Otherwise, describe it at the level the agreement allows, or recreate it with fictional content clearly labeled as a recreation.
- Confidential search: if my search is confidential, no public page may signal that I'm job hunting. Availability appears only on unlisted role pages and in what I send with applications.
- AI disclosure: if AI tools touched a piece, say where and how.
- Consistency: titles, employers, dates, and location statements must match my resume and LinkedIn exactly.
- Wording: use the postings' exact terms only for searchable nouns (titles, skills, tools); everything else stays in my voice. No first person in headlines, and never address the reader as "you."
- Never invent metrics; ask me instead. Every problem you flag comes with its fix. Label every claim about a company or platform as VERIFIED (checked now, with source) or ASSUMED. Don't soften the critique, and don't invent problems.

EVIDENCE BASE (portfolio surveys are small or run by vendors; treat them as directional)

How portfolios get reviewed
- uxdesign.cc survey (100+ recruiters and managers): 80% of recruiters spend 3 minutes or less on a portfolio; 54% of design managers spend 5-10 minutes, and 11% spend more. Put a summary at the top and link to the full study.
- UXfolio "State of UX Portfolios 2026" (100+ hiring managers, 5,000+ portfolios reviewed):
    - Top red flags: low visual quality (55%), confusing navigation (48%), obvious overuse of AI (43%), overly long content (42%).
    - 72% prefer a website over Figma files, PDFs, or slides.
    - 89% say a relevant case study matters most; reviewers open the one that matches the role.
- Resume Genius 2025: 35% of hiring managers have encountered AI-created portfolio projects or creative work.
- Sackett et al. 2022 (a major re-analysis of hiring research): work samples predict job performance at .33 validity; structured interviews rank highest at .42. A proof piece is a work sample you hand them; the live walkthrough is where the interview happens.

Netflix (VERIFY against the current posting)
- Several earlier Netflix design postings asked for a portfolio together with its password: a 2024 Senior Motion Designer posting, a Product Design Manager posting, and a Staff Product Designer posting on the Ads Platform team.
- Current Brand Creative Studio postings say a strong portfolio is required.
- A Product Brand Designer posting asked for the portfolio, reel, or work samples to be linked in the resume or on LinkedIn.
- Netflix Animation's early-career guidelines:
    - Keep name, contact info, and portfolio URL (with password if protected) always visible.
    - Tailor the portfolio to the role.
    - The first minute of a reel must catch the reviewer's eye.
    - Include breakdowns, with the software noted.
    - Put contact info at the start and end of the reel.
- Portfolio presentations of about 45-60 minutes are typical at big tech (an unverified estimate from my career-strategy reference). Ask the recruiter what the actual format is.

Reels (Creative mode)
- School of Motion: about 20-60 seconds, never more than 2 minutes. Artisan Talent (creative recruiter): ideally under a minute, at most 60-90 seconds. Best and most relevant work first.
- Career-strategy starting assumptions (unverified estimates):
    - For product and Staff-level roles, case studies decide and a 60-90 second reel supports; for studio and brand roles, the reel opens doors.
    - Common rejection reasons: clips with no problem or outcome; no explanation of motion choices; never shipped work with engineers; ignoring reduced motion and performance; only single-feature scope; unclear personal contribution.

Verification and online presence
- HireRight 2025: more than three-quarters of employers found discrepancies between what candidates claimed and what checks showed in the past year. In North America, employment-history discrepancies were the second most common (36%).
- Creative leaders verify authorship informally: they email someone else listed on the credits and ask the candidate to walk through a piece (anecdotal).
- CareerBuilder 2018: 70% of employers screened candidates on social media and 66% used search engines; 47% were less likely to interview someone they couldn't find online.
- A class action filed in January 2026 (Kistler v. Eightfold) alleges that Eightfold, the platform behind Netflix's application portal, uses outside data such as LinkedIn profiles and publications. Eightfold disputes this. Either way, keep my public footprint consistent.
- Content Credentials (the digital "CR" authenticity label): LinkedIn shows a "CR" icon on images and video that carry them. Limits:
    - Many platforms strip the metadata on upload.
    - A missing credential proves nothing either way.
    - At CES 2026, many people read the icon as marking AI-generated content.
  "Durable" credentials (Adobe's free Content Authenticity app, which adds an invisible watermark and fingerprint) survive stripping better. Always pair them with a visible credits line on the page.

Search engines, performance, accessibility
- Google's ProfilePage markup: a Person entry with "sameAs" links to LinkedIn and my other profiles. It must match what's visible on the page, it doesn't guarantee a special search result, and how AI assistants use it isn't documented.
- Core Web Vitals "good" thresholds, measured on real visits: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1. Reviewers often use phones.
- WCAG 2.3.3: motion triggered by interaction can be turned off (honor the "reduce motion" setting). WCAG 2.2.2: moving content that lasts more than 5 seconds needs a pause control. For motion roles, handling this well is itself proof of skill.

STAGE 1: DIAGNOSE

Pass 1 [AI] Proof map.
List the postings' 5 shared requirements and the piece that proves each, rated STRONG / WEAK / MISSING. Then list every resume or LinkedIn claim that has no proof on the site.

Pass 2 [AI] First screen and paths.
- Above the fold, in the desktop and phone screenshots: are my name, function, strongest proof, and a one-click path to the matching case study all visible?
- Simulate a 3-minute recruiter visit and a 10-minute hiring-manager visit. Where does each one stall?
- Do case-study card titles say what I did, with labels for role, format or platform, and industry?

Pass 3 [AI] Each case study or work sample.
Check for:
- a summary of about 100 words at the top: problem, my role, scope, timeframe, outcome;
- decisions and trade-offs; constraints; collaborators and handoff;
- numbers; what I'd change; scannability.
Creative mode: also systems artifacts and reduced-motion handling. Work-sample mode: also an excerpt of the artifact itself (plan, memo, deck, dashboard) with its context.
Rate the level each piece would likely be judged at, against what the postings ask for, and name the 1-3 edits that would raise it most.

Pass 4 Reel.
[AI, from shot list and key frames] Length; the first 10-20 seconds; role labels on each shot; breakdowns; contact info at start and end; fit to the role family; padding to cut.
[ME] Show the first 20 seconds to two people who don't know my work, and write down what they say I do.

Pass 5 [AI] About page.
- First lines state my function and proof.
- A photo that actually looks like me; a brief "how I work"; contact; links to LinkedIn and a resume PDF.
- Location stance consistent with my other materials.
- No client information; no generic AI phrasing.
- No job-hunt signal if my search is confidential.

Pass 6 Verification.
[AI] For each piece: provenance; whether a collaborator could confirm the credit as written; an outside anchor (shipped product, live campaign, press, public credit); AI use disclosed.
[AI+WEB or ME] What a search for my name and AI summaries of me show, and any conflicts with my resume or LinkedIn.

Pass 7 Technical.
[AI] Structured data (ProfilePage/Person with sameAs) matching visible content; page titles and meta descriptions; alt text (no client details); video (no autoplay with sound, a poster frame, captions); reduce-motion support and pause controls; broken links.
[ME] PageSpeed results; password pages opened in a private browser window; every link on my resume and LinkedIn opens without a login; uploaded files stripped of identifying metadata.

Pass 8 [AI] Cold read.
Using only the Home page, the first lines of About, and one case-study summary, state in two lines my level, my function, and what I'm best at. Compare that with how I want to come across and with the comparison portfolios.

STAGE 1 OUTPUT
1. Verdict (3 sentences): Does a recruiter reach the right case study within 3 minutes? Does a hiring manager believe the level the postings ask for? Would a verifier find a mismatch? What's the single biggest risk?
2. Questions for me. STOP and wait if any of them blocks proof of a must-have requirement, or if a confidentiality or NDA permission is unresolved.
3. Scorecard, 1-10 each: first screen, proof coverage, case-study depth, reel (if any), About, verification, technical and accessibility, consistency, authenticity.
4. The proof map and audit findings, plus a list of [ME] checks still pending.

STAGE 2: REWRITE (ranked to fit my time budget)
5. Fix list, starting with the first screen, each tagged with how long it takes (30 minutes or less / 2 hours or less / longer).
6. Home page: 3 options for the opening headline and text; case-study card titles and labels; the order of studies for this role family.
7. About page: full rewrite, safe to be public during a confidential search.
8. Each case study or sample: a new ~100-word summary, a restructured outline, cuts, and [NEEDS: ...] markers for missing facts.
9. Reel (Creative mode): an edit list with timecodes, title and end cards, and on-screen role labels.
10. Proof page for each priority posting. It's unlisted and not linked from the site navigation, and it contains: the role title; a 3-line fit summary; a table mapping the 5 shared requirements to deep links into the proof; the password line, if needed; and contact info. Keep it professional, not cutesy. Give each application its own tracked link (a UTM tag or a link tool) so I can see whether the portfolio was opened.
11. Presentation outline: for my 2 strongest studies, the structure for a live walkthrough (context, my role, 3 key decisions and their trade-offs, outcome, what I'd change), plus the 5 questions a panel is most likely to ask.
12. Verification kit:
    - a credits line for each project;
    - an AI-use line where one applies;
    - steps to add durable Content Credentials to key images;
    - the kinds of people (by role, never by name) who could confirm each project;
    - a "full samples available on request" note for gated work.
13. Technical checklist: structured data with placeholders, page titles and meta descriptions, alt text, performance fixes, accessibility fixes, password handling, and a list of links to test.
14. Application packaging for each posting: the exact lines to paste (proof-page link, password, which study to open first); where the link goes on my resume and LinkedIn; which piece to pin in LinkedIn's Featured section.
15. Consistency table: resume vs. LinkedIn vs. site, covering titles, employers, dates, and location, each marked MATCH or FIX.
16. Change log: one line for each cut, with the reason.
```
