---
title: Market data - raw sources and how to read them
as_of: 2026-10-17
---

# Market data: raw sources and how to read them

Sections: §1 Job-board endpoints · §2 Big-tech career sites · §3 Pay records · §4 Reading a posting · §5 Pay-transparency rules · §6 Scan snapshot (2026-10-17)

## 1. Job-board endpoints (public, no login)

`scripts/scan_postings.py` wraps all of these; `boards.json` lists 49 boards verified 2026-10-16. Fetch them directly when the script can't run. Endpoints change; if one fails, find the employer's ATS from a job link on its careers page.

| ATS | List endpoint | Pay |
|---|---|---|
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true` | Single job with `?pay_transparency=true` returns `pay_input_ranges`; otherwise parse the content text |
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/{org}?includeCompensation=true` | `compensation.summaryComponents` (prefer the Salary component) |
| Lever | `https://api.lever.co/v0/postings/{company}?mode=json` | `salaryRange` when present, else text |
| Workday | `POST https://{tenant}.{wdN}.myworkdayjobs.com/wday/cxs/{tenant}/{site}/jobs` with `{"appliedFacets":{},"limit":20,"offset":0,"searchText":"motion"}`; detail at `.../wday/cxs/{tenant}/{site}{externalPath}` | In the description text |
| Eightfold (Netflix) | `https://explore.jobs.netflix.net/api/apply/v2/jobs?domain=netflix.com&query=motion&num=50`; detail `.../api/apply/v2/jobs/{id}?domain=netflix.com` | In `job_description` ("The range for this role is ...") |

Adding a board: `python3 scripts/scan_postings.py --boards greenhouse:{token}` once to confirm it returns jobs, then add it to `boards.json` with a `verified` date.

## 2. Big-tech career sites (not in the scan)

Search these by exact title ("Motion Designer", "Senior Motion Designer", "Staff Product Designer, Motion", "Design Technologist", "Art Director, Motion"), then open each posting for its range.

| Employer | Where | Notes |
|---|---|---|
| Amazon | `https://www.amazon.jobs/en/search.json?base_query=motion%20designer&result_limit=50&country=USA` | JSON works (checked 2026-10-17); open each job page for the range |
| Google | `https://www.google.com/about/careers/applications/jobs/results/?q=%22motion%20designer%22` | Server-rendered HTML; each posting states a US base range and notes bonus + equity |
| Apple | `https://jobs.apple.com/en-us/search?search=motion%20designer` | Apple's old JSON API is gone; fetch the page or search by title |
| Meta | `https://www.metacareers.com/jobs?q=motion` | JS-heavy; search by title and open postings |
| Microsoft | `https://jobs.careers.microsoft.com/global/en/search?q=motion%20designer` (URL may move; search "Microsoft careers motion designer") | Postings state US ranges |

## 3. Pay records: from raw to digested

| Source | What it is | Use it for | Caveats |
|---|---|---|---|
| Posted range on the live req | The employer's band for this posting | The first anchor for any target | A band, not an offer; may be multi-zone by location |
| Recruiter-stated band | What the recruiter says on the screen | The best anchor once in process | Ask early: "What's the range for this role and level?" |
| H-1B wage filings | US Department of Labor LCA disclosure data: employer, job title, wage, worksite, dates. Raw files: `https://www.dol.gov/agencies/eta/foreign-labor/performance`; searchable mirror: `https://h1bdata.info/index.php?em=&job=motion+designer&city=&year=all+years` | Exact base salaries filed for named employers and titles | Base only; H-1B hires only; titles vary ("Motion Designer", "Product Designer") |
| Levels.fyi single offers | One person's offer with date, level, years of experience, location | New-hire TC by level when postings show base only | Self-reported; the averages include incumbents' refreshers and stock gains, so they run above new-hire offers |
| 10-K share-based comp note | A public company's vesting schedule and grant practice | Vesting cadence and front- or back-loading | Company-wide, not per role |
| Blind, Reddit, Glassdoor | Anecdote | Questions to ask, never a decision number | Label as anecdotal |

Rule: each decision-driving number gets a primary source or two independent ones, a date and a link. "Typical" ranges from memory are priors, never a counter-offer anchor.

## 4. Reading a posting

- **Remote truth lives in the text.** Ashby's `isRemote` was true on an OpenAI role whose text said "based in San Francisco ... 3 days in the office per week" (2026-10-14). The scan marks these `conflict`. Read the location sentence.
- **Dates.** Greenhouse `updated_at` is not the posting date (`first_published` is). Netflix's API `t_create` can predate the public posting. Workday shows "Posted N days ago". Record which date you have.
- **Age.** Older than three or four weeks: shortlists are likely forming, so apply today and stack channels. Reposted with new dates: the req may be hard to fill (an opening for a strong fit) or re-scoped.
- **Ranges.** Multi-zone ranges cover location tiers; a remote role's range "varies based on location". Netflix pays salary only (no bonus) and lets employees choose salary vs stock options, so its range is close to cash TC. Google, Meta and Apple add bonus and RSUs on top of the posted base.
- **Level signals.** Title words (Senior, Staff, Principal, Lead), years required, and scope verbs ("sets direction across teams" reads Staff; "complex features within a team" reads Senior). A Staff title with a Senior band, or the reverse, is a question for the recruiter.
- **Requirement emphasis.** Must-haves vs "even better". A line like "hands-on craft role first" tells you what leads the portfolio.
- **Tool demand.** Count requirements across many postings, not one. In the scan's term table, read the Employers column first: one employer posting several similar roles inflates the posting count (Oct 2026: Unreal appeared in 9 postings but only 2 employers).

## 5. Pay-transparency rules

Why it matters: a posted range is the first anchor, and a remote US posting usually has to carry one if the job could be done from a covered state. Checked 2026-10-16 (statute and agency pages plus the SixFifty tracker, updated Sept 2026: https://www.sixfifty.com/resource-library/pay-transparency-laws-by-state/). Laws change; recheck before relying on one.

- **Ranges required in postings:** California, Colorado, Connecticut (from Oct 1, 2026), Hawaii, Illinois, Maine (from Jul 29, 2026), Maryland, Massachusetts (from Oct 29, 2025), Minnesota, New Jersey, New York State, Vermont, Virginia (from Jul 1, 2026), Washington, plus DC, New York City and Cleveland. Delaware follows Sept 2027. Nevada and Rhode Island require disclosure only after an interview or on request.
- **Remote roles covered if someone in the state could do the job:** California ("may ever be filled in California, either in-person or remotely"), Colorado, Washington, New Jersey, Maryland, NYC.
- **Covered only with an in-state tie** (office, supervisor or work location): New York State, Illinois, Vermont.
- **Unclear for remote:** Minnesota, Hawaii, Virginia, Maine, Massachusetts.

Salary-history and pay-scale rules (what an employer may ask, what a candidate may request) vary by state and city. When advice relies on one, read and cite the statute on the legislature's own site with the date checked; tracker sites and law-firm summaries are fallbacks you name as such.

How to use it: a nationally posted remote role with no range is a compliance gap worth noting in negotiation research, not proof the pay is low. When a range is posted, quote it exactly and note that remote ranges often "vary based on location".

## 6. Scan snapshot (2026-10-17, 49 boards, default filters)

A dated example of what the market looked like, for orientation only. Rerun the scan before advising.

| Employer | Role | Posted range | Location truth | Date |
|---|---|---|---|---|
| OpenAI | Motion Designer, Business Marketing | $223K–$247K + equity | SF, hybrid 3 days (board flag says remote) | 2026-10-14 |
| Mercury | Staff Motion Designer - 3D | $170.4K–$236.7K | SF/NY/Portland or remote US/Canada | 2026-09-16 |
| Perplexity | Motion Designer | $180K–$210K + equity | NYC (board flag conflicts) | 2026-09-02 |
| Adobe | Motion Graphics Designer / Animator | $94.9K–$209.6K | San Francisco | 2026-09-24 |
| Adobe | Group Manager, Motion Graphics & Editorial | $118.3K–$259.8K | San Francisco | 2026-09-18 |
| Suno | Motion Designer, Paid Social (contract) | $70–$90/hr | Remote | 2026-09-25 |
| Amazon (site) | Senior Motion Designer, Devices Brand Studio | open the posting | Seattle | 2026-07-28 |

What it showed: one motion posting on these boards had a band whose floor clears $300K, at Senior level. Anthropic's board listed 656 jobs and no motion roles. Figma, Airbnb, Stripe, Duolingo and Pinterest boards listed none either. Across 26 matched postings at 10 employers, the most requested terms by employer count were AI (8), brand (7), product (7), 3D (6) and After Effects (6); Houdini appeared at 1 employer, Rive and Lottie at none.
