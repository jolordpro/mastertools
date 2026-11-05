# Apply Craft — knowledge base and build kit

A source kit for building a Claude Code skill suite that runs a creative professional's job application from choosing targets to interviewing. It is specialized first for the **motion design lane** and **big-company hiring** (Netflix is the first fully researched company).

Everything here was compiled and stress-tested in one research thread: four prompts, each challenged with the `challenger` skill; a dated evidence library; and the lessons those challenge passes caught.

**Evidence current as of:** November 2026. Fast-moving claims carry a `recheck-by` date (see `knowledge/12-evidence-library.md`).

---

## Start here

1. Read **`PLAN.md`**. It is the build plan awaiting approval: architecture, every skill's scope, build phases, evals, and the decisions needed. Then read **`RESEARCH-PLAN.md`**, the research program awaiting approval.
   - Working for a specific person? Read their private handoff first, if one exists. It lives outside this kit (AC-L-009).
2. Skim **`knowledge/00-principles-and-guardrails.md`**. Every skill inherits these rules.
3. When building a skill, give Claude Code its matching `prompts/` file, the relevant `knowledge/` files, and the `templates/`.

## Folder map

```
apply-craft/
├── README.md                         ← you are here
├── CLAUDE.md                         ← build rules Claude Code reads automatically
├── PLAN.md                           ← build plan for approval
├── RESEARCH-PLAN.md                  ← research program for approval (companies, tools, review lane)
├── knowledge/
│   ├── 00-principles-and-guardrails.md   shared rules every skill follows
│   ├── 01-how-screening-works.md         ATS, Eightfold matching, AI on both sides, human skim
│   ├── 02-company-dossier-netflix.md     everything verified about Netflix hiring
│   ├── 03-resume.md                      resume lane: evidence, method, lessons
│   ├── 04-cover-letter.md                cover letter lane
│   ├── 05-linkedin.md                    LinkedIn lane
│   ├── 06-portfolio-and-site.md          portfolio, About page, personal site
│   ├── 07-reel-and-motion-lane.md        reels + motion-specific hiring knowledge
│   ├── 08-channels-timing-warm-path.md   referrals, Spotlights, timing, outreach
│   ├── 09-verification-trust-safety.md   background checks, authorship, scams, privacy
│   ├── 10-challenger-lessons-and-ledger.md  what the challenge passes caught (AC-L-001…AC-L-004)
│   ├── 11-research-backlog.md            open questions for lanes not yet researched
│   ├── 12-evidence-library.md            every source: claim, date, strength, recheck-by
│   └── 13-red-flags-and-contradictions.md  silent deductions by reader + objection map
├── prompts/
│   ├── resume-challenge-v2.md            ready (includes fast lane + level-number patch)
│   ├── cover-letter-challenge-v2-draft.md   draft; not yet challenger-tested
│   ├── linkedin-challenge-v2.md          ready
│   ├── portfolio-challenge-v2.md         ready
│   └── preflight-gate-v1.md              draft; last check before any submission
└── templates/
    ├── user-profile.md                   per-person settings (confidentiality, voice, location…)
    ├── application-ledger.md             tracking + funnel metrics
    └── company-dossier-template.md       structure for researching any employer
```

## Status at a glance

| Lane | Prompt | Research depth | Challenger-tested |
|---|---|---|---|
| Resume | v2 | Deep | Yes (2 passes) |
| LinkedIn | v2 | Deep | Yes |
| Portfolio + site | v2 | Deep | Yes |
| Cover letter | v2 draft | Medium | v1 only |
| Reel (motion) | inside portfolio v2 | Medium | Partly |
| Warm path / referrals | pieces only | Medium | Partly |
| Targeting / company intel | pieces only | Netflix only | Partly |
| Pre-flight gate (red flags, form, objections, blind panel) | v1 draft | Medium | Built in pass 4; not yet run |
| Interview | none | Not yet | No |
| Follow-up / learning loop | none | Not yet | No |

## Conventions used in these files

- **VERIFIED / ASSUMED**: whether a claim about a company or platform was checked against a live source.
- **Strength A–D**: A = primary, official, or peer-reviewed; B = large dataset with a stated method; C = survey, vendor claim, or expert blog; D = anecdote or forum.
- **[AI] / [AI+WEB] / [ME]**: who performs a check (the model from pasted inputs; the model only if it can browse; the person).
- **EST**: an estimate from the `motion-design-career-strategist` reference file, not independently verified here.
