# LinkedIn Challenge v2

**Status:** ready. Challenger-tested (this pass produced AC-L-003).
**Feeds skill:** `apply-linkedin`.
**Knowledge:** `00`, `05`, `08`, `09`, `12`.

## Changes from the version in the thread

- The confidentiality rule now comes from the user's profile instead of one person's background.

## Before porting

- **Run order:** this prompt takes the final resume as input, so it runs after `apply-resume`.
- **Its consistency table** (output 12) should also cover the site and the cover letter once those exist.

## Prompt

```text
LINKEDIN CHALLENGE v2: TWO-STAGE ADVERSARIAL REVIEW
(Evidence current as of Nov 2026)

ROLE
You are reviewing my LinkedIn profile. Don't defend it. Judge it the way it actually gets judged: by LinkedIn's AI search and Hiring Assistant agent, by a recruiter glancing at a search result, by a hiring manager clicking through from my resume, and possibly by an employer's screening system that pulls my profile. Stage 1 diagnoses and asks. Stage 2 rewrites after I answer, or immediately if nothing blocks it.

KEY DIFFERENCE FROM A RESUME
A resume is tailored to one posting. My profile is one public page serving every application at once. Tailor it to the role family, keep it consistent with every resume I send, and let it be broader than any single resume.

INPUTS (* = required)
1.* TARGET: the role family (titles I'm pursuing) and target companies.
2.* 2-5 POSTINGS from that family, full text.
3.* MY PROFILE EXPORT: on a computer, open my profile → More (or Resources) → Save to PDF. Attach it, then add what the export leaves out:
    - skills attached to each position
    - Featured items
    - photo and banner (describe them)
    - my last 5 posts or comments (paste the text)
    - Open to Work status, visibility setting, and the titles, locations, and work types entered
    - verification status
4.* MY FINAL RESUME for the top-priority application.
5.* SOURCE OF TRUTH: master resume, full history, notes.
6.* MY SITUATION: Currently employed? Search confidential? Who at my organization is connected to me (by role, e.g., board, staff)? Location, and willingness to relocate or work onsite, hybrid, or remote.
7. COMPARISON PROFILES: public profile text from 2-5 people in this role family at target companies, names removed. Compare vocabulary and structure only; never copy phrasing.
8. PROOF MATERIAL: portfolio, case studies, decks, talks, press, or work I could turn into a Featured piece.

GROUND RULES
- Truth is the ceiling. Never invent metrics, tools, titles, scope, or outcomes. Flag gaps and ask me.
- Headline truthfulness: the headline describes work I demonstrably do or have done. It never implies I hold or held a title I haven't. Target job titles belong in my Open to Work preferences (which recruiters can see), in Skills, and in a plain closing line of About ("Open to X roles").
- Titles, employers, and dates must match my resumes exactly. Never rename a real title. A truthful parenthetical is allowed only when an internal title hides a standard market equivalent.
- Level-numbered titles: some employers put level numbers in titles (Netflix: "Technical Program Manager 5," "AI Engineer 6"). Search terms use the title without the number. Use the number, plus the posted pay range, only to judge how senior my claims should sound.
- Confidentiality: follow the confidentiality rules in my profile. If my work involves regulated client data (for example, mental health services, healthcare, legal, or youth services), nothing that could identify a client appears anywhere on this public page, including Featured files and post history: no names, initials, towns, schools, dates, or case details. Aggregate, de-identified numbers only.
- Mirror budget: use the role family's exact words for searchable nouns (titles, skills, tools, certifications). Everything else stays in my voice. Never reuse a sentence from a posting or a comparison profile.
- Voice: no first person in the headline. Never address the reader as "you." About may use first person unless I say otherwise.
- No keyword dumps, hidden text, or engagement bait.
- Every problem flagged comes with its fix written out.
- Label every claim about how LinkedIn or a company works as VERIFIED (checked this session, with source) or ASSUMED. LinkedIn doesn't publish how it ranks profiles; say so whenever advice depends on that.
- Don't soften the critique, and don't invent problems.

EVIDENCE BASE (LinkedIn's own figures are "up to" marketing numbers showing correlation, not cause; vendor studies are directional)

How recruiters find profiles
- Jobscan 2025 (384 recruiters): 75% find candidates on LinkedIn; 73.3% always or often check a candidate's profile; about 47% check it against the application; 43.4% filter by location. A profile can be broader than a tailored resume.
- LinkedIn Recruiter now defaults to AI-Assisted Search: the recruiter describes the role in plain language. The Hiring Assistant agent (generally available since Sept 2025) recommends and ranks candidates, reportedly weighing career path, related skills, and engagement, and can surface people who applied before.
- Spotlights (filters recruiters can turn on):
    - Open to Work: people who said they were open within the last 90 days.
    - More likely to respond: based on messaging history.
    - Engaged with the company: followed its page, or liked, shared, or commented on its posts or job posts.
    - Has connections at the company.
    - Past applicants.
- Skills: up to 100, each attachable to positions. LinkedIn's Skills Match compares a job's skills with the skills I list and with skills it picks up from text across my profile.
- LinkedIn "Rock Your Profile" (April 2025), all "up to": photo, 21x more views and 36x more messages; 5+ skills, 17x more views; up-to-date positions, 8x more views and 10x more messages; industry listed, 9x more views; volunteer experience, 6x more views.
- Verification (identity, workplace, or school): LinkedIn says verified members average 60% more profile views and 50% more engagement.

Open to Work, privacy, and safety
- Public #OpenToWork frame: about 40% more likely to get recruiter InMails (LinkedIn data). "Recruiters only" mode has no frame; LinkedIn tries to hide it from recruiters at my current company but can't guarantee it. Some readers see the public frame as desperate, especially at senior levels. That's opinion, not data.
- Before editing, turn off "Share job changes, education changes, and work anniversaries from profile" (Settings & Privacy → Visibility). Job updates can reach my network within two hours.
- Scams: Open to Work hashtags draw fake recruiters (Malwarebytes). FTC-reported job-scam losses rose from $90M (2020) to $501M (2024).

Content and photo
- An Originality.ai study (an AI-detection vendor) estimated 54% of long LinkedIn posts in late 2024 were likely AI-written. Generic AI phrasing is everywhere, so specifics stand out.
- Ringover 2024 (1,087 recruiters): in blind tests, 76.5% preferred AI-generated headshots, but 66% would be put off by an undisclosed AI headshot they recognized. Reported LinkedIn policy: the photo must be my real likeness.

Field limits
- Headline: 220 characters; only about the first 60-120 show in search results and cards.
- About: 2,600 characters; the first few lines show before "see more."
- Position title: 100. Position description: 2,000. Each skill: 80. Connection note: 300.

Connection to the application
- Netflix's portal (built on Eightfold) collects a LinkedIn URL. A January 2026 class action alleges Eightfold uses outside data such as LinkedIn profiles; Eightfold disputes it. Either way, LinkedIn and resume must agree.
- Netflix's open roles skew onsite: 313 of 397 when checked in Nov 2026.
- Machine readers may favor polished, standard phrasing; human readers punish generic text. Resolution: standard structure carrying specifics only I could write.
- Bullet standard (Laszlo Bock): Accomplished [X] as measured by [Y] by doing [Z].

STAGE 1: DIAGNOSE

Pass 1: Role-family target.
Pull out what the postings share: title variants (without level numbers), must-have skills, tools, credentials, and vocabulary. Note the seniority each posting signals (level numbers, years required, pay range). Split items into SHARED (belongs on LinkedIn) and POSTING-SPECIFIC (leave to each resume). Rank shared items by how likely a recruiter is to search for them.

Pass 2: Search-result test.
Show what appears in a search result: name, headline (first ~60 and ~120 characters), current title and employer, location, photo. In one sentence, what would a recruiter conclude? Does the visible slice name my function, my strongest proof, and nothing I can't back up?

Pass 3: Recruiter search simulation.
Write 3 plain-language and 2 keyword-style searches a recruiter at a target company would run. For each: would I come up, and which section carries each term (headline, current title, Skills, About, Experience, Open to Work titles)? List every term that appears nowhere.

Pass 4: Signal audit.
Mark each signal MOVABLE or FIXED and rate it strong / medium / weak. Give the fix for every weak movable signal:
headline · current title · skills (count, order, attached to current role) · About · experience · Featured proof · photo and banner · recent activity · verification · Open to Work (mode, titles, recency) · engagement with target companies · connections there · recommendations · location and work type · employers, dates, actual titles (fixed).

Pass 5: Consistency check.
Compare every title, employer, date, and location statement against my resume. Flag mismatches, and flag anything that weakens the resume's positioning.

Pass 6: Cold read.
From the headline, the first three lines of About, and my current role only: state my level, my function, and the one thing I'm best at, in two lines. Compare that with my intended positioning and with the comparison profiles. List the gaps.

Pass 7: Section audit.
For each section: KEEP / SHARPEN / CUT, with the rewrite. Flag AI-sounding phrasing (tidy lists of three, "passionate," "results-driven," "spearheaded," "drive impact," uniform rhythm, too many dashes, an About section that could be anyone's). Review the photo (real likeness, recent, clear face, fits the role family's norms) and the last 5 posts or comments (anything off-message, generic, or confidential).

STAGE 1 OUTPUT
1. Verdict (3 sentences): Would AI search surface me? Would the search result earn a click? Does the profile hold up next to my resume? What's the single biggest risk?
2. Questions for me: only facts, numbers, or decisions I alone can supply. If any one blocks the headline, About, current role, or location stance, STOP and wait.
3. Scorecard, 1-10 with one-line reasons: search result, findability, skills, About, experience, proof, consistency, credibility signals, authenticity.
4. Search simulation results and the signal audit.

STAGE 2: REWRITE (in the order a viewer sees it)
5. Before-you-edit checklist: settings to change first, in order.
6. Headline: 3 options under 220 characters, each naming truthful work plus my strongest proof first, from different angles. Recommend one.
7. About: full rewrite under 2,600 characters. The first three lines must work on their own. Close with one plain line naming the roles I'm open to.
8. Current role, then each earlier role: exact title unchanged, description under 2,000 characters, X-Y-Z bullets where the source supports numbers, and 3-5 attached skills each. Attach the role family's must-have skills to my current role where truthful.
9. Skills: final ordered list, skills to feature at the top, skills to remove, and which positions each attaches to.
10. Featured: one proof piece that demonstrates the top shared requirement. Specify the format (one-page case study, deck, or short walkthrough video), what it shows, what to scrub for confidentiality, and roughly how long it takes me. Then list what else to add, cut, or reorder (certifications, volunteer, recommendations to request and from which kind of colleague).
11. Visibility plan:
    a) Open to Work: recommended mode for my situation, plus the exact job titles (no level numbers), locations, and work types to enter. Refresh preferences at least every 90 days.
    b) Location stance, stated the same way on LinkedIn, in Open to Work, and on my resume.
    c) Verification steps worth doing.
    d) Target companies: follow their pages, and engage only where I have something real to say.
    e) Connections: which kinds of people to connect with (by role, never by name), plus a note template under 300 characters.
    f) Messaging habit: reply to relevant recruiter InMails promptly, even to decline.
    g) Scam screen: trust recruiter outreach only after it checks out (a Verified Recruiter badge or a corporate-domain email and calendar invite). Never pay fees, never send an SSN or bank details before a verified offer, never install "interview software" from a DM.
    h) When to turn network sharing back on.
12. Consistency table: every title, employer, date, and location statement on resume vs. LinkedIn, marked MATCH or FIX.
13. Change log: one line for each cut, with the reason.
```
