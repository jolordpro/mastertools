---
id: light
title: Light (direction, quality, ratio, motivation)
type: facet
aliases: [lighting, key light, fill light, back light, rim light, hard light, soft light, high key, low key, chiaroscuro, tenebrism, Rembrandt lighting, motivated light, three-point lighting, light direction, light quality]
tags: [facet, light, cinematography, photography, practice]
related: [value-contrast, color, depth-space, texture-detail, painters, filmmakers, photo-craft]
evidence: practice for mood conventions; strong for brightness and contrast drawing attention and shading giving 3D form.
updated: 2026-10-20
---

# Light

## Quick answer
- Light decides what is seen first (brightest contrast), how solid things feel (shading), and the mood (hard vs soft, high vs low key).
- Put the strongest light-dark junction on the subject. `[E-strong for attention]`
- Light direction and quality are choices of meaning, not only exposure. `[Practice]`

## Definition
- **Direction**: front, side (45° or 90°), back, top, under.
- **Quality**: hard (small or distant source, crisp shadows) vs soft (large or diffused source, gradual shadows).
- **Ratio**: brightness of key side vs shadow side (key-to-fill ratio).
- **Key** (overall tonality): high key (light, low contrast) vs low key (dark, high contrast).
- **Color temperature**: warm vs cool sources (see `color`).
- **Motivation**: whether light appears to come from a source in the scene.

## Mechanism
- `[E-strong]` Shading is a primary cue to 3D shape; the visual system tends to assume light from above. `[Unverified: size of the from-above bias]`
- `[E-strong]` Luminance contrast drives early attention (see `attention-saliency`).
- `[Practice]` Side and back light reveal texture and separate subject from background.

## Techniques
- `[Practice]` Three-point lighting: key, fill, back. The baseline for interviews and studio.
- `[Practice]` Rembrandt lighting: key high and to one side, small triangle of light on the shadow cheek.
- `[Practice]` Chiaroscuro and tenebrism: large darks, focal light (Caravaggio).
- `[Practice]` Motivated single-source naturalism (Deakins), top light hiding eyes for menace or secrecy (Gordon Willis, *The Godfather*). `[Unverified]`
- `[Practice]` Edge or rim light to lift a dark subject off a dark background.
- `[Practice]` Pools of light to guide the eye through a deep set.
- `[Practice]` Golden hour and blue hour for low-angle warm light and soft cool fill.
- Ratios `[Unverified, numbers vary by source]`: about 2:1 reads open and even; 4:1 and above reads dramatic.

## By medium
- Photography: shoot with light raking across texture; use reflectors for fill.
- Film: light the scene for the story beat; plan brightness of the focal area per shot.
- Broadcast studio: even, flattering light for talent; graphics must hold contrast against bright sets.
- Motion design and 3D: a key light and environment set mood; rim lights read clearly at small sizes. In Redshift or similar, render a luminance-only pass to check value structure.
- Design: simulated light (gradients, shadows) should share one consistent direction.

## How to measure
- Luminance map; location of brightest regions vs subject mask.
- Subject vs background mean luminance; local contrast at subject edge.
- Shadow direction estimate from shading gradients (hard; Claude can judge visually).
- Lighting type labels: ShotBench lighting-type and lighting-condition categories give a classifier target.

## Failure modes
- Brightest area on the background, not the subject.
- Flat front light that kills form when form matters.
- Inconsistent light direction across composited elements.
- Unmotivated colored light that breaks the scene's logic (unless stylized on purpose).

## Critique questions
- Where is the brightest junction, and is the subject there?
- What does the light's direction and hardness say about mood?
- Is the light consistent across all elements?

## Terms
- key, fill, back, rim, kicker, hair light, practical, bounce, diffusion, hard, soft, high key, low key, chiaroscuro, tenebrism, Rembrandt, butterfly/Paramount, split, loop, motivated, ratio

## Sources
- Livingstone, *Vision and Art*; Gurney, *Color and Light*; Block, *The Visual Story*; ShotBench taxonomy; American Cinematographer coverage of Deakins, Willis. `[Unverified for practitioner specifics]`
