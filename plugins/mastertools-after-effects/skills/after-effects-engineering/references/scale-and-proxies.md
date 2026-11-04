# Working at scale on a big, messy project — verified notes

For jobs where one template must produce dozens of files: how to find the render cost, how
to buy it back with proxies, and how to prune the project without breaking it. All figures
measured on AE 26.5x89, macOS arm64, on a 71-comp / 1920×1080 / 59.94 fps / 600-frame job.

## Contents

- [Measuring render cost so the number means something](#measuring-render-cost-so-the-number-means-something)
- [Attributing cost to a subtree](#attributing-cost-to-a-subtree)
- [Buying it back with comp proxies](#buying-it-back-with-comp-proxies)
- [Pruning: a disabled layer is not a removable layer](#pruning-a-disabled-layer-is-not-a-removable-layer)
- [Proving a structural edit changed nothing](#proving-a-structural-edit-changed-nothing)

## Measuring render cost so the number means something

**Purge between every configuration.** `app.purge(PurgeTarget.ALL_CACHES)` before each timed
render, or you are measuring the disk cache. The same 5-frame span on the same project
measured 675 ms/frame cold and 252 ms/frame warm — a 2.7× swing that read exactly like a
real optimisation win. Planning around the warm number would have understated a 60-file
batch by half.

**A per-frame figure is meaningless without naming the frames.** On one project:

| span | character | ms/frame (cold) |
|---|---|---|
| f44–60 | peak of the transition, heavy motion blur | 820 |
| f0–140 | the animated section overall | ~517 |
| f400–416 | static hold, slow camera push | 325 |

A 2.5× spread inside one 600-frame comp. Quote a whole-file estimate as a weighted sum over
the sections, and say what the weights were:

    600f ≈ 140f animated @820ms + 460f hold @325ms ≈ 4.4 min/file

## Attributing cost to a subtree

To price one precomp: toggle only that named layer, purge, render a fixed span, difference
the timings. Whitelist the layer by name — never disable by index or in bulk.

```javascript
function priceLayer(hostName, layerName, span) {
    var ly = findLayer(hostName, layerName);
    var was = ly.enabled;
    try {
        ly.enabled = false;
        app.purge(PurgeTarget.ALL_CACHES);
        return timedRender(span);
    } finally { ly.enabled = was; }     // always restore
}
```

**Savings are sublinear — measure the combination, never the sum.** Three subtrees priced
at 148 + 183 + 1 = 332 ms/frame individually came to **264 ms/frame** when all three were
disabled together, because removing one also removes the cost of compositing the others.

**Price in more than one section.** A subtree that is only on screen for part of the piece
looks far cheaper across the whole file than its peak suggests:

| subtree | animated span | static span |
|---|---|---|
| background motion tile (on throughout) | 148 ms (18%) | 114 ms (35%) |
| side-card assembly (on ~1/4 of the piece) | **183 ms (22%)** | **14 ms (4%)** |

Reading only the animated span would have justified pre-rendering the side cards as the
bigger win. It is the smaller one.

## Buying it back with comp proxies

A subtree is pre-renderable when nothing inside it varies per output. Prove it rather than
assume it — walk the subtree and check every expression and footage name against the set of
per-output tokens:

```javascript
// collect every expression in the subtree, then assert none references a per-output control
var re = /comp\("([^"]+)"\)|layer\("([^"]+)"\)/g;
```

On the measured job this returned 11 comps / 7 expressions for the background tile and
20 comps / 8 expressions for the side cards, with **zero** per-output references — every one
pointed at a palette colour, a dropdown index or a team name. That is the check that makes
pre-rendering safe.

**Prefer a proxy over replacing the source.** `AVItem.setProxy(file)` /
`setProxyWithSequence(firstFile, false)` leaves the original comp intact and reverses with
`setProxyToNone()`. Nothing in the comp structure changes, so a re-render for a different
variant is a one-line swap.

Three things that bite:

- **`Best Settings` ships with `Proxy Use = "Use No Proxies"`**, so attaching a proxy changes
  nothing until you override the render setting. `applyTemplate` first, then:
  `item.setSettings({ "Proxy Use": "Use All Proxies" })`. Read it back from
  `getSettings(GetSettingsFormat.STRING)["Proxy Use"]` to confirm it took.
- **`AVItem.proxySource` returns `undefined`** on 26.5 even when `useProxy === true`. You
  cannot introspect the attached proxy's dimensions or duration through it — guard the
  access and verify dimensions from the file you just rendered instead.
- **A proxy is not pixel-identical if the container quantises.** A 3840×2160 opaque tile
  pre-rendered to ProRes 422 came back with max channel delta **18–19/255** on 0.18% of
  pixels, mean under 1 LSB, confined to the texture's fine edges — invisible at 1:1 and
  acceptable when the delivery codec is the same ProRes 422, but *not* zero. Diff and look
  before calling it free.

**What the proxy actually recovered**, against the theoretical maximum from disabling the
layer outright:

| span | layer off (ceiling) | proxy | recovered |
|---|---|---|---|
| animated | 148 ms | 90 ms | 61% |
| static | 114 ms | 111 ms | 97% |

Decoding a large frame is not free, so the proxy recovers most of the win where the rest of
the frame is cheap and less of it where other work dominates.

**Container choice follows the alpha question.** Render one frame and measure coverage
before picking a template — an opaque subtree needs no alpha-capable module at all:

| subtree | alpha | container | size |
|---|---|---|---|
| background tile 3840×2160 | 100% opaque | ProRes 422 (`High Quality`) | 1.55 GB / 600f |
| side cards 1920×1080 | needs alpha | PNG sequence (`PNG - Trans`) | 110 MB / 180f |

The mostly-transparent sequence compressed to ~600 KB/frame; empty frames were 8 KB. A
sequence beats a movie badly for sparse content.

## Pruning: a disabled layer is not a removable layer

**Of 151 disabled layers in one project, 45 were load-bearing.** Deleting all of them would
have broken the render in 45 places. A disabled layer still contributes when it is:

- a **track matte** (`layer.isTrackMatte`) — disabled is the *normal* state for a matte
- a **parent** of another layer — a disabled null still drives its children's transforms
- named by an **expression** anywhere in the project
- a **guide layer** (`layer.guideLayer`) — never renders anyway, so deleting it only destroys
  an authoring aid; protect it

```javascript
function removable(ly, isParentIdx, exprNames) {
    if (ly.enabled) { return false; }
    return !(ly.isTrackMatte || isParentIdx[ly.index] ||
             exprNames[ly.name] || ly.guideLayer);
}
```

Scope note: matching expression references by layer *name* project-wide over-protects, since
another comp may have a same-named layer. Over-protecting is the correct direction.

**Delete layers backwards within a comp** — indices renumber as you go. Collect the kill list
in a forward pass, then walk it from the highest index down.

**Prune comps and items only after layers, and iterate to a fixed point.** Removing a layer
orphans the comp it referenced; removing that comp orphans another. On the measured project
this took **3 rounds** and only reached the real total then — a single pass found 2 comps,
the cascade found 6. Report if you hit the round cap rather than stopping silently.

**A dry run cannot see the cascade.** With nothing actually removed, `item.usedIn` still
reports the old referrers, so the dry run under-reports. Say so in its output instead of
letting the operator read it as the final count.

Use `item.usedIn.length === 0` rather than a hand-rolled reachability graph — but keep an
explicit keep-list for roots and dashboards, which legitimately have no referrer.

## Proving a structural edit changed nothing

Render a frame span before the edit, render it again after, and diff. Two calibrations make
the gate trustworthy:

- **The render is deterministic.** Two renders of identical state differ by max 1/255, even
  on the heaviest motion-blur frames. So a real diff is a real change — do not reach for
  "nondeterminism" as an explanation, which is a mistake that costs an hour.
- **But 16 bpc → 8 bpc PNG dithering is not deterministic in its pattern.** 61% of pixels
  differ by exactly 1 between two renders of the same frame. **The gate needs a ±1
  tolerance**; a zero-tolerance diff fails every time and teaches you to ignore it.

Localise before judging. Report the bounding box of changed pixels and the count of affected
frames, not just a max delta — "8 of 141 frames changed, all inside heavy motion blur,
confined to the top-right quadrant" is actionable where "max delta 203" is not.

**A whole-frame metric cannot isolate a small element.** Looking for 30 Hz stepping in a
nested comp, a whole-frame and then a whole-region difference both reported "no stepping",
because the frame was already changing 36–88% per frame from a camera push. The element was
genuinely sampling at half rate. When a global metric says "nothing", bound its sensitivity
before believing it — or isolate by reverting one comp at a time, which is what finally
gave a clean answer.

## Making a pixel gate bit-exact instead of ±1

The ±1 tolerance above is only needed because the *delivery* render path is noisy. It is
not a property of AE. Three **render-settings overrides** — not project mutations, so
nothing is baked into the file and `bitsPerChannel` stays untouched — make a gate render
bit-reproducible:

```javascript
rqi.applyTemplate("Best Settings");
rqi.setSettings({ "Motion Blur":    "Off for All Layers" });
rqi.setSettings({ "Frame Blending": "Off for All Layers" });
rqi.setSettings({ "Color Depth":    "8 bits per channel" });
```

Measured on the same 14 heavy-motion-blur frames, rendered twice from identical state:

| settings | frames differing | max channel delta | pixels differing |
|---|---|---|---|
| delivery (blur on, 16 bpc) | 4 of 4 | 1 | **69.6%** |
| the three overrides above | 0 of 14 | **0** | 0 |

So run gates in this mode and diff at **zero tolerance**. A crisp zero means every later
diff is a real signal, which is worth far more than it costs — the 16→8 dither alone
paints two-thirds of the frame with ±1 noise and trains you to ignore the gate.

**The value strings are case-sensitive and inconsistent between keys.** `"Off for All
Layers"` is correct for both Motion Blur and Frame Blending; `"Off For All Layers"`,
`"Off"` and `"All Off"` all throw `Invalid Value`. Meanwhile `Effects` wants `"All Off"`.
Do not normalise the capitalisation — read each one back and confirm it took. `"Depth"`
is not a key; the key is `"Color Depth"`.

Set each key in its own `setSettings` call and read it back; a refused key otherwise
looks identical to an applied one.

## A long render can emit one inconsistent frame — and no self-check finds it

Two 600-frame renders of **identical** project state, same span, same settings, differed
on exactly one frame: f52, 40.17% of pixels, max channel delta 80. Three later renders
(short spans, different span starts, a second full run) all agreed with each other; the
first full run's copy was the outlier.

Characterise it correctly before deciding how much to care. Max delta 80 sounds like a
wrecked frame, but the **mean absolute difference was 1.38/255** — many pixels shifted
slightly, a few a lot, which is the signature of a sub-pixel *temporal* offset during
fast motion, not a garbage frame.

**Two plausible detectors were tried and both failed. Do not reach for them:**

| heuristic | result |
|---|---|
| PNG file size (robust z-score) | flagged five healthy frames at z > 70, missed the real one. Size tracks content complexity, so a transition frame is legitimately larger than a static hold. |
| temporal self-consistency (frame vs both neighbours) | the bad frame sat 1.38 mean-abs from its known-good twin while **legitimate** neighbour-to-neighbour motion at that point was 47–50. The signal is buried ~35x under real movement. |

So a single render cannot be checked against itself. What works is a **second render of
the same span, diffed at zero tolerance** — which is bit-exact in the test mode above.
That is affordable precisely because the gate is sampled: 4 frames (two proof stills) or
36 frames (six short spans) render twice in seconds, where a full 600 cannot.

Keep the cheap structural checks — missing frames, zero-byte files, count mismatch —
they catch real and different failures. And count files with a real directory listing,
not a shell glob: a glob silently reported 572 of 600 files in one run here.

## Proving a "no-op" migration really is one

The method that worked, in order — each step is cheap and each one eliminates a whole
class of explanation:

1. **Revert everything and re-gate first.** If the fully-reverted state still differs
   from the baseline, the baseline is wrong, not the edit. This is what exposed the
   corrupt frame above, after ~20 minutes spent building style-inheritance theories.
2. **Bisect over a rule table, not by reasoning.** Drive each migrated property from a
   table of `[group, comp, layer, matchName, pathNeedle, oldExpr, newExpr]` and set the
   whole project to old/new per group from one parameter. Five renders of a 6-frame span
   narrowed 15 expressions to the single one responsible; no hypothesis survived contact
   with it.
3. **Locate properties by matching their current expression text**, not by a hardcoded
   path. If the found set and the rule table do not pair up exactly — in *both*
   directions — write nothing. A renamed layer then fails loudly instead of quietly
   retargeting an expression.
4. **Diff by frame number, not sorted position.** Comparing a 6-frame span against a
   600-frame baseline by sorted index compares f50 against f00 and reports nonsense.

## `setValue` quantises to float32; the UI does not

`ADBE Slider Control` *and* `ADBE Point Control` both store what `setValue` gives them as
float32. A value typed into the UI (or loaded from an older project) can be a true
double. So copying a control value from one effect to another is **not** bit-exact when
the value is not float32-representable:

    original Point, UI-entered : 99.900000000000
    after setValue([99.9, 0])  : 99.900001525879      (relative error 1.5e-8)

That 1.5e-6 px position shift moved ~800 px/frame by 1–3/255 across 413 of 600 frames —
invisible, but enough to destroy a zero-tolerance gate. Two consequences:

- **Read values from the source property; never retype them as literals.** A literal in
  the script is also a transcription risk, and the read costs nothing.
- **Classify the residual rather than failing on it.** Compare at full precision, and
  treat a relative error under ~1e-6 (float32 epsilon is ~1.2e-7) as the documented
  `setValue` quantisation — reported, not silently accepted and not a hard failure.
  Anything larger is a real bug.
