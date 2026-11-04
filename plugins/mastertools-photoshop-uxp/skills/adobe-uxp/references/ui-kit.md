# UI kit: markup and CSS that survive UXP

UXP renders HTML with its own engine, not Chromium. These were all seen in Premiere 26.5 / Photoshop 27.9 panels.
`assets/template/src/` already follows every rule below.

| Don't | Because (seen) | Do |
|---|---|---|
| `<button>` | Native widget: ignores height/padding, huge rounded pills, overflows a 200 px panel | `<div class="btn">` with click handler |
| `<header>`, `<footer>` | Children laid out side by side instead of stacked | Plain `<div class="header">` |
| `opacity` for disabled | Didn't render on divs | Change colour: `.btn.disabled { color: var(--dim) }` |
| `dblclick` | Unreliable per host | Compare click timestamps (< 450 ms, same row) |
| `window` `focus` for refresh | Rarely fires | Throttled re-scan on `mouseenter` of `body` (3 s) plus a ↻ button |
| `position: sticky`, `display: grid`, `::before/::after { content }` | Unsupported | Flexbox, real `<span>` elements for marks (✓ ✕) |
| `classList.toggle(cls, force)`, `dataset`, `scrollIntoView` | Not guaranteed | `add`/`remove`, `getAttribute("data-i")`, guard `scrollIntoViewIfNeeded` |
| `input type="search"` | Styling ignored | `type="text"`; expect a native-looking field (dark inner box) |
| `innerHTML` with user text | Fine technically, but escapes are on you | Build with `createElement` + `textContent` |

## Theme
```css
:root {
  --bg: var(--uxp-host-background-color, #232323);
  --text: var(--uxp-host-text-color, #d6d6d6);
  --line: var(--uxp-host-border-color, #3a3a3a);
}
body { background-color: var(--bg); color: var(--text); display: flex; flex-direction: column; height: 100vh; margin: 0; }
.list { flex: 1; overflow-y: auto; }
```
`body` needs an explicit `background-color`. Text sizes around 12 px match host panels.

## Layout skeleton
```html
<div class="header"> chip · search · ↻ </div>
<div id="list" class="list"></div>
<div class="footer"> <div class="row"> div buttons </div> <div class="status"></div> </div>
```
- Put `display: block` on footer children explicitly.
- Status lines wrap; if you click by coordinates, re-locate the buttons after a long message (the footer grows).
- Spectrum UXP widgets (`<sp-button>`, `<sp-textfield>`) exist but weren't tested here. Try them in one host before
  relying on them across PS/ID/PR.
