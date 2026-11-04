# 13: Occlusion by color key (things passing in front of a graphic)

Research snapshot: **2026-10-27**. Scope: a graphic on a surface (a field logo, a floor or wall graphic) that people and objects pass in front of. The broadcast method keys the surface color, so anything that isn't the surface covers the graphic.

Already covered elsewhere, not repeated here:
- Object Matte, Mocha roto, hard and soft mattes, Depth Generator (05).
- Depth models and licenses (composition skill).
- Placing and tracking the graphic (12).

## 1. How broadcast sports does it
**The idea:** treat the surface like a green screen. Draw the graphic only on pixels that look like the surface. Players, the ball and officials don't, so they stay in front.

**Sportvision's 1st & Ten line** (ESPN, late 1990s) [checked 2026-10-27]:
- The system keeps "a palette of colors for the field and another palette for players." Only field-palette pixels change ([Fox News, 2003](https://www.foxnews.com/story/how-the-1st-ten-technology-works)).
- "The colors on the field palette must be changed to compensate for brown mud, white snow, or shadows" (same source).
- Keying ran in **YCbCr**, chosen as the best space for it ([ETHW](https://ethw.org/The_Making_of_Football%27s_Yellow_First-and-Ten_Line)). ETHW dates the launch to the 1997 season; most accounts say 1998. [verify]
- Each camera carried pan, tilt, zoom, focus and extender encoders, and a 3D model of the field placed the line. Program video and audio were delayed "a fixed number of frames" to stay in sync (Fox News).

**The patent detail** (US 6,229,550 "Blending a graphic", Sportvision, filed 1998, expired) ([Google Patents](https://patents.google.com/patent/US6229550B1/en)) [doc]:
- **Inclusions** are colors the graphic may cover. **Exclusions** are colors it must never cover. A pixel that matches both is treated as an **exclusion**. Exclusion wins.
- Each filter is a histogram per channel (Y, Cr, Cb) with a pass band. A pixel matches only if all three channels fall inside.
- Exclusions can also be fixed screen areas, like the game clock.
- **Soft edges:** an "edge fraction" counts how many neighboring pixels are inclusions and not exclusions. That fraction scales the graphic's alpha at the boundary.
- The graphic can be defocused at some zoom levels and fades out between two zoom thresholds.

**Where color keying breaks** [doc]:
- Field color shifts with sun and shadow. A multicolor painted logo can't be covered by a single-color key ([US 8,922,718](https://patents.google.com/patent/US8922718)).
- Crowds and LED boards change every frame, so chroma keys "typically do not achieve good results" there ([US 11,887,289](https://patents.google.com/patent/US11887289), 2024).

**Newer methods** [checked 2026-10-27]:
- **Background history:** warp each frame to a fixed view, record each pixel's color while it's labeled background (≥ 15 frames preferred), then call a new pixel background if its color falls inside that pixel's history. A shell about 5% larger than the history gives soft alpha (US 11,887,289).
- **Learned segmentation:** products like uniqFEED AdApt separate foreground from background with computer vision, no extra hardware ([SVG Europe](https://www.svgeurope.org/blog/technology/adapt-brings-ai-and-machine-learning-to-advertising/); seen in search results only, page not opened). [verify]
- No current Vizrt, Brainstorm or Supponor technical docs on occlusion were found. [verify]

## 2. The AE version
Works when the surface is fairly even in color and the occluders aren't the same color.

### Steps
1. **Track and place** the graphic (12). Its precomp is `GFX`.
2. **Key precomp** `KEY_surface`: the plate, keyed so the **surface is opaque** and everything else is clear.
   - Easiest: duplicate the plate, apply a keyer that keys **out** the surface, then **Invert** the alpha (Invert effect, Alpha, 32 bpc).
   - Restrict it with a mask a little larger than the graphic. The key only needs to work where the graphic is.
3. **Exclusions:** a second key for any surface-like color that must stay in front (a green jersey on grass). Subtract its matte from `KEY_surface`. Exclusion wins, as in the patent.
4. **Clean the matte:** Simple Choker (32 bpc) or Minimax for small holes; Matte Choker (8/16 bpc) for bigger ones. Clip blacks and whites so the open field is a solid 1.0 and players a solid 0.
5. **Apply:** on `GFX`, set **Track Matte → KEY_surface, Alpha** ([Adobe](https://helpx.adobe.com/after-effects/desktop/work-with-transparency-and-compositing/work-with-track-mattes-and-traveling-mattes/track-mattes-and-traveling-mattes.html)). Any layer can be the matte source, and several layers can share one.
6. **Edges:** the plate's own motion blur and defocus already soften the key at player edges. Don't choke the edge hard. Match the matte's softness to plate edges at that depth (11 §8 edge-σ).
7. **Shading on the graphic** (see §3).

### Keyer choice by bit depth
From [Adobe, keying effects](https://helpx.adobe.com/after-effects/desktop/animate-in-after-effects/work-with-keying-effects/keying-effects.html) [checked 2026-10-27]:

| Keyer | Bit depth · use here |
|---|---|
| **Linear Color Key** | 8, 16, 32 · first choice in a 32-bpc project. RGB, hue or chroma matching |
| Keylight 1.2 | not listed on the page [verify] · strongest edges; built for blue/green but takes any screen color |
| Color Range | 8 only · several shades of the surface (sun and shadow) in Lab, YUV or RGB |
| Color Key, Luma Key, Extract | 8, 16 |
| Difference Matte | 8, 16 · needs a clean plate; locked camera only |
| Color Difference Key | 8, 16 · blue/green screens |

- A matte is 0–1 data, so an 8 or 16-bpc keyer inside the key precomp is acceptable [rule]. Keep the key precomp separate so the beauty chain stays 32 bpc (non-negotiable 1).
- Keylight's terms (screen gain, balance, clip black and white) are in 15.

### When to use what
| Situation | Method |
|---|---|
| Even surface, occluders a different color (grass, court, ice, plain wall) | Color key (this file) |
| Surface carries its own logos, lines or patterns | Add their colors as inclusions. With a locked camera, Difference Matte against a clean plate |
| Occluder shares the surface color | Exclusion key, then Object Matte or roto on that occluder (05) |
| Busy surface (crowd, LED board, foliage) | Object Matte or Mocha roto (05). Color keys fail here (§1) |
| People pass at different depths, some in front, some behind | Depth sort (05) |

## 3. Shading: the graphic must take the plate's shadows
- A painted logo sits **under** player shadows. The color key above passes shadowed field as "surface", so the graphic stays fully lit inside the shadow. It reads as floating.
- **Fix** [rule]: multiply the graphic by the surface's shading. Build a shading layer = plate luminance ÷ the unshadowed surface's luminance (a sampled value, or a heavily blurred plate with the shadows painted out), clamp at 1.0, and set it to **Multiply** above `GFX`, clipped by **Preserve Underlying Transparency**. The graphic now darkens wherever the surface does.
- Same idea, finer scale: texture transfer with Displacement Map (11 §7).
- Keep the shadows' color: shadows tint toward the bounce color, never black (11 §7).

## 4. QC [rule]
- **Exaggerate.** View the key with exposure pushed ±2 stops: open field solid, players solid, edges soft.
- **Hunt the edge cases** in motion: shadows, white lines, jersey colors close to the surface, fast limbs.
- **Over time.** The key holds when clouds or light change. If not, keyframe the key color or split the shot.
- **Graphic in shadow.** It darkens with the field.

## Open
- [verify] Keylight 1.2 bit depth in AE 26.x; 1st & Ten launch year; current vendor docs on occlusion (Vizrt, Brainstorm, Supponor).
- A test on a real field plate with a moving shadow, to set the shading layer's clamp and blur.
