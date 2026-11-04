# 07 — Rebuild, Repurpose & Reuse (working with existing scripts)

> The other half of real tool work: an existing script the user wants to **fix, refactor, rebuild to standard,
> harvest for parts, repurpose, or modernize** — or "build one like X." Inherited AE code is an asset with
> embedded knowledge (the author's accumulated edge-case fixes, the user-facing behavior, saved user state).
> The job is to **raise it to standard without destroying that value** — defaulting neither to "patch the mess"
> nor "rewrite from zero." Read with `04` (the rigor usually hiding in the old code) and `00` §5 (which APIs
> changed underneath it).

---

## §1 — INTAKE: ASSESS BEFORE YOU TOUCH

Never start editing until you've characterised it. Produce a short assessment first.

1. **Get the actual source.** Two walls: `.jsxbin` is compiled/unreadable — ask for the `.jsx` (if none exists,
   it's a fresh build informed by *behavior*, not a refactor). No code, only a description / "make one like X" →
   greenfield informed by the tool's behavior (route to `02` + §8 below).
2. **Characterise it (write down):** the **vehicle** (run-once / ScriptUI / CEP); the **target AE version +
   version-dependent APIs**; **ES3 health + hidden polyfill reliance** (does it use `JSON`/`forEach`/`indexOf`
   with *no* polyfill? → it's silently depending on the phantom-polyfill injection, a latent cold-start failure);
   **deprecated/fragile patterns** (index-based refs, localized display names, `trackMatteType`-only,
   `findMenuCommandId("string")`, walking the property tree from the layer root, per-item undo groups);
   **architecture** (does it resemble the `05` §5 section model, or one long flat script?); **external surface**
   (files read/written, preset formats, third-party effect matchNames); **saved user state** (`app.settings`
   keys, preset/JSON files users may already have data in — this constrains how freely you can change things).
3. **Separate the valuable kernel from the replaceable shell.** What's worth keeping (a clever algorithm, a
   hard-won matchName map, an easing function, real edge-case handling) vs. dated scaffolding?

---

## §2 — THE DECISION (run top-down, first match; state the choice + one-line reason)

```
Source unreadable (.jsxbin) or absent (behavior only)?
    → FRESH BUILD informed by behavior (route 02 + §8). Request source if jsxbin.
Small, well-scoped change to fundamentally sound code?
    → PATCH in place. Smallest surgical diff; touch nothing else; preserve behavior.
Behavior must stay identical but the internals are rotting / unsafe?
    → REFACTOR. Restructure to the §5 section model; same outputs, same refs; verify parity (§4).
Intent/UX is right but the code is below standard (ES3 leaks, no guards, weak UX)?
    → REBUILD ON STANDARD. Keep the intent, salvage the kernel, rewrite to the Quality Standard.  [most common]
You only want one idea / algorithm / pattern out of it?
    → SALVAGE. Extract the kernel, reimplement cleanly, discard the rest (§8 on IP).
The job is genuinely different from what the old tool did?
    → REPURPOSE. Reuse the architecture skeleton, swap the transform, re-run intake for the NEW job (§6).
Requirements or architecture fundamentally wrong/obsolete?
    → REWRITE. Greenfield — but mine the old one for edge cases first (§3).
```

The trap in both directions: **don't patch when the architecture is the problem** (you preserve the bug
factory), and **don't rewrite when the code is sound** (you throw away years of edge-case fixes and reintroduce
solved bugs). When unsure between Rebuild and Rewrite, prefer **Rebuild** — it forces you to read and preserve
the old defensive code.

---

## §3 — PRESERVE WHAT WORKS (Chesterton's Fence for AE)

The defining risk of rebuilding AE scripts: **odd-looking code is usually load-bearing defensive code.** Most of
the rigor in `04` is invisible until a hostile project triggers it; a "clean-up" pass that strips it reintroduces
exactly those crashes. Patterns that look removable but almost never are:

- `$.sleep(1)` after `panel.update()` → the only way progress actually repaints (`04` §3).
- Batch removals **sorted index-descending** → forward order corrupts indices (`04` §4).
- `try/catch` around `canSetExpression` / property reads → some groups throw (`04` §5).
- matchName → displayName fallback on `addProperty` → third-party effects (`04` §5).
- `parseFloat(app.version)` guards → version-gating a newer API.
- `_suppressOnChange` flag around listbox mutation → stops arrow-key toggling bugs.
- The `(function (thisObj) {…})(this)` + `instanceof Panel` wrapper → dockability.
- Interpolation-type check before `setTemporalEase` → hold keyframes throw.
- A guarded polyfill block at the top → the cold-start defense (`00` §4).

Also preserve, deliberately: **the author's intent and user-facing behavior** (don't silently "improve" a
workflow the user relies on — if a rebuild changes any behavior, *flag it*); **backward-compatible settings/
preset keys** (§4). When you *do* remove something defensive (a new API makes it unnecessary — e.g., `Layer.id`
replacing an index-validation dance), **say so and name the API that now covers it.**

---

## §4 — BEHAVIOR PARITY (regression safety without a test harness)

There is no DOM unit-test framework (`00` §6), so parity is manual and deliberate.
1. **Capture a behavior inventory of the old tool before rebuilding** — every option, what each does, defaults,
   edge handling (locked/missing/0-dur/camera/etc.), outputs. This becomes the rebuild's acceptance criteria.
2. **Re-run the new build against the same adversarial fixtures** (`00` §6) and confirm it matches item-for-item.
3. **Preserve saved-state compatibility** — keep the keys, or **write a migration** that reads the old shape and
   upgrades it (schema-versioned config, `04` §9). Never orphan a user's saved setups.
4. **No silent behavior change** — any intentional difference is called out; any unintentional one is a regression.

---

## §5 — REBUILD ON THE STANDARD (the common case)

1. **Re-run the workflow analysis (`02`) on the *current* need** — a rebuild is the moment to pay down workflow
   debt; the old primary path may no longer be the user's actual most-common task. Confirm the brief.
2. **Seed the build with the salvaged kernel** (§1.3), not the old scaffolding.
3. Run the normal build sequence — re-confirm the vehicle (`00` §3): a ScriptUI tool that grew a need for
   charts/drag may now justify CEP.
4. Apply the §3 preservation list and the §4 parity checks as you go.

---

## §6 — REPURPOSE (adapt to a new, related job)

"I have a layer renamer; I want a layer-tagger." The **architecture skeleton is reusable** — scan → cache
snapshot → preview from cache → batch-act in one undo group → result object → auto-refresh (`04` §8). What
changes is the *transform/action* and the *labels*. **But re-run the workflow intake (`02`) for the new job** —
repurposing the code is cheap; repurposing the UX blindly gets you a tool optimised for the wrong workflow.

---

## §7 — MODERNIZATION CHECKLIST (old version → AE 25/26)

- [ ] **Re-check every API against the changelog** (`00` §5, verify live); flag anything whose semantics changed
      (e.g., track mattes pre-23 vs `setTrackMatte`).
- [ ] **Adopt newer APIs that delete old hacks**, version-gated: `Layer.id` + `layerByID` (stable refs),
      selectable track mattes, `Property.valueText` (readouts), `app.scheduleTask` (debounce), `Project.replaceFont`/
      `usedFonts`. Keep a `parseFloat(app.version)` fallback. **And ask: does a *native* feature now replace this
      tool's core?** (freshness protocol, `00` §0.)
- [ ] **Purge phantom-polyfill reliance** — add guarded polyfills for any `JSON`/`Array` ES5 methods the old code
      assumed (`00` §4).
- [ ] **Re-verify ES3** across the whole file (no `let`/arrow/template literal crept in from copy-paste).
- [ ] **Re-run the cold-start test** — modernized code is exactly where latent polyfill bugs surface.
- [ ] **Re-confirm install path** for the user's current AE version; **bump the version + update the header
      changelog** (§9).

---

## §8 — INSPIRATION & IP (take ideas, not source)

- Taking inspiration from how a tool *behaves* is encouraged — its disclosure mechanism, defaults, empty-state
  guidance, primary-path economy. Name the mechanism (route to `03`) and apply it. That's design literacy.
- **Do not reproduce proprietary or decompiled code.** If the user pastes something that's plausibly a commercial
  product's source or a decompiled `.jsxbin`, build the *concept* fresh from a clean-room understanding — don't
  transcribe or lightly re-skin it.
- The user's **own** prior scripts are theirs to rebuild freely.

---

## §9 — HEADER & VERSION CONVENTION (make the next rebuild easy)

```javascript
/**********************************************************************
 * Tool Name  —  v2.0.0
 * AE compatibility: 2022+ (uses Layer.id; degrades on older)
 * What it does: one sentence.
 * Author / site / support: …
 * Settings section: "ToolName_v2"   (migrates "ToolName_v1" on load)
 * CHANGELOG:
 *   2.0.0 — rebuilt to standard; adopted Layer.id; settings migration.
 *   1.x   — original (index-based refs, no polyfills).
 **********************************************************************/
```
Keep the changelog in the file, bump the version on every rebuild, record the AE version it was written under.

---

## §10 — QC ADDENDUM FOR REBUILDS (on top of `05` §7 and `04` §11)

- [ ] Behavior parity verified against the old-tool inventory (§4); intended changes flagged.
- [ ] Defensive code preserved — or removed only with the superseding API named (§3).
- [ ] Saved settings/presets either key-compatible or migrated (§4.3).
- [ ] Modernization re-checked against the live changelog; new APIs version-gated; native supersession considered.
- [ ] Cold-start test passed after modernization; header carries version + AE-compat + migration note + changelog.
- [ ] No proprietary source reproduced; ideas reimplemented clean-room (§8).
