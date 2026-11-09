---
name: motion-system-architect
description: "Design, document, extend, or audit a motion system end to end: brand intent, motion thesis, 3-7 owned verbs, physical model, choreography, anti-rules, behavior cards, semantic DTCG motion tokens, reduced-motion modes, component/transition contracts, toolkit parameter surfaces, and governance (versioning, contribution, deprecation, changelog). Use whenever the user mentions a \"motion system\", \"motion language\", \"motion tokens\", \"motion principles\", \"design tokens for animation\", \"easing/duration scale\", \"behavior cards\", \"DTCG\", \"MOGRT toolkit spec\", \"motion for AI states\", or asks to \"document this package as a system\" (retro-documenting shipped broadcast or product work), write motion specs for a portfolio or case study, or define timing and tokens for engineers. Covers product UI, brand, broadcast, and After Effects toolkits. Use even for a bare \"easing scale\" request: it routes to thesis and verbs first. Not for critiquing one animation (motion-critique) or AE scripting (after-effects-engineering)."
---

# Motion System Architect

A motion system is a *language with a grammar*, not a palette of durations. The numbers are the last and cheapest
thing to decide, and the most expensive to change once other people depend on them. This skill walks from
meaning to machinery in a fixed order so the machinery encodes decisions someone actually made.

Before starting, load this user's private overlay if one exists: the `motion-overlay` skill (from a personal plugin), or else `~/.claude/motion-skills-local/motion-system-architect.md`. It holds the user's private context and rules, which take precedence over the defaults here. It never ships with this skill.

## First: size the answer to the ask

Most failures of this skill are overbuilding, not underbuilding. Before picking a mode, read the request for scale words ("quick", "practical", "just", "keep it simple", "for my app", a single component) and set a budget you then keep:

| Ask | Budget |
|---|---|
| Quick or practical (a scale, a few tokens, one flow) | about 8-15 tokens in two tiers (primitive, semantic); per-token metadata limited to role, modes and reduced strategy; prose a page or less; no governance pack, no ladder status report. Mark skipped rungs `not yet` in one line |
| A real system for a team | the ladder below, sized per "Sizing the work" |
| A portfolio case study | full system plus evidence |

A practical answer that a developer can paste beats a complete one nobody reads. Load reference files only for the rung you are on; for a quick ask, the guidance in this file is usually enough.

## Start here: pick the mode

| Mode | Use when | First move |
|---|---|---|
| `new-system` | No system exists; brand/product is the input | Intent interview, then thesis |
| `retro-document` | Work already shipped (a broadcast package, a product's existing animations); recover its grammar | Gather and cluster 20-50 pieces; **label everything as retro-documentation** |
| `extend` | A system exists; add a verb, token, pattern, or platform | Read the existing system, run the four change-control questions |
| `ai-states` | Motion grammar for AI/agent/assistant states | State inventory from the product's real state machine |

**Partial retro** (some shipped motion, no system, fewer than 20 pieces): run `new-system` seeded by a short retro audit of what exists. Label each claim `observed` (measured from shipped work), `inferred`, or `designed-now`.

Auditing an existing implementation (a codebase's motion values, an AE inventory or keyframe export) is a retro audit: measure with a script, write counts rather than universals, and end with a proposed reduced set (grammar-and-derivation.md section 10, step 6). For keyframe exports specifically:
- State what the data cannot show before concluding anything: speed and velocity, property start and end values and distances, spatial versus temporal interpolation, layer identity, expressions and time remapping, and the sample size.
- Read concentration honestly. If the most common recipe covers a small share, or the top two are near-tied, say there is no house default yet rather than naming a "signature".
- Two overlapping keyframe segments on the same property of the same layer cannot both be true. Treat them as a data or export problem (layers merged, rows missing a layer name) and say so, rather than calling them conflicts.
- Know the tool defaults: After Effects Easy Ease is 33.33% influence on both sides, and influence cannot go below 0.1%, so "0%" in a spec means "as low as AE allows". A curve family that matches the default is a default, not a decision.

If the mode is unclear, ask one question: "Is there existing work or an existing system I should read first?"
Then proceed. Several modes can chain (retro-document, then extend). Mode names, rung numbers and words like `not yet` are your working vocabulary; in what the user reads, say it plainly ("I read your file first and kept your values", "not covered yet: contracts, governance"). Keep the `observed` / `inferred` / `designed-now` labels in retro work, because they are honesty labels the user needs.

Intake, asked once and only for what is missing: the medium (product UI, broadcast, social, event, AI, all);
who will use the system after you (solo, a team, vendors, engineers); what artifacts they will take (a document,
tokens, an AE toolkit, code); what already exists (files, brand guidelines, a reel); what must be public vs
internal; the deadline and depth wanted. For portfolio work, default the audience to "a hiring panel that
will look for evidence of scale, governance, and maintenance".

## The ladder: always in this order

Each rung produces an artifact and has a gate. Do not build the next rung until the gate can be answered. This is
the reason the skill exists: tokens written before verbs encode arbitrary values (Compendium C35).

| # | Rung | Output | Gate (can you answer?) | Reference |
|---|---|---|---|---|
| 1 | Intent | what the brand/product does for people; who it must never resemble | What should this motion communicate and never feel like? | grammar-and-derivation.md 1 |
| 2 | Thesis | one falsifiable sentence + 3-7 principles | Can the thesis reject a proposed animation? | grammar 1 |
| 3 | Owned verbs | 3-7 verbs derived from something proprietary | Do they pass the stripped-brand test and ownership test? | grammar 2-3 |
| 4 | Physical model | weight, acceleration, damping/overshoot, settle, as ranges | Is it qualitative with allowed ranges, not constants? | grammar 4 |
| 5 | Choreography | lead/support/resolve rules, concurrency ceiling, stagger, interruption | Is there exactly one focal event at a time? | grammar 5 |
| 6 | Anti-rules | refusals, each with reason and escape route | Would a contributor know what is off-limits and why? | grammar 7 |
| 7 | Behavior cards | one per verb and recurring pattern | Could a stranger implement it from the card alone? | assets/behavior-card-template.md |
| 8 | Tokens | primitive -> semantic -> component -> choreography, DTCG, with modes | Does the validator pass? Is every token a reusable decision? | token-architecture.md |
| 9 | Reduced motion | per-verb strategy; full / reduced / instant | Does the meaning survive without the journey? | token-architecture 6 |
| 10 | Contracts | component/transition contracts, matrices, interruption | Is behavior defined when the user acts mid-motion? | contracts-and-specs.md |
| 11 | Toolkit surface | exposed vs protected parameters, control table, registry | Can a non-specialist make distinct but on-system work? | contracts 7-8, platforms |
| 12 | Governance | lifecycle, semver rules, contribution, exceptions, changelog | Can it change without chaos or a gatekeeper? | governance.md |

Scale the ladder to the job (see "Sizing the work"). Skipping a rung is allowed only if you say so and mark the
dependent artifacts `provisional`.

### The no-milliseconds-first rule
If a user opens with numbers ("give me an easing and duration scale", "what ms for a modal?"), do not start
there. Say, in your own words: *"I can give you values quickly, but they will be arbitrary unless they hang off a
thesis and a few verbs. Give me two minutes on what this should feel like and never feel like, and I will
derive the scale from that."* Then run rungs 1-4 compressed (a few questions, or inferences you state and ask them
to confirm). If they insist, provide starting values explicitly labeled `provisional, not derived`, and still
hang them on a minimal thesis. The reason: a scale with no intent behind it cannot say no to anything, and it
becomes the token cemetery within a year.

## How to run each mode

### new-system
1. Intent interview (rung 1). Use the Motion Grammar Builder prompts in grammar-and-derivation.md 1.
2. Derive verbs from the brand/product's own assets using the seven-step derivation. If the user has nothing
   proprietary, derive from the product's interaction model or the domain's real behavior and say so.
3. Fill rungs 4-7 as prose and cards before any JSON.
4. Only now propose the numeric scale, as ranges per expression tier, then primitives.
5. Build tokens, run the validator, write contracts for the 3-5 most-used components, then the governance pack.
6. Run two stress tests (content mutation, reduced motion) on paper and report what broke.

### retro-document
For a body of work that predates the system (e.g. a shipped broadcast package). Honesty is the whole value.
1. Follow the retro procedure in grammar-and-derivation.md 10. Measure from files where possible (keyframe
   speed/influence, expression values, comp names); do not guess durations from memory. For a broadcast or
   streaming package, inventory it first with references/broadcast-package.md: element families, the variant
   matrix with counts, and dependencies.
2. Label every artifact **RETRO-DOCUMENTED** in its title block, and tag claims `observed` (measured),
   `inferred` (pattern read from the work), or `designed-now` (new decision made while documenting).
3. The thesis is an *interpretation*; say so. Never imply the system pre-dated the work.
4. List gaps the original work never faced (interruption, reduced motion, responsive formats) and fill them as
   `designed-now`, so the system is usable going forward without rewriting history.
5. Output may flow into `extend` mode to propose what the next package should do differently.

### extend
1. Read the existing thesis, verbs, tokens, and changelog first. Do not propose from a blank slate. Keep the user's file structure, tier names and token paths: renaming paths or adding tiers breaks every consumer, so it is a separate, labelled proposal, never part of the fix. Add governance metadata (status, version, provenance) only if the file already uses it or the user asked for governance; the validator reports its absence as a note, not a problem.
2. Answer the four change-control questions (governance.md 3): why existing fails, what semantic value is new,
   can an existing behavior be parameterized, what existing outputs change. Most proposals should end at
   "parameterize an existing verb"; say so when true.
3. If it survives: draft the card, the tokens at `proposed`/`experimental`, the reduced and instant modes, the
   semver bump with the perceptual-impact note, and the changelog entry. Run the validator on the merged file.

### ai-states
Read references/ai-state-motion.md in full. Build the state inventory from the product's actual state machine,
resolve intents to tokens (AI expresses intent, the system owns mechanics), define loop policies and stops,
write reduced and instant forms, and produce a context pack for agents. Refuse designs that dramatize reasoning
or imply certainty the system does not have.

## Sizing the work
- **Quick ask (a scale, a few tokens)**: thesis in 2-3 sentences, 3-5 verbs named in a line each, a small primitive
  scale with semantic roles, modes, validator pass, the accessibility checks above. Mark deferred rungs `not yet`
  in one line. No layers beyond primitive and semantic, no governance, no provenance or version fields.
- **Minimum Viable Motion Language** (default for vague asks): 5 principles, 3 intensity modes, 5 core behaviors
  (reveal, transform, connect, expand, settle), 4 temporal roles, 4 easing families, 4 spatial roles, a handful of
  recipes (Research R18; grammar 11).
- **Full system**: all 12 rungs, 12-document set (contracts-and-specs.md 11), governance pack, platform emitters.
- **Portfolio case study**: full system plus evidence (cards, tokens, contracts, a changelog with a real
  deprecation or rename, a stress-test result, a refusal log). Do not invent adoption numbers; label unknowns.

## Conventions every deliverable follows
- **One canonical statement per idea.** The token file is the source of truth for values; prose references token
  IDs and never repeats numbers. Cards reference tokens; contracts reference cards.
- **Explain the why** in the artifact itself (one sentence per rule). A rule with no reason gets bypassed.
- **Ranges, not constants** for physics and timing at the language level; constants only in tokens.
- **Anti-rules in the form** refusal, reason, escape route.
- **Evidence labels** on claims about outside systems: documented / synthesis / inference. Benchmarks come from
  references/benchmarks.md with its as_of date; volatile items (Figma Motion, Atlassian early access, DTCG
  versions) are re-verified before any public citation.
- **DTCG 2025.10 honestly:** it types duration, cubicBezier, and transition only. Springs, stagger, sequences,
  interruption, and modes go in `$extensions` and contracts; say this when a user assumes the standard covers them.
- **Every semantic duration/transition token has full / reduced / instant modes and a reducedMotion strategy.**
  Reduced motion preserves meaning; it is not "duration times 0.5". Record what survives and what goes in `reducedMotion.preserves` / `reducedMotion.removes`. If the brand forbids instant motion ("nothing snaps"), keep the instant mode anyway and document it as a build/test/system mode, never a visitor-facing style.
- **Duration and curve are coupled.** A strong ease-out on a short duration lands most of its travel in frame 1 and reads as a cut. The validator warns when frame 1 at 60fps covers more than 40% of travel; give fast tiers a gentler curve rather than reusing the signature curve. The warning is a flag for reconsideration, not a ban: a deliberate snap (a wind-up into a hard stop on navigation, for example) is a legitimate tool, but it breaks the rule on purpose, so record it as an exception with its reason. The check is exact for pairs inside a `transition` token or declared with `pairsWith`; other semantic durations and curves get a `snap-risk` sweep, so declare the pairs code really uses (for example `dismiss` with `leave`) to replace the sweep with exact answers. For any single curve, `motion-critique/scripts/bezier_settle.py x1 y1 x2 y2 ms` prints the frame-1 share directly.
- **One verb, several tiers:** model a verb as a group with tier variants (`verb.surface.system`, `verb.surface.signature`) sharing intent and anti-rules, rather than separate verbs.
- **Never encode meaning only in motion**; focus, errors, and announcements never wait on an animation.
- **Timing and loops are accessibility rules, not taste.** Check every system against these (WCAG 2.2, verify the current text before citing publicly):
  - *2.2.2 Pause, Stop, Hide (Level A):* anything that moves, blinks or scrolls, starts on its own, runs longer than 5 s and sits beside other content needs a user control to pause, stop or hide it, unless the motion is essential. Auto-stopping within 5 s also satisfies it; an auto-timeout at 10 minutes does not. Name the threshold and the control in the token or contract.
  - *2.2.1 Timing Adjustable (Level A):* a timed surface the user must act on (an undo toast, a session timeout) needs a way to turn off, adjust or extend the time, or an alternative path to the same action (Undo also in a menu or history). Pausing on hover and focus helps but does not replace this.
  - *2.3.1 Three Flashes (Level A)* for any flash or bright full-screen change; *2.3.3 Animation from Interactions* is Level AAA, so do not present it as a legal floor.
  - *Essential motion:* decide whether the motion is decoration or the content itself. A breathing guide, a progress pulse that carries timing, or a demonstration is content: under reduced motion keep its function with a non-moving equivalent (a counted phase label, a filling bar, haptic or audio pacing), never a still decorative frame.
- **Units travel with values.** Tokens in ms become seconds in SwiftUI and Core Animation, and stay ms in Compose and CSS. State the conversion wherever a platform example appears.
- **When extending or auditing someone else's tokens, keep their values unless a rule fails.** Changing a curve on taste grounds is a separate, labelled proposal. Report DTCG spec errors separately from this skill's house conventions (the validator labels the latter HOUSE): a file can be valid DTCG and still miss roles, modes or reduced-motion strategies.
- **Platform translation, not transcription:** shared semantics, native mechanics (platforms-and-runtimes.md).

## Producing tokens: the loop
1. Write `tokens/motion.tokens.json` following token-architecture.md (tiers, `$extensions` namespace, modes).
   Start from `assets/example-tokens.json`, which passes.
2. Run: `python3 <this skill's folder>/scripts/validate_tokens.py path/to/motion.tokens.json`
   Add `--strict` for CI, `--ns your.namespace` if you renamed the extension namespace.
3. Fix errors, read the warnings (they usually point at a design smell: raw values at the component tier, orphan
   primitives, active tokens on deprecated ones), re-run. Report the final result in your hand-off.
4. Generate emitters (CSS, WAAPI, AE values, Lottie/Rive mapping, SwiftUI/Compose stubs) only after the file passes.
The validator checks structure and discipline, not taste. A passing file can still be a bad system; the gates in
the ladder are what check that.

## Anti-patterns to refuse or flag
| Name | What it looks like | Do this instead |
|---|---|---|
| **Token cemetery** | hundreds of tokens, designers still hand-type values because finding one is harder than inventing | fewer, semantic tokens; discoverability and lint |
| **Token soup** | every property tokenized, names by origin or number, no roles | tokenize decisions, not numbers; roles first |
| **Physics theater** | springs, damping constants, "realism" without a reason tied to the thesis | qualitative physical model; overshoot only where the brand earns it |
| **Template prison** | a toolkit so locked everyone ships the same thing, or so open nothing is on-system | design the parameter surface; controlled freedom zones |
| **Guideline museum** | beautiful docs nobody's workflow touches | contracts in the repo, lint, toolkit controls, golden-path test |
| **Brand cosplay** | verbs borrowed from famous systems (Shift/Transform) with no derivation | seven-step derivation; stripped-brand test |
| **Choreography inflation** | everything animates; no focal event; celebration for routine actions | attention budget, concurrency ceiling, expression tiers by frequency |

Also flag: preset library masquerading as a system, reduced motion as a late CSS override, one-size platform
numbers, versionless brand shifts, and orphaned templates still circulating after a token change.

## Retro-documenting shipped work
For broadcast work, the strongest honest story is a retro-documented package (with `observed` measurements) plus
a forward-looking toolkit spec and an `extend` entry showing the system governing a real change. Label which
parts are retro.

## Hand-off checklist (run before declaring done)
- [ ] Mode chosen (stated in plain words, not as a label); retro artifacts labeled; evidence labels present
- [ ] Thesis can reject something; verbs derived and ownership-tested (or flagged provisional)
- [ ] Every verb has a card; every card names tokens, anti-rules, reduced/instant behavior, interruption
- [ ] Token file passes `validate_tokens.py` (report the result; list any accepted warnings)
- [ ] Reduced motion keeps meaning; focus and announcements never wait on motion
- [ ] Contracts exist for the top components or patterns; interruption policy stated
- [ ] Governance: lifecycle status on everything, semver tolerance written, exception path with expiry, changelog started
- [ ] Unknowns, assumptions, and `designed-now` decisions listed for the user to confirm
- [ ] Benchmarks cited with as_of date; volatile items marked

## Reference map (load only what the current rung needs)
- `references/grammar-and-derivation.md`: rungs 1-6, tiers, anti-rules, retro procedure, stress tests
- `references/token-architecture.md`: rungs 8-9, DTCG, `$extensions`, springs/stagger/sequence, validator use
- `references/contracts-and-specs.md`: rungs 7, 10-11, contract YAML, parameter surface, 12-doc set, QA
- `references/broadcast-package.md`: broadcast package inventory (element families, variant matrix, dependencies, partner guide)
- `references/governance.md`: rung 12, lifecycle, semver, contribution, exceptions, changelog
- `references/platforms-and-runtimes.md`: emitters (CSS, WAAPI/Motion, AE, Lottie/Rive, SwiftUI/Compose), spring translation, integration entry point and production model (section 1)
- `references/benchmarks.md`: calibration facts, as_of 2026-10-04, volatility flags
- `references/ai-state-motion.md`: the `ai-states` mode
- `assets/behavior-card-template.md`, `assets/example-tokens.json`, `scripts/validate_tokens.py`
