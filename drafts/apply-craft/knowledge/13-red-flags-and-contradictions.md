# 13 · Red flags, silent deductions, and contradictions

This file catalogs what costs a candidate points: the subtle deductions, not just the obvious ones. It is organized by **who or what deducts**. Every item has a test and a fix. `prompts/preflight-gate-v1.md` runs this catalog before every submission.

**Labels**
- **Severity:**
  - **Critical:** can end the application on its own.
  - **Major:** a likely downgrade.
  - **Minor:** polish.
- **Evidence:** VERIFIED (sourced; ID or link) or ASSUMED (reasoned from how the system works; verify when possible).

**Ethical boundary**
- Never hide, alter, or disguise a protected identity (race, gender, age, disability, religion) to get past a screener.
- Do remove information that's irrelevant to the job.
- Do standardize formats.
- Do frame work by outcomes.

---

## A. The parser (text extraction, before any human or model sees it)

| # | Flag | Sev | Why it deducts | Test | Fix |
|---|---|---|---|---|---|
| A1 | Ligatures or unmapped embedded fonts drop letters ("Office" → "of?ce") | Critical | Skills and titles silently misspelled in the parsed record, so they don't match | `[ME]` Copy all PDF text into a plain-text editor, or run `pdftotext`; search for every key term | Standard font (Arial, Calibri, Helvetica, Garamond, Cambria); export from Word or Docs; turn off ligatures. Source: [ATS Verification](https://atsverification.com/blog/10-most-common-ats-parsing-failures/) (C) |
| A2 | Portfolio link exists only as hyperlinked text ("Portfolio") | Major | Parsers keep the text and can drop the link target, so the URL vanishes from the record (ASSUMED) | In the extracted text, is the URL itself visible? | Print a short, visible URL (`name.com/work`) |
| A3 | Contact details in the header or footer | Major | Skipped or duplicated per page | Extracted text | Put contact details in the body, first lines |
| A4 | Mixed date formats, "'21", "Now", or years only | Major | Breaks the years-of-experience math. Years-only dates read to humans as hiding a gap | Extracted text | MM/YYYY everywhere; "Present" |
| A5 | Icons, skill bars, text in images, columns, tables | Major | Invisible or scrambled | Extracted text | One column, plain text |
| A6 | File metadata: an author name that isn't the candidate, a template title, "Document1," a creator tool; DOCX tracked changes or comments | Major | Recruiters can see document properties. Leftover comments or tracked changes look careless and can leak drafts (ASSUMED) | `[ME]` File → Properties; in DOCX, accept all changes and delete comments | Set Title to "Firstname Lastname, Resume" and Author to the candidate's name; remove comments |
| A7 | File name "resume_final_v3.pdf" | Minor | Looks careless; the same name on two different versions confuses the record | Look at it | `Firstname-Lastname-Resume-RoleTitle.pdf` |

## B. The matcher (Eightfold stars; Workday HiredScore A–D grades; LLM screeners)

| # | Flag | Sev | Why it deducts | Test | Fix |
|---|---|---|---|---|---|
| B1 | **Craft years computed from titled, dated roles.** The craft was done under a different title (e.g., a leader who also does motion work) | Critical | Years-in-function and "meets basic requirements" are judged from positions. HiredScore grades how well the resume meets the job description's qualifications (A: meets or exceeds … D: doesn't meet) ([Workday docs](https://doc.workday.com/hiredscore/en-us/workday-hiredscore/recruiter-productivity-/concept--hiredscore-grades.html), A–). A "10+ years" must-have is read literally | Add up the years per position *whose title names the craft* | If true: list concurrent freelance or contract craft work as its own dated position with its real title ("Motion Designer, Freelance, 2016–Present"), with clients or projects. Never inflate |
| B2 | Current title far from the target (low title similarity; predicted next title points elsewhere) | Major (fixed) | Eightfold weighs current-title similarity and predicted next title (E06) | Compare the most recent title with the target | Fixed signal, so send it to the warm path. Add a truthful craft line at the top (see H2) |
| B3 | Must-have term appears only in the Skills list | Major | Eightfold marks it "to validate" (E08). Grade-style matchers look for qualifications shown in use | Each must-have appears in a bullet? | Show each in a dated bullet |
| B4 | Posting's literal requirement nouns missing ("broadcast," "live event," "render pipeline," "Cinema 4D," "AI tools") | Major | Requirement matching; recruiters filter by skills 76.4% (E02) | Requirement table: EXACT / CLOSE / MISSING | Use the exact noun where it's true |
| B5 | **Divergent versions to the same company** (different titles, numbers, or framing in two applications) | Major | Most ATS merge duplicates into one candidate record, so recruiters see both versions (ASSUMED for Eightfold; standard ATS behavior) | Compare against every earlier version sent to the company | A company-level master: per-posting changes limited to order, summary line, and emphasis. Identical facts |
| B6 | Applying across unrelated functions at one company (e.g., program management *and* motion) | Major | Reads as unfocused ("turns you into an amateur," a recruiter quoted by [The Big Game Hunter](https://thebiggamehunter.us/applying-for-two-different-types-of-jobs-at-the-same-company-nobsjobsearchadvice-com/), D). Netflix also has an application-limit setting (E55) | Ledger: functions applied to per company | One role family per company per cycle; route the other through a direct conversation |
| B7 | Hidden text, white keywords, prompt injection | Critical | 22% of US hiring managers have caught prompt injections in resumes ([Greenhouse 2025](https://www.greenhouse.com/newsroom/an-ai-trust-crisis-70-of-hiring-managers-trust-ai-to-make-faster-and-better-hiring-decisions-only-8-of-job-seekers-call-it-fair), C) | Select-all in the PDF; check the extracted text | Remove it all |
| B8 | Age proxies that aren't needed (graduation years, 25+ years of roles in full detail) | Minor–Major | Age-discrimination claims against AI screening are live: Mobley v. Workday, an ADEA collective of applicants 40+, HiredScore included as of July 2025 ([AI Governance for HR](https://www.aigovernanceforhr.com/p/the-mobley-v-workday-case-didnt-end), secondary; check the docket). Recruiters filter by graduation year in about 2.5% of searches (Pin audit, vendor, C) | Count the years shown | Last ~15 years in full; earlier roles condensed into one line; graduation year optional. This is relevance editing, not disguise |
| B9 | LLM screeners carry measured biases. Names: white-associated names preferred 85% ([UW, AIES 2024](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/), A–). Disability-related credentials ranked lower; depression-related content worst, even with instructions ([UW, FAccT 2024](https://www.washington.edu/news/2024/06/21/chatgpt-ai-bias-ableism-disability-resume-cv/), A–) | Informational | The candidate can't and shouldn't change identity. But **sector content** (e.g., mental-health services work) may be misread by an LLM as "personal challenges" | Read every sector line cold: could a careless model read it as being about the candidate? | Frame sector work as *operations and outcomes* ("built and ran a program serving N clients") rather than personal-sounding language. Never remove legitimate experience |

## C. The application form (knockouts the documents can't fix)

| # | Flag | Sev | Why it deducts | Fix |
|---|---|---|---|---|
| C1 | Eligibility answers (work authorization, relocation or onsite, required license) | Critical | 92% of recruiters say knockouts are limited to eligibility checks such as these ([Enhancv, 25 recruiters](https://betanews.com/2025/11/10/study-debunks-viral-claim-that-ai-filters-out-most-job-applicants/), C). Small sample, but this is exactly where a hard "no" ends things | Answer truthfully. Decide the location stance *before* applying, and resolve posting conflicts (e.g., "Remote, United States" with a work option of "onsite") with the recruiter |
| C2 | Years-of-experience questions answered differently from what the resume shows | Critical | The form and resume are compared; background checks compare too | Pre-write answers from the resume; same numbers everywhere |
| C3 | Salary expectation above the posted range, or far below it | Major | Above the range: screened out. Far below: leveled down (ASSUMED) | Within the posted range, or "aligned with the posted range" where text is allowed; never contradict across applications |
| C4 | A referral exists but the application went in cold | Major | At Netflix the referral flow sends the candidate an invite. A cold application loses the referral tag (E56) | Have the referrer submit first; apply from their invite |
| C5 | Applying from a **work email or work-managed account** | Critical (for a confidential search) | Organization admins can see managed mailboxes; it also looks unprofessional (ASSUMED) | A personal email, used the same way on every profile, so records merge cleanly |
| C6 | Retyped form fields (titles, dates) that differ from the resume | Major | They become the "official" record that verification checks against | Copy and paste from the resume |

## D. The recruiter skim (about 7 seconds; titles get the most attention, E11)

| # | Flag | Sev | Fix |
|---|---|---|---|
| D1 | Top third doesn't name the target craft in the recruiter's words | Critical | A craft line and strongest proof in the first 2 lines |
| D2 | Most recent title contradicts the target with no bridge | Major | A craft line plus the concurrent craft position (B1) |
| D3 | "Aspiring," "transitioning into," "passionate about," "self-taught" in the opening | Major | These words anchor the candidate as junior. State what has been shipped (ASSUMED) |
| D4 | Bullets over 2 lines; the same opening verb repeated; walls of text | Minor | Bock X-Y-Z (E13); vary the verbs |
| D5 | Unexplained gaps, overlapping full-time roles, concurrent roles without labels | Major | Label each one (Freelance, Part-time, Board), and keep dates honest |
| D6 | Objective statement; photo (US); "References available"; personal details | Minor | Remove them |
| D7 | The proof of the target craft sits on page 2 | Major | Page 1 must stand on its own for the target role |

## E. The hiring manager's deep read

| # | Flag | Sev | Why | Fix |
|---|---|---|---|---|
| E1 | Scope language bigger than the organization ("led an organization-wide transformation" at a small org) | Major | Reviewers calibrate against their own scale. Inflation reads as dishonest | Absolute anchors: budget, headcount, audience, timeline |
| E2 | Numbers that don't reconcile (staff count differs between resume and LinkedIn; percentages with no base; suspiciously round numbers; impossible volume) | Major | One bad number taints the rest | Every number traceable to the source of truth; give the base for every percentage |
| E3 | Generalist dilution: 12 skills, none deep | Major | Senior roles hire depth | Lead with 2–3 differentiators; cut the rest to one line |
| E4 | "We" vs. "I" ambiguity in team work | Major | Unclear contribution is a top rejection reason (EST) | State your exact role |
| E5 | **Tools claimed but not visible in the work** (claims Cinema 4D; the reel is all 2D) | Major | The portfolio is the check | Claim only what the reel or portfolio shows; add a breakdown |
| E6 | Most recent portfolio piece is old | Major | Reads as out of date (ASSUMED threshold ~24 months) | Date projects; add one recent piece aimed at the role |
| E7 | **Leader applying to a senior IC role:** "Will they take direction? Get bored? Leave?" | Major | One of three recruiter questions when an experienced person applies, alongside "Is this a career change?" and "Does the title reflect the real work?" ([The Muse](https://www.themuse.com/advice/3-questions-a-recruiter-will-ask-when-an-overqualified-person-applies), C) | Answer in the letter and the first screen: why hands-on craft now; a story of collaborating as a peer; proof of current, hands-on output |
| E8 | Culture-memo parroting; fan language ("I've loved Netflix since…") | Minor–Major | Reads as generic; Netflix values judgment and candor shown, not stated (E60) | One story showing judgment or candor with an outcome |
| E9 | Sector vocabulary from another world ("stakeholders," "capacity building," "holistic," "programming") | Minor | Signals a different operating context | Translate only where truly equivalent (resume Pass 2e) |
| E10 | **AI posture mismatch:** the posting requires proven AI use, and the materials show none, or claim it vaguely ("AI-powered") | Critical when it's a must-have | A major streamer's live-events motion role lists "proven use of AI tools to speed up asset creation or exploration" as a must-have (VERIFIED, live posting, Nov 2026) | One concrete AI-workflow proof: which tool, which step, time saved, what stayed handmade. Disclosure stays mandatory (`00`) |
| E11 | Cover letter apologizes for gaps ("Although I don't have…") | Major | Hands the reader the objection | Lead with proof; address the gap only with evidence |

## F. Portfolio and reel

| # | Flag | Sev | Fix |
|---|---|---|---|
| F1 | 3D or composite shots with no breakdown | Major | Breakdowns with software noted (E52) |
| F2 | No work in the posting's sub-lane (e.g., no broadcast or live work for a Live role) | Critical when it's a must-have | Lead with the nearest true analog and label it; build a proof piece |
| F3 | Spec work using the target company's IP that isn't clearly labeled | Major | Label it "Personal / spec — not commissioned"; avoid logos that imply a client relationship |
| F4 | Private or expired Vimeo links; password missing from the application | Critical | `[ME]` Private-window test; the password goes in the application text |
| F5 | AI-generated elements undisclosed, **or** no AI proof when the posting asks for it | Major | A disclosure line plus a workflow breakdown (E10) |
| F6 | Projects without dates or roles | Major | Date and role on every card |
| F7 | Licensed music or footage without rights in a public reel | Minor–Major | Licensed or original audio (ASSUMED risk) |

## G. The verifier (background, references, credits)

| # | Flag | Sev | Fix |
|---|---|---|---|
| G1 | Titles or dates differ across resume, LinkedIn, form, and the background check | Critical | Consistency table (`09` §7) |
| G2 | Preferred name vs. legal name mismatch | Minor | Preferred name on documents; legal name in the form's legal-name field; the same preferred name everywhere |
| G3 | **References and verification would expose a confidential search** (for an executive, the current employer *is* the board) | Major | Ask that current-employer contact wait until a conditional offer. Prepare alternates: former supervisors, past board members, funders, collaborators (`09`) |
| G4 | Credits contradicted elsewhere (a studio site credits someone else as lead) | Critical | Credits sheet; match public credits exactly |
| G5 | Old public profiles (Behance, Vimeo, ArtStation, old site) with stale titles or contradictions | Major | Footprint sweep (`[ME]` name search); update or archive |

---

## H. Non-obvious contradictions (the kit's own rules, and the candidate's materials)

| # | Contradiction | Resolution |
|---|---|---|
| H1 | Tailor every resume to its posting **vs.** one merged candidate record per company | Company-level master; per-posting changes limited to order and emphasis (B5) |
| H2 | Exact title correlates with a 10.6x interview rate (E03) **vs.** never claim a title not held (AC-L-003) | Separate **craft** from **employer title**. A top line may name the craft the person demonstrably practices for pay or with shipped work ("Motion designer, 2D/3D, broadcast and brand"). Employer titles stay exact |
| H3 | ATS-plain resume **vs.** a designer expected to show typographic taste | Refined single column (one typeface, real hierarchy, whitespace) for the portal; a designed version on the site or proof page |
| H4 | Two pages preferred 2.3x (E12) **vs.** a 7-second skim and creative norms | Two pages allowed only if page 1 stands alone for the target role |
| H5 | AI-disclosure caution (`00`) **vs.** AI fluency as a must-have (E10) | Disclose *and* prove: AI use is evidence of skill when it's specific and honest |
| H6 | Confidential search **vs.** public proof, Open to Work, referral asks | Proof pages unlisted; recruiters-only Open to Work; outreach to people chosen deliberately (each one learns of the search) |
| H7 | Posting says "Remote, United States" **vs.** a work option of "onsite" (seen on a live posting, Nov 2026) | Ask the recruiter or referrer; never guess in the form |
| H8 | A high posted pay range (e.g., $300k+ for a senior IC) **vs.** modest scope language | A high range means a senior or staff bar; undersold scope gets leveled down. Anchor scope with numbers |
| H9 | Long, mission-driven tenure (stability) **vs.** a performance culture (keeper test) | Show outcomes, decisions, and candor, not loyalty |
| H10 | Running an organization **and** a craft practice at the same time **vs.** "how did they do both?" | Be specific: project count per year, hours, clients. Vague concurrency reads as padding |
| H11 | The model that wrote the resume also grades it (AI self-preference 67–82%, E16) | Blind panel with at least one non-Claude model plus one human from the field (`preflight-gate-v1`) |

---

## J. Patterns from real post-mortems (added 2026-11-05)

These come from post-mortems of real applications. The patterns are generic. They matter more than most wording flags.

| # | Flag | Sev | Why it deducts | Test | Fix |
|---|---|---|---|---|---|
| J1 | **Posting age at submit:** sent weeks after posting, or the posting closed while proof was being built | Critical | Screening often starts within 3 days, and reviewers stop at a threshold (E75). Rolling-review roles reward early sends | Ledger field `posting_age_at_submit_days`; anything over 21 days without a referral is a red flag | **Ship-by rule:** apply within 7 days of discovery on current truthful proof; proof pieces improve the *next* application |
| J2 | **Hub or commute-radius rule ignored** (e.g., "must live near SF, NY or LA"), while the résumé shows another city | Critical | A location knockout or an instant recruiter pass | Read the posting's location *body text*, not just the header | State a truthful hub plan in the form and letter, or don't spend the application |
| J3 | **Pay band at or below the candidate's floor**, or an in-office load the candidate can't carry while employed | Major | A salary field above the band screens; a recruiter reads flight risk | Compare the band with the profile floor before drafting | Skip, or apply only with a stated reason and an in-band answer |
| J4 | **Claim drift over time:** the same number or title differs across versions sent to different employers and the live site or LinkedIn (e.g., an hours-saved figure or an audience number revised between sends) | Major | Reviewers and verifiers compare surfaces; drift reads as inflation | Diff each send copy against the source of truth *on the send date*, plus a public-surface sweep | Freeze claims per cycle; retire old numbers everywhere at once |
| J5 | **An employer heading spans client work** ("Company 2018–2023," where only 2018–2019 was employment and the rest was client work through the candidate's own studio) | Major | Employment verification shows the shorter span | Each heading covers employment only | Put client work under the studio entry, with the client named in the bullet |
| J6 | **A role in the public record is missing from the résumé** (e.g., an officer role in a nonprofit's public filings) | Major | Reads as concealment, not a gap | Search the candidate's name, plus public filings for any org they lead | List it accurately, even as one line |
| J7 | **An award in the headline when it's regional, or not publicly attributable by name** | Major for verification-heavy employers | A checker can't confirm it from public lists | Can a stranger confirm it in 2 minutes? | Keep it in the awards line, stated precisely; the headline carries the craft |
| J8 | **Generator metadata** (Author "Un-named," a tool name) on a sent file | Minor | Looks machine-made | File → Properties | Set Title and Author |
| J9 | **Parallel role families across the search** (VP, CD, AI lead, Lead IC, ops director) | Major | LinkedIn and the site can only match one or two. Recruiters see the mismatch | Count the role families active in the last 30 days | Two at most at once; one per company |
| J10 | **Storefront not live at submit:** the portfolio URL 404s, the site is mid-cutover, LinkedIn not updated | Critical | The reviewer's click dead-ends | `[ME]` Click every link in a private window on submit day | Launch first, or link to a page that's already live |
| J11 | **Warm path deferred until the "storefront is perfect"** | Major (channel) | Referrals change the base rate (E63, E64). Deferral costs more than polish adds | Referral attempt logged for each priority role? | Send the referral ask in parallel with the submit |
| J12 | **Outcomes not logged** (no submit dates, no rejection wording, ambiguous statuses like "all gone") | Major (system) | No learning loop; post-mortems become guesswork | Every row has defined status words and dates | Mandatory ledger fields (see `templates/application-ledger.md`) |

---

## I. Objection map (method)

Every reader carries unspoken doubts. For each one, write:

```
Reader → doubt → where they'll look for the answer → current evidence → fix + placement
```

Default doubts for a **career changer or leader moving to a senior IC role**:
1. Is the craft their profession or a side practice?
2. Do they meet the literal years and domain bar?
3. Will they take direction and stay?
4. Are they current on the tools, including AI?
5. Can they work at this company's speed and scale?
6. Is the work theirs?

Place each answer where that reader looks first:
- recruiter → top third;
- hiring manager → first case study;
- panel → presentation;
- verifier → credits.
