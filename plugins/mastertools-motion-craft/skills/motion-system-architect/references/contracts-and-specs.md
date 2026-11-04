# Contracts, specs, and the documentation set

A token says what a value means. A contract says how a component or pattern *asks* for the behavior, what
happens when the user acts mid-motion, and what survives under reduced motion. This is where motion design
becomes interaction architecture (KB-S 26.2).

## Contents
1. The five tests of executable motion
2. Behavior card (summary; template in assets/)
3. Component / transition contract (YAML template)
4. Transition matrix and interruption rules
5. Minimum spec checklist
6. Parity stack (what must match across platforms)
7. Toolkit parameter surface (AE / MOGRT / Figma / code)
8. Asset registry
9. Performance classes
10. QA layers and stress tests
11. The 12-document canonical set
12. Reference directory tree
13. Five-level packaging

## 1. Five tests of executable motion (KB-C 115.1)
A system is infrastructure, not a PDF, when someone other than its author can enter at a defined point and reach
a correct implementation. Check each:
1. **Discoverability**: the approved behavior and its usage are findable without oral history.
2. **Determinism**: the same token or pattern gives an understandable result in every supported runtime.
3. **Parameter control**: intended variation is a bounded surface, not arbitrary editing.
4. **Portability**: it maps to each runtime or medium without losing semantic identity.
5. **Changeability**: an owner can version, deprecate, migrate, and audit it without hunting every instance.

## 2. Behavior card
Use `assets/behavior-card-template.md`. One card per owned verb and per recurring pattern. A card is the human
artifact; its token IDs are the machine artifact; they must agree. Document important behaviors at five levels
(section 13). Cards for retro-documented systems are labeled and cite observed sources.

## 3. Component / transition contract (YAML template)
Fill one per component or pattern that moves. Keep it in the repo next to the component.

```yaml
contract: Dialog
version: 1.0.0
status: active                    # lifecycle, see governance.md
owner: design-systems
states: [closed, opening, open, closing]
transitions:
  - id: dialog.open
    from: closed
    to: open
    trigger: [pointer-activate, keyboard-activate, programmatic]
    intent: reveal                # owned/functional verb
    morphology: appear
    motionTokens:
      full: component.dialog.enter
    properties: [opacity, transform]       # only these may animate
    origin: invoking-control               # spatial anchor; omit if non-spatial
    path: straight                         # permitted spatial path
    choreography: choreography.dialogOpen  # lead/support relationships, if any
    interruption:
      during: opening
      on: close-request
      policy: retarget                     # retarget | reverse | cancel | snap | ignore
      velocity: inherit                    # inherit | reset
      queue: never                         # queued animation produces stale feedback
    reducedMotion:
      strategy: fade                       # from the token vocabulary
      preserves: [state-order, focus-order, backdrop-scope-cue]
    instant:
      finalState: open
      focusMoves: immediately              # focus, errors, announcements never wait on motion
    focus:
      onOpen: trap-after-enter-ready
      onClose: restore-after-close-complete
    responsive:
      narrow: sheet-from-bottom
      wide: anchored-centered
    platformMappings:
      web: waapi
      ios: native-sheet-spring
      android: compose-motion-scheme
    performance: transform-opacity
    qaStates: [rapid-toggle, keyboard-only, reduced-motion, slow-device, long-localized-content]
    telemetry: [motion.completed, motion.cancelled]   # optional
accessibility:
  noMeaningOnlyInMotion: true
  noInfiniteMotionWithoutStop: true
```
Why each block exists: `interruption` because a timeline presumes the user waits and a state machine presumes
they will not; `reducedMotion.preserves` because the goal is meaning, not removal; `focus` because motion must
never delay critical semantic feedback (Atlassian guidance, KB-S 9.5); `qaStates` so tests are written from the
contract.

## 4. Transition matrix and interruption rules
For anything with more than two states, enumerate every meaningful source -> destination pair, including blocked
ones. Columns: visual transition, interaction availability, focus behavior, announced semantics, reduced-motion
form.

Retargeting vocabulary (KB-S 26.3):
- **Continuous retargeting**: redirect toward the new target without returning to rest (drag, sliders, expanding panels, live data).
- **Velocity inheritance**: new movement keeps or blends the current velocity; no hard stop and restart.
- **State snapping**: for high-frequency controls, snap the state and suppress the flourish so motion is never the rate-limiting step.
- **Cancellation**: let people interrupt when meaning depends on agency.
- **Queued transitions**: avoid unless the queue is itself a meaningful process.

For broadcast or video there is no user input, so replace interruption with **edit-point rules**: what happens
when the clip is trimmed, extended, or cut early (protected regions, minimum hold, safe cut frames).

## 5. Minimum spec checklist (KB-S 12.1)
Intent, trigger, source state, target state, properties, origin, path, timing model (duration/curve/spring/user-
driven), temporal composition, interruption, reversal, responsive rule, reduced motion, platform mapping,
performance constraints, QA states, rationale. Separate subjective descriptors ("snappy") from implementation
descriptors ("150ms ease-out", "response 0.28 damping 0.78"); the first carries intent, the second precision.
A prototype is evidence, not the contract (KB-S 12.4).

## 6. Parity stack (KB-C 120.1)
Match: intent, state logic, hierarchy, relative temporal signature (pacing, hold, settle), physical character,
spatial semantics (origin, direction, continuity), accessibility equivalence. May differ: implementation detail,
internal architecture, exact pixel values, frame rate, native spring constants, rendering mechanism, fallback
technique. This is translation, not transcription: preserve meaning, not every surface detail (KB-C 129.1).
AI-assisted handoff makes specification quality the bottleneck: ambiguous context lets an agent invent behavior
very fast (KB-C 120.2).

## 7. Toolkit parameter surface (KB-C 121; ADV 4.2-4.3)
Controlled freedom for non-specialists. Design the surface *after* you know the invariants.

| Expose | Hide | Why |
|---|---|---|
| Content (text, image, data) | internal expression chains | users change content, not mechanics |
| Approved color roles | raw layer colors | preserve semantic brand mapping |
| Timing presets (named) | arbitrary keyframe editing | protect rhythm |
| Scale/crop/layout within bounds | comp hierarchy | adaptation without breaking composition |
| Intensity mode (e.g. Quiet / Standard / Loud) | physics equations | bounded expressive choice |
| Variant / dialect | all source controls | keep diversity intentional |
| Output format / aspect | renderer internals | production needs without drift |

Design steps: identify the invariant -> identify the variation surface -> define **ranges**, not just names ->
name controls in the system's language ("Energy", "Density", "Exit Tempo", never "Slider 4") -> protect critical
timing, hierarchy, readability -> write aspect-ratio rules before output templates -> stress test (long text,
short text, none, large image, small image, many items) -> document failure modes -> version like software.

After Effects: Essential Properties as parameterized components, MOGRT as packaged behavior, Responsive Design -
Time for protected regions, Creative Cloud Libraries for distribution (platform details in platforms-and-runtimes.md).
For a toolkit spec, produce a **control table**: control name, type, range, default, tier it belongs to, which
token/verb it drives, what it protects, what breaks if misused.

Toolkit maturity (KB-C 121.2): 0 file dump, 1 template with documented controls, 2 systemized toolkit (variants,
semantic controls, examples, docs), 3 connected toolkit (tokens/code outputs/versioning), 4 platform (governed,
analytics, contribution). Name the current level and what reaches the next.

## 8. Asset registry (KB-C 122)
For signature and reusable assets (MOGRTs, Lottie, Rive, video stings) keep a registry row each:
`assetId` (e.g. `brand.motion.hero.logo-reveal.v3`), semantic role, supported platforms, runtime, inputs, output
constraints (aspect, bitrate, frame rate), accessibility variant, dependencies (fonts, icons), owner, lifecycle,
version, preview. A runtime can transport an asset without knowing if it is approved, experimental, or one-off;
the registry carries that meaning.

## 9. Performance classes (KB-C 124)
Annotate behaviors qualitatively instead of inventing universal budgets: `transform-opacity` (cheap),
`layout` (affects layout), `heavy-filter` (blur, large masks), `continuous` (loops, ambient), `large-area`,
`runtime` (shader, canvas, 3D), `network-asset`. Review triggers: frame stability on representative devices,
CPU, GPU, memory, battery, network, interaction latency (animation must never delay input response).

## 10. QA layers and stress tests (KB-C 127; CMP C36)
Layers: schema, naming, values, runtime state transitions, accessibility (reduced motion present), performance,
visual snapshots, temporal (curve/duration/overlap), brand (expert), usability (research), adoption.
Machine checks catch invalid references; only humans catch a choreography that makes a product feel sluggish.
Temporal regression: record canonical demos at fixed conditions, compare curves and end states (not only frames),
test interrupted states, test reduced motion as a distinct expected output, test localization and dynamic content,
test high-frequency repetition, keep signature behaviors under expert review. Stress tests are listed in
grammar-and-derivation.md section 12.

## 11. The 12-document canonical set (CMP C35.01)
| # | Document | Contents | Produced by this skill as |
|---|---|---|---|
| 01 | Motion manifesto | why the brand moves this way | thesis page |
| 02 | Principles | 3-7 statements + anti-principles | principles page |
| 03 | Vocabulary | named behaviors and definitions | verbs + behavior cards |
| 04 | Timing/easing tokens | semantic and base layers | `tokens/*.json` + generated reference |
| 05 | State matrix | interaction and content states | transition matrices |
| 06 | Choreography rules | hierarchy, sequence, concurrency, interruption | choreography doc |
| 07 | Responsive behavior | by format, density, platform | responsive function + stress tests |
| 08 | Pattern library | primitives, recipes, components | contracts |
| 09 | Templates/toolkits | implementation-ready assets | parameter surface + registry |
| 10 | Reduced-motion guide | behavior-level fallbacks | per-verb strategy table |
| 11 | QA checklist | visual, semantic, accessibility, technical | QA doc |
| 12 | Governance | ownership, contribution, release, deprecation, exceptions | governance pack |
For a small job, deliver 01-04, 10, and 12 as one-page sections and mark the rest `not yet`, rather than writing
filler. Order matters: 01-03 before 04.

## 12. Reference directory tree (KB-S 31.1)
```
motion-system/
  principles/        thesis, principles, anti-rules
  taxonomy/          verbs, morphology, expression tiers
  tokens/            primitives/ semantic/ component/ modes/   (canonical JSON lives here)
  patterns/          behavior cards, recipes
  components/        contracts (YAML)
  choreography/      sequences, stagger rules, attention budget
  accessibility/     reduced-motion guide, focus rules
  platforms/         web/ ios/ android/ ae/ broadcast/
  implementation/    emitters, build config
  tooling/           toolkit specs, control tables, lint rules
  testing/           stress tests, regression fixtures
  governance/        contribution, exceptions, release policy
  releases/          CHANGELOG.md
  research/          evidence, critiques
  metrics/           health reports
  decision-log/      dated decisions
```

## 13. Five-level packaging (CMP C17.01)
For each important behavior write: **intent** (why), **example** (what it looks like), **rule** (what to do/not
do), **implementation** (token/component/code), **exception** (when and how to deviate). A gallery shows what;
the five levels let a stranger extend it correctly.
