# 01 · How screening works (2026)

How an application gets surfaced, skimmed, and judged at large companies, with AI on both sides of the table. Strength labels A–D follow `00`. Sources and dates are in `12-evidence-library.md`.

---

## 1. The funnel

```
Portal upload ──► parse into a structured profile ──► matcher / recruiter search ──► human skim (seconds)
   ──► hiring-manager read (minutes) ──► portfolio review ──► screens ──► interview loop ──► background check
```

Every stage can lose a candidate for different reasons. Diagnose which stage is failing before rewriting anything.

## 2. ATS as a searchable database (the classic model)

- **ATS use is near-universal at large employers.** Jobscan found an ATS at 98.4% of Fortune 500 companies (492 of 500). *(B)*
- **Recruiters filter; most systems don't auto-reject on content.** In Jobscan's 2025 survey of 384 recruiters, 99.7% use filters. *(B/C)*

  | They filter by | Share |
  |---|---|
  | Skills | 76.4% |
  | Education | 59.7% |
  | Job title | 55.3% |
  | Certifications | 50.6% |
  | Years of experience | 44% |
  | Location | 43.4% |

  An unmatched resume isn't rejected so much as never found.
- **Title match is the single biggest correlate.** In Jobscan's analysis of 2.5M applications, resumes containing the posting's exact job title saw about a 10.6x higher interview rate. Correlation, not cause. *(B)*
- **Other correlates from the same analysis:** a cover letter (3.4x); an optimized LinkedIn profile (2.2x). *(B, correlational)*
- **What makes candidates stand out to recruiters:** measurable achievements (58%), tailoring (55%), LinkedIn consistent with the application (about 47%). *(C)*
- **Recruiters check LinkedIn:** 75% source candidates there; 73.3% always or often look at a candidate's profile. *(C)*

**Implication:** state each required skill explicitly. Put the target title family where the rules allow (headline language, summary, Skills). Never rename past titles.

## 3. Learned matching: Eightfold (Netflix's application platform)

Source: Eightfold's engineering blog (Aug 2025), strength A as a vendor's description of its own system. The match score combines:

- **Meaning-level embeddings** of the resume and the job description.
- **Skill overlap overall**, plus **skill overlap from the most recent roles only**. Recency matters, so must-have skills belong in the current role where that's truthful.
- **Title fit:** current-title similarity, plus a **predicted next title**. A model reads the sequence of past titles, skills, and tenure and predicts where the career goes next.
- **Industry and company similarity:** whether past employers look like the companies this role values. This is a **fixed signal**; no edit changes it.
- **"Hireability":** a predicted next-company embedding, compared with the hiring company.
- **Similarity to "ideal candidate" reference profiles and to the hiring manager's own profile.**
- The blend is trained on historical outcomes (who advanced, was hired, and thrived) and shown to recruiters as **0–5 stars**.

**Calibration** (Eightfold community guidance; A–):
- Ideal candidates have the most impact on the match score.
- Recruiters are told to choose 3–5, often current employees, with titles close to the role, plus 3+ skills, 3+ alternate titles, and a min/max years of experience.

**Skills validation** (Eightfold blog; A–): each required skill is classified as one of:
- *validated*: claimed, and the AI confirms it;
- *to validate*: claimed, but not confirmed;
- *missing*: not claimed, and not inferable.

So a required skill that is never stated and can't be inferred shows up as **missing**.

**Fraud:** Eightfold markets detection of impersonation and fabricated skills.

**External data (allegation, not established):**
- *Kistler v. Eightfold*, filed January 2026 and in federal court at the pleading stage as of April 2026, alleges Eightfold uses outside data such as LinkedIn profiles, publications, and application history.
- It also alleges Eightfold retains applicant data for other roles and ranks candidates 0–5.
- Eightfold disputes this, saying it works from data candidates share or customers provide.
- Practical takeaway either way: keep LinkedIn and every application to the same company consistent.

## 3b. Workday HiredScore (Netflix's stack includes Workday; whether HiredScore is on is ASSUMED unknown)

- HiredScore grades each candidate on "how well their resumes match the skills and qualifications specified in the job description." *(A–, Workday docs)*
  - **A:** meets or exceeds the basic requirements.
  - **B:** meets them.
  - **C:** meets some.
  - **D:** doesn't meet them.
- Recruiters can sort and filter by grade. The docs add that C and D candidates "might still be a great fit."
- **Implication:** literal requirements (years, named tools, domain) matter on top of semantic similarity. Craft years done under a non-craft title may not count (`13` B1).
- **Legal context:** *Mobley v. Workday*:
  - The ADEA collective (applicants 40+) was certified in May 2025.
  - HiredScore-screened applicants were added in July 2025.
  - In March 2026 the court held that the ADEA covers applicants.
  - Secondary summary; check the docket.

## 3c. How often software actually rejects (myth check)

- Enhancv interviewed 25 US recruiters *(C, small sample)*:
  - 92% said their systems don't auto-reject on formatting or content;
  - knockout questions are mostly eligibility checks;
  - 44% had AI match scores, and more than half ignore or disable them.
- **Real losses come from:**
  - **volume:** reviewers stop once they have enough;
  - **timing:** screening often starts within 3 days of posting;
  - **form knockouts.**
- So the "75% never seen by a human" claim is a myth. "Never found, or found too late" is the real risk.

## 3d. Bias in LLM screeners (informational; never "fix" identity)

- UW, AIES 2024 (3 embedding models; 3M+ comparisons) *(A–)*:
  - white-associated names were preferred 85% of the time;
  - Black male names were never preferred over white male names.
- UW, FAccT 2024 (GPT-4) *(A–)*:
  - CVs with disability-related credentials ranked first only 25% of the time;
  - depression-related content stayed worst even with anti-bias instructions.
- **Practical rule:** describe sector work (such as mental-health services) as operations and outcomes, so a careless model can't misread it as personal. See `13` B9.

## 3e. Recruiter-side fraud vigilance (raises the cost of anything that looks off)

- Greenhouse 2025 (US: 665 hiring managers and recruiters; 1,200 job seekers) *(C, vendor)*:
  - 91% of recruiters have spotted candidate deception;
  - 22% of hiring managers caught prompt injections in resumes;
  - 39% are doing more in-person interviews.
  - On the candidate side, 41% admit to having used prompt injections.
- **Implication:** anything that looks gamed costs disproportionately.

## 4. Parsing and file format

- Single column. No tables, text boxes, side columns, icons, or graphics. Contact info goes in the body, not the header or footer. Standard section names. Consistent dates (MM/YYYY). *(B/C, from career centers and Jobscan)*
- **File type:** a text-based PDF exported from Word or Google Docs, or a DOCX. Never a design-tool export (Canva, InDesign).
- Vendor tests disagree, but most find DOCX parses at least as reliably. *(C)*
- If the profile a portal builds from your upload shows errors, re-upload as DOCX. Netflix's portal asks applicants to review that profile after applying (VERIFIED, Nov 2026).

## 5. The human skim

**Initial skim** (Ladders eye-tracking, 2018; B):
- About **7.4 seconds** on average.
- **Job titles** drew the most attention.
- Strong resumes: simple layouts, clear section and title headers, bold titles over bulleted accomplishments, a layout that follows the F-pattern of how eyes scan a page.
- Weak resumes: multiple columns, long sentences, little white space.
- Keywords should appear in context.

**Deep read once shortlisted:**
- Minutes, not seconds.
- ResumeGo's 2018 simulation (482 hiring professionals): two-page resumes were preferred 2.3x, more strongly at senior levels, when the content earned the space. *(C)*

**Bullet standard** (Laszlo Bock, former Google SVP of People Operations): "Accomplished [X] as measured by [Y] by doing [Z]."

## 6. AI on both sides of the table

- **Machine readers may favor AI text.** Xu, Li & Jiang (AIES 2025; arXiv v4 2026): AI evaluators preferred AI-written resumes over equally qualified human-written ones **67–82%** of the time. *(A)*
- **Human readers penalize generic AI text:**
  - TopResume 2025 (600 hiring managers): about 1 in 5 would reject a resume that looks fully AI-generated. *(C)*
  - Resume Now 2025: 62% say AI resumes without customization get rejected. *(C)*
- **Tailoring stopped signaling.** Galdin & Silbert (2025; Freelancer.com, 2.7M applications to 61,000 coding jobs) found an AI-based measure of how tailored an application was predicted hiring before LLMs and stopped predicting it after. *(A–, working paper)*
  - In their model, losing that signal meant workers in the top fifth by ability were hired 19% less often.
  - The setting is freelance gigs, so treat it as directional for corporate hiring.
- **Resolution:** clean, standard structure (for machines) carrying specifics only the candidate could write (for humans).
- **Hidden prompts get caught.** About 1% of roughly 197,000 resumes contained hidden injections (USENIX Security 2026). More than 90% were embedded data, not instructions. *(A)*

## 7. LinkedIn's AI layer

- **AI-Assisted Search is now the default:** recruiters describe a role in plain language and the system builds the candidate list. *(C, vendor reviews)*
- **Hiring Assistant** (generally available since September 2025) recommends and ranks candidates. Per reviews, it weighs career trajectory, related skills, and engagement signals, and it can surface previous applicants. *(C)*
- See `05-linkedin.md`.

## 8. What predicts hiring later

Sackett et al. 2022 revised the classic meta-analysis of hiring methods (Journal of Applied Psychology; A):

| Method | Validity |
|---|---|
| Structured interviews | .42 (top-ranked) |
| Job knowledge tests | .40 |
| Empirically keyed biodata | .38 |
| Work-sample tests | .33 |
| Cognitive ability | .31 |

**Implications:**
- A portfolio proof piece works as a self-administered work sample.
- The live walkthrough is a structured-interview moment.
- Prepare both.
