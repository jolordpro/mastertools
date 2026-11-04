# AI copy pitfalls (read before every delivery)

## Why this matters
- Writers given AI ideas produced stories judged better individually, but the stories became more similar to each other (Doshi & Hauser, *Science Advances*, 2024).
- Human essays added far more distinct ideas than GPT essays, and the gap persisted after prompt and parameter changes (Moon, Green & Kushlev, 2025).
- Different models converge on similar answers too (Wenger & Kenett, 2025).
- **So a model's first answer is close to everyone's answer.** For brand work that is structurally the wrong answer. For microcopy, convention is fine.

## Detectable patterns (look for clusters, not single words)

| Level | Pattern | Example |
|---|---|---|
| Word | AI vocabulary | delve, tapestry, pivotal, testament, foster, vibrant, intricate, robust, showcase, seamless, elevate, unlock, unleash, harness, resonate |
| Word | "boasts" for "has"; "serves as" for "is" | "The app boasts a seamless interface" |
| Sentence | Negative parallelism | "It's not just a drink. It's a movement." |
| Sentence | Rule of three by reflex | "Bold, innovative, and transformative" |
| Sentence | Inflated significance | "a testament to its enduring legacy" |
| Sentence | Vague attribution | "Experts agree..." |
| Sentence | Rhetorical-question openers as filler | "Ever wondered...?" |
| Word | A day of the week as color (banned) | "A fall isn't failing. It's Tuesday." / "Monday-proof coffee" |
| Structure | Em dashes everywhere | several per paragraph |
| Structure | Every sentence medium length | flat rhythm |
| Structure | Summary closers | "Ultimately...", "In short..." |
| Structure | Over-formatting | bold everywhere, headers on short text |
| Tone | Hedged, balanced, no stance | a great line takes a side |
| Tone | Exclamation marks and emoji standing in for energy | |
| Content | No specific nouns, numbers, names, places | |

## Fixes (imperative)
1. **Generate wide, then cut** - 30+ options across different angles, not 5 polished ones.
2. **Inject specifics only the brand has** - a number, a name, a place, a customer's words.
3. **Run the banned list** (`scripts/check_copy.py` + 08 anti-cliche list).
4. **Break the rhythm** - vary sentence length; use twos and fours.
5. **Replace abstraction with a scene** - character, incident, place.
6. **Take a stance.**
7. **Read aloud** - would a person say this to someone's face?
8. **Final fix when it still sounds generic:** add one surprising true fact, one customer phrase and one stance; then cut 30%.

## More patterns from the reference library
- **"More than X" / "we don't just X, we Y" openers.** Real brand guides use them too (a sports team's rallying page, a brewery's About page); that doesn't make them safe.
- **Stock agency-deck verbs and adjectives** - unlock, elevate, seamless, smooth, "drive impact", "inspire action". Common in capabilities decks, and they mark copy as generic.
- **A repeated header device** ("We are [verb]ing...") has punch once and becomes a tic across a document.
- **Self-coined jargon** ("clutter-busting power") signals talk instead of work. Don't brand your own methods in client-facing rationales (Sullivan p.225).
- **Looking like an ad.** Standard sign-offs, sales-conference phrasing and stock category images make readers turn the page (Sullivan pp.66-67).
- **Invented "quality" puffery and hyped compound adjectives** - replace with a fact (Sullivan pp.8, 42).
- **Unsourced statistics in decks** - a real agency deck in the reference library has a stat strip with no source. Never present unsourced figures.
- **Never claim an audience tested, preferred or "would respond to" a line.** Say it's craft judgment, and what a real test should check.
- **Days of the week as color** - banned (see SKILL.md); the checker fails them.
