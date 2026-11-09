# Broadcast package anatomy

Used by `retro-document` (inventory, step 1 of grammar-and-derivation.md 10) and by rung 11 (toolkit surface)
when the system is a broadcast or streaming graphics package. A package is not a reel of pieces: it is a set of
element families, each shipped in counted variants, opened by people who were not in the room. Inventory it in
that shape before naming verbs, or the thesis gets written from the three pieces you remember.
(Source keys: grammar-and-derivation.md line 7.)

Evidence: **synthesis** of three shipped guides read in 2026 (a US network's 2021 affiliate graphics guide, a
global automotive identity manual, a pro sports team identity guide) plus common broadcast practice. Element
names vary by network; the families do not.

## Contents
1. Element families
2. The variant matrix
3. Dependencies come first
4. Partner guide structure
5. Large-system layers
6. Retro checklist

## 1. Element families

Count every shipped piece into a family. A family nobody can fill is a gap, not a failure.

| Family | Typical elements | What it carries |
|---|---|---|
| Identity | show open, network ID, logo sting, sonic logo | the signature verb at full intensity |
| Segmentation | bumps (in and out), transitions, replay wipes, stingers | rhythm; the most repeated moves in the package |
| Information | lower thirds and keyables (by tier: name, stat, breaking), full-screens, score bug, menus and lineups, tickers | read time and live data; the strictest legibility rules |
| Promotion | promo opens, tune-in, special presentations, end pages | the package selling itself; most variants live here |
| Closing | codas, end slates, credits | resolution; often the least designed family |
| Plates and treatment | backplates, footage treatment (tints, overlays), lower-third plates | the colour system at work behind live video |
| Off-air | square and vertical cut-downs, social lockups, co-branding lockups | the package outside 16:9 and next to partner marks |

## 2. The variant matrix

Each element ships as a product of axes. Write the axes and the count, because the count is what a toolkit,
a QA pass and a partner all need.

- **Axes seen in practice:** colourway (e.g. three gradient pairs), animation style (e.g. two), aspect
  (broadcast 16:9, square, vertical), tier (name / stat / breaking), duration (:05 / :10 / :15), event skin.
- **Count it:** 3 colourways x 2 styles = 6 per aspect; across broadcast and digital = 12 lower-third
  versions. A count of "a few" means nobody knows what ships.
- **Name the switch:** how a user moves along each axis (a precomp toggled on or off, an Essential Property,
  a dropdown control, a separate comp). One switch per axis, the same switch in every element. Mixed switch
  mechanisms across a package are an `observed` inconsistency worth recording.
- **Invariant vs variable:** what never changes across the matrix (curve, logo construction, frame radius)
  is the grammar; what varies (colour, material, place, season) is a dialect. A package re-skinned per event
  keeps the moves and swaps the skin: document the moves as verbs and the skins as modes.

## 3. Dependencies come first

The first failure a partner hits is a project that will not open cleanly. A partner guide's first page lists:

- Fonts: family, weights used, where to license or activate them.
- Third-party plugins: name, version, whether it is paid, which elements need it. Elements that need a paid
  plugin are a toolkit risk; mark them and offer a fallback where one exists.
- Host version and project settings: AE version saved from, colour depth, working space, frame rate.
- What to do when something is missing (which error means which dependency).

Map these to the asset registry's `dependencies` field (contracts-and-specs.md 8).

## 4. Partner guide structure

Order that works for affiliates, vendors and new hires, each page in the system's language:

1. **Touchstones:** 3-6 named attributes, one line each, that a reviewer can test a piece against.
2. **Dependencies** (section 3).
3. **Colour system:** text roles (primary, secondary), background roles, how gradients or tints combine
   with footage. Values come from the token file; the guide references them.
4. **Type:** families, roles, sizes per format, what never gets typed in another face.
5. **One page per element family:** purpose, the variant matrix, how to switch, what to edit (text, data,
   colourway), what not to touch (protected timing, construction), delivery specs.
6. **Delivery:** codec and alpha per element (keyed elements ship with alpha, e.g. ProRes 4444), frame rates
   per destination, safe areas per format, the colour range the network calls broadcast-legal. For live,
   say which elements hand off to a real-time template system (Vizrt, Chyron and the like) and what the
   operator controls: data fields, tokenised fonts and colours, layered source files. Check every spec
   against the destination's own delivery document; specs differ by network.
7. **Misuse:** what partners most often break, shown, with the fix.

Spec or concept work for a brand you don't work for: label it a personal study, keep the owner's logo,
typefaces and event marks out of anything public, and show it after shipped work, not instead of it.

A guide nobody's workflow touches is a guideline museum: pair the guide with toolkit controls (rung 11).

## 5. Large-system layers

Bigger identities add layers a package should at least decide on, even as `not yet`:

- **Layered layout system:** fixed layers (logo zone, safe frame) vs free layers (image, type), stated per format.
- **Sub-brands and dialects:** how a show, event or region inherits the core and what it may change.
- **Sonic logo and coupling:** the audio signature, its lengths, and which visual event it locks to. Then state
  how sound and motion relate across the package (CMP C12): synchronized (a transient drives timing; define sync
  points and a tolerance window), complementary (sound matches the motion family's energy without dictating
  frames), independent (a parallel identity layer), reactive (both respond to data; say which leads when signals
  compete), and silence-safe (meaning survives with no sound, which every element needs for autoplay, social and
  public screens). A shared vocabulary helps (pulse, attack, release, density, resonance, sustain, silence); the
  visual mappings, e.g. sharp transient to a short high-acceleration entrance, are a synthesis, not a standard.
  motion-critique checks the hit frame (SKILL.md, sync to the settle). For product events with audio or haptics,
  see ai-state-motion.md.
- **Co-branding:** lockup rules with partner, sponsor or league marks; clear space; who leads.
- **Rallying line:** a short verbal motto some systems pair with the visual identity; voice belongs with copy, not here.

## 6. Retro checklist

- [ ] Every shipped piece counted into a family; empty families listed
- [ ] Variant matrix per family with axes, counts and the switch mechanism
- [ ] Invariants vs variables written; variables mapped to modes or dialects
- [ ] Dependencies page drafted from the project files (fonts, plugins, versions), `observed`
- [ ] Delivery page: codec and alpha, frame rates, safe areas, legal range, real-time handoff, `observed`
      from the shipped files where possible
- [ ] File hygiene shown: project structure, naming standard, template docs a stranger could follow
- [ ] Gaps the package never faced marked `designed-now`: vertical and square, long names and live data,
      localization, reduced flashes, partner co-branding
- [ ] Toolkit maturity named (contracts-and-specs.md 7) and the step to the next level
