---
id: canon-broadcast-graphics
title: Canon, on-air broadcast graphics in live sports
type: canon
aliases: [sports graphics canon, score bug canon, lower third canon, broadcast package exemplars, on-air graphics exemplars]
tags: [canon, broadcast, sports, score-bug, lower-third, data-graphics, packages]
related: [broadcast-standards, motion-principles, hierarchy-focal-point, clutter-peripheral, attention-saliency, value-contrast, color, gestalt, grids-layout, typography, accessibility-legibility, scale, unity-variety, negative-space, depth-space, reframing, sports-action, genre-checklists, fluency-complexity]
evidence: exemplars are documented by studios, networks and trade interviews (DOC) or read after the fact by others (RETRO). Frame-level structure is often not documented; each entry says what is.
updated: 2026-10-20
---

# Canon: on-air broadcast graphics in live sports

## How to read this file
- Scope: score bugs, lower thirds, full-screen stat graphics, matchup boards, player intros, telestration, data graphics, whole packages.
- Every entry has a page URL. No images were downloaded. URLs are pages, not image files.
- Evidence tags: `DOC` = said by the studio, network or a primary record. `RETRO` = analysis by someone else after the fact. Quality tags follow `01-evidence-legend`.
- "Structure" lists what a source states. Anything I could not confirm is marked `[Unverified: reason]`. Where a source gave no position, size or colour, I say so instead of guessing.
- Many trade pages are teasers for videos behind a paywall (SVG PLAY). Those entries are thin on structure by necessity.
- Mechanism ids in backticks are library files. See `broadcast-standards` and `genre-checklists` for the baseline rules this canon builds on.
- Awards check (2026-10-20): 46th Sports Emmys (2025, for 2024 work) Graphic Design Event/Show = NBC, Paris 2024; Specialty = "For Mexico, For All Time" (UFC). 47th (May 26, 2026, for 2025 work) Event/Show = NBA on NBC & Peacock; Specialty = "Believers" (an MLB team feature). The 47th winners come from search-result summaries of Deadline and ESPN's press room; SVG's own recap confirms the NBC win. No Promax/BDA sports page was found, so none is cited.

---

## A. Score bugs and persistent graphics

### BG-01 FOX NFL minimal score bug · Drive Studio for FOX Sports · 2025 (Super Bowl LIX, revised for the 2025 season) · Sports Emmy nominee 2026 (FOX NFL, Event/Show)
- See: https://www.sportsvideo.org/2026/06/09/designing-the-modern-scorebug-how-broadcast-graphics-teams-are-rethinking-the-most-important-element-on-screen/
- Structure: DOC: score and clock are protected first; everything else is built around them. Boxed elements were dropped for type on a lighter backing (backing described as gradient-based in a NewscastStudio summary; `[Unverified: page blocked, search summary only]`). Team logos replaced letter codes by the next season. Custom face derived from the FOX logo carries the brand. Position, size and colour are not stated in the sources.
- Why it works: the design removes decoration so the game "disappears and returns" (Hartley's framing), which is `hierarchy-focal-point` and `clutter-peripheral` applied to a persistent element. Brand lives in the letterforms, not in plates, so the bug stays small (`typography`, `broadcast-standards`).
- Push move: let the type carry the brand and remove the plate. Replace letter codes with logos for faster team recognition (`gestalt`: logos group faster than three-letter strings `[Infer]`).
- Evidence: DOC (Hartley and DiNapoli in SVG interview, paraphrased) `[Practice]`. The debut drew mostly negative social reaction, which also shows what changing a learned anchor costs (see BG-05).

### BG-02 NBA on NBC and Peacock package, bug and inserts · NBC Sports with loyalkaspar and Tendril Studio · 2025-26 season · Sports Emmy winner 2026 (Event/Show)
- See: https://www.sportsvideo.org/2026/04/09/newstalgia-an-in-depth-look-at-how-the-return-of-the-inba-on-nbc-i-was-driven-by-a-bold-and-ownable-graphics-package/ and https://www.loyalkaspar.com/nbaonnbc and https://www.sportsvideo.org/2026/06/09/designing-the-modern-scorebug-how-broadcast-graphics-teams-are-rethinking-the-most-important-element-on-screen/
- Structure: DOC: a medallion-based logo system covers all 30 teams and their uniform combinations (more than 120 variations) at one consistent logo size, so the score bar never rescales. Flat colour, no gradients or layered treatments, so team palettes stay stable. Core info snaps into place instead of sliding. A separate secondary "game assist" area holds records and quick stats so the score-and-clock read is untouched. Three-point animation fires from the data feed; the dunk animation is fired by an operator because the feed logs a dunk as a two. Light is the colour activator in the wider brand (loyalkaspar). Bug position and size are not stated.
- Why it works: a fixed container with flexible content gives `unity-variety` without rescaling. Flat swatches keep `value-contrast` predictable across 30 kits. Snap-in motion means no one reads a moving element (`motion-principles`, `attention-saliency`: motion onset captures gaze).
- Push move: normalise the container, vary the content. Build the team medallion so the worst-contrast kit still passes before any animation is added.
- Evidence: DOC (SVG, Hudson interview, paraphrased) `[Practice]`. SVG calls this NBC's third straight win in the category; I could not reconcile that with a search summary that named ESPN's "Toy Story Funday Football" as the 45th Event/Show winner. `[Unverified: third-straight claim conflicts with one search summary]`.

### BG-03 NBA All-Star Weekend LA motif · NBC Sports graphics team (onsite) · Feb 2026
- See: https://www.sportsvideo.org/2026/02/17/nbc-sports-graphics-team-goes-onsite-embraces-l-a-motif-for-nba-all-star/
- Structure: DOC: the regular-season look uses elevated drone-style city views; All-Star switches to street-level views of LA landmarks. Each contest gets a landmark that matches its mechanic: Hollywood sign with shooting stars, Griffith Observatory telescope for the 3-point contest (long range), Venice Beach palms for the dunk contest (height). Player inserts swap the home-city background for LA scenes. Palette and type not stated.
- Why it works: the same insert template changes only its background layer, so the system stays recognisable (`unity-variety`) while each contest gets a distinct meaning (`shape`, `rhythm-pattern`: one break in a pattern is the focal point).
- Push move: map each segment's metaphor to its rule of play, and change only one layer of the template per event.
- Evidence: DOC (SVG) `[Practice]`.

### BG-04 ESPN NHL on ESPN package and bug · ESPN Creative Studio with Elastic · 2021 (year inferred from the Oct 12 first game and the March 2021 rights news)
- See: https://smt.com/inside-the-nhl-on-espn-graphics-package-how-a-brand-new-identity-came-to-be-in-just-six-months/
- Structure: DOC: stacked bug in the top-left, about twice the size of the old one, because phone viewing mattered. NHL shield strengthened to match the replay watermark. A zone to the right shows lower-third-style stats (shots, saves, time on ice, lineups) or ad content. A slide-up/slide-down reveals stats per team. Base palette yellow, black, teal, gray; team colour added per team. Flat 2D logo sits on top of 3D animation so ESPN or ESPN+ branding can be applied separately. Built in Cinema 4D, Octane/Redshift, After Effects. The specific look of EDGE tracking graphics is not described.
- Why it works: bug size was set from the smallest screen, which is `clutter-peripheral` and `scale` applied to delivery. The right-hand stat zone keeps the score block fixed (`broadcast-standards`: consistent positions). Layering a flat logo over 3D keeps `depth-space` decisions out of the brand mark.
- Push move: size the bug from the phone down, then check it on the big screen. Keep the logo as a separate flat layer.
- Evidence: DOC (SVG article reprinted by SMT) `[Practice]`.

### BG-05 CBS NFL score bug left unchanged · CBS Sports · Super Bowl LVIII era (2024) per SVG panel
- See: https://www.sportsvideo.org/2026/06/09/designing-the-modern-scorebug-how-broadcast-graphics-teams-are-rethinking-the-most-important-element-on-screen/
- Structure: DOC: CBS kept the bug the same while overhauling the rest of the package for a Super Bowl. The first social comment was that CBS "didn't change anything". Layout details are not in the source.
- Why it works: the most-seen element becomes a learned anchor (`broadcast-standards`: consistent anchor positions; `fluency-complexity`: easy-to-process stimuli are preferred). Change budget goes to the elements that need to feel new.
- Push move: lock the bug; spend novelty on inserts, transitions and full-screens.
- Evidence: DOC (CBS speaker, paraphrased in SVG) `[Practice]`. Which Super Bowl is described as "two Super Bowls ago" in the article; I did not resolve the exact year.

### BG-06 ESPN Monday Night Football 2015 package · Big Block with ESPN Creative · 2015 · Emmy nominee (Outstanding Live Graphic Design)
- See: https://awn.com/news/big-block-provides-new-graphics-package-espn-s-monday-night-football and https://shootonline.com/?p=133834
- Structure: DOC: the score bug is removed during certain plays so the field is clear. NFL inserts use the full 16:9 frame. Planes of action echo the stacked screens of ESPN's studio; projection mapped on lit panels gives a double-exposure effect. Palette: saturated black, red, blue, white, from the redesigned shield. Over 100 elements, each meant to serve a purpose. Which plays trigger the bug removal is not stated.
- Why it works: live action owns the frame during play; the bug yields (`broadcast-standards`: never cover play-critical areas; `negative-space`). Full-frame inserts get room for hierarchy (`hierarchy-focal-point`).
- Push move: hide the bug during the snap and bring it back on the dead ball.
- Evidence: DOC (AWN trade release, SHOOT release) `[Practice]`.

---

## B. Packages and systems

### BG-07 NBC Paris 2024 Olympics · NBC Sports and Olympics graphics team (art directors Chad Hudson, John Schleef; senior creative director Tripp Dixon) · 2024 · Sports Emmy winner 2025 (Event/Show)
- See: https://www.sportsvideo.org/2025/05/22/2025-sports-emmys-nbc-sports-chad-hudson-wade-echer-on-the-2024-paris-olympic-games/ and https://www.newscaststudio.com/2024/08/12/nbc-olympics-2024-motion-graphics/
- Structure: DOC: credits only (about 60 designers plus named leads). Look per a NewscastStudio summary: fine linear elements, distinct colours, artistic textures, sport pictograms built from clean lines offset with solid geometric shapes, gold glints. `[Unverified: NewscastStudio page returned 403; description from a search summary]`. Placement and hierarchy not documented.
- Why it works: a pictogram family is a repeating unit that gives `unity-variety` across 30+ sports and `rhythm-pattern`. Line plus solid shape gives two value levels inside one icon (`value-contrast`).
- Push move: define one repeating unit (a pictogram built from a fixed line weight and one solid shape) and let every sport inherit it.
- Evidence: DOC for credits and award; RETRO for look `[Unverified: summary only]`.

### BG-08 ESPN NFL package 2019 · ESPN Creative with Man vs. Machine and Big Block · 2019
- See: http://espnpressroom.com/press-release/espn-to-unveil-new-graphics-and-animations-for-monday-night-football-and-nfl-studio-shows/
- Structure: DOC: black-on-black and white-on-white scenes with splashes of team colour and one neon-yellow accent called "venom". Materials: smoke, liquid chrome, "battlemesh" with analog scans. Hand-sculpted show and team logos. One look across every NFL studio show. Score bug and layout are not described in the source.
- Why it works: a neutral value field plus one accent hue keeps team colours as the only other hue, which is `color` (save the strongest hue for the focal point) and `value-contrast`.
- Push move: neutral plate, one house accent, team colour as the single guest hue.
- Evidence: DOC (ESPN press release) `[Practice]`.

### BG-09 ESPN College Football 2025-26 system · ESPN Creative Studio with Two Fresh (event package, edit toolkits) and Compadre (College GameDay) · 2025
- See: https://www.sportsvideo.org/2026/03/04/svg-gfx-forum-draws-250-industry-pros-to-talk-creative-philosphy-ar-xr-and-future-of-live-sports-graphics/ and https://www.newscaststudio.com/2025/09/19/espn-college-football-branding-design-graphics/
- Structure: DOC (SVG recap, paraphrased): one system for 130+ teams and 100+ games each weekend, planned for a five-season life; drew on helmets, gloves, crowd energy. Covers inserts, animations, clock-and-score, GameDay look (per an SVG session description). Layout, grid and type not documented. The NewscastStudio page was blocked; its title says "two-year overhaul".
- Why it works: the design starts from the worst-case count (130 teams, 100+ games), so every template must work without hand-tuning (`unity-variety`, `grids-layout`).
- Push move: design to the worst-case team count first, then check the best case.
- Evidence: DOC (ESPN speakers, via SVG) `[Practice]`.

### BG-10 ESPN College Football Playoff · ESPN Creative Studio, Tendril, Two Fresh · Dec 2024 (12-team package) and later Tendril motion film
- See: https://www.stashmedia.tv/tendril-returns-to-the-college-football-playoffs-for-espn/ and https://www.newscaststudio.com/2024/12/20/espn-college-football-playoff-broadcast-design-score-bug/
- Structure: DOC (Stash): type blurs 2D and 3D, forms a customisable system, and sits above, below and inside the animation. 3D pairs the fast intensity of the play with the movement of the player. Colour not described. Per a NewscastStudio summary: brighter look with glass textures and field lines, silver inserts in early rounds, gold in semifinals and championship, one logo system across ESPN and TNT. `[Unverified: page blocked; summary only]`.
- Why it works: a colour ladder (silver to gold) tells the viewer the stage at a glance without reading (`color`, `hierarchy-focal-point`). Type placed above and below the animation keeps the read zone clean (`typography`, `negative-space`).
- Push move: encode tournament stage in a metal tone that never changes the layout.
- Evidence: DOC (Tendril credits and copy) for type and motion; RETRO for silver and gold `[Unverified: summary only]`.

### BG-11 ESPN College Football 2021 · Elastic for ESPN · 2021 · Network Branding award, 2021 Motion Awards
- See: https://2021.motionawards.com/espn-college-football/
- Structure: DOC: a two-minute CG film (Cinema 4D) on an underground assembly line that tests players and then rises to the field. Each scene was built as a standalone toolkit that cuts into transitions and bumpers. Creative director Paul Mitchell. On-screen score and insert layout not described.
- Why it works: building the opener as a toolkit means every scene is a ready transition, so the look recurs on air (`unity-variety`). Fast cuts and textural detail are staged for impact, not for reading (`fluency-complexity`: trade fluency only in non-read graphics).
- Push move: cut the open into bumpers on day one, so the hero film pays off all season.
- Evidence: DOC `[Practice]`.

### BG-12 Fox College Football toolkit · Gretel for FOX Sports · 2015
- See: https://motionographer.com/2015/08/18/gretels-fox-college-football-package-is-all-kinds-of-smart/
- Structure: DOC: parameter-driven formulas generate the elements, so one change updates the whole package; endpages, title cards and lower thirds are scripted templates with team dropdowns that fill logos, team colours and rankings; a custom After Effects panel. Display face United Sans Heavy with built-in stroke, fill and colour variants. Split-screen motif for head-to-head. Bug and grid not described.
- Why it works: team colour is data, not art, so contrast is checked once per rule, not per team (`color`, `value-contrast`). The split screen is a structural `gestalt` (common region, two halves).
- Push move: make team colour a parameter with a contrast rule attached.
- Evidence: DOC (Motionographer) `[Practice]`.

### BG-13 FOX Sports 1 launch package · loyalkaspar · 2013
- See: https://www.awn.com/news/loyalkaspar-creates-new-id-fox-sports-1
- Structure: DOC: concept "color commentator of sports networks". UScore custom fonts. Slanted bars anchor the type and echo the oblique "1". Cascading walls reveal information and imagery; the wave of a stadium crowd inspired the motion. Talent shown with bold crops. Palette not specified.
- Why it works: one geometric device (a slant angle taken from the logo) structures every plate, which gives `line-direction` and `unity-variety` with no extra decoration.
- Push move: take one angle from the logo and use it for every plate edge and type baseline.
- Evidence: DOC (AWN) `[Practice]`.

### BG-14 Troika hierarchy rules (NBC Sunday Night Football, FSN Final Score) · Troika Design Group · undated trade article
- See: https://www.awn.com/vfxworld/sports-motion-graphics-not-just-numbers-game
- Structure: DOC (Mark Bohman, paraphrased): set a priority order so the eye reads the most important item first, using type scale and style, colour and tone, backing plates and animation together. FSN Final Score packs maximum information into grouped categories with a consistent layout and sidebars that tease stories. On SNF, headshots and lower-third banners share an illumination theme with LED-like type. Article date is not shown. `[Unverified: date missing]`.
- Why it works: four channels (scale, colour, plate, motion) all point at the same item, which is `hierarchy-focal-point`. Grouped categories on a fixed layout are `grids-layout` and `gestalt` (proximity, common region).
- Push move: make the same item win on three channels at once, and nothing else win on any.
- Evidence: DOC (designer quoted in trade article) `[Practice]`.

### BG-15 CBS Sports "Pulse" system · Imaginary Forces for CBS Sports · undated trade article
- See: https://www.awn.com/vfxworld/sports-motion-graphics-not-just-numbers-game
- Structure: DOC: a circular button holds the CBS Eye and NFL logo; one identity flexes across football, golf, basketball and tennis; nearly 400 transitional animations for NFL on CBS alone. Graphics scale to the moment: large over partial or full screen for big beats, small and discreet when they must not block play. Date not shown. `[Unverified: date missing]`.
- Why it works: one round container is a stable anchor for the logo, and the size of a graphic is matched to the moment's importance (`scale`, `broadcast-standards`).
- Push move: write a size ladder (discreet, partial, full) and tie each insert to a rung before design starts.
- Evidence: DOC (producer and creative director quoted) `[Practice]`.

### BG-16 DirecTV NASCAR Hot Pass leaderboard · Reality Check Studios · undated trade article
- See: https://www.awn.com/vfxworld/sports-motion-graphics-not-just-numbers-game
- Structure: DOC (Kory Jones, paraphrased): uses each driver's colours and numbers; the leaderboard shows where a driver stands relative to nearby cars, not only in the full order. Rule stated: graphics augment the broadcast and must fit the director's and producer's workflow or they do not air. Date not shown. `[Unverified: date missing]`.
- Why it works: a window of nearby cars is the data a viewer needs now, so the list is short (`clutter-peripheral`). Driver colour and number are the recognition keys (`gestalt`: similarity).
- Push move: show the neighbourhood of the subject, not the whole table.
- Evidence: DOC `[Practice]`.

### BG-17 NBC golf graphics refresh · NBC Sports Group with Troika/Mission Group · Jan 2019
- See: https://www.nbcsports.com/pressbox/press-releases/nbc-sports-group-rolls-out-innovative-on-air-graphics-refresh-for-live-golf-coverage
- Structure: DOC: brighter, bolder colour; larger lettering and more deliberate type; storytelling devices meant to be quicker to take in on small screens; one look across platforms and programs. Leaderboard layout, tracer and placement are not described.
- Why it works: larger type and fewer decisions per graphic is `typography` and `fluency-complexity` in the direction of small-screen delivery.
- Push move: raise the smallest type size to what reads on a phone, then check the TV.
- Evidence: DOC (press release) `[Practice]`.

---

## C. Data graphics, telestration and live-action integration

### BG-18 Prime Vision with Next Gen Stats (Thursday Night Football alternate stream) · Prime Video · 2022-2025
- See: https://awfulannouncing.com/amazon/prime-video-advanced-stats-thursday-night-football.html and https://www.hashtagsports.com/awards/shortlist-2025/prime-vision-with-next-gen-stats
- Structure: DOC: overlays run on a dedicated All-22 feed and, from 2024, on a high SkyCam angle. Defensive Alerts mark likely blitzers with a red circle; Prime Targets mark open receivers with a green orb. Also route trees, speed, fourth-down guides, field-goal target lines. Real-time tracking data synced with video. One source says the red circle sits around the player, another says under; I could not settle it. Colour-blind cues are not documented.
- Why it works: a ring on a few players is pop-out against a calm field (`attention-saliency`, `hierarchy-focal-point`), and the graphic lives on the player, not on a table (`depth-space`: graphic sits in the scene).
- Push move: mark the decision-relevant player with one colour per meaning, and add a second cue beyond hue (`accessibility-legibility`).
- Evidence: DOC (Prime and awards entry) for features; RETRO (Awful Announcing) for the ring detail `[Practice]`.

### BG-19 Burn Bar · Prime Video NASCAR (senior coordinating producer Alex Strand) · 2025 (Coca-Cola 600)
- See: https://www.televisionacademy.com/features/emmy-magazine/articles/prime-video-peacock-sports-graphics
- Structure: DOC: an AI graphic of each driver's fuel use and efficiency. Built after 18 months of asking teams, fans, drivers and crew chiefs what is least understood about televised racing. A future "Remaining Rubber" tire graphic was floated. On-screen placement and form are not stated.
- Why it works: it picks one hidden variable and makes it visible, so the graphic carries new information (`hierarchy-focal-point`: one idea) rather than repeating the lead.
- Push move: ask what the viewer cannot see, then draw only that.
- Evidence: DOC (Television Academy article) `[Practice]`.

### BG-20 Toy Story and Monsters Funday Football · ESPN Creative Studios with Beyond Sports, Pixar, NFL; Big Studios for rule explainers · 2023 and Dec 2025 · Monsters edition a 2026 Event/Show nominee
- See: https://www.sportsvideo.org/2023/09/29/funday-football-in-andys-room-espn-invites-fans-to-toy-story-themed-alternative-broadcast/ and https://www.beyondsports.nl/news/beyond-sports-receives-three-sports-emmy-nominations-for-monsters-funday-football
- Structure: DOC (Toy Story): NFL Next Gen Stats tracking plus Hawk-Eye optical tracking drive an animated field in Andy's room; the field is a rug; players wear current helmets and uniforms; Big Studios made animated rule explainers. Score display design is not described. A search summary says the Toy Story edition won the 45th Event/Show Emmy. `[Unverified: single search summary]`.
- Why it works: the data is the picture. Tracking becomes animated figures, so there is nothing to read (`fluency-complexity`, `depth-space`).
- Push move: when data is the story, replace the graphic with a world that carries the data.
- Evidence: DOC (SVG, Beyond Sports) `[Practice]`.

### BG-21 Formula One race graphics system · DixonBaxi for Formula One · work 2003-04, article 2014
- See: https://www.blackbookmotorsport.com/features/dixonbaxi_the_business_behind_formula_ones_broadcast_branding/
- Structure: DOC: a 2D grid of squares, one datum per square, with animated graphics fed into the frame. About 300 pre-produced components chosen by the director. Designed for the lowest common denominator, including small black-and-white sets. Inspired by LCD watches and video-game heads-up displays, which show data at the moment it is needed. Telemetry latency in fractions of a second. Type, colour and tower layout are not in this source.
- Why it works: one datum per cell is `grids-layout` and `clutter-peripheral` in the same move, and designing to the worst screen is `accessibility-legibility`.
- Push move: build the system on one datum per cell and test it on the worst screen you can find.
- Evidence: DOC (agency co-founder in Black Book Motorsport) `[Practice]`.

### BG-22 Formula 1 on-air package 2018 · Liberty Media with Wieden+Kennedy · 2018
- See: https://motorsportbroadcasting.com/2018/04/22/analysing-formula-1s-new-on-air-package/
- Structure: RETRO (independent critic): timing wall shows a gained place in green and a lost place in red, and rotates team logos, driver numbers and tyre compounds. Font too small at the Australian GP, fixed from Bahrain; long surnames cramped. Two fonts, one with no broadcast-safe version. A yellow-flag graphic covered the lap counter during Safety Car periods; in China the counter moved to the bottom beside the F1 logo. Dark-red Sauber numbers clash with black.
- Why it works (and where it fails): colour-coded position change is fast to read (`color`, `gestalt`: common fate) but hue-only (`accessibility-legibility`). The flag-over-counter overlap is a layer-priority fault (`broadcast-standards`).
- Push move: give every alert its own reserved zone so two graphics never share pixels.
- Evidence: RETRO `[Practice]`. Author is a broadcast-watching blogger, not a designer.

### BG-23 Formula 1 graphics refresh 2022 · Formula 1 (Dean Locke) · 2022
- See: https://www.motorsport.com/f1/news/first-look-at-f1s-fresher-new-tv-graphics/9098527/ and https://uxdesign.cc/a-design-perspective-on-the-new-and-frustrating-formula-one-tv-graphics-ec0a35c3a761
- Structure: `[Unverified: motorsport.com returned 502 and uxdesign.cc 403; details come from a search summary]`. Summary: logo moved to the top-left; a strip down the left side given more prominence; refresh described as bolder and younger. Critique summary: heavily styled driver numbers hard to read on black; tight line spacing on FIA flag notices; weak repetition causing confusion.
- Why it works (and where it fails): a persistent left strip is a learnable anchor (`broadcast-standards`). Style that beats legibility fails `typography` and `accessibility-legibility`.
- Push move: judge every styled numeral at thumbnail size on its worst background before approving.
- Evidence: RETRO `[Unverified: summary only]`.

### BG-24 Premier League "Field of Play" · DixonBaxi for the Premier League · 2016
- See: https://www.stashmedia.tv/?p=28362
- Structure: DOC: a flexible base described as the canvas, playing field and world that match statistics play out on; live data (tables, charts, player profiles, in-match info) shown in one connected system; vibrant palette, refined type, layouts for hundreds of elements; serves 12+ shows on a 24/7 schedule. Motion rules came from watching hundreds of hours of football for speed, inertia, impact and agility. In-match score placement not described.
- Why it works: motion tied to the sport's physics, not generic easing (`motion-principles`), and one data layer for all shows (`unity-variety`).
- Push move: watch the sport, write four motion behaviours from it, and make every animation use one.
- Evidence: DOC (Stash feature, agency copy) `[Practice]`. Sky and BT use their own scoreboards, so this is a league system, not Sky's on-air look.

### BG-25 Eurosport Tour de France graphics · DixonBaxi · 2018
- See: https://www.designweek.co.uk/issues/9-15-july-2018/dixonbaxi-creates-branding-for-tv-coverage-of-tour-de-france
- Structure: `[Unverified: page returned 403; from a search summary]`. Summary: titles, post-race infographics and a "shrinking picture" layout in which live racing is squeezed back so analysis shares the frame.
- Why it works: the live picture is kept on screen and scaled, not covered (`broadcast-standards`: live action is primary; `reframing`).
- Push move: when a graphic needs real area, shrink the picture into a plate instead of drawing over it.
- Evidence: RETRO `[Unverified: summary only]`.

### BG-26 NASCAR 2025-26 packages · TNT Sports with Big Studios ("Black Octane", 2025); FOX Sports with Big Star (2026)
- See: https://www.newscaststudio.com/2025/06/30/nascar-tnt-sports-broadcast-design-motion-graphics/ and https://www.newscaststudio.com/2026/02/26/fox-sports-redesigns-nascar-graphics-with-bold-type-and-upgraded-data-display
- Structure: `[Unverified: both pages returned 403; search summaries only]`. TNT: dark palette with vibrant accents; running order kept familiar to fans; creative director Jordan Shorthouse called it fast and contemporary with a touch of nostalgia. FOX: centres on the scoring pylon with bolder type.
- Why it works: a dark ground with bright accents suits night races and reds/blues of cars (`value-contrast`); keeping the running order familiar protects the anchor (BG-05).
- Push move: change the skin, not the structure of the order list.
- Evidence: RETRO `[Unverified: summaries only]`.

### BG-27 2023 ESPYS system · loyalkaspar for ESPN Creative Studio · 2023
- See: https://www.brandknewmag.com/?p=25793
- Structure: DOC: bright blue and magenta chosen to avoid sport or team conventions; wavy line patterns; a redrawn "notch" mark that works small and large; silver materials with neon accents; mood dialled down for serious segments. ESPN's Chris Harmon noted that motion that looks moderate on a 20-inch monitor looks much faster on a 70-foot screen.
- Why it works: motion speed was judged at the delivery size, not on the desk (`scale`, `motion-principles`).
- Push move: review motion on the largest and smallest delivery screens, and slow it for the large one.
- Evidence: DOC (Brand Knew mag, paraphrased) `[Practice]`.

---

## What separates exceptional from solid
1. One read is protected, everything else yields. Score and clock are guarded first (BG-01, BG-02), the bug leaves during play (BG-06), and secondary information gets its own zone (BG-02, BG-04). Mechanism: `hierarchy-focal-point`, `clutter-peripheral`.
2. Anchors are fixed and viewers learn them. CBS kept its bug while changing the rest (BG-05); FOX paid a social cost for moving its anchor (BG-01); a flag graphic on the lap counter shows what happens when two graphics fight for one place (BG-22). Mechanism: `broadcast-standards`, `fluency-complexity`.
3. Graphics respect the play. The bug disappears during plays (BG-06), the picture shrinks into a plate (BG-25), markers sit on players, not over the field (BG-18). Mechanism: `broadcast-standards`, `sports-action`.
4. Data is shown as an image tied to the subject, not as a table. Rings on players (BG-18), a neighbourhood leaderboard (BG-16), one datum per cell (BG-21), and a full animated world (BG-20). Mechanism: `attention-saliency`, `gestalt`, `clutter-peripheral`.
5. Plate and colour strategy handles team colour. Fixed medallion and flat colour (BG-02), neutral field with one accent (BG-08), colour as a parameter (BG-12). Mechanism: `value-contrast`, `color`.
6. The package is a system sized to the worst case. 130 teams and 100+ games (BG-09), formula-driven elements (BG-12), open cut as bumpers (BG-11), size ladder (BG-15). Mechanism: `unity-variety`, `grids-layout`.
7. Motion comes from the sport and is staged to be read. Snap-in core info (BG-02), motion rules from watching play (BG-24), speed checked at screen size (BG-27). Mechanism: `motion-principles`, `attention-saliency`.
8. Delivery is designed from the smallest screen. Phone-sized bug (BG-04), small black-and-white TVs (BG-21), small type failures (BG-22), larger type for small screens (BG-17). Mechanism: `accessibility-legibility`, `scale`, `reframing`.

## Solid-but-not-exceptional traps
1. Redesign the bug for brand, lose the anchor. Fix: keep position and reading order; change type and plate only, and test at 10% size (BG-01, BG-05).
2. Meaning carried by hue alone (red/green rings, green/red position change). Fix: add shape, arrow or value difference as a second cue (BG-18, BG-22).
3. Two graphics sharing one zone (flag over lap counter). Fix: give each alert a reserved zone and a priority (BG-22).
4. Small or tightly set type on towers and bugs. Fix: set the minimum size from the phone, test the longest name (BG-22, BG-04, BG-17).
5. Team colour used as a background with no value rule. Fix: a fixed plate or flat swatch with a contrast check per kit (BG-02, BG-12). This one is `[Infer]` from the design logic; the 2023-24 Premier League scoreboard described as using kit colours as backgrounds comes from a fan site, so I did not use it as an exemplar.
6. Texture or 3D behind the data. Fix: keep texture in transitions and full-frame openers; keep read zones flat (BG-04, BG-10, BG-08).
7. The hero open without a toolkit. Fix: cut the film into transitions and bumpers from the start (BG-11, BG-12).
8. Features bolted onto the bug. Fix: design expanded states with the base bug; add only what the operator and data feed can hold under load (BG-01, BG-02). SVG reports that each added feature raises operator workload and failure risk.
9. Motion tuned on a monitor. Fix: review at the largest and smallest delivery size (BG-27).

## Push move candidates
Values marked `[Infer]` are starting points chosen here, not figures from a source.

| Name | When | How | Rung | Exemplars |
|---|---|---|---|---|
| Lock the anchors | Bug or package redesign | List every fixed position (bug, clock, down, tower). Keep position and reading order; change type and plate only. | FIX | BG-05, BG-01, BG-22 |
| Phone-first size check | Any bug, tower, lower third | Size from the phone view; also check at 10% of frame width `[Infer]`. | FIX | BG-04, BG-17, BG-21 |
| Bug leaves the play | Football, any sport with a fixed play window | Fade or slide the bug out at the snap (6 to 10 frames `[Infer]`), restore on the dead ball. | S→W | BG-06 |
| Fixed medallion | Many teams, many kits | One container size for every logo; flat swatches; test the three lowest-contrast kits before animating. | C→S | BG-02 |
| Reserved secondary zone | Records, quick stats, ads | A separate area beside the score block so the score read is never touched. | C→S | BG-02, BG-04 |
| Temporary bug state | Matchups, comparisons | Shrink or reconfigure the bug for about 10 seconds, then restore the base state (value from the SVG interview with LaPlante). | C→S | BG-02 |
| Data-event triggers | Scoring animations | Auto-fire what the feed logs correctly; give the operator a manual trigger for what the feed mislabels (dunks). | C→S | BG-02 |
| Mark the player | Telestration, analytics | One ring per meaning; second cue beyond hue; ring sits on the player, not on the field. | S→W | BG-18 |
| Neighbourhood list | Racing, golf, tables | Show the subject plus the items nearest to it, not the whole order. | C→S | BG-16, BG-21 |
| One datum per cell | Data-heavy full screens | One datum per cell; type size set by the worst screen. | C→S | BG-21 |
| Neutral plate, one accent | Package identity | Black and white field, one house accent, team colour as the only guest hue. | C→S | BG-08, BG-02 |
| Stage colour ladder | Tournaments | Encode round in a tone (silver to gold) that never changes layout. | C→S | BG-10 |
| Worst-case count first | Leagues, conferences | Build templates for the largest team count and weekly game count before the hero shots. | C→S | BG-09 |
| Toolkit-first open | Package launch | Plan every scene as a standalone bumper; deliver as cut-ready clips. | C→S | BG-11, BG-12 |
| Derive motion from the sport | Package motion language | Watch game footage; write four behaviours (for example speed, inertia, impact, agility) and use only those. | S→W | BG-24 |
| Event metaphor per segment | Special events | Map one scenic metaphor to each contest's rule; swap only the background layer of the template. | S→W | BG-03 |
| Draw the invisible | Analytics | Ask what viewers cannot see, then make one graphic for that variable. | S→W | BG-19 |
| Squeeze-back plate | Analysis over live play | Shrink the live picture into a plate and share the frame, instead of covering it `[Unverified: single summary source]`. | S→W | BG-25 |
| Test at delivery scale | Motion on large screens | Preview motion on the largest and smallest screens; slow moves for large LED. | FIX | BG-27 |

## Sources
Checked 2026-10-20. "Read" = page fetched and summarised by the fetch tool. "Summary" = from a web-search result summary only, page not read. "Blocked" = fetch returned an error. The fetch tool returns model summaries of pages, so quoted detail is paraphrase.

Read:
- https://www.sportsvideo.org/2026/06/09/designing-the-modern-scorebug-how-broadcast-graphics-teams-are-rethinking-the-most-important-element-on-screen/
- https://www.sportsvideo.org/2026/04/09/newstalgia-an-in-depth-look-at-how-the-return-of-the-inba-on-nbc-i-was-driven-by-a-bold-and-ownable-graphics-package/
- https://www.sportsvideo.org/2026/05/28/nbc-sports-chad-hudson-on-developing-graphics-for-the-return-of-nba-on-nbc/
- https://www.sportsvideo.org/2026/02/17/nbc-sports-graphics-team-goes-onsite-embraces-l-a-motif-for-nba-all-star/
- https://www.sportsvideo.org/2026/03/04/svg-gfx-forum-draws-250-industry-pros-to-talk-creative-philosphy-ar-xr-and-future-of-live-sports-graphics/
- https://www.sportsvideo.org/2026/03/26/sports-emmys-roundup-with-espn-fox-nbc-nfl-and-prime-video/ (47th nominees: Event/Show, Specialty)
- https://www.sportsvideo.org/2025/05/22/2025-sports-emmys-nbc-sports-chad-hudson-wade-echer-on-the-2024-paris-olympic-games/
- https://www.sportsvideo.org/2023/09/29/funday-football-in-andys-room-espn-invites-fans-to-toy-story-themed-alternative-broadcast/
- https://www.sportsvideo.org/2026/06/04/prime-video-caps-first-nba-season-with-sports-emmy-win-carries-in-house-production-into-wnba-campaign/ (no graphics design detail found)
- https://smt.com/inside-the-nhl-on-espn-graphics-package-how-a-brand-new-identity-came-to-be-in-just-six-months/
- https://www.televisionacademy.com/features/emmy-magazine/articles/prime-video-peacock-sports-graphics
- https://www.hashtagsports.com/awards/shortlist-2025/prime-vision-with-next-gen-stats and https://www.hashtagsports.com/awards/shortlist-2023/tnf-prime-vision-next-gen-stats
- https://awfulannouncing.com/amazon/prime-video-advanced-stats-thursday-night-football.html
- https://www.loyalkaspar.com/nbaonnbc and https://www.loyalkaspar.com/nascar-on-prime (the NASCAR page was read but not used: no on-screen graphics detail)
- https://www.awn.com/news/loyalkaspar-creates-new-id-fox-sports-1
- https://www.brandknewmag.com/?p=25793
- https://www.blackbookmotorsport.com/features/dixonbaxi_the_business_behind_formula_ones_broadcast_branding/
- https://motorsportbroadcasting.com/2018/04/22/analysing-formula-1s-new-on-air-package/
- https://www.stashmedia.tv/?p=28362 (Premier League, DixonBaxi)
- https://www.stashmedia.tv/espn-college-football-playoffs-by-tendril/ and https://www.stashmedia.tv/tendril-returns-to-the-college-football-playoffs-for-espn/
- https://2021.motionawards.com/espn-college-football/
- https://motionographer.com/2015/08/18/gretels-fox-college-football-package-is-all-kinds-of-smart/
- https://awn.com/news/big-block-provides-new-graphics-package-espn-s-monday-night-football and https://shootonline.com/?p=133834
- http://espnpressroom.com/press-release/espn-to-unveil-new-graphics-and-animations-for-monday-night-football-and-nfl-studio-shows/
- https://www.awn.com/vfxworld/sports-motion-graphics-not-just-numbers-game
- https://www.nbcsports.com/pressbox/press-releases/nbc-sports-group-rolls-out-innovative-on-air-graphics-refresh-for-live-golf-coverage
- https://nexusstudios.com/insight/sports-emmys-ufc-two-wins/ (UFC Specialty win confirmed; page gives no design detail, so not an exemplar)

Summary only or blocked (used only where marked `[Unverified]`):
- https://www.newscaststudio.com (several pages, all 403): NBC Paris 2024, Fox NFL 2025 bug, Fox NASCAR 2026, TNT NASCAR 2025, ESPN CFP 2024, ESPN CFB 2025 overhaul, ESPN College Football 2021 Q&A.
- https://uxdesign.cc/a-design-perspective-on-the-new-and-frustrating-formula-one-tv-graphics-ec0a35c3a761 (403)
- https://www.motorsport.com/f1/news/first-look-at-f1s-fresher-new-tv-graphics/9098527/ (502)
- https://www.designweek.co.uk/issues/9-15-july-2018/dixonbaxi-creates-branding-for-tv-coverage-of-tour-de-france (403)
- 47th winners: Deadline https://deadline.com/2026/05/2026-sports-emmys-winners-list-1236921362/ and ESPN press room https://espnpressroom.com/us/press-releases/2026/05/espn-earns-10-sports-emmy-awards-led-by-college-gameday-nfl-live-and-e60/ (search summaries; the official PDF https://theemmys.tv/wp-content/uploads/2026/07/2026-Sports-Winners-v1.9.pdf could not be read).
- SVG sessions on SVG PLAY (CBS Super Bowl LVIII, ESPN MNF AR, NFL roundtable, ESPN NBA 2022-23) are paywalled teasers with no design detail.

Not found (searched, no usable page): any Promax/BDA sports graphics winner page; a Sky Sports current-season Premier League scoreboard case study; OBS Paris 2024 athlete-graphics design detail; current Wimbledon graphics (only a 2011 BBC/IBM item, not used); MLB, NHL (beyond ESPN 2021) and Olympic score-graphic case studies; recent Sarofsky, Brand New School, Possible, Troika sports case-study pages (Elastic's site redirected to makemake.com). The search budget ran out before a regional sports network's 2026 MLB team bug and Motionographer/Creative Review breakdowns could be checked.
