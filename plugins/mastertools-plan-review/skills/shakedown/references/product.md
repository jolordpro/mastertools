# Shakedown — Product & Experience Reference

Audits how the artifact lands on the person who meets it. Applies to shipped
UI, prototypes, design files, decks-as-product, and interactive anything.
Implementation correctness lives in `code.md`; this file is about the
experience being right even when the code is. Load both for working software.

## Contents

1. First contact
2. The state matrix
3. Motion and perceived performance
4. Flow integrity
5. Accessibility
6. Responsive and environmental reality
7. Content and microcopy
8. Consistency as a system
9. Privacy and trust in the interface
10. What first passes miss (sweep list)

---

## 1. First contact

The opening is the highest-leverage surface in the build.

- **Cold start:** what does a first-time user see before any data exists?
  Empty states that orient and invite action, or a blank grid that looks
  broken? Every empty state should answer "what is this, and what do I do?"
- **Time to first value:** how many actions from arrival to the moment the
  product proves itself? Count them. Every step is a tax; justify or cut.
- **Defaults:** are the defaults the right choice for the typical user, or
  the easiest choice for the builder? A default is a decision made for the
  user — audit it as one.
- **The demo path** (when the milestone is a demo or pilot): walk it cold,
  as the audience will see it. Anything rough on this path is automatically
  one severity tier higher.

## 2. The state matrix

For every significant view, verify all states exist and are designed —
not just the happy one:

| State | The check |
|---|---|
| Loading | Skeleton or indicator — not a blank flash. Long loads say so. |
| Empty | Orienting, actionable (see above). |
| Populated | The designed case — usually fine; check with real-length data. |
| Overflowing | 10× the expected data. Truncation, scrolling, pagination — deliberate or accidental? |
| Error | Human-readable, specific, recoverable. Retry where retry makes sense. Never a silent blank. |
| Partial / degraded | Some data loaded, some failed — does the view handle a mix? |
| Stale / offline | Is old data marked as old? Does an action queue or fail loudly? |

Missing error and empty states are the most common findings in this file and
routinely reach High at demo-bearing milestones.

## 3. Motion and perceived performance

For any product whose brand promise includes polish or cinematic quality,
**motion performance is a defect-class concern, not an enhancement** — jank
is a broken feature, because smoothness *is* the feature.

- **Frame rate under load:** animations and transitions at 60fps with real
  data volumes, on mid-tier hardware, not just the dev machine. Test the
  heaviest realistic scene.
- **Animation causes:** transforms and opacity (compositor-friendly) vs.
  layout-triggering properties (width, height, top/left) animated at scale.
- **Perceived speed:** instant feedback on every interaction (<100ms
  acknowledgment even when the operation takes longer), optimistic where
  safe, skeletons over spinners, streaming over blocking.
- **Motion with intent:** does each animation communicate (hierarchy,
  causality, continuity) or decorate? Decoration that costs frames is a
  finding. Duration/easing consistent as a system, not per-element whims.
- **Reduced motion:** is `prefers-reduced-motion` respected? (Also an
  accessibility item; it's a one-line check and a cheap finding.)

## 4. Flow integrity

- **Interruption:** refresh, back button, tab close mid-flow — is progress
  lost silently? Multi-step flows preserve state or warn.
- **Undo over interrogation:** destructive actions — is the pattern
  "confirm dialog" (friction, and users click through) or "do it with a
  5-second undo" (better)? Irreversible actions with neither are High.
- **Dead ends:** any state the user can reach with no forward path — error
  screens without exits, empty results without suggestions, completed flows
  without a "what next."
- **Feedback loops:** every user action produces visible acknowledgment.
  Actions that succeed silently read as failures.
- **Keyboard and power paths:** can the frequent operations be done fast —
  tab order, enter-to-submit, escape-to-dismiss, shortcuts where the
  audience expects them?

## 5. Accessibility

Minimum bar at any tier; expanded at Full:

- Color contrast meets WCAG AA (4.5:1 body text) — check the actual palette,
  especially brand colors on brand backgrounds.
- Meaning never carried by color alone (states, charts, validation).
- Full keyboard operability; visible focus states; focus managed on
  modal open/close and route changes.
- Images and icons that carry meaning have text alternatives; decorative
  ones are hidden from assistive tech.
- Form inputs have real labels (placeholders are not labels).
- Semantic structure: headings in order, landmarks present, buttons are
  buttons and links are links.
- Text scales to 200% without loss; touch targets ≥ 44px on touch surfaces.
- `prefers-reduced-motion` respected (see section 3).

## 6. Responsive and environmental reality

- The actual breakpoint set — checked at the awkward in-between widths, not
  just phone/desktop.
- Long content: German-length labels, long names, long titles — truncation
  and wrapping deliberate?
- The audience's real environment (from calibration): projector-washed
  colors for a live demo, boardroom TVs, hotel wifi, the client's locked-
  down browser. Audit against where it will actually be seen.
- Print/export paths if the artifact will be exported or shared as static
  output — does it survive the conversion?

## 7. Content and microcopy

- Error messages: written for humans, specific, and actionable — not codes
  or developer prose leaking through.
- Labels and CTAs: verbs that say what happens ("Save draft," not "OK").
- Placeholder/lorem content anywhere in a milestone-bound build is a
  finding — it *will* appear in the demo.
- Tone consistent with the brand register throughout, including the error
  and empty states everyone forgets to write.

## 8. Consistency as a system

- One spacing scale, one type scale, one color system — or a catalog of
  one-offs? Sample across screens and diff.
- Same action, same pattern everywhere (delete works one way, not three).
- Component variants that have drifted apart (two button styles doing one
  job).
- The design system (if one exists) vs. the shipped reality — where has the
  build silently forked from the system?

## 9. Privacy and trust in the interface (security/liability sub-pass)

The UX-layer counterpart to `code.md`'s security pass — how the interface
itself exposes or protects the person. Mandatory at Full tier for anything
handling personal or client data:

- **Data on display:** personal, client, or sensitive data shown where it
  needn't be, cached in the interface, or left in a screenshot-able state
  during a demo. What's on screen when the projector is on?
- **Data in the URL:** IDs, tokens, emails, or PII in query strings or paths
  — copied, logged, and shared without anyone meaning to.
- **Consent and permission UX:** permission prompts (camera, location,
  notifications) requested with context and at the right moment, not
  cold on load. Consent flows honest about what's collected.
- **Dark-pattern check:** nothing that tricks, shames, or traps — forced
  continuity, confirm-shaming, hidden opt-outs, roach-motel cancellation.
  A liability and brand-trust finding, not just an ethics note.
- **Trust signals on money and destructive actions:** irreversible or
  paid actions clearly labeled, with a real confirm-or-undo — the user
  should never be surprised by what an action cost or destroyed.
- **Compliance surface:** cookie/consent banners where the audience's
  jurisdiction requires them; accessibility compliance where the format is
  regulated (see section 5).

## 10. What first passes miss (sweep list)

Steer the Sweep with these — the experience checks a first pass reliably
skips even when it worked the matrix honestly:

- **Partial/degraded and stale states.** Loading, empty, and error get
  checked; the mixed case (some data loaded, some failed) and the
  old-data-unmarked case almost never do.
- **`prefers-reduced-motion`** — a one-line check, forgotten in nearly every
  first pass that wasn't explicitly about accessibility.
- **Focus management on route change and modal close** — keyboard users land
  nowhere; invisible to a mouse-driven audit.
- **The awkward in-between breakpoints** — audits check phone and desktop;
  the 900px window a client actually resizes to goes unchecked.
- **Error and empty-state microcopy** — the states everyone forgets to
  write are also the states everyone forgets to audit.
- **The second run** — first-contact gets walked; the *returning* user with
  existing data, half-finished flows, and stale cache does not.
- **What the projector shows** — sensitive data, dev toolbars, notification
  popups in the demo environment; checked only when someone imagines the
  room.
- **The keyboard path for frequent operations** — tab order and
  enter-to-submit on the form users will fill fifty times.
