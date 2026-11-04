# Context dialects

The same motion can be right in one context and wrong in another. Identify the dialect first, then weight the review. State your assumption if the user did not name it.

## Contents
1. Corpus bias warning
2. Product UI
3. Broadcast and brand (opens, stings, lower thirds, packages)
4. AE toolkit, templates and rigs
5. AI and agent states
6. Cross-dialect translation
7. Intensity ladders and multimodal concordance

## 1. Corpus bias warning

The research this skill is distilled from is heavily product-UI and design-system oriented: platform guidelines (Apple, Material, Fluent, Carbon, Atlassian), HCI and perception studies, and software case studies. Studio and broadcast work appears mainly as brand-motion systems and narrative craft (rhythm, holds, anticipation, kinetic type, camera, temporal texture), not as a delivery-specs literature. Therefore:

- The broadcast guidance below mixes corpus-derived craft with standard industry practice from general domain knowledge. The safe-area, flash-limit and legibility points are general broadcast practice, not findings from the research corpus. Verify against the specific network, platform or delivery spec before treating any number as binding.
- Product rules such as "frequent actions should be near instant", "never block the user", and "cancel whenever possible" do not transfer unchanged to a show open or a sting. Their underlying reasoning (repetition cost, attention budget, honesty) does. Reason from that.
- Say plainly when a note is a transfer from product reasoning rather than broadcast evidence.

## 2. Product UI

Priorities, roughly in order:
1. **State truth**: motion must not imply system state that is not confirmed (success before commit, progress with no basis). Acknowledge intent, then show outcome.
2. **Interruption**: users act while motion runs. Retarget or cancel; preserve velocity; never leave stale state.
3. **Latency and agency**: first visible response begins fast enough to feel causal; separate acknowledgement from completion.
4. **Frequency**: duration is a budget spent every use. A small saving repeated hundreds of times can outweigh an impressive one-time flourish. Expression scales inversely with frequency.
5. **Input coupling**: one-to-one tracking while direct, velocity-aware release, thresholds, hysteresis, modality differences (touch, pointer, keyboard).
6. **Layout and content robustness**: real, long and localized content; responsive reflow; retarget to the current destination, not a stale coordinate.
7. **Accessibility**: reduced-motion as a designed branch; motion never the sole channel.
8. **Performance**: frame integrity; transform and opacity are commonly safer than layout-triggering properties, but understand the cost rather than recite a rule.
9. **System fit**: semantic tokens, equivalent actions with equivalent motion, documented exceptions.

Typical notes: entrance easing and exit semantics, scale-aware duration, stagger tax, spring overuse, no reduced-motion branch, no retrigger behavior, motion hiding latency instead of acknowledging it.

Reduced-motion mapping (what must remain):
| Original role | Reduced strategy | Must remain |
|---|---|---|
| Spatial orientation | Immediate state change plus focus/selection cue | Where the user is and what changed |
| Direct manipulation | Less or no travel, keep immediate state feedback | Agency and outcome |
| Decorative flourish | Remove | Nothing, if it was truly decorative |
| Progress | Static percent, text, non-moving indicator | Actual progress |
| Celebration | Concise confirmation, icon, text, haptic/audio if available | Completion meaning |
| Parallax and depth | Flatten layers, opacity-based changes | Hierarchy and context |
| Staggered reveal | Grouped state or controlled focus order | Reading order and availability |

Reduced motion is a stress test: if the interface becomes confusing without animation, find what was encoded only in movement. Scaling, spinning, multi-axis movement, depth simulation, animated blur and peripheral motion are the commonly cited triggers; replace with fades or non-spatial cues when the motion carried meaning, and tighten or remove springs.

## 3. Broadcast and brand

Priorities, roughly in order:
1. **Legibility at distance and on real displays**: type size and weight for a living-room viewing distance, contrast during motion, motion blur not smearing the read, safe areas (SMPTE ST 2046-1, the current HD standard: safe title 90% of the frame, 5% margins, 96 px left at 1920; safe action 93%, 3.5% margins, about 67 px; check the delivery spec, which may differ), aspect ratio crops for social cut-downs.
2. **Read time**: on-screen text needs hold time to be read, not merely seen. Estimate reading time from character or word count plus a floor (subtitle norms as a ceiling: Netflix caps adult subtitles at 20 characters per second, BBC guidance is about 160 to 180 words a minute, roughly 15 cps; viewers splitting attention with live action read slower than subtitle readers); motion during the read window competes with reading. Type motion hierarchy runs block, line, phrase, word, character; as granularity rises the attention cost must be justified. Character-level on long copy is usually a legibility failure. Preserve letterform integrity (stretch and warp can undermine recognition).
3. **Live-data and operator robustness**: on live TV, lower thirds usually run from pre-programmed templates (Vizrt and similar), with the operator taking them in and out; in edits they typically hold 2 to 3 seconds, depending on name length and shot length, then animate off. So aim a "lengthen the hold" note at the template default or the editor, not the animator; it is a fair push back whenever the graphic is not up long enough to read. Also check names, numbers and titles in real lengths; accented and long strings; two-line wraps; what happens when the operator takes it out early or retriggers; what the graphic does on a late or missing data field; no reliance on a perfect first frame.
4. **Photosensitivity and comfort**: avoid rapid luminance flashes and high-contrast patterns across large screen areas; commonly cited broadcast guidance limits flashes to a small number per second (three or fewer is the commonly quoted threshold) and restricts large saturated red flashes and patterns. Check the delivery spec and run the proper analysis tool for anything with strobing, rapid cuts to white, glitch effects, or repeating stripes. This is a safety veto, not a taste note. Also consider vestibular comfort for large-scale camera moves and parallax on big screens.
5. **Sound sync and audio structure**: does the visual hit land on the audio transient, and on the right visual event? A hit should land where the viewer's eye goes, usually when the title or key element settles, not when a secondary layer starts; compare the hit frame with each element's settle frame. Repeated stingers and whooshes across a show also fatigue the ear, so check the audio at repetition tier as well as once. (ITU-R BT.1359-1: offsets become detectable past audio 45 ms early or 125 ms late, and unacceptable past 90 ms early or 185 ms late. Those figures come from lip-sync tests, so treat a 3 to 4 frame late hit at 29.97 as borderline, not as a certain break.) Sound clarifies rhythm and intended feeling. Check sound-off clarity and visuals-minimized structure. Audio that ends long after the visual makes it feel late. Avoid dependency on sound unless it is guaranteed.
6. **Narrative shape**: setup, anticipation, primary event, consequence, hold, resolution; crescendo; match cuts and visual rhyme; premature closure; connective beats. Stings and opens are editorial language, not UI animation. They can and should spend time and expression the way a product control cannot.
7. **Frame rate and temporal texture**: ask for the delivery format before timing notes (1080i59.94, 1080p59.94, 720p, 2160p; field order for interlaced; the network's own safe-area and graphics spec), because frame counts, thin-line twitter and fast-move judder all depend on it. Delivery frame rate versus comp rate, interlacing and field order where relevant (thin horizontal lines and small serifs flicker on interlaced output), judder on pans, stepped or held-keyframe styles as intentional brand physics versus accidental frame-rate mismatch. Reduced frame rate and held keyframes can be a legitimate identity (decisive, graphic, energetic); check that it is applied deliberately and consistently.
8. **Package cohesion and reuse**: a package should read as one family. Strong practice starts from a still frame for each piece (a storyboard or a single style frame each), checks that the stills belong together as a series, then animates; one piece's motion moves and design elements are reused across its versions and cut-downs. Pieces built from scratch under different deadlines drift apart in quality and stop looking related.
9. **No interaction, and screen furniture**: broadcast has no press or feedback loop, so product-UI feedback rules do not transfer, and anything that looks tappable or tactile is usually a distraction unless it is very well made. Safe areas differ sharply from app and social layouts: tickers, scrollers and bugs can cover the lower part of the frame, so key information placed low (as a UI designer might) can disappear under them.
10. **Brand ownership and register**: the distinctiveness test; does it feel like this network, show or brand without a logo; wrong register (too corporate for a sports package, too frantic for a news hour); inconsistency of physical worldview across the package.
11. **Camera and depth**: who moves, object or camera? A camera move has a higher perceptual load; it needs a narrative job. Parallax only if it adds meaning.
12. **Package system fit**: does it sit in the show's rhythm; does it live with neighboring elements (bumpers, lower thirds, transitions); do versions across durations and formats stay in family.

Typical notes: hold too short for the copy; lower third eased like an app toggle; open spends its hero beat on the logo's least interesting move; transition and logo animate at the same intensity so neither is the hero; strobing or flash risk in an impact; sound hit lands 3 frames after the visual; camera shake on top of text; type crushed by motion blur; one-size-fits-all timing for varied name lengths.

Frequency is still real in broadcast: a lower third appears dozens of times per show, a bumper many times per day, a show open weekly. Match expression to repetition tier: the sting played ten times per broadcast should not be a 6-second cinematic moment.

## 4. AE toolkit, templates and rigs

Review the thing as a tool used by other people on content you have not seen.
- **Content robustness**: very short, very long, accented, RTL or multi-line text; different image aspect ratios; missing optional fields.
- **Controls**: are the right parameters exposed, with sane ranges, defaults, and names? Are timing roles (arrive, hold, depart) separable from content duration? Does changing hold length break the exit?
- **Expressions**: do they survive precomping, duplication, renaming, language or locale, and frame-rate changes? Is anything hard-coded to a layer name or index? Does an expression-driven spring or overshoot behave when the keyframes move? Cost per frame.
- **Structure**: naming, layer order, color labels, precomp strategy, guides, notes; can a stranger operate it without opening layers.
- **Timing logic**: speed graph hygiene (consistent influence values, intentional asymmetry), spatial versus temporal interpolation, motion blur settings, work-area and trim for handoff.
- **Render and performance**: effects that dominate render time; 3D or heavy blur where a cheaper approach reads the same; RAM preview versus render difference.
- **Portability**: Lottie/Bodymovin or Rive handoff constraints (supported features, runtime text, sizing, state coverage); a Lottie that cannot react to runtime state is a clip with extra steps.
- **Documentation and variants**: does a family share one physical language; are variants named by meaning.

When asked for notes on keyframes: ask for or read the speed graph. State, per property, where speed peaks, how long the tail is, whether ease in and out are symmetric where they should not be, and whether related properties share a profile when they should (common fate) or deliberately differ when they should not.

## 5. AI and agent states

State language for uncertainty, progress and agency. Distinguish: idle, listening, thinking or processing, streaming, waiting for a human, success, partial, failure, canceled. Motion must not imply certainty, progress or completion the system lacks.
- A state loop (processing, listening, streaming) sustains an ongoing condition; it must not imply measurable progress.
- Interruption: can the user stop or redirect while it runs, and does the visual reflect that truthfully?
- Streaming content: avoid layout shifts that move the text being read; motion at the growth edge should not drag attention from the content already there.
- Review generated motion as generated code: what state model did it assume, what happens on interruption, what content it assumed, accessibility mapping, cost, semantic reason, and whether another person could govern it with named parameters rather than an opaque sequence.
- Generic polish is cheap; the differentiator is semantic grammar and constraints.

## 6. Cross-dialect translation

When a behavior moves between dialects, translate the verb, not the spectacle.
- Brand to product: keep the physical worldview and the signature verb; cut amplitude, duration and concurrency to fit frequency. A campaign reveal becomes a brief identity-shaped transition on a milestone, not on every click.
- Product to broadcast: keep honesty and hierarchy; spend time on read and on narrative beats; decouple from the "instant" ideal.
- AE to runtime: separate what is essential behavior (states, thresholds, retargeting) from what is cinematic embellishment; identify which parts the runtime can express.
- Check that the intensity fits the destination tier of the expressiveness budget.

## 7. Intensity ladders and multimodal concordance

Notification-style intensity should follow importance and persistence:

| Event class | Motion intensity | Pattern |
|---|---|---|
| Passive background update | Near zero | Localized content change or subtle status transition |
| Useful, non-urgent | Low | Small emphasis, badge, ambient update understood later |
| Time-sensitive | Moderate | Persistent, glanceable, with direct action |
| Critical or safety-relevant | High only when necessary | Strong multimodal interruption with clear escape |
| Promotional | Lowest attention cost | Do not hijack motion; preserve user agency |

The same principle in broadcast: a breaking-news sting earns more intensity than a weather bumper; a sponsor tag should not out-shout the content.

Multimodal concordance: channels should agree about what happened, when and how significantly. Visual, haptic and audio carry the same event with matching intensity and sharpness; each channel adds distinct information or is omitted. Audio duration affects perceived timing; haptics are strongest as punctuation at discrete thresholds; sound should reinforce a state that already has visual grounding and be optional where it can be silenced. Audio transients define perceived impact; motion prepares the eye; a haptic grounds it. When channels disagree, the result feels uncanny even if each is polished.

Same-element calibration (the disclosure panel at four levels): L1 specify an entrance; L2 feedback and continuity; L3 gesture coupling, interruption, responsive content, reduced motion and state transitions; L4 a reusable pattern with semantic tokens, guidance, QA, governance, adoption. See scorecard.md.
