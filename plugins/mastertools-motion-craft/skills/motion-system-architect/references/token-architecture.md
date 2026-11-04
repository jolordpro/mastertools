# Token architecture (DTCG 2025.10)

Tokens are the *last* layer of the thinking and the first layer of the machinery. A token is a reusable decision
with a meaning, not a repeated number (KB-C Part VIII.3, 116.4). Read this after verbs and cards exist.

## Contents
1. Seven classes of motion token, and which become JSON
2. The four tiers
3. DTCG 2025.10 facts and gaps
4. The $extensions convention
5. Springs, stagger, sequences
6. Modes: full / reduced / instant
7. Naming
8. What not to tokenize
9. Pipeline and source of truth
10. Build gates and the validator
11. Worked snippet

## 1. Seven classes, and where each lives
KB-C Part IV defines seven token classes. Only some belong in a DTCG file; forcing the rest into JSON is how token
soup starts.

| Class | Encodes | Lives in |
|---|---|---|
| Strategic | brand intent, emotional posture | thesis and principles docs |
| Behavioral | named verbs (Reveal, Settle) | behavior cards + `semantic.verb.*` tokens |
| Physical | weight, stiffness, damping, overshoot | primitives (+ spring extension) |
| Temporal | duration, delay, hold, stagger | primitives + semantic duration |
| Choreographic | follow, overlap, handoff, resolve | `choreography.*` tokens / pattern docs |
| Contextual | dialect (product, social, event) | modes or dialect alias sets |
| Constraint | explicit negative space | anti-rules in cards, lint rules, `$extensions` limits |

## 2. The four tiers (plus modes)
```
primitive      raw calibrated values: durations, curves, spring constants. Literals live ONLY here.
semantic       role + intent: durations by role, easing by role, verbs as composite transitions.
component      "where it is invoked": dialog.enter, toast.enter. Aliases semantic tokens, never raw values.
choreography   relationships over time: sequence, stagger, handoff. Composes component/semantic tokens.
```
Every semantic duration/transition token carries three modes: **full** (the `$value`), **reduced**, **instant**.
Why this shape: change a primitive and everything downstream follows; change a semantic role and teams keep their
intent; component authors never see a millisecond. Brand motif and behavioral-pattern layers (KB-C 116.3) sit as
semantic verbs plus choreography; pre-rendered signature moves are assets, not tokens.

Rules of thumb that the validator enforces:
- Component tier: raw literal is an error; direct alias to a primitive is a warning (it skips the semantic decision).
- Semantic tier: alias primitives; a raw literal is a warning (a scale change would no longer propagate).
- Every semantic token needs `semanticRole`; every semantic duration/transition needs reduced + instant modes
  and a `reducedMotion.strategy`.
- `status` on everything above primitives; deprecated tokens need `replacedBy`; active tokens must not reference retired ones.

## 3. DTCG 2025.10 facts and gaps
(Design Tokens Community Group "Format 2025.10". It is a Community Group report, not a W3C Standard; check
designtokens.org before citing publicly.)

- Tokens are objects with `$value`; optional `$type`, `$description`, `$extensions`, `$deprecated`. Groups can set `$type` for children.
- Motion-relevant types: `duration` `{"value": 200, "unit": "ms"}` (units ms or s), `cubicBezier` `[x1,y1,x2,y2]` with x in [0,1], and composite `transition` `{duration, delay, timingFunction}`.
- Aliases: `"{group.token}"`. Deprecation: `$deprecated` (boolean or message).
- Older drafts and KB examples use duration strings like `"200ms"`; the validator accepts them with a warning.
- **Gaps (state these to users):** no `spring`, `stagger`, `sequence`, interruption policy, focus handoff, gesture-linked motion, or state machine type. The spec also does not say which property a transition applies to. Everything above must be an extension or live in contracts.

## 4. The $extensions convention
Use a reverse-DNS namespace so tools ignore it safely, ideally built on a domain the system's owner controls (example.com gives `com.example.motion`). This skill's default is `dev.motion-system`; pass `--ns` to the validator when you rename it.

If the file wraps everything in one top-level group (e.g. `{"brand": {...}}`), aliases must include it: `{brand.semantic.duration.short}`, not `{semantic.duration.short}`.

```jsonc
"$extensions": { "dev.motion-system": {
  "semanticRole": "enter",              // what the motion is for (enter, exit, move, feedback, confirmation, settle, rhythm...)
  "contexts": ["dialog", "toast"],      // approved environments
  "reducedMotion": { "strategy": "fade", "preserves": "arrival order", "removes": "28px travel" },   // instant | fade | reduce-amplitude | reduce-depth | reduce-parallax | tighten-spring | remove-repetition | state-only | static
  "modes": { "reduced": <value|alias>, "instant": <value|alias> },   // same $type as $value
  "status": "active",                   // proposed | experimental | active | preferred | deprecated | retired
  "version": "1.2.0",                   // semver, see governance.md for what counts as breaking
  "provenance": "motion-system/core",   // owner or origin; for retro-documentation: "observed: ShowOpen_v4 comp 'Reveal_A'"
  "replacedBy": "{semantic.verb.reveal}",    // required when deprecated/retired
  "pairsWith": "{semantic.easing.reveal}",   // duration+curve pairs code combines (alias or list); gets an exact frame-1 snap check
  "platformMappings": { "css": "--motion-reveal", "ae": "Verb/Reveal", "swiftui": ".snappy", "compose": "MotionScheme.defaultSpatialSpec" },
  "performanceClass": "transform-opacity",   // optional; transform-opacity | layout | heavy-filter | continuous | runtime
  "llm": { "use": "Primary content arrives", "avoid": "High-frequency feedback" }   // optional context for AI agents
}}
```
Why `modes` and `reducedMotion` both: `modes` holds the *values* (so emitters can generate CSS for each mode);
`reducedMotion.strategy` holds the *policy* (what meaning survives and how), which reviewers and AI agents read.

## 5. Springs, stagger, sequences
**Spring.** A spring token is a `transition` whose DTCG `$value` is a *fallback* (duration + curve approximating the
settle) so tools that ignore the extension still work, plus a spring extension:
```json
"spring": { "stiffness": 700, "damping": 0.9, "mass": 1 }      // physical form (damping as ratio), or
"spring": { "duration": 0.35, "bounce": 0.15 }                  // perceptual form (seconds, bounce in (-1,1))
```
Prefer the perceptual form for cross-platform systems and name families by feel, not by constants
(`snappy / smooth / soft / playful`); platform adapters translate (platforms-and-runtimes.md). Reference Material 3
for slot naming: speed (fast/default/slow) x property type (spatial = may overshoot, effects = no overshoot).

**Stagger.** `"stagger": { "interval": "{semantic.duration.stagger}", "order": "forward", "maxItems": 6 }`
(`order`: forward / reverse / center-out / edges-in). `maxItems` caps total time; a stagger without a cap is a bug
for long lists.

**Sequence.** On a choreography token:
`"sequence": [{ "token": "{component.dialog.enter}", "role": "lead", "offset": {"value":0,"unit":"ms"} }, { "token": "...", "role": "support", "offset": "{primitive.duration.d100}" }]`.
Exactly one `lead`. Offsets are relative to the lead's start, or to its resolution if you document that
convention in the choreography doc; pick one and write it down.

Scroll-, gesture-, and input-linked motion have different timing sources than clock time (ADV 7.3). A duration
token cannot describe them; model them as pattern contracts with a `timingSource` field instead.

## 6. Modes
- **full**: normal semantic and expressive motion.
- **reduced**: preserve meaning, remove the journey. Classify each behavior: remove, replace with fade, reduce amplitude, reduce depth, reduce parallax, tighten spring, remove repetition, or preserve only the state change (CMP C15.01). It is not "duration x 0.5" and not "set to zero everywhere" (that destroys causal continuity).
- **instant**: final state, no travel. Focus order, reading order, and announcements never wait on motion.

Optional extra modes: `performance` (low-end devices), `expressive`/`quiet` (dialect intensity). Keep these as
alias sets over the same semantic tokens rather than new tokens.

## 7. Naming
Intent, scope, direction: `semantic.verb.reveal`, `component.popup.exit.right`, `component.tab.indicator.enter.left`,
`choreography.listReveal`. Avoid subjective speed labels as the *only* name ("fast", "slow") and avoid names that
describe historical origin ("campaign2023"). Primitive names may be neutral scales (`d100`, `d200`). Never name by
number of milliseconds if you expect to retune (`d200` that holds 180ms is a lie; either keep the scale honest
or name by step).

## 8. What not to tokenize (KB-C 116.4)
One-off values with unproven reuse; full choreographies with content-specific timing or editorial pauses (those
are patterns/compositions); every property at maximum granularity; single-campaign exceptions; hacks that
compensate for one code constraint; historically named tokens. Opacity, blur, and per-property amounts rarely
earn tokens (RES R09). Intensity/expression modes and verbs earn them readily.

## 9. Pipeline and source of truth
Reference flow (KB-C 117.1): source -> schema validation -> reference resolution -> semantic checks -> platform
transforms -> package/CDN/library -> consumers -> QA and telemetry -> versioned change back to source.
Source patterns: design-tool-first, repo-first, two-way sync, hybrid canonical + mirrors. Default advice: one
canonical JSON in a repo, everything else generated mirrors; the Fluent duplicate-representation drift is the
cautionary tale. Style Dictionary is the usual transform engine; emitters are described in platforms-and-runtimes.md.
For retro-documentation or portfolio work, a repo-hosted `tokens/motion.tokens.json` plus generated CSS and an
AE-readable JSON is enough.

## 10. Build gates and the validator
Eight gates (KB-C 117.3): schema validity; reference integrity; semantic naming/role; value constraints; deprecation
hygiene; platform completeness; reduced-motion coverage; docs generated from the same source.

`scripts/validate_tokens.py` covers gates 1-5 and 7 for a single JSON file:
```
python3 scripts/validate_tokens.py path/to/tokens.json            # report; exit 1 on errors
python3 scripts/validate_tokens.py path/to/tokens.json --strict   # warnings fail too (use in CI)
python3 scripts/validate_tokens.py path/to/tokens.json --json     # machine-readable
python3 scripts/validate_tokens.py path/to/tokens.json --ns com.example.motion
```
Run it on every token file you produce and report the result. `assets/example-tokens.json` is a passing reference.
The validator does not judge taste or choreography; value-range policy (e.g. max duration per tier) is a team
decision you add as a lint rule on top.

## 11. Worked snippet (semantic transition)
```json
"semantic": { "verb": { "$type": "transition",
  "reveal": {
    "$value": { "duration": "{semantic.duration.medium}", "delay": "{primitive.duration.instant}", "timingFunction": "{semantic.easing.enter}" },
    "$description": "REVEAL: make existing information legible, anchored to its source.",
    "$extensions": { "dev.motion-system": {
      "semanticRole": "enter", "contexts": ["dialog", "list-item", "toast"],
      "reducedMotion": { "strategy": "fade", "preserves": "arrival order", "removes": "28px travel" },
      "modes": {
        "reduced": { "duration": "{semantic.duration.short}", "delay": "{primitive.duration.instant}", "timingFunction": "{semantic.easing.move}" },
        "instant": { "duration": "{primitive.duration.instant}", "delay": "{primitive.duration.instant}", "timingFunction": "{semantic.easing.move}" } },
      "status": "active", "version": "1.0.0", "provenance": "example-system/core" } } } } }
```
