# VERSION TIMELINE — What Changed When

Every row **[V]** against Maxon release notes on **2026-08-20** unless marked.

Purpose: decide whether a tutorial, a habit or a remembered setting still
applies. Redshift shipped nine feature releases in eleven months. A workflow
from a year ago is describing a different renderer.

## Contents

1. Live feature parity — read this before trusting a Live preview
2. The 2026 cycle
3. Cross-product version map — C4D numbers are not Redshift numbers
4. Minimum version history
5. Tutorial-era translation

---

## 1. Live feature parity

**This is the most consequential table in the skill for glass work.**

| Feature | Arrived in Live | Note |
|---|---|---|
| Live itself | **2026.4** | Replaced and discontinued Redshift RT |
| Depth of field | **2026.7** | DOF bokeh in Live |
| **Refraction** | **2026.8** | Live could not render refraction at all before this |
| Trace depths | **2026.8** | Combined, reflection, refraction |
| Transparent shadows | **2026.8** | |

What follows from this, and it is not a small thing: **if the user is running
anything earlier than 2026.8, Redshift Live cannot show them what their glass
does.** Not "shows it approximately" — the feature was absent. Every glass
lookdev decision made in Live on 2026.4 through 2026.7 was made against an
incomplete render.

On 2026.8 or later, Live becomes usable for glass lookdev for the first time.
Still validate in Bucket before delivery, but the preview is now telling the
truth about refraction.

Live also received in 2026.8: reduced shader compile time, better performance
when objects are added, a fix for false out-of-memory reports, and a fix for
manual exposure on macOS. Two of those four are Mac-relevant.

---

## 2. The 2026 cycle

| Version | Date | What landed |
|---|---|---|
| **2026.0.0** | 2025.09 | Dropped Cinema 4D R25 and S26. Distance-unit handling for physically correct lights, volumes and geometry across scene scales. Cloud object. Bump mapping upgraded across shader combinations |
| **2026.1.0** | 2025.10 | Precompiled Metal kernels for macOS Tahoe. Multiple Metal fixes. Light and volume samples on Sun & Sky |
| **2026.2.0** | 2025.12 | **Texture Displacement introduced.** UV Context Projection shader. HWRT back-ends updated. AMD RX 9000 support. Automatic displacement via global render settings |
| **2026.2.1** | 2025.12 | Auto Bump support added to Texture Displacement |
| **2026.3** | 2026.02 | Texture displacement performance. Smooth normals for texture displacement. Numerous displacement fixes |
| **2026.4** | 2026.03 | **Redshift Live added, Redshift RT discontinued.** RS Standard → OpenPBR material conversion in C4D. RenderView auto-detects monitor display profile (OCIO). Per-polygon materials with texture displacement |
| **2026.5** | 2026.04 | Minimum raised to C4D 2026.2. Enhanced auto-bump with displacement nodes. Preliminary UDIM/UVTILE for texture displacement. HWRT startup performance. Experimental HIP RT |
| **2026.6** | 2026.05 | OpenVDB 10.0.1 → 13.0.0. OpenImageIO 2.5.10 → 3.1.11. Material preset rework. Multiple Live stability fixes |
| **2026.7** | 2026.06 | **DOF in Live.** OptiX 9.0 (needs NVIDIA driver 570+). Hex-tile random flip. Revit support. Displacement Blender with texture displacement |
| **2026.7.1** | 2026.06 | Fixes |
| **2026.8.0** | 2026.07 | **Minimum raised to C4D 2026.3.** Live: refraction, trace depths, transparent shadows. Combined/Reflection/Refraction trace depths in Live for C4D. New OCIO config `maxon-cg-v1.0_ocio-v2.4.ocio` with ACES v2.0. Command-line DOF now matches Picture Viewer. Material preview fixed for non-cm document units. Scratches shader. HWRT out-of-memory interactivity fix |
| **2026.8.1** | 2026.08 | Patch, released 12 Aug 2026 (current on 2026-08-20) |
| **2026.9** | 2026.09 | OCIO updated to 2.5.2. Fixed wrong monitor name for a display profile. **[V]** 2026-10-31 |
| **2027.0** | 2026.10 | New device memory architecture: less memory, faster time to first pixel. **[V]** 2026-10-31 |
| **2027.0.1** | 2026.10 | **Current patch on 2026-10-31.** **[V]** |

### Two fixes worth reading twice

**Command-line DOF parity (2026.8).** Before this, the command-line renderer
produced different depth of field from the Picture Viewer. Any farm or batch
output with DOF, rendered before 2026.8, does not match what was approved in
the viewer.

**Material preview with non-cm units (2026.8).** If the document is in inches
or millimetres, material previews were wrong. Broadcast scenes built to
real-world signage dimensions are exactly the scenes that use non-cm units.

---

## 3. Cross-product version map

**The two products share a numbering scheme and nothing else.** All **[V]**,
2026-08-20.

| Cinema 4D | Released | Ships with Redshift |
|---|---|---|
| 2026.0 | 10 Sep 2025 | 2026.0.0 |
| 2026.1.4 | 17 Mar 2026 | 2026.2.0 |
| 2026.2.0 | 15 Apr 2026 | **2026.5.0** |
| 2026.3.0 | 10 Jun 2026 | **2026.7.0** |
| 2026.3.4 | 5 Aug 2026 | **2026.7.0** |
| — | 12 Aug 2026 | 2026.8.1, manual update only |
| 2027 | not yet checked | Not verified. Ledger §11 holds the hole |

The offset runs two to four releases and it varies. Never infer one from the
other.

This map is also the answer to a question that looks like a documentation
contradiction. Cinema 4D 2026.2's feature list describes Redshift Live, which
seems to conflict with Live shipping in Redshift 2026.4. It does not. C4D
2026.2 bundled Redshift 2026.5, one release after Live arrived. Both documents
are correct and the version numbers simply do not line up.

## 4. Minimum version history

| Redshift | Requires |
|---|---|
| 2026.0.0 | C4D 2026.0 (R25 and S26 dropped) |
| 2026.5 | **C4D 2026.2** |
| 2026.8 | **C4D 2026.3** |

Note that Redshift 2026.5 and C4D 2026.2 shipped the same day, 15 April 2026 —
the minimum was raised to the version being released alongside it.

Reaching Redshift 2026.8 means updating separately through the Maxon App.
Installing Cinema 4D and assuming the bundled renderer is current is a common
and quiet way to sit two feature releases behind.

---

## 5. Tutorial-era translation

| If a tutorial says | Read it as |
|---|---|
| "Redshift RT" | Discontinued 2026.4. Replaced by Live, which is a different engine with different controls |
| "RS Standard Material" as the default | OpenPBR is the standard material for new materials in C4D 2026. Conversion from Standard arrived in 2026.4 |
| Displacement without qualification, pre-2025.12 | Predates Texture Displacement. Assumes vertex displacement and its tessellation costs |
| Local samples equations, min/max ratios, "more local than max" | Pre-Automatic Sampling era. Under Automatic Sampling, threshold is the only control on primary sample count |
| Any glass workflow demonstrated in Live before 2026.8 | Refraction was not supported. The demonstration is incomplete |
| Any Live DOF demonstration before 2026.7 | DOF was not supported |
| A C4D version number used to date a Redshift feature | Cross-product inference. Check the map in §3 |
| S26, R25, or earlier documentation | Support dropped in 2026.0.0. Numbers may survive; citations do not |

### When the user shows up with a tutorial

Ask its date and the Redshift version on screen, then check it against this
table before evaluating the technique. A correct technique for 2024 can be a
wrong one now, and the tutorial will not mention that.
