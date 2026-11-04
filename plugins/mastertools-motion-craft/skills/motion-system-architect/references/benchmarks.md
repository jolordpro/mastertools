# Benchmarks: public systems, facts to calibrate against

**as_of: 2026-10-04.** Compiled from the supplied knowledge bases (KB-C Part III/IV, KB-S sec. 29, CMP C24, ADV).
These are calibration points, not prescriptions: copying numbers from another system gives you its numbers, not
its coherence. Use them to sanity-check a proposed scale ("is our long duration out of family?") and to cite
precedent for an architectural choice.

**Verify live before citing publicly.** Volatility column: **L** = stable architecture or historical fact;
**M** = documentation changes occasionally; **H** = early-access, beta, or versioned-spec items that can change
within months. Anything marked H, and any exact number you quote in a portfolio, public article, or interview,
should be re-checked at the primary source (links in the source keys of the KBs) the day you publish. Items marked
"reported by the owner" are self-reported claims, not independent validation.

## 1. Token and timing systems
| System | Fact | Why it matters here | Vol. |
|---|---|---|---|
| **GitHub Primer** | Base durations 0, 50, 100, 200, 300, 400, 500 ms (+600-1000 extended). Functional/semantic: micro 100, short 200, medium 300, long 500. Semantic easing: hover, enter, exit, move. Composite transitions: hover, stateChange, enter, exit. DTCG-style `$value/$type`; Style Dictionary-style pipeline to CSS, docs JSON, Stylelint data. | Best public example of primitive -> functional separation plus a build pipeline | M |
| **Material 3 (Android/Compose)** | Springs named speed x property: fast/default/slow x spatial/effects. Spatial damping 0.9; effects damping 1.0 (no overshoot). Stiffness: fast spatial 1400, fast effects 3800, default spatial 700, default effects 1600, slow spatial 300, slow effects 800. Curve system: 7 easing attributes, 16-step duration scale 50-1000 ms tied to travel area. `MotionScheme` supplies theme-level motion in Compose. Material 3 Expressive adds shape morphing and spring-heavy motion. | The clearest precedent for splitting curve motion from physics motion and for semantic spring naming | M |
| **IBM Carbon** | Durations cited: 70, 110, 150, 240, 400, 700 ms. Productive vs expressive easing families; standard/entrance/exit curves; non-linear dynamic duration (Motion Generator); Stylelint tooling that flags and can autofix non-token values. | Enforcement, plus a tonal range instead of a preset list | M |
| **IBM Design Language** | Productive (efficient, responsive) and expressive (enthusiastic, vibrant) as a weighted range, not UI vs marketing. | Model for expression tiers | L |
| **Atlassian** | Interaction motion roughly 50-150 ms; transition motion roughly 150-400 ms. Event tokens bundle duration + easing + property by component/context (modal enter/exit, popup enter/exit by direction, avatar). Entry/exit asymmetry. Warns against landing focus, errors, or announcements only after motion ends. | Component-semantic token naming; accessibility ordering rule | **H** (documented as early access) |
| **Microsoft Fluent / WinUI** | Standard durations ~83, 167, 250 ms. Duration related to size and distance; stagger for grouped elements; choreography and hierarchy guidance; reduced-motion handling. A Fluent issue documented drift between duplicated token representations. | One canonical source, generated mirrors | M |
| **OpenCRVS** (GitHub issue #12632, opened 2026-05-14) | Migration from scattered CSS transitions to a small set of custom properties sourced from Figma: durations 0/150/250/400/600 ms, easings linear/standard/accelerate/emphasized. Pilot on dropdowns and dialogs; Stylelint validates references; reduced-motion left as an open decision. | Model for incremental rollout and honest open questions | M (issue may evolve) |
| **Shopify Polaris** | Stylelint rules reject hard-coded motion units; intentional divergence allowed with a written disable reason; versioned migration docs. | The exception-with-reason pattern | M |
| **Adobe Spectrum** | Historical micro/macro timing ~130-250 / 300-500 ms; formal machine-readable taxonomy that may run ahead of populated tokens. | Spec maturity is not adoption maturity | M |
| **MUI** | Theme-level transition durations and easings, dynamic duration calculation, reduced-motion configuration. | Runtime theme composition | M |

## 2. Platform accessibility and interaction guidance
| Source | Fact | Vol. |
|---|---|---|
| **Apple HIG / SwiftUI** | Motion should support feedback, status, instruction, agency, context; be brief, purposeful, cancellable. Reduced motion: reduce automatic and repetitive animation; avoid problematic scaling, depth, and blur; prefer fades when relocating objects; tighten springs; do not delete all animation, because removing it can hurt understanding. Supplement visual motion with haptics and audio. SwiftUI springs expose perceptual duration/bounce and preserve velocity across retargeted animations. | M |
| **WCAG 2.2** | 2.3.3 Animation from Interactions (AAA): non-essential interaction-triggered animation can be disabled. Seizure guidance limits flashing (no more than three flashes per second, or below thresholds). `prefers-reduced-motion` is broadly available on the web (MDN, updated June 2026). | L (spec) / M (MDN) |
| **Vestibular research** | Large translations, scaling, depth changes, looping, and multi-axis motion are the main discomfort triggers cited across platform guidance. | L |

## 3. Standards and tools
| Item | Fact | Vol. |
|---|---|---|
| **DTCG Format 2025.10** | Types `duration` (`{value, unit}` ms/s), `cubicBezier`, composite `transition` (duration, delay, timingFunction); aliases, `$deprecated`, `$extensions`. Community Group report, not a W3C Standard. No spring/stagger/sequence types. | **H** (version and status can change) |
| **Style Dictionary** | Config-driven transforms and formatters from token source to platform outputs; the usual build engine. | M |
| **Figma Motion** | 2026 release: timeline, animated components, motion variables with modes, Dev Mode timeline inspection, CSS/JSON/React output, MCP delivery to coding agents. Help docs describe it as open beta / subject to change. | **H** |
| **Adobe After Effects** | Essential Properties, MOGRT export, Responsive Design - Time (documented May 2026). | M |
| **Lottie / dotLottie, Rive** | Lottie: portable authored assets, versioned via CDN. Rive: state machines, runtime inputs. | M |
| **View Transition API** | Widely available in modern browsers since 2025, with compatibility caveats on older environments (MDN). | M |

## 4. Brand and studio systems
| System | Fact | Lesson | Vol. |
|---|---|---|---|
| **BUCK, EA SPORTS FC 24** | Football distilled into trajectory, formation, momentum, match cuts; 1,028 animated compositions packaged in a custom After Effects toolkit with aspect-ratio, color, and type controls; motion guidelines so future partners can extend it. | Domain-derived principles; tool built around likely production variables. The closest precedent for a broadcast-style AE toolkit | L |
| **Studio Dumbar/DEPT, Apple Football Design System** | Customizable "Team X vs Team Y" animation systems producing hundreds of thousands of combinations; daily App Store updates during the tournament. | A strong rule set generates large diversity inside a fixed grammar | L |
| **Studio Dumbar, Instagram / MSI 24 / OpenAI DevDay 2025** | Instagram: physics-first identity; guidelines, templates, toolkits. MSI 24: vendor-scale governance, "Aberration" with multiple states. DevDay: identity from type, motion + sound + interaction. | Governance and vendor usability are part of the identity deliverable | L |
| **Pinterest / DIA** | Identity reorganized around product interaction: pin behavior, collage rhythm, grid. Generative templates, named components, adaptable formats, governed across internal and external teams. | Derive behavior from the product's own interaction model | L |
| **Stack Overflow** | Click, Follow, Snapback with construction rules and explicit "do not" rules (unapproved easing, excess movement, opposing directions, animated body copy, needless cursor rotation). | Small vocabulary + anti-rules | L |
| **Figma (Config 2024)** | Four principles: Shift, Transform, Amplify, Activate; interchangeable motion library for many executions. | Language, not rigid system | L |
| **GitHub Brand Toolkit** | Facilitate, Engage, Impact; container transform, container masking, lateral transitions, enter/exit. | One language across brand and product | L |
| **HSBC** | Opening (hexagon), Advancing, Emulating; expression and speed layers. | Brand foundation -> driver -> verb -> expression -> speed | L |
| **Greenhouse** | Growth metaphor; upward, controlled; exits faster than entrances; no bounce; minimal parallax; no gratuitous 3D. | Anti-rules as first-class | L |
| **Salesforce Kinetics** | Functional, structural, expressive motion roles; coded prototype tuned speed/acceleration/overlap; existing cascade felt too slow in new navigation and was adapted. | Systems supply constraints and intent, not frozen choreography | L |
| **Mastercard, Visa** | Motion + sound + haptics as one sensory system keyed to the payment event; Mastercard reports consumer preference and perceived-assurance findings (reported by the owner, not independent). | The semantic unit can be the event, not the animation | M |
| **Pinterest Gestalt (adoption)** | Adoption measured by scanning Figma files and comparing against recent handoff files rather than counting components. | Measure real use | M |

## 5. How to use this table
- Calibrating a scale: expect utility feedback around 50-150 ms, enters/exits around 150-400 ms, large and rare moves higher and dependent on distance and salience. Broadcast has no input latency to protect, so the same ranges are a starting point only; pace comes from editorial rhythm and frame rate.
- Citing in public: name the system, the fact, and the as_of date; mark H items and self-reported claims; link the primary source.
- Do not present a benchmark as a rule. Say "Carbon documents X; we chose Y because of our thesis."
