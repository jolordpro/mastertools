# Apply Craft — Research Plan v1

**Status:** for approval · 2026-11-05
**Approver:** the suite owner (Jo)
**Runs in:** Claude Code, after approval. See the private handoff for repo locations and privacy rules.
**This file is public-safe:** it contains no candidate data. Candidate-specific priorities, fit notes and outcomes live in the private bundle.

---

## 0. Why this plan exists, and what changed

Three findings from 2026-11-05 shape everything below.

1. **Candidates often already have records worth building on:** a source of truth for their numbers, claim checks, prior audits, a job board. Research extends those. It doesn't rebuild them.
2. **The real application losses weren't about wording.** Post-mortems of real applications point to five causes:
   - **timing:** packages sent weeks or months after posting, or never sent;
   - **knockouts:** hub-location and in-office rules;
   - **claim drift:** numbers and titles changing across versions and public surfaces;
   - **public-record mismatches**;
   - **channel:** referrals deferred.

   So the research is aimed at **decisions**:
   - where to apply;
   - through which door;
   - past which screen;
   - with what proof;
   - and how fast.
3. **No research beats a live posting check plus a referral.** Research may never block a submit (rule R-0 below).

## 1. The six questions every research item must answer

Any finding that doesn't answer one of these doesn't get collected.

| # | Question | Example output |
|---|---|---|
| **Q1 Reachability** | Can this candidate actually hold this job? Covers remote policy, hub or commute rules, in-office days, posted pay vs. the candidate's floor, and level. | "Meta: product design roles are hub-based, 3 days a week (VERIFIED, date). Fails a remote-only rule." |
| **Q2 Door** | Which ATS and AI layer, knockout questions, referral mechanics, application limits, posting-age patterns, recruiter structure. | "Pinterest: Greenhouse; referral field on the form; no AI grade seen." |
| **Q3 Bar** | How the creative team judges work: portfolio and reel expectations, exercises, interview loop, leveling, rubric. | "Google UX: portfolio presentation plus app critique; leveling set by a hiring committee." |
| **Q4 Signal** | What insiders say stands out, and what sinks candidates. This is the **review lane**. | "Buck CDs: reel shows taste in the first 10 seconds; role clarity per shot." |
| **Q5 Channel** | Warm paths: the referral program, vendor studios that make the company's work, alumni, recruiters, events. | "Airbnb's miniature campaigns are made by Buck, a calibration and intro path." |
| **Q6 Risk** | Verification depth (background checks, Work Number, references), AI-use rules in hiring, fraud vigilance, company-specific red flags. | "Company X runs employment verification before the offer; current employer contacted only with consent." |

## 2. Scope

### 2a. Companies

**Tier rule:** Q1 (reachability) is checked first, in R0, for every company. A company that fails the candidate's location or pay rule gets a one-line record and no deep research, unless the owner overrides.

Remote-policy hints marked *(Recalled)* come from memory and are often stale. R0 verifies them.

**Tier 1: named by the owner, or live now**

| Company | Lane | Why | First check |
|---|---|---|---|
| Netflix | Live / broadcast motion; brand studio | Live and brand-studio motion roles recur; dossier exists (`knowledge/02`) | Refresh only: portal, open roles, loop |
| Pinterest | Product / brand motion, Staff | A Staff motion role existed in 2026 (closed); the company posts motion roles | Current roles; remote policy *(Recalled: remote-friendly)* |
| Meta | Brand / product motion, Reality Labs | Large motion teams; owner-named | In-office rules *(Recalled: hub-based)*; current motion roles |
| Google (incl. YouTube) | Brand studio, Material motion, YouTube (incl. sports) | Owner-named; Material motion and YouTube are lane fits | In-office rules *(Recalled: hybrid)*; current roles |
| Buck | Studio: brand, 3D, campaign | Owner-named; makes work for big-tech clients (a calibration path) | Staff vs. freelance hiring; remote policy; how they review reels |

**Tier 2a: live, sports and streaming (broadcast pedigree is current relevance)**
- Amazon: Prime Video Sports, Thursday Night Football
- Apple: TV+ / MLS Season Pass
- ESPN / Disney
- NFL Media, NBA
- FanDuel, DraftKings, Fanatics

**Tier 2b: brand and product motion at tech and AI**
- Anthropic, OpenAI, Spotify, Airbnb, Figma, Adobe, Canva, Duolingo

**Tier 3: studios and broadcast-design agencies** (verify each is active and hiring)
- Gunner, Oddfellows, ManvsMachine, Elastic, Imaginary Forces, Psyop
- Giant Ant, Golden Wolf, Tendril, Ordinary Folk
- Broadcast and sports branding: Troika, Loyalkaspar, Gretel, Trollbäck+Company, Sarofsky

The owner can add or remove companies at approval (decision 1).

### 2b. Automated services (the machine lane)

For each tool, research:
- what it reads;
- what it scores and how;
- what the candidate sees;
- which knockouts employers can configure;
- published docs;
- bias audits;
- legal status.

| Category | Tools to profile |
|---|---|
| ATS front doors | Greenhouse, Ashby, Lever, Workday (+ HiredScore grades), Eightfold, iCIMS, SmartRecruiters, Avature, Phenom, Oracle Recruiting, SAP SuccessFactors, Jobvite. In-house systems at Google, Meta, Amazon, Apple |
| AI ranking and sourcing | LinkedIn Recruiter (AI-Assisted Search, Hiring Assistant), Gem, SeekOut, hireEZ, Findem, Beamery, Paradox |
| AI interviews and interview notes | HireVue, Eightfold AI Interviewer, BrightHire, Metaview (interview recording and summaries) |
| Verification | HireRight, Sterling / First Advantage, Checkr, The Work Number (Equifax), identity and deepfake checks in video interviews |

**How (method):**
1. **Detect the ATS** for every target from its careers URL and page source (`boards.greenhouse.io`, `jobs.ashbyhq.com`, `jobs.lever.co`, `myworkdayjobs.com`, Eightfold `/careers`). This is fast and reliable.
2. **Public job JSON** where it exists: Greenhouse, Lever and Ashby public boards; the Eightfold `api/apply/v2/jobs` call used for Netflix. From these, read posting dates, locations, work-location options, and pay.
3. **Vendor docs and help centers** (A–). Examples: Workday's HiredScore grade definitions; Eightfold's engineering blog.
4. **NYC Local Law 144 bias-audit summaries.** Employers using automated tools for NYC roles must post them publicly. They can reveal **which employer uses which tool**.
5. **Court dockets and law-firm trackers:** Mobley v. Workday, Kistler v. Eightfold.
6. **Testable without submitting:**
   - open an application form and list its questions (knockouts) without sending;
   - use parse previews where a portal offers them.

### 2c. The review lane: insider testimony ("look deeper")

**Source ladder, highest first.** Every claim records its rung.

| Rung | Source | Grade | Use |
|---|---|---|---|
| L1 | Company-published hiring guidance: "how we hire" pages, interview-prep guides, design-blog posts about hiring, the postings themselves (portfolio instructions) | A | Process facts |
| L2 | Named hiring managers, creative directors and recruiters (current or former) on record: conference talks (Config, Adobe MAX, Motion Plus Design, Blend), podcasts (School of Motion, Motion Hatch, Design Better, Dive Club), posts, AMAs. **Verify the speaker's role and date** | B | What stands out; what sinks |
| L3 | Studio founders and creative directors on hiring | B | Reel and portfolio bar |
| L4 | Candidate reports: Glassdoor, Blind, Fishbowl, Reddit, prep vendors (igotanoffer, Exponent, Prepfully) | D | Process shape only. **≥3 independent reports** before a claim counts |
| L5 | Primary conversations through warm ties (informational, 20–30 min, fixed guide) | B (small n) | The only source for a specific team's current bar |

**Starter sources found 2026-11-05** (Sourced; not yet read in full):
- School of Motion, ["How to Get Hired: Insights from 15 World-Class Studios"](https://schoolofmotion.com/blog/how-to-get-hired-motion-design-ebook) (L3).
- School of Motion Podcast, [Buck co-founder Ryan Honey](https://schoolofmotion.com/blog/studio-ascended-buck-cofounder-ryan-honey-som-podcast) (L3).
- School of Motion, [2026 Motion Design Hiring Guide](https://schoolofmotion.com/motion-design-hiring-guide): 13,287 listings and a reel scorecard. The employer-facing guide shows how studios are told to evaluate (L3, vendor).
- Buck's own postings on [Homerun](https://buck.homerun.co/freelance-senior-after-effects-animator) (L1).
- [igotanoffer: Meta product designer interview](https://igotanoffer.com/blogs/tech/facebook-product-designer-interview) and Glassdoor Meta and Google design interview reports (L4).
- [Prepfully: what portfolio-review interviewers look for](https://prepfully.com/video-interview-guides/udit-from-prepfully-deep-dives-into-the-portfolio) (L4).
- [Weston Karnes: product design interviews at Google, Dropbox, Lyft](https://medium.com/@westonkarnes/learnings-from-product-design-interviews-7a494d531960) (L2/L4).

**Extraction: the Insider Claims Ledger.** One row per claim:

```
id | company | team | lane (brand / product / live / studio) | level | speaker (role, current/former, verified Y/N)
| date | source + rung | quote (≤25 words) | claim type (stands out / sinks / process / portfolio / reel / exercise / leveling)
| grade | corroborations | recheck-by
```

**Synthesis:**
- **Per company:** an *evaluation rubric*. What they score, in what order, and what fails fast.
- **Across companies:** a *stands out / sinks* matrix by lane. The lanes differ:
  - brand and marketing motion;
  - product and UI motion;
  - live and broadcast;
  - studio.

**Rules:**
- A claim from one anecdote never becomes a rule.
- Conflicts between sources are logged, not averaged.
- Product-design hiring advice isn't assumed to apply to brand-motion hiring.

**L5 primary conversations.** A question guide ships with R4. Conditions:
- Only through people the candidate already knows, or vendor-side contacts.
- Purpose stated honestly.
- Nothing recorded without consent.
- Nothing that exposes a confidential search to the wrong room.

### 2d. The candidate's own outcome data

This feeds everything above, and it's the cheapest research there is.

- Log every application with these fields:
  - submitted date;
  - posting age at submit;
  - channel;
  - referral (yes/no);
  - furthest stage;
  - outcome and date;
  - exact rejection wording.
- Send one polite feedback request after each rejection.
- Reconstruct missing dates from email.
- Re-run the pre-flight gate on every past package. Each defect it finds becomes an eval fixture.

## 3. Method and quality bar

- **Labels:**
  - evidence grade A–D (plus EST) and a recheck-by date (`knowledge/12`);
  - VERIFIED / ASSUMED on every claim about a company or tool.
- **Recency:**
  - process claims ≤24 months old;
  - portal, location and pay facts ≤30 days old, and re-verified at application time.
- **Triangulation:**
  - an L4 claim needs 3 independent reports;
  - an L2 claim needs a verified speaker role;
  - any rule that changes a skill needs at least one A or B source.
- **Vendor bias:** a tool's own claims are A– at best. Vendor surveys are C.
- **Ethics and confidentiality:**
  - No question in public that reveals a confidential search.
  - No contacting employees under a false pretext.
  - No scraping behind logins, and no ToS violations.
  - No personal data on named people beyond their public role.
  - No research into gaming screens (prompt injection, hidden text).
- **Tooling:**
  - The `deep-research` skill for each company.
  - Parallel subagents in Claude Code, one company each, with the fixed output template in §4.
  - Public job APIs.
  - The existing `scan_postings.py` and `warm_paths.py` in `mastertools-career`.

## 4. Outputs, and where they go

| Output | Contents | Public-safe? |
|---|---|---|
| `dossiers/<company>.md` (template exists) | Q1–Q6 facts, dated and graded | Yes: company facts only |
| `<candidate>/fit/<company>.md` | Fit, gaps, channel names, priority | **No:** private bundle only |
| `knowledge/15-ats-and-ai-tools.md` | Tool profiles (§2b) | Yes |
| `knowledge/16-insider-claims-ledger.md` (+ CSV) | The ledger (§2c) | Yes, if speakers are public figures quoting on record; L5 notes stay private |
| `knowledge/17-what-stands-out-by-lane.md` | Cross-company matrix and per-company rubrics | Yes |
| Updates to `01`, `07`, `08`, `12`, `13`, and the pre-flight gate | Folded findings | Yes |
| `evals/fixtures/` | Real-package defects, anonymized | Yes, once anonymized |

**Fixed subagent output template** (one per company, R1):

```
# <Company> dossier — <date>
Q1 Reachability: policy (VERIFIED/ASSUMED, source, date) · open motion/creative roles (title, location, work option, posted date, pay) · verdict PASS/FAIL against <profile rule>
Q2 Door: ATS (how detected) · AI layer · knockout questions seen · referral mechanics · limits
Q3 Bar: loop stages · portfolio/reel/exercise expectations · leveling
Q4 Signal: top 5 "stands out" and top 5 "sinks" claims with ledger ids
Q5 Channel: referral program, vendor studios, recruiters (by role), events
Q6 Risk: verification, AI policy, red flags
Unknowns + how to resolve
Sources (graded)
```

## 5. Phases

**R-0 (standing rule):** no research phase ever gates a live posting. A live application for a reachable role ships on the gates it already has. Research improves the next application.

| Phase | Work | Effort | Done when |
|---|---|---|---|
| **R0 Reachability and doors sweep** | For about 35 companies:<br>• remote/hybrid policy (VERIFIED)<br>• open motion or creative roles<br>• ATS detected<br>• posting ages<br>• posted pay<br>Outputs a ranked target sheet | ~2–3 h AI; 15 min owner review | Every Tier 1–2 company has a VERIFIED reachability verdict |
| **R1 Tier-1 dossiers** | Netflix (refresh), Pinterest, Meta, Google/YouTube, Buck: Q1–Q6 | ~1 h AI each | Five dossiers pass the template, with graded sources |
| **R2 Machine lane** | Profiles of the ~10 tools R0 found; NYC LL144 audit lookup; legal tracker | ~4–6 h AI | `knowledge/15` written; each Tier-1 company maps to its tools |
| **R3 Review lane** | ≥15 L1–L3 sources per Tier-1 company where they exist; the ledger; rubrics; the cross-lane matrix | ~1–2 days AI | Saturation: 3 sources in a row add no new claim |
| **R4 Primary conversations** | 3–5 calls through warm ties, using the guide | Owner time, ~30 min each | Notes filed privately; claims added to the ledger as L5 |
| **R5 Synthesis into skills** | Fold findings into knowledge, the red-flag catalog and the pre-flight gate. Run the gate on the next real application. Fixtures from real defects | ~1 day AI | Gate updated; ≥10 real fixtures; evals pass |
| **R6 Cadence** | Monthly R0 sweep; quarterly review-lane refresh; a portal re-check before every application | Ongoing | Stale claims under 10% at each refresh |

**Stopping rules:**
- A company that fails Q1 stops at R0.
- The review lane stops at saturation.
- R0–R3 is capped at about four working sessions unless the owner extends it.

## 6. Risks

| Risk | Mitigation |
|---|---|
| Research becomes the procrastination channel | R-0. Every phase ends with a dated action on a live posting |
| Insider claims are anecdotes | The ladder, triangulation rules, and conflicts logged rather than averaged |
| Remote policies change monthly | 30-day recency on Q1 facts; re-check at application time |
| Confidential search leaks through research | No public questions; L5 only through pre-cleared people; sports-media rooms treated as high-overlap |
| Public repo leak | Candidate data never enters this kit; a private bundle only (see handoff) |

## 7. Decisions for approval

1. **Company list and tiers.** Add or remove anything in §2a. Is Buck in scope for staff roles, freelance, or calibration only?
2. **Reachability rule for R0.** Use the profile's rule as written (remote, pay above floor), or allow named hybrid exceptions?
3. **R4 primary conversations.** Yes or no, and which relationships are pre-cleared.
4. **Where research output lives.** Public-safe findings go into the public tools repo (as part of the career plugin) or stay private. Candidate data stays private either way.
5. **Order.** R0 first and fast, with Tier-1 dossiers right after. The live application is never blocked (R-0).
6. **Budget.** Is about four sessions for R0–R3 the right cap?

Sources:
- [School of Motion: How to Get Hired (15 studios)](https://schoolofmotion.com/blog/how-to-get-hired-motion-design-ebook)
- [School of Motion Podcast: Buck co-founder Ryan Honey](https://schoolofmotion.com/blog/studio-ascended-buck-cofounder-ryan-honey-som-podcast)
- [School of Motion: 2026 Motion Design Hiring Guide](https://schoolofmotion.com/motion-design-hiring-guide)
- [Buck: freelance Senior After Effects Animator posting](https://buck.homerun.co/freelance-senior-after-effects-animator)
- [igotanoffer: Meta product designer interview](https://igotanoffer.com/blogs/tech/facebook-product-designer-interview)
- [Prepfully: portfolio review interview](https://prepfully.com/video-interview-guides/udit-from-prepfully-deep-dives-into-the-portfolio)
- [Weston Karnes: product design interviews](https://medium.com/@westonkarnes/learnings-from-product-design-interviews-7a494d531960)
- [Workday docs: HiredScore grades](https://doc.workday.com/hiredscore/en-us/workday-hiredscore/recruiter-productivity-/concept--hiredscore-grades.html)
- [Perkins Coie: NYC Local Law 144 final rules](https://www.perkinscoie.com/insights/update/new-york-city-adopts-final-rules-law-governing-automated-employment-decision-tools)
