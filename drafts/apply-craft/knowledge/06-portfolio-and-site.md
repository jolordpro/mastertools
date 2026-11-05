# 06 · Portfolio, About page, and personal site

**Prompt:** `prompts/portfolio-challenge-v2.md` (ready)

---

## Principle

**The resume claims; the portfolio proves.** Every major claim needs proof one click away. Every piece must be clearly the candidate's own, clearly scoped, and checkable.

## Who reads it, and how long they spend

| Reader | Time |
|---|---|
| Recruiter | ≤ 3 minutes |
| Hiring manager | 5–10 minutes |
| Presentation panel | 45–60 minutes (EST) |
| Search engines and AI tools | Ongoing |
| Verifiers | When checking |

## Evidence

**Review behavior**
- uxdesign.cc survey (100+ recruiters and managers): 80% of recruiters spend 3 minutes or less on a portfolio; 54% of design managers spend 5–10 minutes, and 11% spend more. Put a summary at the top and link to the full study. *(C)*
- UXfolio "State of UX Portfolios 2026" (100+ hiring managers; 5,000+ portfolios reviewed): *(C)*

  | Finding | Share |
  |---|---|
  | Red flag: low visual quality | 55% |
  | Red flag: confusing navigation | 48% |
  | Red flag: obvious overuse of AI | 43% |
  | Red flag: overly long content | 42% |
  | Prefer a website over Figma, PDF, or slides | 72% |
  | Say a relevant case study matters most | 89% |

  Reviewers open the case study that matches the role.
- Uxcel reviewer guidance: titles should say what you did, with labels for role, platform, and industry. Avoid walls of text; put an overview first and make details collapsible. *(C)*
- Resume Genius 2025: 35% of hiring managers have encountered AI-created portfolio projects or creative work. *(C)*

**What predicts hiring**
- Sackett et al. 2022: work samples .33, structured interviews .42 (top-ranked). *(A)*
- A proof piece is a work sample; the live walkthrough is where the interview happens.

**Online presence and verification**
- CareerBuilder 2018: 70% of employers screen on social media and 66% use search engines; 47% are less likely to interview someone they can't find online. *(B, dated)*
- HireRight 2025: more than three-quarters of employers found discrepancies; in North America, employment history was the second most common (36%). *(B)*
- Creative leaders verify authorship informally: they email someone else on the credits and ask for a walkthrough of the brief, idea, production, and who helped. *(D)*

**Machine readability, performance, accessibility**
- Google ProfilePage structured data: a Person with `sameAs` links to the person's other profiles. It must match visible content and guarantees no special search result; AI assistants' use of it is undocumented. *(A)*
- Core Web Vitals "good" thresholds, at the 75th percentile of real visits: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1. *(A)*
- WCAG 2.3.3: interaction-triggered motion can be turned off (honor `prefers-reduced-motion`). WCAG 2.2.2: moving content longer than 5 seconds needs a pause control. For motion roles, doing this well is itself proof of skill. *(A)*

**NDA work**
- Ask permission. Abstract or recreate (labeled). Password-protect only what must be gated.
- Some advise against passwords because of the friction, but **Netflix explicitly asks for the password** (see `02`). Keep public context visible and gate the details.

**Job-specific pages**
- A career-services lesson argues they impress hiring managers; designers on Fishbowl are split. Superfolio sells job-specific links that show when portfolios are opened. Opinion and product claims, not data. *(C/D)*
- Hence: an **unlisted, professional proof page** per priority posting, sent with a tracked link.

## Rules (from challenger passes)

- **Tag every check by who does it.** The model can't watch video, open password pages, or search without web access. `[ME]` checks are listed as pending, never guessed.
- **Mode switch:**
  - CREATIVE: case studies plus reel.
  - WORK SAMPLES: one-page case studies, plans, memos, decks, dashboards, talks. Use this for program, operations, or leadership roles.
- **Search-safe public pages:** if the search is confidential, the About page never says the person is looking. Availability lives on unlisted proof pages.
- **Content Credentials** (the C2PA authenticity standard):
  - Limits: many platforms strip the metadata on upload; a missing credential proves nothing; at CES 2026 many people read the "CR" icon as marking AI content.
  - Use durable credentials (watermark plus fingerprint) for key images, and **always pair them with a visible credits line**.
- **Confidentiality:** client-identifying details must stay out of images, alt text, captions, and file metadata too, not just page copy.
- **Each case study opens with a ~100-word summary:** problem, role, scope, timeframe, outcome.
- **Presentation outline** for the 2 strongest studies: context, role, 3 decisions and their trade-offs, outcome, what you'd change, and likely panel questions.
- **Application packaging:** the proof-page link, password, and "open this study first" line for each posting.

## About page checklist

- [ ] First lines state function and proof (no job-hunt signal if the search is confidential).
- [ ] A photo that looks like the person, recent.
- [ ] A brief "how I work" (principles, not adjectives).
- [ ] Contact info, LinkedIn, resume PDF.
- [ ] Location and work-type stance consistent with resume and LinkedIn.
- [ ] No client information; no generic AI phrasing.
- [ ] Every fact matches resume and LinkedIn.
