# Behavior Card: {{VERB OR PATTERN NAME}}

> Status: {{proposed | experimental | active | preferred | deprecated}} · Version: {{x.y.z}} · Owner: {{name/role}} · Last reviewed: {{date}}
> Mode: {{new-system | retro-document | extend | ai-states}}  (retro-documented cards carry the label "RETRO-DOCUMENTED: derived from shipped work, not original intent")

A behavior card is the unit of meaning in the system. Write it so a competent stranger could implement the behavior
in a new medium without asking you anything. Delete guidance lines in italics when filling in.

## 1. Meaning
| Field | Entry |
|---|---|
| **Name** | *One short word a team will actually say out loud. Verb, not effect ("Settle", not "Bouncy slide").* |
| **Intent** | *What problem does it solve for the viewer or user? One sentence.* |
| **Brand meaning** | *Why this belongs to this identity. Cite the thesis or source asset it derives from.* |
| **User meaning** | *What state or message it communicates (arrival, cause, completion, uncertainty...).* |
| **Morphology** | *appear / disappear / reposition / expand-collapse / transform / merge-split / reorder / reveal-conceal / assemble / environmental* |
| **Semantic verb family** | *reveal / redirect / confirm / progress / reorganize / emphasize / celebrate / error / loop / exit (or your own owned verb)* |

## 2. Behavior
| Field | Entry |
|---|---|
| **Trigger** | *The event that starts it (pointer, data arrival, navigation, editorial cut, agent state change).* |
| **Primary motion** | *What actually moves or transforms. Origin and destination. Direction logic.* |
| **Physical model** | *Weight, acceleration/deceleration character, damping, overshoot (allowed? how much?), settle.* |
| **Timing** | *Semantic duration class and range, delay, holds, stagger. Numbers come last and live in tokens: reference token IDs.* |
| **Choreography** | *Lead / support / resolve. What enters, follows, overlaps. One focal event.* |
| **Interruption** | *If new input arrives mid-motion: retarget, reverse, cancel, or snap. Velocity inherited? Never "queue".* |
| **Resolution** | *When is it done? What is the stable end state? Where does attention hand off?* |

## 3. Range and context
| Field | Entry |
|---|---|
| **Expression tier** | *Utility / System / Signature / Milestone / Flagship (pick the home tier, then the allowed range).* |
| **Expected frequency** | *Per session / per screen / per shot. High frequency forces restraint.* |
| **Contexts (dialects)** | *Product UI, broadcast, social, event, AI states... and how it changes in each (quieter, faster, bigger).* |
| **Invariants** | *What must stay recognizable in every execution.* |
| **Variables (bounded)** | *What may change, with ranges: intensity, scale, distance, speed, density.* |

## 4. Rules
| Field | Entry |
|---|---|
| **Do** | *2-4 positive rules, each with its reason.* |
| **Do not (anti-rules)** | *2-4 refusals, each with its reason and the escape route ("unless an exception record is approved").* |
| **Reduced motion** | *Strategy (instant / fade / reduce-amplitude / reduce-depth / tighten-spring / remove-repetition / state-only) and what meaning is preserved.* |
| **Instant mode** | *The final state with no travel. Focus, reading order, and announcements must not wait on motion.* |
| **Performance class** | *transform/opacity only / layout-affecting / heavy filter / continuous / runtime-dependent / network asset.* |

## 5. Implementation
| Field | Entry |
|---|---|
| **Token IDs** | *e.g. `semantic.verb.reveal`, `semantic.easing.enter` (never raw values).* |
| **Component mappings** | *Components that consume it and their contract file.* |
| **Platform mappings** | *CSS / WAAPI / SwiftUI / Compose / AE (Essential Property names) / Lottie / Rive. Same meaning, native mechanics.* |
| **Toolkit controls** | *Which parameters a non-specialist sees (name them in the brand's language: "Energy", not "Slider 4").* |
| **Reference examples** | *Links or filenames for 2-3 executions, including one quiet and one at the top of the range.* |
| **Evidence** | *Prototype, test, or critique that justified it. Mark each claim documented / synthesis / inference.* |

## 6. Lifecycle
| Field | Entry |
|---|---|
| **Replaces / replaced by** | *Aliases and migration note if renaming.* |
| **Change log** | *Date, version, what changed, perceptual impact.* |
| **Open questions** | *What is still unknown or unverified.* |
