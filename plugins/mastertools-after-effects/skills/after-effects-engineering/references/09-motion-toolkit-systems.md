# 09 — Motion Toolkit Systems (AE toolkits, templates and MOGRTs as infrastructure)

> Use when the deliverable is not "one animation" but something **other people will produce animation with**:
> an AE template, an Essential Properties component, a MOGRT, a scripted rig, a token-driven toolkit.
> The unit of value is not "I built a good template" but "other people produce good work without specialist
> intervention on every output." All code is **strict ES3** — see `04` (guarded polyfills, matchName, undo,
> `try/finally`) and `00` §4. Provenance: distilled from the Motion Systems KB review (Motion Ops stack;
> Motion systems KB Parts 121/122/123/127/138; deep compendium C22/C36). Facts about AE versions/APIs stay
> provisional — verify per the freshness protocol in `SKILL.md`.

---

## §1 — AE as system infrastructure (the mapping)

| AE capability | Systems concept | Design question it forces |
|---|---|---|
| Essential Properties (nested comp) | **Parameterized component** | Which controls are part of the creative contract? |
| MOGRT / Essential Graphics | **Packaged behavior** | What does a non-specialist editor get to touch? |
| Responsive Design – Time | **Protected timing regions** | Which moments must keep their timing when duration changes? |
| Media Replacement | Content abstraction | Is visual logic separated from changing media? |
| Expressions / control layers | Procedural layer | Is art direction encoded as a rule, or hand-keyed? |
| Creative Cloud Libraries / shared folder | Distribution | Is the approved version the *easiest* version to get? |

**The Motion Ops stack** (what a toolkit sits inside): source templates → controls → formats (16:9, 9:16,
4:5, OOH, broadcast) → guardrails → documentation → distribution → QA → governance (owners, versioning,
deprecation). A toolkit that only has the first two layers is a template, not a system.

**The real design problem is deciding what is safe to expose.** Overexposed toolkits become parameter soup.

---

## §2 — Design procedure (do in this order)

1. **Name the invariant** — what must stay recognizable (signature mechanic, hierarchy, readability).
2. **Name the variation surface** — what creators are *supposed* to change.
3. **Define ranges, not just defaults.** A control without a documented min/max/step is a trap. Clamp in the
   expression (`clamp(v, lo, hi)`), do not rely on slider limits alone (sliders accept typed values).
4. **Name controls as concepts.** `Energy`, `Density`, `Exit Tempo`, `Brand Palette` — never `Slider 4`,
   `Dropdown 2`, `Checkbox`. If you cannot name it as a concept, it is an implementation detail: hide it.
5. **Aspect ratio first.** Decide format rules *before* building output templates; it is a system problem,
   not an export problem. Build the 16:9 -> 9:16 -> 4:5 -> 1:1 behavior (reflow vs scale vs re-stage) up front.
6. **Protect timing and hierarchy** unless variation is explicitly required (Responsive Design – Time regions
   for intros/outros/signature beats; lock or hide everything else).
7. **Build stress fixtures before distributing** (§5). **Document failure modes and boundaries.**
8. **Version like software** (§6).

### Expose vs protect

| Expose | Protect / hide | Why |
|---|---|---|
| Content (text, media) | Internal expression chains | Users change content, not mechanics |
| Approved color *roles* | Raw layer colors | Preserves semantic mapping |
| Timing *presets / modes* (e.g. Calm / Standard / Punchy) | Arbitrary keyframe editing | Protects rhythm and character |
| Density within a range | Hierarchy, structural relationships | Variation without chaos |
| Intensity mode / expression level | Physics equations, signature mechanics | Bounded latitude |
| Variant / dialect | All source controls | Keeps diversity intentional |
| Safe text-length range | Readability thresholds | Prevents overflow |
| Aspect-ratio rules, output format | Focal staging, comp hierarchy, renderer internals | Legibility; no implementation drift |

**Prefer enumerated modes over free numbers** for anything that carries brand rhythm. A dropdown of three
timing modes that map to tokens beats a duration slider that invites 0.37 s one-offs.

---

## §3 — Toolkit maturity model (where is this toolkit, and what is the next rung?)

| Level | Behavior | Outcome |
|---|---|---|
| 0 File dump | Downloadable project files | Knowledge stays with the specialist |
| 1 Template | Editable template, documented controls | Basic production scaling |
| 2 Systemized | Variants, semantic controls, examples, docs | Non-specialists produce consistent work |
| 3 Connected | Tokens, components, code/runtime outputs, versioning | Design and engineering share one motion language |
| 4 Platform | Governed platform with analytics + contribution flow | Organizational infrastructure |

Rungs 2 -> 3 is where scripting earns its keep: tokens in, rigs configured, registry out (§4, §7).
Say which level you are targeting before building; do not claim level 3 for a toolkit with hard-keyed values.

---

## §4 — Reading motion tokens into ExtendScript

**Source format.** Motion tokens are commonly authored as DTCG JSON (Design Tokens Community Group format;
the spec is still evolving — **verify the current `duration` value shape against the live spec**, since it
has varied between a string like `"200ms"` and an object `{ "value": 200, "unit": "ms" }`). Typical shapes:

```json
{ "motion": {
    "duration": { "fast": { "$type": "duration", "$value": "150ms" },
                  "base": { "$type": "duration", "$value": { "value": 240, "unit": "ms" } } },
    "easing":   { "standard": { "$type": "cubicBezier", "$value": [0.2, 0, 0, 1] } },
    "enter":    { "$type": "transition",
                  "$value": { "duration": "{motion.duration.base}", "delay": "0ms",
                              "timingFunction": "{motion.easing.standard}" } } } }
```

**ES3 rules specific to this job** (extend `04`'s discipline):
- `JSON` is **not** native to the ExtendScript engine, and a dev machine may have it injected by an Adobe panel
  (the phantom-polyfill trap). Ship a **guarded** parser: `if (typeof JSON === "undefined") { JSON = {}; }`
  then `if (typeof JSON.parse !== "function") { JSON.parse = … }`. Use a vetted ES3 json2-style implementation,
  not a hand-rolled one. The quick `eval("(" + s + ")")` fallback is acceptable **only** for a local,
  user-owned token file after the json2 safety regex has rejected anything but JSON syntax — never for a file
  fetched from a URL.
- Keys beginning with `$` are legal identifiers in ES3 but use **bracket access** (`tok["$value"]`) for
  consistency; never `tok.default`/`tok.class`-style reserved words as dotted keys (ES3 forbids them).
- No trailing commas in anything you emit; no `Array.isArray` (use `Object.prototype.toString.call(x) ===
  "[object Array]"`); no `Object.keys`; iterate with `for (k in obj) if (obj.hasOwnProperty(k))`.
- Read with `var f = new File(path); f.encoding = "UTF-8"; f.open("r"); var s = f.read(); f.close();` — check
  `f.exists` and `f.open()` return values; **return a structured failure, never `alert()`** (`SKILL.md` hard rule).
  File write-back (registry, report) needs the "Allow Scripts to Write Files and Access Network" pref.
- Resolve aliases (`"{motion.duration.base}"`) with a **cycle-guarded** walk (depth-limit ~10); an unresolved
  or cyclic alias is a reported error, not a silent default.
- Normalize on read: durations -> **seconds** (AE time unit), ms/s/frames handled explicitly; cubicBezier
  -> a validated 4-number array with `x1, x2` in [0, 1] (reject otherwise; DTCG requires it).
- Treat the token file as the **single source of truth** and stamp its version into the output (§6).

```javascript
// Duration token -> seconds. Accepts "150ms", "0.2s", or {value, unit}. Returns null on anything else.
function tokDurationSec(v) {
    var n, u;
    if (typeof v === "string") {
        var m = /^\s*(-?[0-9]*\.?[0-9]+)\s*(ms|s)\s*$/.exec(v);
        if (!m) return null; n = parseFloat(m[1]); u = m[2];
    } else if (v && typeof v === "object" && typeof v["value"] === "number") {
        n = v["value"]; u = v["unit"];
    } else { return null; }
    return u === "ms" ? n / 1000 : (u === "s" ? n : null);
}
```

---

## §5 — Mapping `cubic-bezier` to AE temporal ease (the honest version)

**Why it works at all.** For a single animated value between two keyframes, AE's temporal interpolation *is* a
cubic Bezier in (time, value) space whose handles are set by each keyframe's **influence** (handle length as
% of the segment's time span) and **speed** (handle slope, in value-units/second). CSS `cubic-bezier(x1,y1,x2,y2)`
is the same curve normalized to a 1x1 box. So for 1-D properties the mapping is exact in principle.

Let `D` = segment duration in seconds (`key B time - key A time`) and `dV = valueB - valueA`:

| Handle | Influence (%) | Speed (units/s) |
|---|---|---|
| Key A **out** | `x1 * 100` | `(y1 / x1) * dV / D` |
| Key B **in**  | `(1 - x2) * 100` | `((1 - y2) / (1 - x2)) * dV / D` |

```javascript
// Returns {outInfl, outSpeed, inInfl, inSpeed} for one segment, or null if the curve is not mappable.
function bezierToAEEase(bz, dV, D) {
    if (!bz || bz.length !== 4 || D <= 0) return null;
    var x1 = bz[0], y1 = bz[1], x2 = bz[2], y2 = bz[3];
    if (x1 < 0 || x1 > 1 || x2 < 0 || x2 > 1) return null;      // invalid CSS/DTCG; reject
    var MIN = 0.1, MAX = 100;                                      // AE influence bounds (verify per version)
    function clampInfl(p) { return p < MIN ? MIN : (p > MAX ? MAX : p); }
    var oi = clampInfl(x1 * 100), ii = clampInfl((1 - x2) * 100);
    // Slope from the *clamped* influence so speed stays consistent with the handle AE will actually hold.
    var oSlope = y1 / (oi / 100), iSlope = (1 - y2) / (ii / 100);
    return { outInfl: oi, outSpeed: oSlope * dV / D, inInfl: ii, inSpeed: iSlope * dV / D };
}
// Apply (1-D property; keys kA, kB are key indices):
//   prop.setTemporalEaseAtKey(kA, [prop.keyInTemporalEase(kA)[0]], [new KeyframeEase(r.outSpeed, r.outInfl)]);
//   prop.setTemporalEaseAtKey(kB, [new KeyframeEase(r.inSpeed, r.inInfl)], [prop.keyOutTemporalEase(kB)[0]]);
// Interpolation must be BEZIER (not HOLD/LINEAR): setTemporalInterpolationAtKey(k, KeyframeInterpolationType.BEZIER, ...) first.
```

**Limits — state these to the user, do not paper over them:**
- **x = 0 or x = 1 endpoints.** `x1 = 0` (e.g. `cubic-bezier(0, 0, ...)`) gives infinite slope and zero influence;
  AE's minimum influence is >0, so the curve is *approximated*, not reproduced. Common "snappy" curves
  (`0.2, 0, 0, 1` is fine; `0, 0, 0.2, 1` is borderline) show visible deviation near the clamp. Quantify by sampling (below).
- **Per-segment, not global.** Ease lives on keyframes; a token curve describes one A->B segment. Multi-keyframe
  tracks need the mapping applied per segment, and a shared middle key has *both* in and out set by different segments.
- **Multi-dimensional properties.** Non-spatial vectors (Scale) take one `KeyframeEase` **per dimension** (array
  length = dimensions) with `dV` per dimension. **Spatial** properties (Position, Anchor) take one ease and the
  speed is along the *path* (units/s along path length), so `dV` is the path length, which equals the straight-line
  distance only for linear spatial interpolation. Verify array-length requirements against the live
  scripting guide for the target AE version.
- **Overshoot / y outside [0,1].** Representable (negative or >1 slopes) but real AE ease can be clamped or
  behave differently when speeds are extreme; always sample-verify.
- **Not mappable at all:** CSS `linear()`, spring/physics tokens, step functions, multi-segment curves.
  Springs need a baked-keyframe approach (sample the spring, write keyframes, accept raw keys) or an expression
  — and a baked result is **not token-driven** (flag it in the audit, §8).
- **Frame quantization.** AE samples at comp frame rate; a 150 ms token at 24 fps is 3.6 frames. Decide and
  document a rounding policy (round to frame vs allow sub-frame keys) per token.
- **Reduced frame-rate / held styles** (stepped-motion identities) are not expressible as one cubic-bezier.

**Always verify numerically, never by eye:** after applying, sample `prop.valueAtTime(t, false)` at ~10-20 points
and compare with the reference `bezier(t/D)` scaled by `dV`; report max absolute deviation as % of `dV`; fail the
rig (or warn) above a stated tolerance (e.g. 2%; the threshold is a project decision — write it down).

**Reverse direction (audit):** read `keyOutTemporalEase`/`keyInTemporalEase`, invert the table above
(`x1 = infl/100`, `y1 = x1 * speed * D / dV`) to *recover* an equivalent cubic-bezier and match it to the
nearest token within tolerance. A keyframe pair that matches no token is **raw** (§8). Guard `dV == 0`
(no motion; skip) and hold keyframes.

**Duration tokens** map to keyframe *spacing*; **transition tokens** (`duration + delay + timingFunction`) map to a
whole segment: start time = `delay`, end = `delay + duration`.

---

## §6 — Versioning, registry, reduced motion

**Version like software.** Put a semver + token-file hash on the toolkit (a text layer/marker/project metadata
or an XMP/comp comment — pick one place and document it). Keep a changelog with **breaking-change** notes
(renamed control, changed range, changed default timing). A stale toolkit circulating after the tokens moved is the
"orphaned toolkit" anti-pattern; the version stamp is what makes staleness *detectable*.

**Asset registry** (one row per approved template/MOGRT; a spreadsheet/JSON is fine):
`assetId` (e.g. `brand.motion.hero.logo-reveal.v3`) · semantic role · platforms · runtime (AE/MOGRT/Lottie/Rive/video)
· inputs (text, image, palette, locale) · output constraints (aspect ratios, frame rate, bitrate) · accessibility
(reduced-motion variant / static fallback / audio independence) · dependencies (fonts, plugins, footage) · owner ·
lifecycle (active/deprecated/archived) · semver · preview.

**Reduced motion is part of the contract, modeled per behavior, not "slow it down".** Give each semantic behavior a
default *and* a reduced mapping, and expose a single "Reduced Motion" switch on the template that the preview can show:

| Behavior | Default | Reduced |
|---|---|---|
| Spatial enter | translate + opacity + settle | opacity / instant placement / small local move |
| Large zoom | scale/camera | opacity + focal highlight |
| Parallax | depth movement | static or subtle fade |
| Continuous ambient | looping | static / user-activated |
| Elastic settle | spring | snap or minimal settle |
| Hero reveal | multi-stage choreography | static reveal / reduced amplitude |

Acceptance: state is understandable without movement; vestibular triggers removed (not merely slowed);
nothing infinite without an alternative; a designer can *see* the reduced behavior in review.

---

## §7 — Stress fixtures and tests (required before distribution)

Ship a fixtures comp/folder with the toolkit. A toolkit without fixtures is unproven.

| Stress test | Method | Failure it reveals |
|---|---|---|
| Aspect-ratio mutation | Same content at 16:9, 9:16, 4:5, 1:1, 2:3 | Rigid composition / bad responsive logic |
| Content mutation | Long / short / **no** text; long names; image / no image; RTL and CJK strings | Hidden timing and layout assumptions |
| Sequence mutation | Same component earlier/later; different durations (Responsive Time) | Overfitted choreography |
| Interruption (runtime ports) | New input mid-motion | Non-interruptible state machine |
| Silent playback | Mute everything | Overdependence on sound |
| Reduced motion | Switch on | Lost hierarchy or state meaning |
| Partner / novice authoring | Hand to a competent outsider with only the docs | Documentation and guardrail quality |
| Volume | Generate 100-1,000 variations (script it) | Entropy, duplication, performance |
| Token change propagation | Change one token, re-run, diff | Architecture / governance quality |

**Temporal regression (scriptable in AE):** for each canonical fixture record, per animated property, the
`valueAtTime` samples at fixed times plus keyframe times; commit as JSON; after any toolkit/token change re-sample
and diff. Compare *curves and endpoints*, not single frames. Keep brand-critical signature moments under manual
expert review even when the diff passes.

**Metrics worth reporting (turn "it feels consistent" into numbers):** temporal drift = % of keyframe segments
outside the approved duration/easing bands; exception rate = % of executions needing special handling; token
coverage = % of segments matching a token; accessibility coverage = % of behaviors with a tested reduced mapping;
time-to-first-correct-output for a new user. **Never invent these numbers** — compute them or mark `[CONFIRM]`.

---

## §8 — Toolkit audit checklist (run on any template, MOGRT or rig)

**Raw vs token-driven**
- [ ] Keyframes with durations/eases matching no token (raw)? List count and % of segments.
- [ ] Hard-keyed values for something that should be a control (color, position offsets, delay)?
- [ ] Baked spring/physics keys without a recorded source token (untraceable)?
- [ ] Expressions with literal numbers where a token or clamp range belongs?

**Control surface**
- [ ] Unlabeled or generic names (`Slider 4`, `Checkbox`, `Layer 12`, default effect names)?
- [ ] Controls with no documented min/max/default/step, or no clamp in the driving expression?
- [ ] Exposed controls that touch protected timing/hierarchy? Protected things left exposed?
- [ ] Parameter count: more than a novice can hold (rule of thumb: >7-9 top-level controls needs grouping/modes)?
- [ ] Enumerated modes used where free numbers invite one-offs?

**Responsive / timing**
- [ ] Protected (Responsive Time) regions defined for intro/outro/signature beats?
- [ ] Aspect-ratio behavior defined and tested for each supported format?

**Fixtures and accessibility**
- [ ] Stress fixtures present: long / short / **no** text, large / small / no image, multiple items?
- [ ] Reduced-motion mapping present, visible, and reviewed?
- [ ] Silent-playback and interruption cases considered (where applicable)?

**Governance**
- [ ] Version stamp present and matching the current token file hash? (stale = flag)
- [ ] Registry entry present with owner and lifecycle?
- [ ] Changelog records breaking changes?
- [ ] Dependencies (fonts, plugins, footage) listed and resolvable cold (no phantom dependencies)?
- [ ] Known failure modes and boundaries documented?

**Output format for an audit run:** one structured result object (counts + per-item findings with layer/comp/
property path), a severity ranking, and a maturity level (§3) with the single next rung. No `alert()`.

---

## §9 — Production anti-patterns (name them in reviews)

Token cemetery (hundreds of tokens, designers copy old values) · black-box component (works, exposes no semantics
or a11y) · screenshot contract (a movie is the spec) · reverse-handoff trap (engineer's build becomes the standard
unreviewed) · generator monoculture (toolkit so easy that output turns repetitive) · mirror-source problem (Figma,
code, AE disagree, no owner) · versionless brand shift (token change, no impact analysis) · accessibility afterthought
· orphaned toolkit · expert-dependency trap (only the owner can combine patterns correctly).

## §10 — Precedents (cite carefully; verify before quoting publicly)

- **BUCK, EA SPORTS FC 24** — reported 1,028 animated compositions plus a custom AE toolkit (aspect-ratio, light/dark
  palette, typography controls) and partner guidelines: *large prebuilt library + toolkit*.
- **Studio Dumbar, Apple Football design system (2024)** — customizable "Team X vs Team Y" animation producing hundreds
  of thousands of combinations with daily updates: *parameterized generator*. Choose per problem; they are different
  scaling models, not a ladder.
