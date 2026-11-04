---
title: Search operations - getting from posting to interview
as_of: 2026-10-17
---

# Search operations: from posting to interview

Sections: §1 Req dossier template · §2 Evidence map · §3 Outreach templates · §4 Base rates · §5 Tracker and predictions · §6 ATS facts and myths · §7 Confidential search · §8 The 10-second test with real reviewers · §9 Getting the person's raw records

## 1. Req dossier template

```markdown
## [Employer] · [Exact title] · [Req ID]
- URL: [link] · Checked: [date] · Age: [N days since posted/created; which date]
- Level: [title word + scope verbs + years] · Team: [name]
- Location truth: [quote the location sentence]
- Posted range: [exact text] · Cash vs equity: [salary-only / base + bonus + RSU / base + options]
- Target ({{TARGET}}, the person's own; none given → report the band, don't assume one): [clears / inside / stretch / out], because [math]

**Why this req exists now** (inference): [launch, live events, reorg, backfill; source]

**Requirement lines → proof**
| Requirement (verbatim) | Must/Plus | Strongest true proof (where it lives) | State | Fastest truthful fix |
|---|---|---|---|---|

**What the panel will test:** [from emphasis, team's work, level]
**The lead:** [2–3 pieces, order, why] · Positioning line: "[...]"
**Pre-mortem:** 1. [cut reason → cheapest fix] 2. [...] 3. [...]
**Channels:** [referral path · recruiter · hiring manager · dates]
```

State values: **shown** (an artifact a stranger can open), **claimed** (stated, nothing to inspect), **missing**.

## 2. Evidence map rules

- Map must-haves first. A missing must-have is the pre-mortem's first line.
- Proof must be the person's own. On team work, name the personal role ("I designed the toolkit; the team animated with it").
- A gap closes truthfully in one of three ways: surface work that exists but isn't shown (cheapest), make a small real artifact now (a before/after, a one-page spec, a 20-second breakdown), or say it plainly in the interview as a growth area. Never describe undone work as done.
- AI-tool requirements ("proven success using AI tools to speed up asset creation") want a before/after with real numbers: what the tool did, what the person did, time saved. A tool list doesn't count.
- Retro-documenting shipped work as a system is legitimate when labeled as retro and limited to what was built.

## 3. Outreach templates

Fill only with facts the person supplies. Placeholders stay `{{LIKE_THIS}}` until they do.

**Recruiter note** (≤300 characters; check the current LinkedIn note limit for the account type)
```text
Hi {{FIRST_NAME}}, I applied to {{ROLE_TITLE}} ({{JOB_ID}}). I {{ONE_PROOF_TIED_TO_THE_TOP_REQUIREMENT}}. Reel: {{REEL_URL}}. Happy to share more on {{SECOND_PROOF}} if useful.
```

**Hiring-manager note** (≤4 sentences)
```text
Hi {{FIRST_NAME}}, {{ONE_SPECIFIC_THING_THEIR_TEAM_SHIPPED_AND_WHY_IT_LANDED}}. I {{ONE_RESULT_THAT_MATCHES_THE_REQ}}; 60-second reel: {{REEL_URL}}. I've applied for {{ROLE_TITLE}}. If it's a fit, I'd value 15 minutes, or a pointer to the right recruiter.
```

**Referral ask with a forwardable blurb**
```text
Hi {{FIRST_NAME}}, {{EMPLOYER}} posted {{ROLE_TITLE}} ({{URL}}). Would you be comfortable referring me? Here's a blurb you can forward:

{{NAME}} is a senior motion designer ({{YEARS}} years) who {{STRONGEST_PROOF}}. Strongest fit for this role: {{ONE_SENTENCE_TIED_TO_THE_TOP_REQUIREMENT}}. Reel: {{REEL_URL}}. Portfolio: {{PORTFOLIO_URL}}.

No pressure at all if it's not a fit.
```

**"Look before referral"** (the contact doesn't know the work yet)
```text
Hi {{FIRST_NAME}}, I'm going after {{ROLE_TITLE}} on your {{TEAM}} team. Would you take 2 minutes to look at this 60-second cut and tell me if it reads right for that team? {{REEL_URL}}
```

**One follow-up** (5–7 business days later; after that, only with something new)
```text
Hi {{FIRST_NAME}}, following up on {{ROLE_TITLE}} ({{JOB_ID}}). Reel's here if useful: {{REEL_URL}}. Thanks for considering it.
```

Log every send in the tracker (§5).

## 4. Base rates (directional)

Checked 2026-10-16. All funnel data comes from ATS vendors (Ashby, Greenhouse, Gem) or applicant-side trackers (Huntr), skewed to tech and growth companies. None of it samples broadcast, studio or entertainment hiring. Use bands, not points.

| What | Figure | Source (date) |
|---|---|---|
| Cold application → interview | 3.6–4.7% (was 7–8% in 2021); 291 applications per hire | Ashby, 109M applications (2026-04-28) https://www.ashbyhq.com/talent-trends-report/reports/2023-recruiter-productivity-trends-report |
| Cold application → first screen → onsite → offer | 6% → 20% → 35%; 0.4% of inbound hired (2024) | Gem 2025 benchmarks, 140M applicants (2025-01-08) https://lp.gem.com/rs/972-IVV-330/images/2025%20Recruiting%20Benchmarks%20-%20Gem.pdf |
| Referral → interview → offer | 40% reach interview; 16% of those reach offer (~6% application to offer) | Ashby, 38M applications (2025-05-16) https://www.ashbyhq.com/talent-trends-report/reports/referrals |
| Referral hire yield | Referrals ~1.6% of applications, ~17% of hires; "11x" inbound conversion | Gem 2025; Gem 2026 summary |
| Recruiter-sourced → first screen | 44% vs 6% inbound; hired 5–8x as often | Gem 2025; Gem 2026 summary |
| Design specifically | 0.2% application to hire (~500 applications per hire); 37 interviews per hire; 53 days to hire (2024) | Gem 2025, department table |
| Remote-only vs hybrid jobs | 3.53% vs 6.07% recorded interview rate per application | Huntr Q2 2026 (2026-08-12) https://huntr.co/research/job-search-trends-q2-2026 |
| Volume | 8.12% interview rate per application at 11–20 applications vs 2.86% at 100+ (correlation, not proof that fewer is better) | Huntr Q2 2026 |
| Referral evidence, academic | Software firm: referred applicants hired ~5.9x as often; referred hires quit 10–30% less | Burks, Cowgill, Hoffman & Housman, QJE 2015 (IZA DP 7382) |
| Time to hire | Median application to hire 40 days for technical roles incl. design (75% within 57); design average 53 days; first interview ~6 days after applying, offer ~10 days after interviews | Ashby (2026-04-28); Gem 2025; Huntr Q2 2026 |
| Résumé first pass | ~6 s (Ladders 2012, 30 recruiters) and 7.4 s (Ladders 2018, sample undisclosed), résumés only | Ladders reports |

How to use them:
- A cold application to a $300K role is roughly a 3–6% shot at a screen (Ashby 3.6–4.7%, Gem 6%; Ashby's referral page puts inbound near 3%); a referral roughly 40%; an outbound recruiter contact roughly 44%. That arithmetic is why warm paths beat volume.
- Plan parallel processes on a 6–8 week application-to-offer window (inference from the figures above) and start them within about two weeks of each other. Ask each recruiter for the stage calendar on the first call.
- Never apply the "6 seconds" figure to reels or portfolios; no credible study measures those. Front-load the strongest work as a craft principle.
- Myths that don't hold up: "70–80% of jobs are never posted" (no primary measurement; the supported version is that roughly half of hires come through non-inbound routes such as referrals and sourcing) and "75% of résumés are auto-rejected" (traces to a 2012 vendor pitch).
- Full table with confidence ratings: the October 2026 fact check that built this section.

## 5. Tracker and predictions

Tracker CSV columns for `scripts/funnel.py` (case-insensitive; extra columns ignored):

| Column | Values |
|---|---|
| `company`, `role` | text |
| `channel` | `cold`, `referral`, `recruiter_inbound`, `recruiter_outreach`, `hm_outreach`, `other` |
| `stage` (furthest reached) | `applied` < `recruiter_screen` < `hiring_manager` < `panel` < `offer` |
| `status` | `active`, `rejected`, `withdrawn`, `ghosted`, `accepted`, `declined` |
| optional | `level_target`, `posted_date`, `applied_date`, `last_update` (YYYY-MM-DD preferred), `notes` (paste rejection wording verbatim) |

Everyday labels are read too ("Phone Interview", "Final round", "Pending", "Friend referral", "LinkedIn Easy Apply"). A bare "Interview" is read as `recruiter_screen`. Slash dates are read month-first (US) unless a value over 12 in the first place proves the file is day-first; pass `--day-first` when the person writes day-first and no date proves it. A file with proof of both orders reads each settled value its way, and dates that could be either never age a row.

Run: `python3 scripts/funnel.py tracker.csv --min-n 5 [--today YYYY-MM-DD] [--no-response-days 30] [--predictions predictions.json] [--format json]`.

- **Data check first.** The report opens with rows read vs used, skipped rows, labels it interpreted (stage, status and channel), channels it counted as `other`, and unreadable or ambiguous dates. Relay anything it corrected, and ask the person to fix interpreted rows that went further or sit in the wrong channel. If more than 10% of rows are skipped, the script withholds the diagnosis and the channel verdicts: get the labels fixed before diagnosing.
- **Resolved rows only.** Active rows haven't had a chance to convert, unless they've been quiet for over 30 days. Quiet days run from `last_update`; at the applied stage, from `applied_date` when `last_update` is blank. Those rows count as no response at their stage (a heuristic; `--no-response-days 0` turns it off) and appear in the stale list. Rows past applied with no `last_update`, and rows with an either-way date in a mixed-order file, never age out; the data check says so.
- **The leak.** Among stages with at least `--min-n` resolved rows, a stage is a clear shortfall when it converts 20% or more below its reference rate (the §4 base rates, with applied → screen weighted by the person's channel mix), or when its whole 90% interval sits below the reference. The leak is the clear shortfall furthest below its reference. Low-confidence under 10. It says "No leak" when every eligible stage is at or above its reference, and "No clear leak" when the shortfalls are all within noise. When it names a leak that isn't the lowest raw rate, it prints the lowest raw rate too. Read the per-channel tables and the notes before agreeing with it.

Predictions file (write it when you prescribe a change; check on the date):
```json
{"applied->recruiter_screen": 0.30, "recruiter_screen->hiring_manager": 0.6, "hiring_manager->panel": 0.5}
```
funnel.py flags SURPRISE when a predicted rate falls outside the 90% Wilson interval of what was observed. A surprise means the model of the search is wrong: say which assumption failed.

## 6. ATS facts and myths

| Claim | Reality |
|---|---|
| "75% of résumés are auto-rejected by ATS" | Traces to vendor marketing with no published method. Modern ATSs (Greenhouse, Lever, Ashby, Workday, Eightfold) rank, search and route to humans; knockout questions (work authorization, location, minimum years) are the main automatic filter. Answer them accurately. |
| "70–80% of jobs are never posted" | Poorly sourced; don't build strategy on it. The documented advantage is referrals, not a hidden job market. |
| Keyword stuffing or pasting the job description | Semantic matching reads context, and the human reviewer reads it too. Mirror real terminology only where true. |
| White or hidden text, prompt injection aimed at AI screeners | Parsers extract it as visible text; it reads as deception in a small industry. Never. |
| Apply to everything | Recruiters see all of a candidate's applications. One to three well-matched roles per employer. |

Parse-safe résumé: text-based PDF or DOCX, single column, standard headings, dates as Mon YYYY, reel and portfolio URLs as plain text near the top, nothing important in headers, footers or text boxes. After uploading, check the autofilled fields: garbled there means garbled for the recruiter.

## 7. Confidential search

When the person is employed, apply these unasked:
- Open to Work: recruiter-only setting, never the public banner. LinkedIn says it "take[s] steps to prevent LinkedIn Recruiter users who work at your current company" from seeing it but "can't guarantee complete privacy", and it decides which company to hide from by the profile entry marked "I am currently working here", so keep that entry accurate (LinkedIn Help a507508, checked 2026-10-17: https://www.linkedin.com/help/linkedin/answer/a507508). Agency recruiters working for the employer may still see it.
- Profile changes: no "open to new roles" in the headline; refresh gradually and frame it as portfolio work.
- References: none from the current employer until offer stage, on the person's timing, pre-cleared people only.
- Portfolio: no confidential or unreleased employer work, internal numbers or employer-owned tools without clearance.
- Logistics: personal email and devices; interviews outside core hours where possible.

## 8. The 10-second test with real reviewers

Model opinion is not market data. Before a big push, get two or three people who hire at the target level to do this cold:
1. Show the LinkedIn top card, the résumé's top third and the first 10 seconds of the reel. Ask: "What level and what kind of motion designer is this? Would you open the portfolio?"
2. Give five minutes on the portfolio. Ask: "Which project would you ask about first? What's missing for {{LEVEL}} on {{TEAM_TYPE}}?"
3. Write down their exact words. If two of three name the same gap, it's the leak.

Who: former colleagues now at target teams, design leaders on mentorship platforms (ADPList), recruiters who have placed the person before. Not friends who will be kind.

## 9. Getting the person's raw records

- **LinkedIn connections:** Settings & Privacy → Data privacy → Get a copy of your data → choose Connections → Request archive. The connections file usually arrives within minutes; a full archive can take up to a day. Run `python3 scripts/warm_paths.py Connections.csv targets.txt` (targets: one company per line, aliases with `|`, e.g. `Meta|Facebook|Instagram`).
- **Reel analytics:** Vimeo and YouTube show audience retention by second. A drop in the first 10 seconds means the opening is the problem, not the length.
- **Application history:** rebuild from email ("application received", "thank you for applying") and LinkedIn's applied-jobs list into the §5 tracker.
- **Rejections:** paste the exact wording into `notes`; it often names the leak.
