# Application ledger (template)

Copy this to `data/ledger.md`. The router writes one row per application and updates it as things change. After about 10 rows, `apply-followup` reads it to diagnose where applications are being lost.

---

## Applications

| ID | Date applied | Company | Role (no level #) | Level / range seen | Posting age at apply | Channel | Referral? | Resume ver. | Letter? | Proof page | Tracked link | Gate passed? | Portfolio opened? | Status | Last update | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | YYYY-MM-DD | | | | __ days | portal / referral / recruiter / HM note / agency | Y/N | v__ | Y/N | URL | URL | Y/N | Y/N/unknown | applied / screen / HM / panel / offer / rejected / ghosted / withdrawn | YYYY-MM-DD | |

**Field meanings**
- **Channel:** how the application actually reached the company. A portal application plus a referral counts as "referral."
- **Gate passed:**
  - parse-safe;
  - every must-have covered;
  - consistency table all MATCH;
  - no AI tells;
  - no confidentiality leaks;
  - links and passwords tested.
- **Portfolio opened:** from tracked-link or analytics data. "Unknown" if not tracked.
- **Status:** the furthest stage reached. "Ghosted" means no response 21+ days after the last contact (a working threshold until research item B2 lands).

## Required outcome fields (AC-L-011)

Every row also records:
- `submitted_on`
- `posting_age_at_submit_days`
- `referral` (y/n)
- `furthest_stage`
- `outcome`: one of *sent / closed by employer / rejected / withdrawn / never sent / offer*
- `outcome_on`
- `outcome_text`: the exact rejection or closure wording
- `feedback_requested_on`

Phrases like "all gone" aren't statuses.

## Application slots (companies with limits)

| Company | Limit seen | Scope known? | Used | Remaining | Notes |
|---|---|---|---|---|---|
| Netflix | 2 (portal setting) | No | | | Verify the scope before using a slot |

## Warm-path log

| Date | Company | Contact (by role only) | Ask | Sent via | Reply? | Outcome |
|---|---|---|---|---|---|---|
| | | | referral / intro / 15-min chat | LinkedIn / email | Y/N | |

## Funnel (recompute every 10 applications)

| Metric | Value | Target |
|---|---|---|
| Applications | | |
| Gate pass rate | | 100% |
| Warm-path attempt rate on priority roles | | ≥ 80% |
| Portfolio open rate (tracked) | | track; investigate if under 50% |
| Recruiter screens / applications | | baseline |
| Hiring-manager or panel rounds / screens | | baseline |
| Offers / panels | | baseline |
| Screens by channel (portal vs. referral vs. direct) | | baseline |

**Diagnosis** (from PLAN §2)

| Symptom | Likely cause | Skill to re-run |
|---|---|---|
| No response; link never opened | Not surfaced by screening | resume, target |
| Opened; no screen | Proof or level mismatch | portfolio, proof-piece |
| Screen; no next round | Positioning, level, or pay | target, interview |
| Late-stage losses | Interview performance | interview |

## Lessons from outcomes

```
- YYYY-MM-DD · [application ID] · [what happened] · [what changes next time]
```
