---
id: color
title: Color (hue, saturation, harmony, temperature, relativity)
type: facet
aliases: [colour, palette, color harmony, color scheme, complementary, analogous, triadic, split complementary, color temperature, warm and cool, saturation, chroma, simultaneous contrast, Itten contrasts, Albers, color script, color grading, color psychology, WAVE]
tags: [facet, color, palmer-schloss, albers, itten, evidence-mixed, measurable]
related: [value-contrast, light, depth-space, hierarchy-focal-point, accessibility-legibility, filmmakers]
evidence: strong that preference is learned from object associations and that color is relative; mixed for specific harmony rules.
updated: 2026-10-20
---

# Color

## Quick answer
- Color is relative and secondary to value for structure. `[E-strong]`
- Color preference is mostly learned from objects we like or dislike. `[E-strong]`
- Use a limited palette and save the strongest saturation or hue contrast for the focal point. `[Practice]`

## Definition
- **Hue**: color family. **Saturation / chroma**: intensity. **Value**: lightness (see `value-contrast`).
- **Temperature**: warm (red, orange, yellow) vs cool (blue, green, violet).
- **Harmony schemes**: monochromatic, analogous, complementary, split-complementary, triadic, tetradic.
- **Relativity**: the same color changes appearance with its surround.

## Mechanism and evidence
- Palmer & Schloss 2010, Ecological Valence Theory `[E-strong]`
  - WAVE (Weighted Affective Valence Estimate) explained 80% of variance in average preference across 32 colors; a cone-contrast model explained 37%.
  - Exposure to liked red objects raised red preference.
- Taylor & Franklin 2012: WAVE fit weaker for females (45%) than males (74%). `[E-mixed]`
- Albers 1963: color relativity, one color can look like two, two like one. `[Practice] [Unverified]`
- Itten's seven contrasts: hue, light-dark, cold-warm, complementary, simultaneous, saturation, extension (area). `[Practice] [Unverified]`
- "Warm advances, cool recedes": `[E-mixed]`. Aerial perspective (loss of contrast and saturation, shift toward the sky color) is the more reliable depth cue.
- Ou & Luo and Schloss & Palmer harmony models exist; coefficients not verified here. `[Unverified]`
- Saturation and hue contrast pop out pre-attentively. `[E-strong]`

## Techniques
- `[Practice]` One dominant hue family, one accent. Accent on the subject.
- `[Practice]` Itten's contrast of extension: small area of strong color balances a large area of muted color.
- `[Practice]` Complementary accent (orange skin against teal shadows is a common film grade).
- `[Practice]` Color script: plan color across a sequence to track emotion (Pixar practice).
- `[Practice]` Storaro assigns symbolic meaning to colors across a film. `[Unverified]`
- `[Practice]` Desaturate backgrounds to push them back and lift the subject.
- `[Practice]` Brand colors: check they hold value contrast, not only hue contrast.

## By medium
- Photography: white balance sets temperature mood; mixed sources create color contrast.
- Design: limited brand palette; test in grayscale and for color-vision deficiency.
- Film: grade sets world and emotion; shifts in palette mark acts or perspectives.
- Broadcast: team colors are fixed; keep legibility by managing value, not only hue.
- Motion: color changes over time should follow story beats.

## How to measure
- Convert to CIELAB. K-means palette (5 to 8 clusters) with area shares.
- Hue histogram; saturation (chroma) distribution.
- Subject vs ground ΔE and ΔL*; chroma contrast subject vs ground.
- Harmony template fit (hue templates) as a descriptive note only.
- Color-vision deficiency simulation; check key distinctions survive.

## Failure modes
- Too many saturated hues competing.
- Hue contrast with no value contrast (fails in grayscale and for colorblind viewers).
- Accent color used on a non-focal element.
- Inconsistent white balance across composited elements.

## Critique questions
- What is the dominant hue family, and where is the accent?
- Does the color hierarchy agree with the value hierarchy?
- What mood does the palette set, and does it fit the intent?

## Terms
- hue, saturation, chroma, value, temperature, complementary, analogous, triadic, split-complementary, simultaneous contrast, contrast of extension, color script, grade, LUT, CIELAB, ΔE

## Sources
- Palmer & Schloss 2010; Taylor & Franklin 2012; Albers 1963; Itten 1961; Gurney 2010; Livingstone 2002.
