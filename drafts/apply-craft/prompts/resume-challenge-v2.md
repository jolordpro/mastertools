# Resume Challenge v2

**Status:** ready. Challenger-tested twice; the fast-lane / level-number / location patch is folded in.
**Feeds skill:** `apply-resume`. Port the passes into `references/method.md`, and the evidence block into `references/evidence.md`, citing IDs from `knowledge/12`.
**Knowledge:** `00`, `01`, `02`, `03`, `09`, `12`.

## Changes from the version in the thread

- The confidentiality rule now comes from the user's profile instead of one person's background.
- **Output 8** follows AC-L-003: the headline names truthful work; target titles go in Open to Work.
- Patch applied:
  - input 9 (posting date and location stance);
  - the level-number rule;
  - the fast lane;
  - a location and work-type check in Pass 2b.

## Before porting

- The Netflix evidence block is the company dossier. When building the skill, load it from `data/dossiers/<company>.md` instead of hard-coding it. Use `templates/company-dossier-template.md` for other companies.
- Add the suite conventions this version only implies:
  - actor tags;
  - the time budget;
  - a consistency table (`00` §3).
- Everything else carries over as is.

## Prompt

```text
RESUME CHALLENGE v2: TWO-STAGE ADVERSARIAL REVIEW
(Evidence current as of Nov 2026)

ROLE
You are reviewing a resume an AI drafted for me. Don't defend it. Screen it the way it will actually be screened: by a learned matching model, by a recruiter skimming for seconds, and by a hiring manager reading closely. Work in two stages. Stage 1 diagnoses and asks questions. Stage 2 rewrites after I answer, or right away if nothing blocks it.

INPUTS (* = required)
1.* TARGET: company, exact role title, posting URL.
2.* JOB POSTING: full text, unedited.
3.* RESUME DRAFT to challenge.
4.* SOURCE OF TRUTH: my master resume, full history, and notes. Every claim must trace back to this.
5. COMPARISON PROFILES: public profile text (headline, About, experience) for 2-5 people currently in this role or team at the company, plus the likely hiring manager if known. Names removed. Use these to compare vocabulary and structure only; never copy their phrasing.
6. MY LINKEDIN: headline, About, and experience as currently written.
7. OTHER POSTINGS I'm considering at the same company.
8. PORTFOLIO / REEL link, if the role is creative.
9. POSTING DATE (when it went up, or "unknown") and my location / relocation stance.

GROUND RULES
- Truth is the ceiling. Never invent metrics, tools, titles, scope, or outcomes. Flag gaps and ask me about them; never paper over them. Eightfold markets detection of fabricated skills, and the interviews will test everything.
- Never rename a real job title. A truthful parenthetical is allowed only when an internal title hides a standard market equivalent.
- Confidentiality: follow the confidentiality rules in my profile. If my work involves regulated client data (for example, mental health services, healthcare, legal, or youth services), nothing that could identify a client appears anywhere: no names, initials, towns, schools, dates, or case details. Use aggregate, de-identified metrics only. If my pasted inputs contain identifying details, stop and ask me for a de-identified version.
- Mirror budget: match the posting exactly only for filterable nouns (title, skills, tools, certifications, degrees). Verbs, sentence shape, and framing stay in my voice. Never reuse a sentence or distinctive phrase from the posting or the comparison profiles.
- No hidden text, white or tiny font, keyword blocks, or instructions aimed at AI screeners.
- Every problem you flag comes with its fix written out.
- Label every claim about how this company screens as VERIFIED (checked in this session, with the source) or ASSUMED.
- Don't soften the critique and don't invent problems. If something is already strong, say so and leave it.
- Level-numbered titles (Netflix: "Technical Program Manager 5"): search terms and the headline use the title without the number; use the number and posted pay range only to judge how senior my claims should sound.
- Fast lane: if the posting is 4 days old or newer, skip the questions gate for non-blocking gaps. Produce Stage 2 right away from verified facts only, and list the open questions for the next application. (Talent Works: applying in the first 96 hours made interviews up to 8x more likely; older data, directional.)

EVIDENCE BASE (reason from this; vendor surveys are directional; if you can browse, re-verify anything company-specific)

Netflix's application portal (verified from its live configuration, Nov 2026)
- Applications go through explore.jobs.netflix.net, which runs on Eightfold. Netflix's own ATS job postings name Eightfold and Workday.
- The portal matches uploaded resumes to open positions and hides the match score from candidates.
- After applying, candidates are asked to review the profile the system built from their resume and add any missing work or education. The parsed profile is what gets matched, so parsing errors cost you.
- The configuration includes an application-limit setting of 2. Its scope and time window aren't stated. Treat each application as scarce until confirmed otherwise.
- There is an employee referral flow: a referral sends the candidate an email to apply, and they aren't considered until they do.
- The candidate profile includes a LinkedIn URL field.

How Eightfold's match score works (Eightfold engineering blog, Aug 2025; Eightfold community guidance)
- It combines meaning-level matching of the resume and job description with: skill overlap overall; skill overlap from the most recent roles only; current-title similarity; a predicted next title modeled from the sequence of past titles, skills, and tenure; company and industry similarity; and similarity to the "ideal candidate" reference profiles and the hiring manager's profile. The blend is trained on past hiring outcomes and shown to recruiters as 0-5 stars.
- Eightfold's guidance says ideal candidates have the most impact on the match score. Recruiters are told to choose 3-5, often current employees, with titles close to the role.
- MOVABLE signals (editing can change them): how skills are named, which role shows each skill, title clarity, and vocabulary overlap with the comparison profiles. FIXED signals (no edit changes them): employer names, actual titles, tenure. Don't spend edits on fixed signals; send those gaps to the warm-path output.
- A January 2026 class action (Kistler v. Eightfold; in federal court at the pleading stage as of April 2026) alleges Eightfold also uses outside data such as LinkedIn profiles and publications, and keeps applicant data for other roles. Eightfold disputes this. Either way, the practical move is the same: keep LinkedIn and every application to the same company consistent.

How recruiters search and skim
- Jobscan 2025 (survey of 384 recruiters): 99.7% filter inside the ATS: by skills (76.4%), education (59.7%), job title (55.3%), certifications (50.6%), years of experience (44%), location (43.4%). In Jobscan's analysis of 2.5M applications, resumes containing the posting's exact job title saw about a 10.6x higher interview rate. Recruiters say measurable achievements (58%) and tailoring (55%) make candidates stand out, and about 47% check LinkedIn against the resume.
- LinkedIn Recruiter now defaults to plain-language AI search, and its Hiring Assistant agent weighs career trajectory and related skills (per 2026 recruiting-tool reviews). My LinkedIn profile gets screened by AI too.
- Ladders 2018 eye-tracking study: the first screen averaged about 7.4 seconds, and job titles drew the most attention. Strong resumes had simple layouts, clear headers, and bold titles over bulleted accomplishments. Weak ones had multiple columns, long sentences, and little white space. Keywords should appear in context.
- Once shortlisted, a resume gets minutes, not seconds. ResumeGo 2018 (482 hiring professionals): two-page resumes were preferred 2.3x, more strongly at senior levels, when the content earns the space.
- Bullet standard from Laszlo Bock (former Google SVP of People Operations): "Accomplished [X] as measured by [Y] by doing [Z]."

AI on both sides of the table
- Machine readers may favor AI-polished text. Xu, Li & Jiang (AIES 2025) found AI evaluators preferred AI-written resumes over equally qualified human-written ones 67-82% of the time. Eightfold says its match score doesn't rely solely on AI language models.
- Human readers penalize generic AI text. TopResume 2025 (600 hiring managers): about 1 in 5 would reject a resume that looks fully AI-generated. Resume Now 2025: 62% say AI resumes without customization get rejected.
- Resolution: clean, standard structure for the machine (standard headings, clear verbs, consistent bullet shape) carrying content only I could write for the human (named projects, real numbers, real constraints, decisions I made).
- Tailoring alone no longer signals quality. Galdin & Silbert (2025) found a measure of how tailored an application was predicted hiring before LLMs, and stopped predicting it after. Specifics signal; mirroring doesn't.

Format and integrity
- Single column; no tables, text boxes, side columns, icons, or graphics. Contact info goes in the body, not the header or footer. Standard section names. Consistent dates (MM/YYYY).
- File: a text-based PDF exported from Word or Google Docs, or a DOCX. Never a design-tool export. Vendor tests disagree, but most find DOCX parses at least as reliably. If the profile the portal builds after you apply shows errors, re-upload as DOCX.
- Hidden prompts and white-text keywords appeared in about 1% of resumes in a study of roughly 197,000 resumes (USENIX Security 2026). Parsers expose them, and vendors flag them.
- Netflix culture memo (June 2024): selflessness, judgment, candor, creativity, courage, inclusion, curiosity, resilience, plus the keeper test (would a manager fight to keep you?). Show these through outcomes; never list them as adjectives.

STAGE 1: DIAGNOSE (show your work; keep it tight)

Pass 1: Decode the posting.
Build a requirements map: must-haves, preferred, implied (the real problem behind this hire), exact vocabulary (title, skills, tools, credentials, both acronym and full form), and culture signals. Rank each by how likely a recruiter is to filter on it or put it in the match setup. If item 7 is provided, rank all the postings by my fit and recommend which ones to spend my limited applications on, and why.

Pass 2: Machine read.
a) Parse test: render the resume as plain text. Report anything that would scramble, drop, or misorder fields (name, titles, employers, dates, skills).
b) Signal audit: for each match signal (skills overall, recent skills, current title, title history, company/industry, similarity to comparison profiles), mark it MOVABLE or FIXED and rate its current strength (strong / medium / weak). Give the specific edit for every weak movable signal. For every weak fixed signal, say so plainly and carry it into the warm-path output.
   Location and work type: does the resume's location line match the posting's onsite/hybrid/remote terms and my real stance? Make it consistent with LinkedIn and Open to Work.
c) Coverage: mark each requirement EXACT / CLOSE VARIANT / MISSING. Every must-have skill must be named at least once AND shown in a bullet, in the most recent role where that's truthful.
d) Comparison profiles (if item 5 is provided): what vocabulary, structure, and kinds of evidence do they share that my resume lacks? Adopt only what's true for me, in my own words.
e) Sector translation: if my background comes from a different sector, translate terms into the posting's vocabulary only where they're truly equivalent. Flag any translation that would overstate my scope.

Pass 3: 7-second skim.
Look only at the name, headline, top third, titles, employers, dates, and the first 3-5 words of each bullet. In one sentence, state what a recruiter would conclude. If it isn't "this is the hire," specify the fix.

Pass 4: Blind pool test.
a) Cold read: judging only from what's literally on the page, state in two lines my level, my function, and the one thing I'm best at. Compare that with my intended positioning and list every gap. (For a truly independent read, I may run this step in a fresh chat with only the posting and the resume.)
b) Pool: write 3 short, realistic profiles of strong applicants this posting would attract, labeled SYNTHETIC. Rank me among them twice: once as the matcher would (using the Pass 2b signals) and once as the hiring manager would (evidence of outcomes). For each place I lose, name the edit that would change the ranking, or say plainly that it's a real gap no edit can fix.

Pass 5: Line audit.
Make a table: every line → requirement served → KEEP / SHARPEN / MERGE / CUT → rewrite. Cut or compress anything that doesn't advance this application. Sharpen with Bock's X-Y-Z wherever the source supports a number. Within each role, order bullets by relevance to this posting. Flag weak verbs (helped, responsible for, worked on) and empty adjectives (passionate, results-driven, dynamic).

Pass 6: Stand-out and authenticity.
Name my 2-3 strongest differentiators for this posting. Confirm they sit in the top third and come up once more in context lower down. Flag AI tells: tidy triplets, clusters of spearheaded / leveraged / orchestrated, "drive impact," vague "cross-functional stakeholders," every bullet the same length, dash overuse. Replace them with specifics only I could have written.

STAGE 1 OUTPUT
1. Verdict (3 sentences): Will the matcher surface this resume? Will it survive the skim? Will it win the deep read? What is the single biggest risk?
2. Questions for me: only facts and numbers I alone can supply, each tied to the requirement or signal it would unlock. If any question blocks a must-have, STOP here and wait for my answers. Otherwise continue straight to Stage 2.
3. Scorecard, 1-10 with a one-line reason each: parse safety, movable-signal strength, coverage, title alignment, skim test, quantified evidence, differentiation, authenticity.
4. The signal audit table (Pass 2b) and the blind pool results (Pass 4).

STAGE 2: REWRITE
5. The full revised resume: plain text, single column, ready to paste, built only from verified facts. Mark anything still missing as [NEEDS: ...]. Re-run the cold read on the revision and report whether each gap closed.
6. Top 10 changes, ranked by impact.
7. Post-apply checklist: which file format to upload, and exactly what to check in the profile Netflix builds after I apply (titles, employers, dates, skills).
8. LinkedIn alignment: headline (truthful work + strongest proof; target titles go in Open to Work preferences, never in the headline), the first two lines of About, skills to add or reorder, and any title or date mismatches with the resume.
9. Warm-path notes, each under 600 characters: one for a contact who could refer me, one for the recruiter or hiring manager directly. Each names the role, my single strongest proof point, and one specific ask. Then add one line, for me only, on which fixed-signal gap a referral would offset.
10. Change log: one line for each cut and why.
Appendix: requirements coverage table and the line audit table.
```
