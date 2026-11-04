# Grammar and derivation: from intent to a defensible vocabulary

Everything here comes before a single millisecond. The reason: infrastructure built before a motion language
codifies arbitrary decisions (Compendium C35). Numbers are the last, cheapest thing to decide and the most
expensive thing to change after teams depend on them.

Source keys: KB-C = Motion systems KB v8 (Part/section), KB-S = Scalable KB, CMP = Compendium (C-code), RES = Research (R-code), ADV = Advanced v5.

## Contents
1. Intent and thesis
2. Deriving owned verbs (seven steps) and the stripped-brand test
3. Verb vocabulary: owned verbs vs functional verbs vs morphology
4. Physical model
5. Temporal and choreographic grammar
6. Expression tiers and frequency
7. Anti-rules
8. Dialects and controlled freedom
9. What to systemize vs art-direct
10. Retro-documentation procedure
11. Maturity and minimum viable language
12. Stress tests (gate the vocabulary before tokens)

## 1. Intent and thesis
Start from what the brand or product does for people, not from what it looks like. Answer the Motion Grammar
Builder (KB-C Part VII, Tool 2) in one sitting, in plain language:

- The brand/product behaves like... (a physical or human analogy: a precision instrument, a crowd, a conductor)
- It should feel... / It should never feel... (the second line produces your first anti-rules)
- The signature physical idea is... (one sentence; if it needs two, you have two ideas)
- The 3-7 core verbs are... / The most important behavior is...
- The recurring choreography pattern is... / The flagship exception is...
- The product dialect becomes quieter by... / The reduced-motion equivalent is...

The **motion thesis** is one sentence connecting a brand truth to a physical behavior, e.g. "Broadcast energy with
engineering discipline: everything arrives with intent, nothing wobbles." A good thesis can be falsified: you can look
at a proposed animation and say it violates it. If it cannot reject anything it is a slogan.

Principles (3-7) sit under the thesis: rules of tone and behavior ("purposeful", "spatially coherent",
"restrained by default"). Test: can another designer tell a principle from an effect? "Use ease-out" is an effect.
"Arrivals are decisive and departures are quicker" is a principle.

## 2. Deriving owned verbs (KB-C Part XXXVI)
Ownership comes from deriving behavior from something proprietary, not from importing a trend.

Derivation sources: logo geometry (open, fold, rotate, split, expand), core metaphor (grow, connect, explore),
product interaction (swipe, drag, assemble), cultural behavior (crowd, sport, craft, code, music), physical
environment (gravity, terrain, depth, flow), typography (tracking, stretch, variable axes), data/computation
(streaming, recursion, grids, clustering). Public precedents: HSBC (hexagon opening), SUSE (forward-moving infinity
form), EA FC (trajectory, formation, momentum, match cuts), Pinterest/DIA (pin behavior, collage rhythm, grid).

Seven steps:
1. Inventory distinctive brand assets and metaphors before animating anything.
2. Name the physical action each implies (opening, connecting, folding, streaming, stacking).
3. Abstract each action into one or more verbs.
4. Identify the physical rules that make it recognizable: weight, acceleration, elasticity, direction, scale, persistence.
5. Generate several executions from each verb. If it only produces one, it is an effect, not a verb.
6. Write anti-rules that stop it drifting into generic motion vocabulary.
7. Run the stripped-brand test.

**Stripped-brand test:** remove logos, type, and colors from three executions. Can a trained viewer still tell
the system apart? If not, diagnose which layer is generic: physicality, easing, choreography, or behavior.

If the user cannot supply brand assets (e.g. a new product), derive from the product's own interaction model
(DIA/Pinterest move) or from the domain's true behavior (BUCK/football move). Say which source you used.

## 3. Verb vocabulary
Three layers of "verb". Keep them distinct or the vocabulary bloats.

| Layer | Count | Purpose | Examples |
|---|---|---|---|
| **Owned verbs** | 3-7 | Identity. What this system does that others do not. | Stack Overflow: Click, Follow, Snapback. HSBC: Opening, Advancing, Emulating. Figma Config: Shift, Transform, Amplify, Activate. |
| **Functional verbs** | ~10 | Universal communication jobs every product needs. Owned verbs are *executed as* these. | reveal, redirect, confirm, progress, reorganize, emphasize, celebrate, error, loop, exit (CMP C06.02) |
| **Morphology** | 10 | Classify the state relationship before choosing mechanics (ADV 2.2). | appear/disappear, reposition, expand/collapse, transform, merge/split, reorder, reveal/conceal, assemble/disassemble, environmental response |

Workflow for any new interaction: classify morphology -> choose functional verb -> express through the owned
verb's physical model -> only then pick duration/curve/spring. A verb earns its place if it passes the
**ownership test**: distinctive (other brands would not move this way), repeatable (3+ contexts), composable
(combines with other verbs), teachable (a new contributor can describe it in one sentence).

Grammar elements for describing any sequence (CMP C06.01): subject, verb, modifier (how it feels), cause, anchor
(what relationship is preserved), sequence, resolution, context. Use this as the vocabulary in behavior cards.

## 4. Physical model
Describe in qualitative parameter families first, numbers later:
weight (light/neutral/heavy), acceleration profile (decisive start / soft start), deceleration (hard landing /
long settle), damping and overshoot (none / restrained / playful), directionality (axes, gravity, "always arrives
from source"), dimensionality (flat / layered / depth; parallax allowed?), persistence (does anything linger,
echo, hold?). Record **allowed ranges**, not single values.

Cross-platform rule: standardize the *perceptual* spring family (snappy, smooth, soft, playful) and map to native
physics per platform; do not pretend raw stiffness/damping values are portable (KB-S 28.4-28.5). Springs are not
"bounce": bounce is one outcome of damping (KB-S 28.4).

Invariants vs variables (KB-C 115.3, Part V): semantic role, hierarchy, physical worldview, signature gesture,
and accessibility intent are invariant. Parameter values, platform mechanism, exact physics constants, surface
treatment, and fallback mechanism vary.

## 5. Temporal and choreographic grammar
Timing is more than duration: duration, delay, stagger, hold, cadence, overlap, tempo (CMP C07). Prefer
relational rules ("support starts when lead is 60% resolved") over arbitrary delays. Duration depends on distance,
size, frequency, and salience, so give ranges per tier, not one number per use.

Easing as a semantic family (CMP C08.01): enter (arrive with attention, resolve quickly), exit (leave decisively),
move (reposition with continuity), emphasis (momentary, sparing), settle (resolve a physical response),
linear-loop (uniform ongoing change), expressive (the brand's signature shape).

Choreography is where several motions become one message. Specify per pattern (KB-C Tool 6, CMP C09):
trigger -> attention acquisition (what leads) -> primary move -> secondary response -> handoff -> resolution
-> interruption -> reduced-motion form. Rules: **one focal event at a time**; parallelize only motions that
communicate one event; stagger to orient, but cap total time; end with the highest-priority content resolved.
Treat attention as a budget: define a concurrency ceiling, a focal hierarchy, and an escalation rule (CMP C09.01).

Responsive and multi-format motion is a function, not a pile of exports (CMP C13.01):
`output = intent + content variables + format constraints + motion rules + platform profile`.
Protect identity moments (entry cue, focal reveal, resolution) and let supporting motion stretch or compress,
which is the idea behind After Effects "Responsive Design - Time" (ADV 7.2).

## 6. Expression tiers and frequency
Frequency controls expression: the more often a viewer sees it, the quieter it must be (CMP C07.01, KB-C Part XXXIX).

| Tier | Purpose | Expression | Frequency | Overuse risk |
|---|---|---|---|---|
| Utility | Make it understandable | Very restrained | Very high | Fatigue |
| System | Continuity and orientation | Moderate | High | Visual noise |
| Signature | Brand recognition | Distinctive | Medium | Repetition |
| Milestone | Celebrate important moments | High, controlled | Low | Loses impact |
| Flagship | Memorable brand moments | Highest | Very low | Overshadows content |

For broadcast, map tiers to: lower thirds, bumps and wipes (utility/system); show opens and recurring stingers
(signature); big reveals or season launches (milestone/flagship). For products: hover, press, enter/exit (utility);
navigation (system); onboarding and celebration (signature/milestone).

Variance budget (CMP C33.02): principles near-zero variance, semantic behavior low, parameters moderate, recipes
high, templates moderate-high, signature moments very high but rare. Put variance where it creates value.
IBM's productive/expressive is the cleanest public precedent: a range, not a binary.

## 7. Anti-rules
A system is defined as much by what it refuses (KB-C Part V, Greenhouse, Stack Overflow). Anti-rules are
first-class: write them in the thesis stage, then each card inherits and sharpens them.

Format: **Refusal, reason, escape route.** "No overshoot on utility motion: it reads as playfulness and fights
the precise character. Escape: Signature tier, exception record."

Common categories: generic trend effects, over-animation (motion competing with content), conflicting directions,
excessive bounce, unbounded 3D or parallax, line-by-line body copy animation (respect reading time), arbitrary
easing, one-size expression, motion as the only carrier of meaning, infinite loops without a stop.
Tokens can encode a "constraint" class (no-bounce, max-concurrent), but most anti-rules live in cards and lint rules.

## 8. Dialects and controlled freedom
Dialects let one language serve many media without sameness (KB-C Tool 7): product UI (quiet, high frequency),
broadcast (large-scale, editorial pacing), campaign, social (fast, recognizable gestures), event, AI states
(bounded, uncertainty-aware), internal/enterprise (clarity first). For each dialect state: primary job,
expression range, frequency, signature use, primary risk.

Controlled freedom zones (KB-C Part XXVI) - rigid systems get bypassed, weak ones fragment:

| Layer | Fixed | Adjustable |
|---|---|---|
| Core behavior | semantic meaning, fundamental relationship | intensity, scale |
| Physics | qualitative family, allowed range | exact values inside validated bounds |
| Timing | semantic class, accessibility limits | exact duration where context warrants |
| Choreography | hierarchy, causal relationship | minor overlap and pacing |
| Brand signature | the gesture | medium, scale, narrative context |
| Experiment | nothing (sandbox) | maximum exploration |
| Exception | needs rationale | local custom with review and migration path |

## 9. What to systemize vs art-direct
Systemize when the decision is repeated, measurable, meaningful, and costly to re-decide (RES R10, KB-C 116.4).
Systemize aggressively: core timing families, enter/exit intent, brand physics, recurring transitions, component
states, naming, accessibility modes. Systemize selectively: narrative pacing, contextual choreography, intensity
modes, generative ranges. Keep art-directed: hero-film storytelling, one-off emotional beats, bespoke simulation,
campaign-specific metaphor, final taste. A token is a reusable decision, not a repeated number.

## 10. Retro-documentation procedure (existing shipped work -> a system)
Used for `retro-document` mode, e.g. a broadcast package already on air. The honest framing matters for a
portfolio and for credibility: you are *recovering* the grammar the work already obeys, not claiming it was
written first. Label the artifact "Retro-documentation" in the title block and on every card.

1. Gather 20-50 representative pieces across tiers and contexts (open, bumps, lower thirds, transitions, packaging, socials).
   For a broadcast package, count them into element families with their variant matrix (broadcast-package.md).
2. Cluster by behavior before naming anything: direction, timing character, spatial logic, physics.
3. Separate intentional patterns from accidental consistency. Promote only patterns that recur *and* carry meaning.
4. Draft 3-7 verbs; test whether most observed work can be described with them. Keep a "unexplained work" list.
5. Extract invariants (what makes it recognizably this package) and variables (what actually varied).
6. Measure, do not guess: pull real durations and curves from the project files (AE keyframe speed/influence,
   expression values). Record them as *observed ranges*, with the source comp names. When the data is an
   export (inventory JSON, keyframe dump), count with a script, not by eye, and check every universal claim
   ("each", "every", "none", "always") against every row before writing it: one exception makes it false, so
   prefer counts ("7 of 9 overlapping pairs differ in easing"). Then propose the consolidated set: the
   reduced durations and curves with the observed values each one absorbs, and what to check before applying it.
7. Write the thesis last, as an interpretation. State that it is an interpretation.
8. Write anti-rules from observed refusals ("the package never uses X") and from known failures.
9. Build cards, then tokens, labeling every value `observed` vs `normalized` (rounded to a scale you propose).
10. List gaps the work never needed to solve: interruption, reduced motion, localization, responsive formats.
    Mark them as `designed-now` (new decisions), never as retroactive facts.

Evidence labels used in retro mode: **observed** (measured in files), **inferred** (pattern read from the work),
**designed-now** (new decision made during documentation). Never present designed-now as original intent.

## 11. Maturity and minimum viable language
Maturity (RES R03): 0 ad hoc, 1 consistent style, 2 motion language, 3 systemized toolkit, 4 motion
infrastructure, 5 adaptive/generative, 6 machine-readable brand behavior. Most work should not jump to 4-5
before 2 exists. Climb meaning -> behavior -> rules -> implementation.

Minimum viable motion language (RES R18): principles (5), modes (supportive / standard / expressive), 5 core
behaviors (reveal, transform, connect, expand, settle), temporal roles (instant / quick / standard / deliberate),
easing families (responsive / confident / fluid / physical), spatial roles (from source / toward focus / around /
through), a handful of recipes, a handful of controls. This is a proposed synthesis, not a standard. Offer it as
the default scope when the user's ask is vague.

## 12. Stress tests (run before tokenizing, again before release; CMP C36)
Aspect-ratio mutation, content mutation (short/long, image/no image), sequence mutation (same component earlier
or later), state interruption, reduced-motion pass, silent playback, partner authoring (experienced outsider),
novice authoring, high-volume generation (100-1,000 variants), long-term maintenance (change a token and
propagate). Review protocol: hide source files and ask reviewers to name the language; ask which behaviors are
invariant; give a partner a new brief and measure self-sufficiency.
