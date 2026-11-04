---
id: accessibility-legibility
title: Legibility and accessibility (contrast ratios, color vision, motion)
type: domain
aliases: [WCAG, contrast ratio, color contrast, legibility, readability, accessibility, a11y, colorblind, color vision deficiency, APCA, reduced motion, photosensitivity, text contrast]
tags: [design, accessibility, standard, measurable]
related: [value-contrast, color, typography, broadcast-standards, motion-principles]
evidence: published standards; color vision deficiency prevalence widely documented.
updated: 2026-10-20
---

# Legibility and accessibility

## Quick answer
- WCAG 2.x text contrast: at least 4.5:1 for normal text, 3:1 for large text (AA); 7:1 and 4.5:1 for AAA. `[Standard]`
- Never carry meaning by hue alone; color vision deficiency is common, mostly red-green. `[E-strong]`
- Legibility on screen is luminance contrast plus size plus a quiet background.

## Contrast standards `[Standard]`
- WCAG 2.1/2.2 SC 1.4.3 (AA): 4.5:1 normal text; 3:1 large text (about 18 pt regular or 14 pt bold and up).
- SC 1.4.6 (AAA): 7:1 normal; 4.5:1 large.
- SC 1.4.11: 3:1 for meaningful non-text graphics and UI components.
- Contrast ratio = (L1 + 0.05) / (L2 + 0.05), using relative luminance of the lighter (L1) and darker (L2) colors.
- APCA (Advanced Perceptual Contrast Algorithm) is proposed for the WCAG 3 draft; status not settled. `[Unverified]`

## Color vision `[E-strong]` `[Unverified: exact prevalence rates by population]`
- Red-green deficiencies are the most common, affecting a substantial minority of men (commonly cited near 1 in 12 among men of Northern European descent).
- Test palettes with deficiency simulators; add shape, position or label redundancy.
- Sports implication: team color pairs (red vs green, orange vs teal) may be confusable; separate by value.

## Motion and flashing `[Standard] [Unverified details]`
- WCAG: avoid content flashing more than three times per second.
- Broadcast has its own photosensitive epilepsy guidance (e.g. Ofcom, ITU-R BT.1702). Check before airing strobing graphics.
- Respect reduced-motion preferences in interactive work.

## By medium
- Broadcast: WCAG is a web standard, but its contrast math is a useful proxy for on-air text. `[Infer]`
- Design: check every text and background pair, including text over images at the worst point.
- Motion: check contrast at every frame where text is on screen, not only the hold.

## How to measure
- Compute relative luminance of text color and of the background region behind each text box (use the darkest or lightest local value, not the average, over images).
- Simulate protanopia, deuteranopia, tritanopia; re-run hierarchy checks.
- Flash detection: frame-to-frame luminance change frequency.

## Failure modes
- Mid-gray text on photos.
- Red/green status indicators with no other cue.
- Thin light fonts at small sizes.
- Strobing transitions.

## Critique questions
- Does every text element meet 4.5:1 (or 3:1 if large) at its worst background point?
- Does meaning survive in grayscale and under colorblind simulation?

## Terms
- contrast ratio, relative luminance, WCAG AA, WCAG AAA, APCA, color vision deficiency, protanopia, deuteranopia, tritanopia, photosensitive epilepsy, reduced motion

## Sources
- W3C WCAG 2.1/2.2; ITU-R BT.1702 and Ofcom guidance (not checked this pass).
