# Pattern library summary (v0, 2026-10-16)

Six jobs, desktop web, measured live. Full tables, values and gaps go in `DT/patterns/<job>/README.md` when captured (`scripts/shoot.mjs`, `scripts/ui.js`). The Proven option on real work starts here.

| Job | Products | Proven answer | Steps | Open gaps |
|---|---|---|---|---|
| Search + filters | Airbnb, Booking.com, Redfin | Chip row for top filters (1 tap) + full panel with histogram price slider, live-count apply button, text-link reset. | 1 common, 3 any | phone, loading, error |
| List + map | Airbnb, Redfin, Booking.com | Map as a half-width peer of the list when place is the decision; a thumbnail that opens a full map when it isn't. | — | Zillow (bot wall), phone toggle |
| Listing / product detail | Airbnb, DoorDash, Apple | Sticky decision panel; section anchors on scroll; options as tiles with price; inline "unavailable" state with a fix button. | — | gallery, phone |
| Options + add to cart | DoorDash, Apple, Airbnb | Required choices marked; main button carries price and says what's missing; explicit "no" for add-ons. | 3 to cart | cart, checkout, payment (not touched on purpose) |
| Pick dates | Airbnb, Booking.com | Two months side by side; Dates/Flexible tabs; ± days chips; day cells ≥ 44 px. | — | third product, phone |
| Sign in / sign up, first step | Airbnb, Uber, DoorDash | One door, one identifier field, Continue (48 px), social below as secondary. | 1 to code | code step, errors |

Not yet in the library: live tracking, account settings, onboarding beyond step 1, any phone layout. Phone flows would need recordings from a real phone (Claude can't install App Store apps), so phone evidence comes from public pages captured at phone size. Some sites block automated visits (Zillow, DoorDash home in headless); opening them in a visible browser got DoorDash through, not Zillow.
