# Cover Letter Challenge v2 (DRAFT)

**Status:** draft. It is built from v1, the first challenger pass's patches, and the conventions the later prompts adopted.
- **Not yet challenger-tested.** Run one `challenger` pass before marking it ready (PLAN Phase 2).
- **Feeds skill:** `apply-cover-letter`.
- **Knowledge:** `00`, `04`, `08`, `09`, `12`.

## What changed from v1

**Patches from challenger pass 1**
- Profile-driven confidentiality rule.
- Questions gate.
- Warm-path notes (two versions).
- Proof-piece call.

**Conventions adopted from resume, LinkedIn, and portfolio v2**
- Two stages; fast lane; time budget.
- Actor tags.
- Dual-reader rule.
- Level-number rule.
- Mirror budget.
- Consistency table.
- Netflix portal facts.

**New in this draft (to stress-test in the challenger pass)**
- A "letter-only readers" check.
- A "resume-only readers" check.

## Prompt

```text
COVER LETTER CHALLENGE v2 (DRAFT): TWO-STAGE ADVERSARIAL REVIEW
(Evidence current as of Nov 2026)

ROLE
You are reviewing a cover letter an AI drafted for me. Don't defend it. Read it the way its real readers will: a hiring manager who may read it before the resume, a recruiter who may skip it entirely, and possibly an AI screener reading the whole application. Stage 1 diagnoses and asks. Stage 2 rewrites after I answer, or right away if nothing blocks it.

WHO DOES WHAT
[AI] = you do it from what I paste.
[AI+WEB] = you do it only if you can browse; if you can't, say so and give me the exact steps.
[ME] = I do it and paste the result back.
Never guess a result you couldn't observe.

TIME BUDGET (I pick one): 30 minutes / 2 hours / 1 day. Rank fixes to fit it.

INPUTS (* = required)
1.* TARGET: company, exact role title, posting URL, and the date the posting went up (or "unknown").
2.* JOB POSTING: full original text, unedited.
3.* COVER LETTER DRAFT to challenge.
4.* FINAL RESUME: the version I'm submitting with this letter.
5.* SOURCE OF TRUTH: master resume, full history, and notes. Every claim must trace back to this or to item 6.
6.* MY REAL REASONS: why I want this role and this company, in my own words, however rough. Include any connection, conversation, product moment, or piece of their work that actually matters to me.
7.* SUBMISSION FORMAT: uploaded file, pasted text box, email, or recruiter message, plus any word or character limit.
8. MY LINKEDIN and PORTFOLIO link, for consistency.
9. WARM PATH: anyone at the company I know or could reach (by role, never by name), and whether a referral is possible.

GROUND RULES
- Truth is the ceiling. Never invent stories, metrics, motives, connections, or enthusiasm. If the letter needs something the inputs don't support, ask me.
- Confidentiality: follow the confidentiality rules in my profile. If my work involves regulated client data (for example, mental health services, healthcare, legal, or youth services), nothing that could identify a client appears anywhere: no names, initials, towns, schools, dates, case details, or "anonymized" stories with unique details. Aggregate, de-identified numbers only. If my inputs contain identifying details, stop and ask for a de-identified version.
- NDA or employer work: mention it only at the level the agreement allows.
- Titles, employers, and dates match my resume exactly. Never rename a real title.
- Level-numbered titles (Netflix: "Technical Program Manager 5"): name the role without the number in the letter's text unless the posting's own title must be quoted exactly; use the number and pay range only to judge how senior to sound.
- Mirror budget: use the posting's exact words only for the role title and 3-5 must-have nouns (skills, tools, credentials). Everything else stays in my voice. Never reuse a sentence or distinctive phrase from the posting.
- No flattery and no recycled culture-memo vocabulary. No childhood origin stories unless they're true AND relevant to the job.
- No hidden text or instructions aimed at AI screeners.
- Voice: never address the reader as "you" in a salesy way; no stock openers or closers. First person is fine.
- Every problem you flag comes with the rewrite.
- Label any claim about how this company handles cover letters as VERIFIED (checked now, with source) or ASSUMED.
- Don't soften the critique, and don't invent problems. If a sentence already works, leave it alone.
- Fast lane: if the posting is 4 days old or newer, skip the questions gate for non-blocking gaps, produce Stage 2 from verified facts now, and list open questions for next time.

EVIDENCE BASE (reason from this; vendor-run surveys are directional)
- Tailoring is what pays. ResumeGo's field experiment (7,287 applications, 2019-20): callbacks were 10.7% with no letter, 12.5% with a generic letter, 16.4% with a tailored one. A generic letter barely beats none.
- Jobscan 2025 (2.5M applications): including a cover letter correlated with a 3.4x higher interview rate.
- Readership is split. Resume Genius (625 hiring managers): 83% always or often read cover letters; 45% read the letter BEFORE the resume. Novorésumé (Dec 2025, 200+ recruiters): 51.7% never read them, though heads of HR (29.4%) and HR managers (22.9%) skip them far less. Implications: the opening must stand alone, and no must-have may appear only in the letter.
- AI made generic tailoring worthless as a signal. Galdin & Silbert (2025; 2.7M freelance applications): a measure of tailoring predicted hiring before LLMs and stopped predicting it after. What still signals is what an LLM couldn't produce from the posting alone: specific, checkable details only I could know. (Freelance coding, not corporate hiring: directional.)
- Two readers, two tastes. Machine readers may favor polished AI-style text (Xu, Li & Jiang, AIES 2025: 67-82% self-preference); human readers penalize it (TopResume 2025: 25% call AI unacceptable for cover letters; 52% accept AI help if a human produces the final). Resolution: clean, standard structure carrying specifics only I could write.
- CV Genius: a tone mismatch between resume and cover letter is a common AI giveaway, and it follows the candidate into the interview.
- Length: ResumeLab (205 HR professionals): 42% prefer half a page to one page; 40% prefer under half a page. Target 250-400 words unless a limit says otherwise.
- Netflix (VERIFY on the posting): applications go through explore.jobs.netflix.net (Eightfold), which reportedly accepts extra documents such as a cover letter. Whether Eightfold scores letter text is unknown; assume both software and people may read it. The portal has a referral flow (a referred candidate still has to apply).
- Netflix culture memo (June 2024): selflessness, judgment, candor, creativity, courage, inclusion, curiosity, resilience, plus the keeper test. Show them through a story; never list them.
- Referrals: Jobvite data (reported secondhand) puts referrals at about 7% of applications but about 40% of hires. Vendor data and pre-filtered candidates, so directional.

STAGE 1: DIAGNOSE

Pass 1 [AI / AI+WEB] The real job.
In 2-3 sentences, the problem this hire exists to solve; the 3 requirements the hiring manager cares about most, ranked. If you can browse, what's happening at the company or team right now that makes this role matter (VERIFIED or ASSUMED).

Pass 2 [AI] Division of labor.
Map each sentence against the resume. The letter must add what the resume can't: why this role, why now, the thread connecting my experience, context for any pivot or gap, and one proof story told with its stakes. Flag every sentence that only restates a resume bullet.

Pass 3 [AI] Two-reader check.
a) Letter-only reader: if someone reads the letter and never opens the resume, do they learn my level, function, strongest proof, and the role title?
b) Resume-only reader: confirm every must-have is covered in the resume, so nothing depends on the letter being read.

Pass 4 [AI] Opening test.
Read only the first two sentences. Do they name the exact role title and give the single strongest reason I fit? Kill stock openers ("I am writing to express my interest," "I am excited to apply," "As a passionate ___"). Write 3 alternative openings from different angles (a result, the problem, a real connection) and recommend one.

Pass 5 [AI] Proof.
Pick 1-2 stories that hit the top-ranked requirements: the situation in one line, what I specifically did, how it worked, and the result with a number from the source of truth. If a number likely exists but isn't in the inputs, ask me.

Pass 6 [AI] Swap test (why this company).
For every sentence about the company, swap in a direct competitor's name. If it still works, it's generic. Rewrite it around something specific and true about this company and team, connected to the work I'd do. Draw only on my real reasons (input 6).

Pass 7 [AI] Costly-signal test.
Mark every sentence an LLM could have written for any qualified applicant from the posting alone. Replace each with a detail only I could supply: a named project, a decision I made and why, a number, a constraint, a lesson that changed how I work. If I haven't given enough raw material, ask targeted questions instead of polishing.

Pass 8 [AI] Voice and authenticity.
Does it sound like one specific person talking to another? Flag uniform rhythm, tidy triplets, "leverage / spearhead / passionate / dynamic / thrilled," dash overuse, and stock closers. Check that tone and claims match the resume and would hold up out loud in an interview.

Pass 9 [AI] Machine and format.
The exact role title appears once, naturally. 3-5 must-have terms appear in context, never as a list. The text survives a paste into a plain text box: no tables, columns, icons, or header/footer content. For uploads, a clean file name (Firstname-Lastname-Cover-Letter-RoleTitle.pdf).

Pass 10 [AI] Length and close.
250-400 words or the stated limit. Cut anything that doesn't advance fit, proof, or motive. End with a specific, confident line tied to the work, not a request for consideration.

STAGE 1 OUTPUT
1. Verdict (3 sentences): Would a hiring manager who reads only the first paragraph want the resume? Would one who reads the whole letter want the interview? What's the single biggest risk?
2. Questions for me: only details I alone can supply, each tied to the sentence it would upgrade. If any question blocks a must-have or a confidentiality call, STOP and wait (unless the fast lane applies).
3. Scorecard, 1-10 with one-line reasons: opening, proof, specificity (swap and costly-signal tests), complement to the resume, two-reader check, voice and authenticity, length and format.
4. Sentence-by-sentence audit table: sentence | job it does | KEEP / SHARPEN / CUT | rewrite.

STAGE 2: REWRITE
5. Three alternative openings, with your pick.
6. The revised letter in plain text, ready to paste, built only from verified facts. Mark anything missing as [NEEDS: ...].
7. Short version under 600 characters for application text boxes.
8. Warm-path notes, each under 600 characters:
   a) to a contact who could refer me, written so saying yes takes them under a minute (include a 2-line blurb they can forward);
   b) to the recruiter or hiring manager directly.
   Each names the role, gives one proof point, and makes one specific ask. Then one line, for me only, on which fixed gap (employer, title, tenure) a referral would offset.
9. Proof-piece call: is a short work sample (one page or a two-minute walkthrough) worth it for this role? If yes: what it shows, which requirement it proves, and roughly how long it takes me. If no: why.
10. Consistency table: title, employer, dates, and location as stated in the letter vs. resume vs. LinkedIn, each MATCH or FIX.
11. Change log: one line for each cut and why.
```

## Questions for the challenger pass

- Is Pass 3 (two-reader check) redundant with Pass 2? Could they merge?
- Should the proof-piece call move to `apply-proof-piece` with only a flag left here?
- Do the warm-path notes belong in `apply-warm-path` instead, leaving the letter skill focused on the letter?
- Is the time budget too fine-grained for a single letter?
