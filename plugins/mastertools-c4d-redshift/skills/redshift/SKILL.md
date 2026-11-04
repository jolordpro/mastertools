---
name: redshift
description: The source of truth for Cinema 4D + Redshift 2026 and 2027 work on Apple Silicon, built for broadcast sports motion design. Fire this whenever the user asks anything about Redshift or Cinema 4D rendering — settings, render times, noise, fireflies, glass, refraction, trace depth, sampling, threshold, GI, motion blur, DOF, displacement, AOVs, denoising, Redshift Live, color management, or Mac memory and hardware ray tracing — and fire it proactively whenever a project involves rendering decisions, look development, a render that is too slow or too noisy, an animation that flickers, or a preset that needs building. Also fire it before answering any Redshift question from recall, because this skill's ledger overrides both training data and web search on every fact it covers. Stay dormant only for Cinema 4D work with no rendering component (modeling, rigging, UV layout, simulation setup).
---

# REDSHIFT — Render Doctrine

If `~/.claude/overlays/redshift/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

A backlot is where the studio keeps the standing sets: the street you shoot
every week, already built, already lit, already known. This skill is the
standing set for Redshift. The point is not that it knows more than the web.
The point is that what it knows has been checked, dated, and signed.

Redshift shipped nine feature releases between September 2025 and August 2026.
Training data describes a renderer that no longer exists, and most tutorials
describe one that was retired two versions ago. Both failure modes produce
confident, fluent, wrong settings. The ledger exists to make that impossible.

## Jurisdiction — the seams

- **The always-on rules** (mastertools-core's `rules/ALWAYS-ON.md`, when installed) govern the session. This
  skill is domain knowledge inside them, not a replacement for them. Their
  confidence marks and disagree-early duty still apply.
- **scout** (`plan-review:scout`, when installed) owns acquiring new evidence. When this skill hits a gap, it fires
  scout to fill it, then writes the result into the ledger. Scout produces;
  this skill stores. Without scout, fetch the Maxon page directly and
  record it the same way.
- **shakedown** (`plan-review:shakedown`, when installed) audits a built scene or delivered frame. This skill supplies
  the render-side defect taxonomy shakedown checks against.
- **challenger** (`plan-review:challenger`, when installed) pressure-tests a look or a pipeline choice before it is built.
- **timecard** (`ledgers:timecard`, when installed) attaches when render work produces a script or automation.
- **Knowledge documents** that touch render settings must agree with this
  ledger or be marked Recalled.

## Law 1 — The ledger outranks everything, and the right tree outranks the wrong one

On any fact this skill covers, precedence runs:

1. `references/ledger.md` — verified, dated, sourced.
2. Current Maxon documentation, **from the tree that owns the subject**.
3. Nothing else.

Which tree owns which subject:

| Subject | Authoritative tree |
|---|---|
| Renderer behaviour, settings, release history, feature dates | `help.maxon.net/r3d/cinema/en-us/` |
| Cinema 4D integration, UI, Material Manager, native object behaviour, C4D what's-new | `help.maxon.net/c4d/2026/` |
| Anything on a `/s26/`, `/2023/`, or other older tree | Legacy only, and only when labelled as such |

Both live trees are authoritative inside their subject. Reaching for the wrong
one is how the original reference got Live's release date backwards. Redshift
release history lives in Redshift's release notes, never in a C4D what's-new
page.

Training-data recall, tutorials, forum posts, render-farm blogs, and AI
summaries are not evidence for a Redshift fact. They may suggest what to
verify. They may never be the answer.

If the ledger and a fresh Maxon page disagree, the Maxon page wins and the
ledger entry is corrected with a new date. Say so out loud when it happens.

**Never state a Redshift number that is not in the ledger without labelling
it.** An unlabelled number reads as fact and gets typed into a render setting.

## Law 2 — One evidence label per number

Every non-obvious numeric recommendation carries one of these. No exceptions,
no second system.

| Label | Meaning | May Claude state it as fact? |
|---|---|---|
| **[V]** | Verified against current Maxon docs on a stated date | Yes |
| **[D]** | Derived by arithmetic or logic from a [V] fact | Yes, with the derivation shown |
| **[P]** | Practitioner practice, recurring but not standardised | No. Never a default |
| **[T]** | Test range, chosen to bracket plausible values | No. Must be measured first |
| **[A]** | Art direction. A look, not a claim | Not applicable. Nothing to verify |
| **[R]** | Recalled — was asserted, failed verification or went stale | Never use. Say it was recalled |

[P] never becomes [V] by repetition. [T] never becomes [V] by seeming
reasonable. The only path to [V] is a fetched, dated Maxon page.

**[A] exists because some numbers are not claims.** A 180° shutter is not an
unverified fact awaiting measurement, it is a decision about how motion should
look. Labelling it [T] would imply a right answer exists in a document
somewhere. It does not. Filing creative choices as [A] keeps them out of the
verification queue and stops the ledger from pretending taste is evidence.

## Law 3 — Diagnose the artifact, then act

This is the load-bearing idea in the whole domain. Quality in Redshift is not
one slider, and lowering Threshold is not a general-purpose fix. Most render
problems are the wrong kind of problem for the lever people reach for.

Before recommending any setting change, name the artifact:

| What you see | What it actually is | Wrong lever people reach for |
|---|---|---|
| Glass renders black, inner objects missing | Ray path terminated too early | More samples |
| Glass grainy but complete | Monte Carlo noise | More refraction depth |
| Single bright speckles | Hot ray outliers | Global threshold |
| Edges crawl on a camera move | Image-frequency and filtering | More samples |
| Clean still, flickering sequence | Temporal instability, GI or denoiser | Lower threshold |
| AOV goes noisy only after a comp grade | Importance optimisation discarded dim samples | Denoising |
| Whole frame uniformly grainy | Genuine global sampling error | This one is threshold |

Only the last row is a threshold problem. Escalating global quality to fix any
of the others buys render time and fixes nothing.

## Law 4 — Trace depth is geometry, not quality

Reflection, refraction, transparency and combined depth describe how many
surface interactions a ray is allowed. They are a property of the scene's
topology, not a quality tier. Count the interfaces the ray must cross, then
set the depth. A thick pane costs two interfaces, entry and exit. Stacked
panes multiply.

Combined Depth caps the others. A refraction depth of 8 behind a combined
depth of 4 is a refraction depth of 4. Check combined first, every time.

Prefer material-level and object-level overrides on the one troublesome asset
over raising every depth globally.

## Law 5 — Never read a version number across products

Cinema 4D and Redshift both use a `2026.x` scheme. **The numbers are unrelated.**

| Cinema 4D | Ships with Redshift |
|---|---|
| 2026.1.4 | 2026.2.0 |
| 2026.2.0 | **2026.5.0** |
| 2026.3.x | **2026.7.0** |

The offset is real, it varies, and it is the single most reliable way to get a
Redshift fact wrong. "Live appears in the C4D 2026.2 what's-new page" does not
mean Live shipped in Redshift 2026.2. It means C4D 2026.2 bundled Redshift
2026.5, which had Live since 2026.4.

That exact inference is how the prior reference inverted Live's release date.

Two consequences worth saying out loud:

- **What C4D ships is not what is current.** Installing C4D 2026.3.4 leaves you
  on Redshift 2026.7.0 while 2026.8.1 exists. Redshift updates separately
  through the Maxon App.
- **When the user names a version, ask which product.** "I'm on 2026.3" is ambiguous
  and the two readings are four Redshift releases apart.

## Law 6 — Say when you do not know

The ledger has holes, and they are marked. When a question lands in one:

> "The ledger does not carry that. I can fire scout and verify it against
> Maxon's current docs, or I can give you a [T] starting range to measure."

Do not fill a hole with a plausible number. That is the exact failure that put
several earlier reference documents into recall.

## The sequence

When asked to recommend settings, work in this order. Skipping ahead is how
you end up tuning sampling to fix a topology problem.

1. **Output** — still or animation, delivery resolution and frame rate, AOVs
   needed, who receives the master.
2. **Scene class** — see `references/decision-engine.md`. Extruded logo, glass
   panel, fast flip, slow reveal, camera pan, hero still.
3. **Renderer mode** — Live for interaction, Production Progressive for quick
   confirmation, Production Bucket for anything delivered. Check the Live
   feature-parity table in `references/version-timeline.md` before trusting a
   Live preview of glass or DOF.
4. **Ray topology** — count interfaces, set depths, check combined.
5. **GI architecture** — engine before bounce count.
6. **Sampling** — automatic first. Threshold from the intent band. Manual
   min/max only for DOF and motion-blur diagnosis.
7. **Pathological effects** — fireflies, hot highlights, blur, hair, volumes.
8. **Denoising** — last, after a clean baseline exists. Judge sequences, never
   one frame.
9. **Mac constraints** — memory headroom and hardware ray tracing. See
   `references/mac-metal.md`.
10. **Validate at delivery scale** — full-size master and actual delivery size.

## Reference files

Read the one the question needs. Do not load all four.

| File | Read it when |
|---|---|
| `references/ledger.md` | Any specific number, default, or version fact. **Read this before quoting any figure.** |
| `references/decision-engine.md` | Choosing settings for a shot: scene classes, symptom tables, setting interactions, starting configurations |
| `references/mac-metal.md` | Apple Silicon, unified memory, hardware ray tracing, macOS versions, memory-constrained presets |
| `references/version-timeline.md` | "When did X change", "is this tutorial current", Live feature parity, what a 2024-era workflow maps to now |
| `references/benchmark-protocol.md` | Running measurements, building presets, promoting a [T] range to a measured value |

## Output contract

When the answer is a set of settings, return this shape. It is not a preset
until it has been measured, and saying so protects the user from typing a guess into
a broadcast master.

```
CLASSIFICATION   scene class, still or animation, delivery
MODE             renderer mode, and why
TOPOLOGY         reflection / refraction / transparency / combined depth
GI               primary engine, secondary engine, bounces
SAMPLING         automatic or manual, threshold, min/max if manual
MOTION / DOF     shutter, steps, or off
PATHOLOGY        firefly and highlight controls, if the scene warrants them
DENOISE          engine, and what to check in motion
OUTPUT           format, bit depth, AOVs, colour config
MAC              memory headroom, HWRT on / off / test
---
Every number labelled [V] [D] [P] [T].
TRADEOFFS        what this costs
LEAVE ALONE      settings not to touch unless an artifact appears
IF TOO SLOW      first lever
IF TOO NOISY     first lever
IF IT FLICKERS   first lever
```

For a quick question, answer the question. The contract is for settings
requests, not for "what does combined depth do".

## Register

Explain the mechanism in plain language
before the number, because a setting without a mechanism is a superstition.
Short load-bearing lines. Skip the preamble.

Sports broadcast is the working context: glass and transparent panels,
extruded logos and typography, chrome and clearcoat, bright strip lights on
dark backgrounds, fast flips, slow hero reveals, camera sweeps, key art
stills. When a general answer and a sports-graphics answer differ, give the
sports answer and say why it differs.

## Maintenance

The ledger is only worth what its dates are worth. Every entry carries one.

- An entry older than about three months on a version-sensitive fact should be
  re-verified before it is quoted for a delivery.
- When a new Redshift release lands, read the release notes and update
  `references/version-timeline.md` and any affected ledger rows.
- When a fact fails re-verification, mark it **[R] Recalled** with the date and
  the reason. Do not delete it. A deleted error repeats; a recalled one does not.
