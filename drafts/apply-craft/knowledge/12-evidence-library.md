# 12 · Evidence library

Every claim the suite relies on, with its source, date, strength, and when to recheck it. Skills cite claims by ID (for example "E06") in their `references/evidence.md`.

**Strength**
- **A:** primary, official, or peer-reviewed.
- **A–:** primary but vendor-run, or a working paper.
- **B:** large dataset with a stated method.
- **C:** survey, vendor claim, or expert blog.
- **D:** anecdote or forum.
- **EST:** estimate from the `motion-design-career-strategist` reference.

**Recheck-by**
- **Feb 2027:** fast-moving (platform features, portal settings, lawsuits, AI-attitude surveys).
- **Nov 2027:** slower (studies, standards).
- **Per app:** re-verify on every application.
- **Historical:** a dated study, kept for direction. Replace it when newer data exists.

**At run time:** if a claim behind a decision is past its recheck-by date, the skill re-verifies it with web search, or labels it ASSUMED.

---

## 1. Screening, ATS, and selection science

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E01 | 98.4% of the Fortune 500 use an ATS | [Jobscan: Fortune 500 ATS report](https://www.jobscan.co/blog/fortune-500-use-applicant-tracking-systems/) | 2025 | B | Nov 2027 | 01 |
| E02 | 99.7% of recruiters use filters. Filters by: skills 76.4%, education 59.7%, job title 55.3%, certifications 50.6%, years of experience 44%, location 43.4% | [Jobscan: State of the Job Search 2025](https://www.jobscan.co/state-of-the-job-search) | 2025 | C | Feb 2027 | 01, 03 |
| E03 | Matching the posting's title correlated with about 10.6x interview rate; cover letter 3.4x; optimized LinkedIn 2.2x | Jobscan 2025 (as E02) | 2025 | B (correlational) | Feb 2027 | 03, 04, 05 |
| E04 | What makes candidates stand out: measurable achievements 58%, tailoring 55%. About 47% of recruiters check LinkedIn against the application | Jobscan 2025 | 2025 | C | Feb 2027 | 03, 05 |
| E05 | 75% of recruiters source on LinkedIn; 73.3% check profiles; 69.4% rate referrals very or extremely important | Jobscan 2025 | 2025 | C | Feb 2027 | 05, 08 |
| E06 | Eightfold matching uses:<br>• semantic embeddings<br>• skill overlap (overall and recent roles)<br>• current-title similarity<br>• predicted next title<br>• company and industry similarity<br>• "hireability"<br>• similarity to ideal-candidate and hiring-manager profiles<br>It is trained on outcomes and scores 0–5 stars | [Eightfold Engineering: AI-powered talent matching](https://eightfold.ai/engineering-blog/ai-powered-talent-matching-the-tech-behind-smarter-and-fairer-hiring/) | Aug 2025 | A– | Feb 2027 | 01, 03 |
| E07 | In calibration, ideal candidates have the most impact; recruiters pick 3–5 | [Eightfold Community: Calibration best practices](https://community.eightfold.ai/best-practices-how-to-discussions-71/calibration-filters-best-practices-2091) | 2025 | A– | Feb 2027 | 01 |
| E08 | Skills are classed as validated, to-validate, or missing | [Eightfold: Trust but validate](https://eightfold.ai/blog/trust-but-validate/) | 2025 | A– | Feb 2027 | 01, 09 |
| E09 | Eightfold markets detection of candidate fraud, including fabricated skills | [Eightfold: Candidate fraud](https://eightfold.ai/trust/candidate-fraud/) | 2026 | C (vendor claim) | Feb 2027 | 00, 09 |
| E10 | Kistler v. Eightfold:<br>• filed January 20, 2026<br>• an FCRA class action<br>• alleges use of external data (LinkedIn, publications)<br>• Eightfold disputes it<br>• at pleading stage as of April 2026 | [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/ai-company-eightfold-sued-helping-companies-secretly-score-job-seekers-2026-01-21/); [Akin Gump tracker](https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/ai-hiring-platform-faces-fcra-class-action-over-data-use-or-kistler-et-al-v-eightfold-ai-inc) | Jan–Apr 2026 | A (filing) / B | Feb 2027 | 01, 09 |
| E11 | Recruiters skim an initial resume in about 7.4 seconds; job titles get the most attention | [Ladders eye-tracking study (PDF)](https://csuglobal.edu/sites/default/files/blog-files/theladders-eyetracking-studyc2.pdf) | 2018 | B | Historical | 01, 03 |
| E12 | Recruiters preferred two-page resumes 2.3x over one page (for experienced candidates) | [ResumeGo: one or two pages](https://www.resumego.net/research/one-or-two-page-resumes/) | 2018 | B | Historical | 03 |
| E13 | X-Y-Z bullet formula: "Accomplished X, as measured by Y, by doing Z" | Laszlo Bock (former Google SVP People), widely cited | 2014 | C | none | 03 |
| E14 | Validity of selection methods: structured interviews .42, job knowledge .40, biodata .38, work samples .33, cognitive ability .31 | Sackett, Zhang, Berry & Lievens, *J. Applied Psychology* 2022, [doi:10.1037/apl0000994](https://doi.org/10.1037/apl0000994) | 2022 | A | Nov 2027 | 01, 06 |
| E15 | Hidden prompt injection in about 1% of 196,682 de-identified resumes (hireEZ). More than 90% were hidden data (extra keywords), not explicit instructions. Some may come from templates | USENIX Security 2026, via [Let's Data Science](https://letsdatascience.com/news/applicants-hide-prompts-in-resumes-becd8ae8) and [Built In](https://builtin.com/articles/hidden-ai-prompts-in-resume); likely the paper at [arXiv 2605.28999](https://arxiv.org/html/2605.28999v1) (confirm) | 2026 | A– | Nov 2027 | 00, 09 |

## 2. AI on both sides of hiring

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E16 | LLM screeners prefer resumes written by the same model 67–82% of the time | Xu, Li & Jiang, AIES 2025, [doi:10.1609/aies.v8i3.36755](https://doi.org/10.1609/aies.v8i3.36755); [arXiv 2509.00462](https://arxiv.org/abs/2509.00462) | 2025 | A– | Nov 2027 | 00, 01 |
| E17 | After LLMs, a tailoring-based signal stopped predicting hiring. Top-quintile workers were hired 19% less often; bottom-quintile 14% more often | Galdin & Silbert, "Making Talk Cheap," [arXiv 2511.08785](https://ideas.repec.org/p/arx/papers/2511.08785.html) | 2025 | A– (working paper) | Nov 2027 | 00, 04 |
| E18 | About 1 in 5 hiring managers would reject an AI-looking resume; 25% find AI unacceptable for cover letters; 52% accept AI help if the final is human | [TopResume 2025 survey (600 HMs)](https://topresume.com/career-advice/ai-in-hiring-survey) | 2025 | C | Feb 2027 | 04, 09 |
| E19 | 62% of employers are more likely to reject AI-generated resumes that lack personalization | [Resume Now: AI Applicant Report](https://www.resume-now.com/job-resources/careers/ai-applicant-report) | 2025 | C | Feb 2027 | 03, 09 |
| E20 | 35% of hiring managers have seen AI-created portfolio or creative work | [Resume Genius: AI impact on hiring](https://resumegenius.com/blog/job-hunting/ai-impact-on-hiring) | 2025 | C | Feb 2027 | 06, 09 |
| E21 | A tone mismatch between resume and cover letter is a common AI giveaway | CV Genius survey, via [Black Enterprise](https://www.blackenterprise.com/hiring-managers-reject-ai-generated-job-applications/amp/) | 2025 | C | Feb 2027 | 04 |
| E22 | About 54% of long LinkedIn posts in late 2024 were likely AI-written | [Originality.ai](https://originality.ai/blog/ai-content-published-linkedin) | 2024 | C (detector vendor) | Feb 2027 | 05 |
| E23 | Ringover AI-headshot survey (1,087 recruiters):<br>• 76.5% preferred AI headshots in blind tests<br>• 66% would be put off by an undisclosed AI headshot they recognized<br>• 88% want disclosure | [Staffing Industry Analysts](https://www.staffingindustry.com/news/global-daily-news/majority-of-recruiters-prefer-ai-headshots-over-real-ones) | 2024 | C | Feb 2027 | 05, 09 |

## 3. Cover letters

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E24 | Callback rates in a field experiment (7,287 applications): no letter 10.7%; generic 12.5%; tailored 16.4% | [ResumeGo: cover letters](https://www.resumego.net/research/cover-letters/) | 2019–20 | B | Historical | 04 |
| E25 | 81% of hiring professionals value tailored over generic letters | ResumeGo (as E24) | 2020 | C | Historical | 04 |
| E26 | 83% of hiring managers always or often read cover letters; 45% read the letter before the resume (625 HMs) | [Resume Genius: cover letter statistics](https://resumegenius.com/blog/cover-letter-help/cover-letter-statistics) | 2025 | C | Feb 2027 | 04 |
| E27 | 51.7% of recruiters never read cover letters; heads of HR (29.4%) and HR managers (22.9%) skip them far less | [Novorésumé: cover letter statistics](https://novoresume.com/career-blog/cover-letter-statistics) | Dec 2025 | C | Feb 2027 | 04 |
| E28 | 42% of HR professionals prefer half a page to a full page; 40% prefer under half a page | [ResumeLab](https://www.resumelab.com/cover-letter/how-long), via [The Muse](https://www.themuse.com/advice/how-long-should-cover-letter-be) | 2020s | C | Nov 2027 | 04 |

## 4. LinkedIn

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E29 | Spotlights:<br>• Open to Work (within 90 days)<br>• More likely to respond<br>• Engaged with your talent brand<br>• Has company connections<br>• Past applicants | [LinkedIn: Prioritize warm leads with Spotlights (PDF)](https://business.linkedin.com/content/dam/me/business/en-us/talent-solutions/resources/pdfs/lts-global-newsletter-leads-spotlights.pdf) | Older | A– | Feb 2027 | 05, 08 |
| E30 | Skills Match compares a job's skills with the member's explicit Skills list. A third-party explainer says implicit skills from the profile text count too | [LinkedIn Help a793433](https://www.linkedin.com/help/linkedin/answer/a793433) (A); [Big Game Hunter](https://thebiggamehunter.us/newlinkedinfeature-skills-match/) (B) | 2025 | A / B | Feb 2027 | 05 |
| E31 | "Rock Your Profile" (all "up to," correlational):<br>• photo: 21x views, 36x messages<br>• 5+ skills: 17x views<br>• current positions: 8x views<br>• industry listed: 9x views<br>• volunteer experience: 6x views | [LinkedIn Rock Your Profile deck (Apr 2025)](https://www.hancockcollege.edu/pd/documents/CH%20LinkedIn%20Rock%20Your%20Profile%20Deck_-April_2025.pdf) | Apr 2025 | B (marketing) | Feb 2027 | 05 |
| E32 | Verified members see 60% more profile views and 50% more engagement on average | [LinkedIn Help 140551](https://www.linkedin.com/help/linkedin/answer/140551) | 2025 | A– (platform claim) | Feb 2027 | 05 |
| E33 | The public Open to Work frame made members about 40% more likely to get recruiter InMails | [LinkedIn blog 2020](https://blog.linkedin.com/2020/october/29/the-benefits-of-sharing-with-your-community-you-re-open-to-work); [Fortune 2024](https://www.fortune.com/2024/09/05/linkedin-opentowork-badge-recruiters-job-search) | 2020/2024 | A– (dated) | Feb 2027 | 05, 08 |
| E34 | "Recruiters only" mode can't guarantee privacy from the current employer | [LinkedIn Help 67405](https://www.linkedin.com/help/linkedin/answer/67405) | 2025 | A | Feb 2027 | 05 |
| E35 | A visibility toggle controls sharing profile changes with the network; job updates can reach the network within 2 hours | [LinkedIn Help 86236](https://www.linkedin.com/help/linkedin/answer/86236) | 2025 | A | Feb 2027 | 05 |
| E36 | Field limits: headline 220, About 2,600, position title 100, description 2,000, skill 80, connection note 300 | LinkedIn Help and trackers, e.g. [AuthoredUp](https://authoredup.com/blog/linkedin-character-limit) | 2026 | B | Feb 2027 | 05 |
| E37 | AI-Assisted Search is the Recruiter default; Hiring Assistant became generally available in September 2025 | [VentureBeat](https://venturebeat.com/ai/linkedin-upgrades-its-recruiter-with-an-ai-hiring-assistant); LinkedIn announcements | 2025 | B | Feb 2027 | 05 |
| E38 | LinkedIn shows a "CR" icon on images that carry Content Credentials | [LinkedIn Help a6282984](https://www.linkedin.com/help/linkedin/answer/a6282984) | 2025 | A | Feb 2027 | 06, 09 |

## 5. Portfolio, site, and web standards

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E39 | 80% of recruiters spend 3 minutes or less on a portfolio; 54% of design managers spend 5–10 minutes, and 11% spend more | [uxdesign.cc: How recruiters look at your portfolio](https://uxdesign.cc/ever-wonder-how-recruiters-look-at-your-design-portfolio-cc8dd1ecb698) | 2020s | C | Nov 2027 | 06 |
| E40 | UXfolio 2026:<br>• red flags: low visual quality 55%, confusing navigation 48%, obvious AI overuse 43%, overly long content 42%<br>• 72% prefer a website<br>• 89% say a relevant case study matters most | UXfolio "State of UX Portfolios 2026," via [LinkedIn post](https://bg.linkedin.com/in/kalin-zdravkov). **Find the primary report** | 2026 | C (secondhand) | Feb 2027 | 06 |
| E41 | Reviewer guidance: titles say what you did; overview first; details collapsible | [Uxcel: red flags and green flags](https://uxcel.com/blog/ux-portfolio-review-red-flags-green-flags) | 2025 | C | Nov 2027 | 06 |
| E42 | 70% of employers screen social media; 66% use search engines; 47% are less likely to interview a candidate they can't find online | CareerBuilder, via [Security Magazine](https://www.securitymagazine.com/articles/89441-percent-of-employers-check-candidates-social-media-profiles) | 2018 | B | Historical | 06, 09 |
| E43 | ProfilePage / Person structured data with `sameAs` links. It must match visible content and guarantees no special search result | [Google Search Central: ProfilePage](https://developers.google.com/search/docs/appearance/structured-data/profile-page) | 2025 | A | Nov 2027 | 06 |
| E44 | Core Web Vitals "good" thresholds (75th percentile): LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 | [web.dev: Web Vitals](https://web.dev/articles/vitals) | 2024+ | A | Nov 2027 | 06 |
| E45 | WCAG 2.3.3: interaction-triggered motion can be turned off | [W3C: Understanding 2.3.3](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions) | Standard | A | Nov 2027 | 06, 07 |
| E46 | WCAG 2.2.2: moving content longer than 5 seconds needs pause, stop, or hide | [W3C: Understanding 2.2.2](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide) | Standard | A | Nov 2027 | 06, 07 |
| E47 | Creative directors check authorship by contacting others on the credits and asking for a walkthrough | [Fishbowl thread](https://www.fishbowlapp.com/post/cds-gcds-ecds-when-youre-hiring-how-do-you-know-if-the-person-did-the-work-in-their-book-broader-question-what-are-the-practical) | 2020s | D | none | 06, 09 |
| E48 | Job-specific portfolio pages: a career-services lesson says they impress; designers are split; one product sells open-tracking | [Coda lesson](https://coda.io/@timothy-moore/career-services-in-coda-katie-rivard/lesson-creating-a-company-or-job-specific-portfolio-page-35); [Fishbowl](https://www.fishbowlapp.com/post/when-applying-for-jobs-do-you-submit-a-tailored-version-of-your-portfolio-or-do-you-submit-your-website-as-is-im-noticing-that); [Superfolio](https://peerlist.io/company/superfolio) | 2020s | C/D | Nov 2027 | 06, 08 |
| E49 | Ways to show NDA work: permission, abstraction, recreation, password | [uxdesign.cc: NDA](https://uxdesign.cc/is-nda-in-the-way-of-your-design-career-5-ways-to-navigate-around-it-215176bea567) | 2020s | C | Nov 2027 | 06 |

## 6. Reels and the motion lane

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E50 | Reels: about 20–60 seconds; never more than 2 minutes; best work first | [School of Motion](https://schoolofmotion.com/blog/top-tips-tricks-killer-motion-design-demo-reel) | 2020s | C | Nov 2027 | 07 |
| E51 | Reels ideally under a minute; at most 60–90 seconds | [Artisan Talent: Ask a recruiter](https://creative.artisantalent.com/ask-a-recruiter-making-a-motion-design-reel) | 2020s | C | Nov 2027 | 07 |
| E52 | Netflix Animation early-career guidelines:<br>• the first minute must catch the eye<br>• contact info at the start and end<br>• breakdowns, with software noted<br>• tailored to the role<br>• password shown | [Netflix Animation submission guidelines](https://sites.google.com/netflix.com/earlycreatives/submission-guidelines) | 2025–26 | A | Feb 2027 | 07 |
| E53 | Motion sub-lanes, the case-study template, rejection reasons, the interview loop, tool expectations | `motion-design-career-strategist` reference | — | EST | Verify in sprint D1 | 07 |

## 7. Netflix

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E54 | The careers portal runs on Eightfold ([explore.jobs.netflix.net](https://explore.jobs.netflix.net/careers)), with Workday behind it | Portal (observed) | Nov 2026 | A | Per app | 02 |
| E55 | Portal settings include an application limit of 2 (scope unknown), a hidden match score, and a recommended star threshold of 4.0 | Portal configuration (observed) | Nov 2026 | A (observed) | Per app | 02, 08 |
| E56 | After applying, candidates review the parsed profile. The portal has a referral flow (the referred person must still apply) and a LinkedIn URL field | Portal (observed) | Nov 2026 | A | Per app | 02, 03, 08 |
| E57 | 313 of 397 listed roles were onsite | Portal snapshot | Nov 2026 | A | Per app | 02 |
| E58 | Titles carry level numbers (TPM 5, AI Engineer 6); Levels.fyi maps L5 to Senior TPM; engineering levels run 3–7 | Postings; [Levels.fyi TPM L5](https://www.levels.fyi/companies/netflix/salaries/technical-program-manager/levels/l5); [Levels.fyi levels thread](https://www.levels.fyi/community/thread/btbwqn/netflix-has-introduced-5-engineering-levels-starting-from-engineer-3-going-up-to-engineer-7) | 2025–26 | A / B | Feb 2027 | 00, 02 |
| E59 | Posted pay ranges (see table in `02`) | Individual postings | 2026 | A | Per posting | 02 |
| E60 | Culture memo:<br>• 4 principles<br>• 8 values (selflessness, judgment, candor, creativity, courage, inclusion, curiosity, resilience)<br>• the keeper test | [Netflix Culture](https://jobs.netflix.com/culture) | Jun 2024 version | A | Feb 2027 | 02 |
| E61 | Older design postings asked for a portfolio link and its password | e.g. [Senior Motion Designer (Entertainment Careers)](https://www.entertainmentcareers.net/netflix/senior-motion-designer/job/458674/); [Staff Product Designer, Ads (Teal)](https://www.tealhq.com/job/staff-product-designer-ads-platform_7ea1a135994911ce0d73a6bd4ca802c7638ae) | 2024 | A (dated) | **Verify current posting** | 02, 06 |
| E62 | 2026 Brand Creative Studio postings say "strong portfolio required" | e.g. [Manager, Motion Design (HollyList)](https://www.hollylist.com/job/manager-motion-design-nKHHfD3ANJrx3xpKM); [Production Designer (Teal)](https://www.tealhq.com/job/production-designer_7ea1a1eb2a52404d450af67bd3349388fa6c3) | 2026 | A | Per posting | 02, 07 |

## 8. Channels, timing, and safety

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E63 | Referrals are about 7% of applications but about 40% of hires | Jobvite, via [Personnel Today](https://www.personneltoday.com/?p=162186) | Older | C (secondhand) | Nov 2027 | 08 |
| E64 | Referral hire rate about 30% vs. about 7% from job boards | Jobvite/Aptitude 2024, via [Recruitmentzilla](https://recruitmentzilla.pages.dev/posts/employee-referral-programs-guide) | 2024 | C (secondhand) | Nov 2027 | 08, PLAN |
| E65 | Talent Works:<br>• applying within 96 hours made applicants up to 8x more likely to get an interview<br>• about −28% per day after that<br>• a typical applicant had about 2% interview odds<br>• Mondays and 6–10am did better | [Talent Works: apply within 96 hours](https://talent.works/blog/2017/09/28/getting-ghosted-on-your-job-applications-heres-fix-1-apply-within-96-hours/); [Talent Works: Science of the job search](https://talent.works/blog/2018/01/08/the-science-of-the-job-search-part-i-13-data-backed-ways-to-win/) | 2017–18 | C | Historical | 00, 08, PLAN |
| E66 | FTC-reported job-scam losses rose from $90M (2020) to $501M (2024) | FTC Consumer Sentinel data, via [Fortune](https://fortune.com/2025/11/17/ftc-data-confirms-job-offer-text-scams-more-common-now) | 2025 | A– | Feb 2027 | 05, 08, 09 |
| E67 | #OpenToWork posts attract fake recruiters leading to phishing and malware (Malwarebytes) | [Help Net Security](https://www.helpnetsecurity.com/2025/05/08/job-employment-scams/) | 2025 | B | Feb 2027 | 05, 08, 09 |

## 9. Verification and provenance

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E68 | More than three-quarters of employers found candidate discrepancies. North America's most common: criminal history 41%, employment history 36% | [HireRight 2025 Global Benchmark](https://hireright.com/company/newsroom/hireright-releases-2025-global-benchmark-report); [Insurance Business](https://www.insurancebusinessmag.com/uk/business-strategy/real-risk-growth-of-identity-fraud-and-candidate-misrepresentation-550067.aspx) | Jun 2025 | B | Feb 2027 (2026 edition) | 00, 09 |
| E69 | Durable Content Credentials pair metadata with an invisible watermark and a fingerprint, so provenance survives stripping | [Content Authenticity Initiative: Durable Content Credentials](https://contentauthenticity.org/blog/durable-content-credentials) | 2024–25 | A | Nov 2027 | 06, 09 |
| E70 | Many platforms strip metadata on upload; a missing credential proves nothing | [CAI: Three pillars of provenance](https://contentauthenticity.org/blog/three-pillars-of-provenance); [SoftwareSeni](https://www.softwareseni.com/durable-content-credentials-how-provenance-survives-metadata-stripping) | 2025 | A / B | Nov 2027 | 06, 09 |
| E71 | At CES 2026 many viewers read the "CR" icon as meaning "AI-made" | Coverage gathered during portfolio research. **Re-locate the source** | Jan 2026 | C | Feb 2027 | 06, 09 |
| E72 | Adobe and LinkedIn support creator Content Credentials; Adobe's Content Authenticity app is free | [Adobe + LinkedIn partnership](https://music.ai/news/creativity/adobe-linkedin-partner-on-content-authenticity); Adobe | 2025 | B | Feb 2027 | 06, 09 |

## 10. Added in challenger pass 4 (Nov 5, 2026)

| ID | Claim | Source | Date | Str | Recheck | Used in |
|---|---|---|---|---|---|---|
| E73 | HiredScore grades A–D on how well the resume matches the job description's skills and qualifications. Recruiters sort and filter by grade | [Workday docs: HiredScore grades](https://doc.workday.com/hiredscore/en-us/workday-hiredscore/recruiter-productivity-/concept--hiredscore-grades.html) | 2026 | A– | Feb 2027 | 01, 13 |
| E74 | Mobley v. Workday:<br>• ADEA collective (applicants 40+) certified May 2025<br>• HiredScore users added July 2025<br>• ADEA held to cover applicants, March 2026 | [AI Governance for HR (secondary)](https://www.aigovernanceforhr.com/p/the-mobley-v-workday-case-didnt-end); [Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/05/federal-court-allows-collective-action-lawsuit-over-alleged) | 2025–26 | B (check docket) | Feb 2027 | 01, 13 |
| E75 | Enhancv (25 recruiters):<br>• 92% say no auto-reject on formatting or content<br>• knockouts are mostly eligibility checks<br>• 44% have AI match scores; more than half ignore or disable them<br>• screening often starts within 3 days of posting | [BetaNews on Enhancv](https://betanews.com/2025/11/10/study-debunks-viral-claim-that-ai-filters-out-most-job-applicants/) | Nov 2025 | C | Feb 2027 | 01, 13 |
| E76 | Embedding-based LLM screening preferred white-associated names 85%, female names 11% | [UW News (AIES 2024)](https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/) | Oct 2024 | A– | Nov 2027 | 01, 13 |
| E77 | GPT-4 ranked disability-enhanced CVs first only 25% of the time; depression-related content stayed lowest even with instructions | [UW News (FAccT 2024)](https://www.washington.edu/news/2024/06/21/chatgpt-ai-bias-ableism-disability-resume-cv/) | Jun 2024 | A– | Nov 2027 | 01, 13 |
| E78 | Greenhouse 2025 (US):<br>• 91% of recruiters have spotted deception<br>• 22% of hiring managers caught prompt injections<br>• 39% are doing more in-person interviews<br>• 41% of job seekers admit using injections | [Greenhouse AI in Hiring Report](https://www.greenhouse.com/newsroom/an-ai-trust-crisis-70-of-hiring-managers-trust-ai-to-make-faster-and-better-hiring-decisions-only-8-of-job-seekers-call-it-fair) | Nov 2025 | C (vendor) | Feb 2027 | 01, 13 |
| E79 | Recruiter questions when an experienced person applies: is this a career change? does the title reflect the real work? will they be comfortable reporting to a boss? | [The Muse](https://www.themuse.com/advice/3-questions-a-recruiter-will-ask-when-an-overqualified-person-applies) | — | C | Nov 2027 | 13 |
| E82 | Ligatures and unmapped embedded fonts can drop letters in extracted text ("Office" → "of?ce") | [ATS Verification](https://atsverification.com/blog/10-most-common-ats-parsing-failures/) | 2026 | C | Nov 2027 | 13 |
| E83 | Applying to two different job types at one company reads as unfocused | [The Big Game Hunter](https://thebiggamehunter.us/applying-for-two-different-types-of-jobs-at-the-same-company-nobsjobsearchadvice-com/) | — | D | none | 13 |

## 11. Other sources cited in the thread (not separately numbered)

These were cited in answers during the thread. Most are secondary copies or summaries of sources already numbered above; a few are distinct supporting sources. Give one an ID if a skill starts relying on it.

| Source (as cited) | URL |
|---|---|
| ATS Verification: PDF vs Word for ATS | <https://atsverification.com/blog/pdf-vs-word-for-ats> |
| Built In: Eightfold AI hiring lawsuit | <https://builtin.com/articles/eightfold-ai-hiring-lawsuit> |
| Built In: Netflix Senior Manager, Production Design Lead | <https://builtin.com/job/senior-manager-production-design-lead/8294587> |
| Career Karma: How to get a job at Netflix | <https://careerkarma.com/blog/?p=27966> |
| LinkedIn: Spotlights guide (Korean edition PDF) | <https://customersuccess.linkedin.com/content/dam/customersuccess/learningAndEducation/files/korean/PrioritizeWarmLeads_wSpotlights_KO.pdf> |
| Google Search Central: ProfilePage structured data | <https://developers.google.com/search/docs/appearance/structured-data/profile-page?authuser=1> |
| Glyn Dewis: Content Credentials | <https://glyndewis.com/blog/content-credentials> |
| Galdin & Silbert, Making Talk Cheap (Princeton seminar abstract) | <https://irs.princeton.edu/events/2025/jesse-silbert-analysia-watley-princeton-university> |
| Lifehacker: Is the Open to Work badge helping or hurting? | <https://lifehacker.com.au/?p=1188098> |
| LinkedIn Formatter: LinkedIn character limits | <https://linkedin-formatter.pages.dev/blog/linkedin-character-limit> |
| Master HR: Updated validity estimates (Sackett et al.) | <https://master-hr.com/insights/new-study-providing-updated-validity-estimates> |
| Naacp Job Finder: Open to Work customization | <https://naacpjobfinder.com/resources/should-you-use-open-to-work-on-linkedin> |
| NRCA / U.S. Chamber: TopResume 2025 survey | <https://nrca.net/RoofingNews/hiring-managers-sometimes-reject-applicants-who-use-ai.9-16-2025.12931/Details/Story> |
| Open Skill Index: Accessible motion (WCAG 2.2.2 summary) | <https://openskillindex.com/skills/majiayu000-claude-skill-registry-accessible-motion> |
| Originality.ai: AI-generated LinkedIn posts | <https://originality.ai/pt/blog/ai-content-published-linkedin> |
| Paul van der Laken: Talent Works application timing | <https://paulvanderlaken.com/page/47> |
| Resume Genius: Cover letter statistics | <https://resumegenius.com/blog/cover-letter-help/cover-letter-statistics/t3> |
| Resume Genius: AI impact on hiring | <https://resumegenius.com/blog/job-hunting/ai-impact-on-hiring/t4> |
| ResumeVera: Do cover letters still matter? (Novorésumé and Resume Genius comparison) | <https://resumevera.com/blogs/do-cover-letters-still-matter-2026> |
| Schemacheck: ProfilePage validation | <https://schemacheck.vercel.app/schema-types/profile-page> |
| Searchlab: Structured data and AI assistants | <https://searchlab.nl/gids/schema-voor-ai> |
| Tuck School of Business: What happens to hiring when AI writes job applications? | <https://tuck.dartmouth.edu/news/articles/what-happens-to-hiring-when-ai-writes-job-applications> |
| W3C: Understanding SC 2.3.3 Animation from Interactions | <https://w3c.github.io/wcag/understanding/animation-from-interactions.html> |
| Netflix Product Design Manager posting (We Love Product) | <https://weloveproduct.co/jobs/product-design-manager-emerging-creative-netflix-f2vf57> |
| Agile Brand Guide: Core Web Vitals | <https://www.agilebrandguide.com/wiki/metrics/core-web-vitals-cwv> |
| Aixploria: Adobe Content Credentials overview | <https://www.aixploria.com/?p=32447> |
| Netflix: Solutions Architect L5, ATS Configuration (Built In LA) | <https://www.builtinla.com/job/solutions-architect-l5-ats-configuration/7710642> |
| Laszlo Bock, My Personal Formula for a Winning Resume (Cal State LA copy) | <https://www.calstatela.edu/sites/default/files/formula_for_a_winning_resume.docx> |
| Netflix Product Brand Designer posting (Entertainment Careers) | <https://www.entertainmentcareers.net/netflix/product-brand-designer/job/379719> |
| HireMyMom summary of the ResumeGo callback experiment | <https://www.hiremymom.com/?p=2212318> |
| JD Supra / Ogletree: Eightfold FCRA lawsuit | <https://www.jdsupra.com/legalnews/groundbreaking-lawsuit-tests-whether-ai-7379594> |
| Jobscan: Resume tables and columns | <https://www.jobscan.co/blog/resume-tables-columns-ats> |
| Jobscan: What is an applicant tracking system | <https://www.jobscan.co/blog/what-is-an-applicant-tracking-system> |
| Lilach Bullock: LinkedIn Save to PDF | <https://www.lilachbullock.com/?p=146425> |
| LinkedIn Help: Share profile updates | <https://www.linkedin.com/help/billing/answer/86236> |
| Mediabistro: Updating LinkedIn while employed | <https://www.mediabistro.com/get-hired/when-to-update-linkedin> |
| Noon: LinkedIn Recruiter AI features 2026 | <https://www.noon.ai/blog/articles/09-linkedin-recruiter-ai-features-2026> |
| Pin: AI resume screening bias audit (vendor) | <https://www.pin.com/blog/ai-resume-screening-bias-study> |
| Pin: LinkedIn Recruiter AI features | <https://www.pin.com/blog/linkedin-recruiter-new-features> |
| ResumeAdapter: Netflix Resume Guide 2026 | <https://www.resumeadapter.com/companies/netflix> |
| SIOP: Is cognitive ability the best predictor of job performance? | <https://www.siop.org/tip-article/is-cognitive-ability-the-best-predictor-of-job-performance> |

---

## Adding a claim

```
| E7X | [claim, with exact numbers] | [Source title](URL) | [date] | [A–D] | [recheck-by] | [knowledge files] |
```

Rules:
- Record a vendor-run study as at most A–.
- If you only have a secondhand report, say so in the Source column.
- Never round numbers in ways that change the claim.
