---
name: "copywriting"
description: Writes, rewrites and critiques advertising and marketing copy in the tradition of top creative agencies - campaign concepts, taglines, headlines, manifestos, scripts, posters, brand voice guides, landing pages, emails, social posts and UX microcopy. Use when the user asks for copy, a slogan, a headline, ad concepts, brand voice or messaging, or wants marketing text made sharper, more distinctive or less generic. Not for final line-polish of an existing draft that only needs tightening.
---

If `~/.claude/overlays/copywriting/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

# Copywriting

Great copy is one true, specific thing that matters to the reader, said in the simplest and most surprising way only this brand could own. A model's first answer is the average answer, and average copy is invisible. This procedure forces width before choice. In blind tests it beat plain Claude 11-2; the procedure, not the research library, carries that gain - so follow every step.


## House style (overrides every reference)

- **No "I", "me" or "my" in headlines or ad copy.** A first-person line speaks for the brand or a character, not to the viewer. A customer quote can be proof in the body, never the headline.
- **No "you" or "your".** Calling the viewer out is the lazy route. Evoke the feeling instead: a scene, an object, an observation, a truth the viewer recognises without being named. Show the rent getting paid; don't say "you won't have to choose".
- **Imperatives are fine** when they don't name the viewer ("Think different", "Count the pleats").
- **Exceptions, where address is functional:** UX microcopy, transactional emails (receipts, payment reminders) and legal or safety instructions. Even there, prefer an impersonal form when it reads naturally.
- **Never use a day of the week as color** ("It's Tuesday", "a Monday kind of tired"). Find the detail the day was standing in for. Days are allowed only as schedule facts from the brief (opening hours, delivery days).
- Where a reference shows "you" or "I" - including tested examples such as first-person buttons - treat it as evidence of a technique and rewrite it to house style.

## 1. Brief (always first)

Fill these in from the request. If something is missing, infer it, write the assumption down, and keep going. Ask only if a wrong guess would waste the whole job.

- **Job:** brand (memory, feeling, fame, long-term) or activation (click, sign-up, sale, now)? Never both in one line.
- **Reader:** one specific person, their situation and what they already know (unaware / problem-aware / solution-aware / product-aware / ready).
- **Truth:** the truest thing about the product, including the unflattering part.
- **Tension:** the enemy, convention, contradiction or fear the idea pushes against.
- **Single-minded proposition:** one sentence, no "and".
- **Proof:** numbers, names, places, customer words, demonstrations available.
- **Voice:** 3 traits + the tone this moment needs. If the brand has no voice, propose one.
- **Format and constraints:** length, channel, mandatories.

Owned specifics are the raw material. If the brief has none, invent nothing factual; mark placeholders like `[CUSTOMER QUOTE]` or `[NUMBER]` and say what to fill in.

## 2. Diverge (do not skip, do not shortcut)

Write at least 30 raw options for any headline, tagline or concept task (10+ for a body-copy opening or microcopy). Spread them across these angles, at least 4 each:

1. **Product truth:** a specific, checkable fact only this brand has.
2. **Customer words:** the reader's own phrasing of the pain or the wish.
3. **Enemy / tension:** name what the brand is against.
4. **Reframe / 180:** flip a weakness into proof, or do the opposite of the category.
5. **Scene:** a character, an incident, a place.
6. **Absurd / exaggeration:** push a true benefit until it is funny.

Get the obvious lines out first and keep the best one: it is the baseline every other option has to beat, not a line to avoid. If nothing beats it head to head, ship it.

Write the options down - in a scratch file or a scratch section the user does not need to read. Do not "diverge in your head"; options you never wrote down don't count.

## 3. Converge

Cut to the best 5, always including the best obvious line. Compare them head to head ("A or B, which would a top creative director run?") rather than scoring each in isolation. For taglines and platforms, prefer the line that can carry many executions and ties to something the brand already owns (a name, a ritual, a product detail) over a clever line that only works once. Then score the top 3 on the rubric.

| Criterion | A 5 looks like |
|---|---|
| Distinctive | A competitor could not sign it. Owned specifics. |
| Single-minded | One idea, one promise. |
| Right job | Feeling, story or fame for brand; specific reason or offer for activation. |
| Concrete | A number, name, place, scene or the customer's words. |
| Human | Sounds like a person said it out loud. No AI-pattern clusters. |
| On-voice | Matches the traits and the tone the moment needs. |
| Clear | Understood in one read. Conversion copy reads at about grade 5-7. |

Ship a line only if it scores 3+ on every criterion and 4+ on Distinctive and Single-minded. If nothing passes, go back to step 2 with the angle that produced the best near-miss.

## 4. Craft

- Lead with what matters to the viewer, shown through a scene, an object or a truth they recognise - never by addressing them.
- Keep the reader's pain in the copy when the brief names it (the moment, the time of day, the feeling). Proof supports the pain; it never replaces it. Put methodology (sample sizes, survey notes) in small print, not in headlines or subheads.
- Specifics over adjectives: replace every hype word with the fact it was hiding.
- Active voice. Nouns back into verbs. Plain words (help, not assist).
- Vary sentence length. Use twos and fours, not reflexive threes.
- Brand work: show a scene. Activation: state the reason and the next step.
- Clever only on top of clear. If the joke needs explaining, cut it.
- Humour where it fits the job and lands with the audience; never at the customer's expense.

## 5. Check

One point? So what? Would it still work with a competitor's name on it? Read it aloud. If anything fails, revise and re-check.

## 6. Deliver

Default shape (adapt to what was asked):

```
RECOMMENDED
<the line or piece>
Why: <one sentence: the move and why it works for this reader>

ALTERNATES
1. <line> - <angle>
2. <line> - <angle>

ASSUMPTIONS / TO FILL
- <assumed facts, placeholders, things to verify>
```

For longer pieces (pages, emails, scripts), deliver the piece itself, then a 2-3 line rationale. Do not show the 30 raw options unless asked. Never present invented statistics, testimonials or claims as real.

- Every alternate must be one you'd be happy to see chosen; weak filler gets picked. Make one of them the stretch option.
- **Name the source.** Whenever an answer draws on a book note, a named copywriter's method, or a slogan from the library, say so to the user: the book title and author, or the brand and agency/year where the library has them. Never present borrowed material as your own.
- Write the "Why" as strategy (the reader fact, the proposition, why this execution carries it), never as taste ("punchy", "fun"). Never claim a line would test well or that an audience would prefer it.

## Degrees of freedom

- **High** (many right answers): ideas, angles, taglines. Push for surprise.
- **Medium:** formats and structures. Adapt to the job.
- **Low:** factual honesty.

## Optional extras (open only when needed)

- **Mechanical check:** `python scripts/check_copy.py <file>` flags hype words, AI-sounding patterns, ad-speak, weak CTAs, reading level, days of the week and house-style breaks (I/me/my, you/your). Add `--allow-address` for microcopy and transactional emails, `--allow-days` for real schedule facts. Useful as a last pass; it can't judge quality.
- **Research library** in `references/`: open a file only when the user asks for that depth, never by default (in testing, loading it before drafting made brand copy more literal).
  - Brand voice guide or tone map: references/13-voice-library.md
  - Script, manifesto, poster, radio, brief, naming, client intake and customer-interview questions, capabilities decks and proposals, pitch and payment-reminder emails: references/11-formats.md
  - Microcopy rules, landing-page structure, email, body copy, response copy, case studies: references/06-conversion-copy.md
  - Stuck, or need more angles and idea starters: references/02-concepting-process.md
  - Presenting options, rationales, handling feedback and revisions, copy testing: references/16-presenting-and-feedback.md
  - "Write like X": references/07-copywriter-profiles.md
  - Effectiveness questions (emotion vs. reason, humour): references/10-effectiveness-evidence.md
  - Slogans by technique: references/04-slogan-library.md
  - Before/after examples: references/12-worked-examples.md
  - Before citing any fact, credit or statistic: references/15-verification-notes.md
