# Canon (v0, 2026-10-16)

What top shipped products do, measured live on desktop web on 2026-10-16 (DT/patterns/). Each principle names its products. **Strength** = how many independent products showed it. One-source principles are candidates, not canon, until a second product confirms them. Mainstream apps redesign often: re-measure in calibrate mode.

| # | Principle | Products | Strength |
|---|---|---|---|
| 1 | **Keep the deciding thing in view.** The booking card, product image or cart stays put while the page scrolls. Price and main action never scroll away. | Airbnb listing (sticky 373 px card), Apple buy page (sticky image), DoorDash store (sticky menu and cart) | 3 |
| 2 | **The main button names the outcome and the number.** "Show 1,000+ places", "See 2,346 homes", "Add to cart – $6.33". | Airbnb, Redfin, DoorDash | 3 |
| 3 | **Empty and error states name the cause and offer the fix as a button.** "No exact matches" + "Remove price filter"; unavailable dates + "Change dates". | Airbnb (two states) | 1 |
| 4 | **A blocked button says what is missing instead of going grey.** "Make 1 required selection – $6.33". | DoorDash | 1 |
| 5 | **Top tasks one tap, the rest one panel away.** Common filters as chips outside the panel; the full set in a panel with a live count. Booking's always-open sidebar is the dense extreme. | Airbnb, Redfin (Booking as contrast) | 2 |
| 6 | **Show the shape of the data inside the control.** Price filter as a histogram slider. | Airbnb, Redfin | 2 |
| 7 | **One loud action per view; the rest stay quiet.** Reset as a text link left, primary filled right; social sign-in as grey secondary under a near-black Continue. | Airbnb, Redfin, Uber | 3 |
| 8 | **One door for sign-in and sign-up, one identifier first.** "Log in or sign up", "What's your phone number or email?", then Continue. | Airbnb, Uber (DoorDash splits them) | 2 |
| 9 | **Offer a flexible path where precision is a burden.** Dates / Flexible tabs and ± days chips; two months side by side. | Airbnb, Booking | 2 |
| 10 | **Required add-ons include an explicit "no".** Choose "No AppleCare" rather than a hidden default. | Apple | 1 |
| 11 | **A narrow type system.** One family, 2–3 weights, body 14–17 px, about 6 sizes in view. Apple 400/600; Redfin 400/700; DoorDash 500/700/800; Airbnb 400/500/700. | Apple, Redfin, DoorDash, Airbnb, Booking | 5 |
| 12 | **Near-black text with one grey for secondary,** not pure black. #222 / #6C6C6C (Airbnb), #1D1D1F (Apple), #191919 / #606060 (DoorDash), #131313 / #4F4F4F (Redfin). | 4 products | 4 |
| 13 | **Touch targets are a touch rule.** 44 pt (iOS) and 48 dp (Android) on touch layouts. Desktop products routinely go below (35 of 62 Airbnb controls in view, 40 of 56 Booking, 83 of 99 Redfin). Day cells in date pickers stay at or above 44 (Airbnb 52, Booking 40x44). | Apple HIG, Material 3 (floors); measured products | floor |

## Sources still to read (free only)
- Platform guidelines: Apple HIG, Material 3 (P29, P30, captured 2026-10-16).
- Open design systems: Base Web (Uber), Primer (GitHub), Carbon (IBM), Polaris (Shopify), USWDS. Read their own pages for the "why".
- Designers in their own words: Airbnb, Uber, DoorDash engineering and design blogs.
- Crafted and Expressive lanes are not yet in the canon. Expressive principles never lead.

## Not canon
- Load-time promo or sign-in pop-ups (Airbnb, Booking) serve the business, not the task. See anti-patterns.
- Any single year's visual trend.
