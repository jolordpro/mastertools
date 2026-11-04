# Shakedown — Writing & Creative Reference

Audits documents, copy, brand language, scripts, decks-as-documents, and
creative deliverables. The defect hunt here is contradiction-hunting and
claim-checking; the stress test is the hostile reader.

## Contents

1. Structural integrity
2. Claim verification
3. Internal consistency
4. Voice and register
5. The hostile-reader stress test
6. Licensing, IP, and liability
7. Delivery-format checks
8. What first passes miss (sweep list)

---

## 1. Structural integrity

- **The promise audit.** What does the opening promise — explicitly or by
  framing? Now check: does the piece deliver it, and does anything later
  quietly break it? Section 4 contradicting section 1's premise is the
  written equivalent of a contract-drift bug.
- **Load order.** Does the most important thing arrive where the reader's
  attention actually is (early), or is it buried after throat-clearing?
  Flag openings that warm up instead of opening.
- **One job per unit.** Sections/paragraphs doing two jobs at once, or two
  sections doing the same job in different words (merge candidates).
- **The skim path.** Read only headings, first sentences, and anything
  bold. Does the skeleton alone carry the argument? Most readers will only
  ever meet the skeleton.
- **Ending audit.** Does it end, or stop? Does the close tell the reader
  what to do, decide, or remember — or trail off into summary?

## 2. Claim verification

- Inventory every factual claim: numbers, dates, names, superlatives
  ("first," "only," "fastest"), attributions, statistics.
- Verify against sources — with real tools for anything checkable, flagged
  for the human where verification needs access you don't have.
- **Superlatives and absolutes are liability candidates**, not just accuracy
  ones (see section 6): "guaranteed," "proven," "#1" need substantiation or
  softening.
- Quotes: verbatim and attributed correctly? Paraphrases presented as
  quotes are findings.
- Numbers that must reconcile (totals, percentages, before/after) —
  reconcile them.

## 3. Internal consistency

- Terminology: one name per concept throughout. A product called three
  things in one document is three findings or one, but it's not zero.
- Tense, person, and formatting conventions held throughout (dates,
  capitalization of product terms, serial commas — whatever the convention
  is, drift is a finding).
- Cross-references that still point where they claim (section numbers,
  "as shown above," links).
- Facts stated twice, differently (a date, a price, a spec).

## 4. Voice and register

- Is there an established voice spec for this author or brand? Audit
  against *it*, not against generic "good writing."
- Voice drift: sections written at different times (or by different tools)
  that read like different authors. Sample beginnings, middles, ends.
- Register match to audience and stakes: profanity, humor, and looseness
  where the context permits it; none where it doesn't (legal, client-
  formal, bio/cover-letter contexts).
- AI-tell scan: committee-speak, hedging stacks, symmetrical listicle
  rhythm, empty intensifiers, the words on the author's banned list if one
  exists. Flag with locations.

## 5. The hostile-reader stress test

Read the piece as each of these; note where each one wins:

- **The skeptic:** looking for the weakest claim to dismiss the whole
  thing. What do they seize on?
- **The rushed reader:** skips to the middle, reads 20 seconds. What do
  they take away — and is it the intended message?
- **The literalist:** takes every sentence at exact face value. What's
  technically claimed that wasn't meant?
- **The out-of-context reader:** meets one excerpt (a pull-quote, a shared
  screenshot, a forwarded paragraph). What travels badly when detached?
- **The lawyer:** see section 6.

## 6. Licensing, IP, and liability

The thing that's fine until it's a lawyer's problem. Mandatory at Full tier
for anything published, broadcast, or client-delivered:

- **Fonts:** licensed for this use (web embed, broadcast, resale in a
  deliverable)? Desktop licenses on web deployments are a classic finding.
- **Footage, images, music:** rights cover this specific use, territory,
  and term? "Found it in a folder" is not a license. AI-generated assets:
  usage terms of the generator checked for commercial/broadcast use?
- **League, team, and trademark exposure:** logos, marks, likenesses used
  under an actual rights relationship, or assumed? Broadcast partners have
  rights *within scopes* — is this use inside the scope?
- **Claims requiring substantiation:** performance claims, comparisons,
  testimonials — flagged with what would substantiate them.
- **People:** identifiable individuals — releases where the use requires
  them? Minors: a hard stop for review, always, at any tier.
- **Confidentiality:** anything in the piece that discloses client,
  partner, or personal information the author may not have the right to
  disclose. Clinical, legal, and HR-adjacent contexts get extra caution.
- **Accessibility compliance** where the format is regulated (captions on
  broadcast/video, alt text on published web content).

## 7. Delivery-format checks

- The artifact opened in the tool/context the *recipient* will use — fonts
  substitute? Layout survives? Links live?
- Filename, metadata, and document properties clean (tracked changes
  accepted, comments resolved, author metadata appropriate to share).
- Version confusion risk: is it unambiguous which file is final? "final_v3_
  FINAL(2)" is a workflow finding.
- Export fidelity: PDF/print/handout versions checked, not assumed.

**Time-based media (motion, video, broadcast).** When the deliverable is a
render or cut heading to a broadcast partner, platform, or client, the
delivery *spec* is a defect surface, not a preference:

- **Codec, container, bitrate, resolution, frame rate** match the recipient's
  exact delivery spec — not "what exported." A broadcast partner's spec is a
  hard contract; a mismatch is a Blocker for that milestone.
- **Loudness and audio:** integrated loudness meets the target standard
  (broadcast loudness norms, or the platform's spec); no clipping; channel
  layout correct.
- **Color:** color space and range (broadcast-legal levels where required)
  correct end to end; no illegal values, no unintended shifts from the
  working space.
- **Frame-rate and color-space consistency** held across every source clip in
  the timeline — mixed frame rates and mismatched color are classic silent
  defects.
- **Title-safe / action-safe** areas respected; lower thirds and captions
  inside safe margins for the broadcast target.
- **Captions/subtitles** present, in sync, and in the required format where
  the format is regulated (see section 6).

## 8. What first passes miss (sweep list)

Steer the Sweep with these — the defects that survive an honest first read:

- **Cross-references and links** — "see section 3," anchors, URLs; nobody
  clicks them on a first pass, and reorganizations silently break them.
- **Facts stated twice, differently** — a date, price, or spec repeated far
  apart; each instance reads fine alone.
- **Numbers that must reconcile** — totals vs. parts, percentages vs.
  bases, before/after pairs; checked only when someone actually adds them.
- **The ending** — first passes tire; the close that stops instead of ends,
  or contradicts the opening's promise, escapes notice.
- **The out-of-context excerpt** — the paragraph that will be screenshotted
  or forwarded alone and reads wrong detached.
- **Document metadata** — tracked changes, comments, author fields,
  revision history; invisible in the reading view, visible to the
  recipient.
- **Terminology drift in the back half** — the name discipline holds for
  ten pages, then the draft's older vocabulary resurfaces.
- **The claim implied but never stated** — what the framing promises that
  no sentence commits to; the literalist and the lawyer read past it in
  opposite directions.
