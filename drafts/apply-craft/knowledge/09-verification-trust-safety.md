# 09 · Verification, trust, and safety

Everything the application claims will be checked by software, by people, or by a background check. This file covers what gets checked, how, and the rules that keep the candidate safe at the same time.

---

## 1. What employers verify

**Background checks**
- **HireRight 2025 Global Benchmark** (B): more than three-quarters of employers found a discrepancy in a candidate's background in the past year.
- North America's most common discrepancies:
  - criminal history (41%);
  - employment history (36%): dates, titles, employers;
  - education.
- Implications:
  - Dates, titles, and employer names must match across the resume, LinkedIn, site, and the application form exactly.
  - "Close enough" dates (Jan vs. Mar) read as discrepancies.

**Authorship of creative work**
- **Credits checks** (D, from creative directors on Fishbowl):
  - reviewers email someone else listed on the project;
  - they ask in the interview for a walkthrough: brief → idea → production → who did what.
- Implication: every piece states the candidate's exact role, names the team, and the candidate can narrate the decisions.

**Skills**
- **Eightfold skills validation** ("trust but validate"; A–, vendor primary):
  - skills are classed as validated, to-validate, or missing against the role;
  - Eightfold markets candidate-fraud detection, including fabricated skills.
- Implication: list a skill only where a role, project, or proof piece shows it in use.

**Online presence**
- **CareerBuilder 2018** (B, dated):
  - 70% of employers screen social media;
  - 66% use search engines;
  - 47% are less likely to interview a candidate they can't find online.
- Implication: run a name search `[ME]` and fix what comes up first:
  - site;
  - LinkedIn;
  - reel host;
  - old portfolio accounts.

**External data in AI screening**
- **Kistler v. Eightfold** (filed January 20, 2026; FCRA class action; pleading stage as of April 2026):
  - The plaintiffs allege the platform compiles candidate reports using outside data such as LinkedIn profiles and publications.
  - Eightfold disputes this.
- Implication: assume the public footprint *may* be read alongside the application, and keep it consistent. Never treat the allegations as established fact.

## 2. AI detection and authenticity (dual-reader rule)

**AI-text signals**

| Source | Finding | Strength |
|---|---|---|
| TopResume 2025 (600 hiring managers) | About 1 in 5 would reject an AI-looking resume; 25% find AI unacceptable for cover letters; 52% accept AI help if the final is human | C |
| Resume Now 2025 | 62% of employers are more likely to reject AI-generated resumes that lack personalization | C |
| Resume Genius 2025 | 35% of hiring managers have seen AI-created portfolio work | C |
| UXfolio 2026 | 43% rate "obvious AI overuse" a portfolio red flag | C |
| Xu, Li & Jiang (AIES 2025) | LLM screeners prefer resumes written by the same model 67–82% of the time | A– |

**Rule:**
- Standard, parseable structure, carrying specifics only the candidate could write.
- Flag the AI-tell list in `00`, then replace the flagged text with real detail. Don't just reword it.

**AI in the work itself**
- Disclose where and how AI tools were used in any piece.

**Headshots**
- Ringover (C): 66% of recruiters would be put off by an undisclosed AI headshot they recognized.
- Use a real, recent likeness.

## 3. Content Credentials (C2PA)

**What it does**
- An open standard: cryptographically signed provenance attached to a file (who made it, with what, and what edits).
- LinkedIn shows a "CR" icon on images with credentials (LinkedIn Help).
- Adobe's Content Authenticity app is free and can attach creator credentials.

**Limits**
- Many platforms strip metadata on upload.
- A missing credential proves nothing.
- "Durable" credentials add an invisible watermark plus a fingerprint so provenance can be recovered after stripping (Content Authenticity Initiative).
- Reported at CES 2026: many viewers read the "CR" icon as meaning "AI-made."

**Rule:**
- Optional and secondary.
- Apply durable credentials to key stills if it costs under 30 minutes.
- **Always** pair them with a visible credits line, which is what humans actually read.

## 4. System integrity: never game the screen

- **Hidden prompt injection:** a USENIX Security 2026 study found hidden text aimed at AI screeners in about 1% of 196,682 resumes. Parsers expose it to recruiters and vendors flag it. **Banned** (see `00`).
- **No keyword stuffing.** A wall of terms in white text, or a skills dump unconnected to roles, breaks the dual-reader rule and fails skills validation.
- **One identity.** The same name and contact details everywhere. If the person uses a different professional name, record it in the profile and use it consistently.

## 5. Candidate safety

**Scams**
- FTC-reported job-scam losses rose from $90M (2020) to $501M (2024) (A–).
- Malwarebytes: #OpenToWork posts attract fake recruiters (B).
- **Scam screen** before engaging any outreach:
  - Verified Recruiter badge, or a corporate-domain email and calendar invite;
  - the role exists on the company's own careers site;
  - no fees;
  - no SSN or bank details before a verified offer;
  - no software installs from a DM;
  - no "interview" over chat apps only.

**Privacy of the candidate**
- Don't publish a home address or personal phone on public pages (city and region are enough).
- Proof pages stay unlisted, not indexed.

**Confidential search**
- Recruiters-only Open to Work.
- Sharing turned off before edits.
- No job-hunt language in public text (see `05`).

## 6. Privacy of third parties (profile-driven)

- Confidentiality rules come from `data/profile.md` (see `00` and `templates/user-profile.md`).
- For regulated sectors (healthcare, mental health, legal, youth services, education):
  - **no client-identifying information anywhere**: copy, images, video, captions, alt text, file names, metadata, testimonials, or "anonymized" stories with unique details;
  - aggregate, de-identified numbers only.
- **NDA or employer work:** permission first; otherwise abstract it, or recreate it with fictional content labeled as a recreation.
- **The skill itself:**
  - never stores client or third-party personal data in `data/`;
  - never saves it to memory;
  - if pasted inputs contain it, the skill stops, says so, and asks for a de-identified version.

## 7. Consistency table (required output)

| Fact | Resume | LinkedIn | Site/About | Cover letter | App form | Status |
|---|---|---|---|---|---|---|
| Name | | | | | | MATCH/FIX |
| Each title | | | | | | |
| Each employer | | | | | | |
| Each date range (month/year) | | | | | | |
| Location / work type | | | | | | |
| Degree / certs | | | | | | |
| Key numbers reused | | | | | | |
