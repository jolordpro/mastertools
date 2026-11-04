# 08 — Expressions (the third engine)

> Expressions are **not** scripts. They live on a property, re-evaluate **every frame**, and run in a different
> language engine than ExtendScript. Conflating the two is a classic bug. This file covers the engine truth, the
> common rigs, and per-frame cost. (Writing/clearing expressions *from a script* — backups, engine-match, escaping
> — is in `04-extendscript-rigor.md` §6.)

---

## §1 — TWO ENGINES, STATE WHICH ONE

- **Default engine = JavaScript (modern, ES6-ish)** since AE 16 / 2019. `const`/`let`, arrow functions, template
  literals, `Math` helpers, etc. are all fine here — the **opposite** of script (ES3) code.
- **Legacy ExtendScript engine** is opt-in per project (File ▸ Project Settings ▸ Expressions, or
  `app.project.expressionEngine` → `"javascript-1.0"` vs `"extendscript"`).
- **Always state which engine an expression targets**, and flag anything that behaves differently between them.
  Default to the **JS engine** and say so.

**Differences that bite when switching engines:**
- **Implicit return:** in the JS engine, the expression's value is the last evaluated statement; an `if/else`
  that doesn't assign to a single trailing value can behave unexpectedly — prefer assigning to a `var result`
  and putting it on the last line.
- **`$.…` / `system` / ExtendScript globals** exist only in the Legacy engine — don't use them in JS-engine
  expressions.
- **Number/string formatting** and some `Math`/`Date` edge behavior differ; test both if the project might flip
  engines.
- **Performance:** the JS engine is generally faster and is where Adobe invests; recommend it unless the project
  is pinned to Legacy for compatibility.

---

## §2 — THE SCRIPT vs EXPRESSION LINE

| | Script (`.jsx`) | Expression |
|---|---|---|
| Language | ExtendScript **ES3** | **Modern JS** (default) / Legacy ExtendScript |
| When it runs | on demand, once | **every frame**, live on a property |
| What it touches | the whole project/DOM (`app.project`) | its own property + referenced layers/comps/footage |
| Cost model | one-time | **per-frame × every frame rendered** |

Use a **script** to *set up* a rig (add controls, write expressions, build layers); use an **expression** to make
a value *react live*. A script that writes an expression must write syntax matching the **target engine** (`04`
§6).

---

## §3 — COMMON RIGS (JS engine unless noted)

- **Loop / cycle:** `loopOut("cycle")` / `loopOut("pingpong")` / `loopOut("offset")` / `loopOut("continue")`;
  `loopIn(...)` for the head.
- **Ease / remap:** `ease(t, tMin, tMax, vMin, vMax)` and `linear(...)` to map one range to another (e.g., a
  slider 0–100 → 0–360°). `clamp(v, min, max)` to bound.
- **Inertia / overshoot / bounce:** sample the last keyframe velocity (`velocityAtTime`) past the final key and
  decay it with a damped sine — the standard "inertial bounce" rig (Dan Ebberts / motionscript.com is the
  authority).
- **Wiggle:** `wiggle(freq, amp)` for organic motion; `temporalWiggle`/`seedRandom(idx, true)` for per-layer
  determinism. Mind the cost (§4).
- **Time / counters:** `Math.round(time * fps)`; build counters/timecode by formatting `time` or a slider; pad
  with a small helper. On 26.0+ you can read a property's *displayed* text via `Property.valueText` from a script
  for readouts (verify live).
- **Spatial / 3D:** `toComp`, `toWorld`, `fromWorld`, `lookAt(fromPoint, atPoint)` for camera/orientation rigs;
  dot/cross products for facing/lighting math.
- **Data / text:** `thisComp.layer("Data").text.sourceText` + parsing; `comp("X")` / `footage("data.json")
  .sourceData` (JSON) for data-driven graphics — "if you're typing a score into a graphic by hand, you're doing
  it wrong."
- **Control rigs:** drive expressions from **slider/checkbox/angle/color** Expression Controls effects so the
  artist edits controls, not code. *"Every magic number in an expression is a future bug"* — expose it as a
  control or a comment.

---

## §4 — PER-FRAME COST (warn about this)

Expressions run every frame, so cost compounds:
- **`sampleImage`** (reads pixels) is expensive — avoid in hot paths.
- **`valueAtTime` / `velocityAtTime` chains** re-evaluate the referenced property's whole expression at another
  time — a chain across many layers multiplies fast.
- **Large `wiggle` networks** and deep cross-comp reference chains (`comp()`/`footage()` resolved every frame)
  add up.
- Prefer **baking** to keyframes (`Animation ▸ Convert Expression to Keyframes`) when a rig is final and the
  expression is costly, or move heavy logic into a one-time **script** that writes the result.

When delivering an expression, name the engine, comment any non-obvious math, expose magic numbers as controls,
and flag any construct whose behavior differs between the JS and Legacy engines. Authoritative reference:
motionscript.com (Dan Ebberts) and Adobe's Expression Language Reference — verify any newer expression API per
the freshness protocol (`00` §0).
