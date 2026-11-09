# Platforms, runtimes, and emitters

Choose the execution model, not just the tool (KB-C 119): the same verb has different engineering consequences as a
CSS transition, a Web Animation, a view transition, a native spring, a vector runtime, or pre-rendered media.
Principle for every emitter below: **translate, do not transcribe.** Preserve semantic role, hierarchy, relative
timing, and physical character; let curves, frame rates, and constants differ (KB-C 129.1).
All code here is illustrative; verify against the current platform docs and OS/browser versions before shipping.
(Source keys: grammar-and-derivation.md line 7.)

## Contents
1. Runtime selection, integration entry point, production model
2. CSS custom properties
3. WAAPI and Motion.dev
4. After Effects (values, frames, Essential Properties)
5. Lottie and Rive
6. SwiftUI and Compose
7. Spring translation
8. Emitter checklist

## 1. Runtime selection (KB-C 119)
| Runtime | Strength | Fits | Model this limit |
|---|---|---|---|
| CSS transitions/animations | declarative, broad | component states, light web motion | complex choreography and dynamic control get awkward |
| Web Animations API | programmatic playback, reversible | interactive sequencing, retargeting | needs careful implementation |
| View Transitions | state-to-state view continuity | navigation, view changes | not a replacement for component motion |
| Native (SwiftUI/UIKit, Compose) | native physics and gestures | high-fidelity app interaction | parity needs semantic mapping |
| Rive | interactive vector + state machines | expressive brand/product components | runtime integration and governance of state machines |
| Lottie / dotLottie | portable authored assets | illustration, expressive sequences | can become a black box without documented semantics |
| After Effects / MOGRT | rich authoring, broadcast/editorial templates | broadcast, social, editorial toolkits | not a product runtime; interactivity bounded by exposed controls |
| Pre-rendered video | maximum control | campaign, broadcast, hero | lowest adaptability, poorest semantic interoperability |

Timing sources differ: clock-time (duration), scroll-linked, gesture-linked, input-linked. A duration token cannot
describe the last three; give them contracts (`timingSource`).

**Integration entry point (DOS 43).** Before picking runtimes, decide what the system is built around first:

| Entry | Fits when | Strength | Risk |
|---|---|---|---|
| Token-first | many products share fundamentals; code consumption matters | easy global change | becomes too abstract |
| Component-first | behavior is component-specific; designers need ready patterns | high usability | behavior duplicated across components |
| Pattern-first | interaction logic spans components and workflows | captures choreography and state | hard to maintain without a strong taxonomy |
| Tool-first | production volume is huge and output varies widely | high production throughput | the tool outlives the design logic it encoded |

Most mature systems end hybrid (tokens, behaviors, components, patterns, tools, code, governance). Name the entry
point and the risk you are watching.

**Production model (CMP C18.01-C18.02, C19).** A brand or toolkit system also picks how outputs get made:

| Model | Characteristics | Tradeoff |
|---|---|---|
| Static export | pre-rendered assets | most craft control, least flexibility |
| Template-driven | variables in editable source files | strong operational gain, moderate flexibility |
| Parametric | rules generate the variants | high scale; needs stronger system design |
| Runtime | renders live from data and context | most adaptable; needs engineering and QA |
| Agentic | AI or agents assemble assets under rules | huge scale; governance and taste become critical |

For parametric, runtime and agentic models, use **bounded randomness**: define the space of legal outputs (input
schema and validation, brand rules, seed and distribution, a deterministic mode for review, a runtime fail-safe,
human override and approval points, and snapshot plus rule QA), and never ask the generator to "make it on-brand".
Selection and rejection criteria: governance.md 6, generated variants. Once motion runs as infrastructure, the
system is a small software product: schemas, error handling, versioning, observability and permissions (CMP
C19.01).

## 2. CSS custom properties
Emit one variable per primitive and per semantic member, then composite shorthands. Keep reduced/instant as
overrides on the same names so components never branch.
```css
:root {
  --motion-duration-medium: 300ms;
  --motion-easing-enter: cubic-bezier(0.16, 1, 0.3, 1);
  --motion-reveal-duration: var(--motion-duration-medium);
  --motion-reveal-delay: 0ms;
  --motion-reveal-easing: var(--motion-easing-enter);
  --motion-reveal-travel: 12px;          /* spatial amount is a separate variable so reduced can zero it */
}
@media (prefers-reduced-motion: reduce) {
  :root { --motion-reveal-duration: 200ms; --motion-reveal-travel: 0px; }   /* strategy: fade */
}
:root[data-motion="instant"] { --motion-reveal-duration: 0ms; --motion-reveal-travel: 0px; }
.dialog { transition: opacity var(--motion-reveal-duration) var(--motion-reveal-easing) var(--motion-reveal-delay),
                      transform var(--motion-reveal-duration) var(--motion-reveal-easing) var(--motion-reveal-delay); }
```
Values that only change duration cannot express "replace slide with fade"; encode the *amount* (travel, scale,
blur) as variables so reduced mode zeroes them. Lint: Stylelint rule requiring `var(--motion-*)` in `transition`
and `animation` declarations (Carbon, Polaris, OpenCRVS precedent), with a documented-disable path for exceptions.
Registered custom properties (`@property`) enable typed interpolation where needed.

## 3. WAAPI and Motion.dev
```js
const css = (n) => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
function reveal(el) {
  return el.animate(
    [{ opacity: 0, transform: `translateY(${css('--motion-reveal-travel')})` }, { opacity: 1, transform: 'none' }],
    { duration: parseFloat(css('--motion-reveal-duration')), easing: css('--motion-reveal-easing'), fill: 'both' });
}
// interruption: el.getAnimations().forEach(a => a.reverse())  // or cancel/commitStyles per the contract's policy
```
Motion.dev: `animate(el, { opacity: [0, 1] }, { duration: 0.3, ease: [0.16, 1, 0.3, 1] })`; springs
`{ type: "spring", duration: 0.35, bounce: 0.15 }` (check current option names: Motion has used `bounce` and
`visualDuration`). Read tokens from the generated JSON/CSS, never hard-code. For navigation use the View
Transition API with named transitions mapped to `shift`/`reveal` tokens, and skip it under reduced motion.

## 4. After Effects
Why this section matters for broadcast and toolkit work: AE is where the system's invariants get *protected*.
Key facts (ADV 4.2; KB-C 121, 135): Essential Properties turn a nested comp into a parameterized component;
Essential Graphics exports those controls as a Motion Graphics Template (MOGRT); Responsive Design - Time protects
regions (intros/outros) while the middle retimes; JSON files imported as footage can be read by expressions
(`footage("motion.tokens.json").sourceData`) so one canonical token file can drive many comps. Confirm behavior in
the current AE version; for scripting/tooling defer to the `after-effects-engineering` skill.

**Emit these for AE:**
1. A flattened JSON (`ae-values.json`) with each semantic token as seconds, frames at each project fps (e.g. 23.976, 25, 29.97, 59.94), and bezier handles. Frame counts must be integers: 300 ms = 9 frames at 29.97, 18 at 59.94. Snap to whole frames and record the rounding.
2. Bezier-to-keyframe handles: for `cubicBezier [x1,y1,x2,y2]` over a segment of duration `T` and value change `V`, the Easy Ease handles are `outInfluence = x1 * 100 %`, `inInfluence = (1 - x2) * 100 %`, `outSpeed = (y1 / x1) * (V / T)`, `inSpeed = ((1 - y2) / (1 - x2)) * (V / T)` (guard x1 = 0 and x2 = 1). Always eyeball in the graph editor; influence is clamped at 0.1-100 %.
3. A springs expression library keyed by perceptual family (snappy/smooth/soft/playful) with `freq`, `decay` or stiffness/damping parameters, so settle behaves like the platform spring without matching constants.
4. A naming convention for Essential Properties and layers so the toolkit reads like the system.

**Essential Property naming (control surface in the system's language):**
| Convention | Example | Why |
|---|---|---|
| `Verb / Control` | `Reveal / Energy`, `Settle / Tempo` | ties a control to the owned verb |
| Ranges in the label or tooltip | `Energy (0-100, default 40)` | parameter ranges, not just names |
| Mode controls as dropdowns | `Intensity: Quiet / Standard / Loud` | bounded expressive choice |
| Protected items prefixed or in a locked comp | `_LOCK Timing Core` | invariant stays unexposed |
| Version stamp on the template | `LM_Toolkit v1.3.0` | orphan detection |

Do not expose `Slider 4`, raw keyframes, or expression chains. Document which control drives which token and what
it protects (control table in contracts-and-specs.md section 7).

For broadcast packages also specify: frame-rate and field handling, safe areas, loudness-independent (silent
playback) meaning, minimum hold frames for readability, edit-point protection (trim handles), and a lower-third
stress set (very long name, very short, three lines, no title).

## 5. Lottie and Rive
**Lottie** transports baked keyframes. A `cubicBezier [x1,y1,x2,y2]` maps to the keyframe out tangent `o = (x1, y1)`
and in tangent `i = (x2, y2)` (Lottie stores them as `{x:[..], y:[..]}`); duration becomes a frame span at the
file's `fr`. Semantics (which verb, which mode) do not travel with the file, so carry them in the registry row
and in file naming/metadata. Provide a reduced-motion variant as a separate file or a poster frame; never
rely on the player to guess. dotLottie supports versioned, themeable packages (check current features).
**Rive** is a runtime with state machines: model modes as a number or boolean **input** (`motionMode`: 0 full,
1 reduced, 2 instant) and verbs as triggers or states, so the same asset honors the contract. Authored easing is
baked per animation; keep a mapping from token ID to animation name in the registry. Neither format governs
semantics for you; the registry does (KB-C 136).

## 6. SwiftUI and Compose
```swift
// SwiftUI stub (verify against current OS APIs)
enum Motion {
    static let reveal = Animation.smooth(duration: 0.30)                  // verb: reveal, perceptual spring, no overshoot
    static let settle = Animation.spring(duration: 0.35, bounce: 0.15)    // verb: settle, allowed overshoot
    static func reduced(_ full: Animation) -> Animation { .easeOut(duration: 0.20) }  // strategy: fade
}
struct Panel: View {
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var open = false
    var body: some View { /* withAnimation(reduceMotion ? Motion.reduced(Motion.reveal) : Motion.reveal) { open.toggle() } */ EmptyView() }
}
```
Native SwiftUI springs preserve velocity across retargeting, which meets the contract's `velocity: inherit`.
```kotlin
// Compose stub (verify against current Material 3 / Compose versions)
object Motion {
    val reveal = tween<Float>(durationMillis = 300, easing = CubicBezierEasing(0.16f, 1f, 0.3f, 1f))
    val settle = spring<Float>(dampingRatio = 0.9f, stiffness = 700f)   // Material 3 default spatial slot
}
```
Android has no direct `prefers-reduced-motion`; respect the system animator duration scale and any in-app
setting, and route through the same `reducedMotion.strategy`. Material 3's `MotionScheme` is the theme-level
mechanism for supplying component motion; map semantic verbs onto its spatial/effects slots rather than inventing
parallel constants.

## 7. Spring translation
Relations (unit mass; Apple's perceptual spring parameters, verify in current docs):
`stiffness = (2*pi / duration)^2`, `dampingRatio = 1 - bounce` for `bounce >= 0`, `damping = 2 * dampingRatio * sqrt(stiffness)`.
So Material's default spatial spring (damping ratio 0.9, stiffness 700) is about `duration 0.24 s, bounce 0.10`;
fast spatial (0.9, 1400) about 0.17 s; slow spatial (0.9, 300) about 0.36 s. Effects springs use damping ratio 1
(no overshoot). Treat conversions as starting points; tune by feel and by interruption behavior, then record
the per-platform values in `platformMappings`. Do not tell a team to "use stiffness 700 everywhere".

## 8. Emitter checklist
- One canonical JSON; each platform output generated, with the token version stamped in a header comment.
- Modes emitted (full/reduced/instant) in each target's native mechanism.
- Spatial amounts (travel, scale, blur) exposed as separate values so reduced can zero them.
- Springs mapped per platform, not copied.
- Unsupported behaviors declared `unsupported` in the platform map, not silently dropped (build gate 6, KB-C 117.3).
- A fixture for each platform that plays the same three verbs, used for parity review and regression.
