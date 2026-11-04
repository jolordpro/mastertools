// Function checks for a page Claude designed: WCAG AA text contrast and touch-target size.
// Targets are controls (links, buttons, inputs, roles) and any outermost element with cursor: pointer.
// usage: node check.mjs <url-or-file> [ios|android|desktop] [--shot out.png]
//   ios: 390x844, targets >= 44 CSS px (= 44 pt)   android: 412x915, targets >= 48 (= 48 dp)
//   desktop: 1440x900, contrast only (target size is a touch rule)
// Exit code 1 when anything fails, so it can gate. Step counts are checked by hand against patterns.md.
// "taste" holds warnings on common taste variables (type families, filled buttons, serif display headings,
// AI tells), measured on the first screen. They never change pass/fail: fixed rules predict picks worse than the judge.
// --shot saves a full-page PNG for the taste judge.
import { spawn } from 'node:child_process';
import { mkdtempSync, readFileSync, writeFileSync } from 'node:fs';
import { resolve } from 'node:path';
import { tmpdir } from 'node:os';
const argv = process.argv.slice(2);
const si = argv.indexOf('--shot');
const shot = si >= 0 ? resolve(argv.splice(si, 2)[1]) : null;
let [target, mode = 'ios'] = argv;
if (!/^https?:|^file:/.test(target)) target = 'file://' + resolve(target);
const VP = { ios: [390, 844, 44], android: [412, 915, 48], desktop: [1440, 900, 0] }[mode];
// Port 0 lets Chrome pick a free port, so several checks can run at once.
const profile = mkdtempSync(tmpdir() + '/dtcheck-');
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new', '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
let info;
for (let i = 0; i < 60 && !info; i++) {
  await sleep(250);
  try {
    const port = readFileSync(profile + '/DevToolsActivePort', 'utf8').split('\n')[0];
    info = await (await fetch(`http://127.0.0.1:${port}/json/version`)).json();
  } catch {}
}
if (!info) { chrome.kill(); console.error('check.mjs: Chrome did not start'); process.exit(2); }
const ws = new WebSocket(info.webSocketDebuggerUrl); await new Promise(r => ws.onopen = r);
let id = 0; const pending = new Map();
ws.onmessage = (m) => { const d = JSON.parse(m.data); if (d.id && pending.has(d.id)) { pending.get(d.id)(d); pending.delete(d.id); } };
const send = (method, params = {}, sessionId) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
await send('Emulation.setDeviceMetricsOverride', { width: VP[0], height: VP[1], deviceScaleFactor: 1, mobile: mode !== 'desktop' }, sessionId);
await send('Page.navigate', { url: target }, sessionId);
await sleep(3000);
const probe = `(() => {
  const MIN = ${VP[2]}, W = ${VP[0]};
  const parse = (c) => { const m = c.match(/rgba?\\(([^)]+)\\)/); if (!m) return null; const p = m[1].split(/[ ,\\/]+/).filter(Boolean).map(Number); return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 }; };
  const lum = ({ r, g, b }) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b); };
  const blend = (top, under) => ({ r: top.r * top.a + under.r * (1 - top.a), g: top.g * top.a + under.g * (1 - top.a), b: top.b * top.a + under.b * (1 - top.a), a: 1 });
  const bgOf = (el) => { const layers = []; for (let e = el; e; e = e.parentElement) { const cs = getComputedStyle(e); if (cs.backgroundImage !== 'none') return null; const c = parse(cs.backgroundColor); if (c && c.a > 0) { layers.push(c); if (c.a >= 1) break; } } let base = { r: 255, g: 255, b: 255, a: 1 }; for (const l of layers.reverse()) base = blend(l, base); return base; };
  const fails = [], unknown = [];
  let checked = 0;
  for (const el of document.querySelectorAll('body *')) {
    if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
    const r = el.getBoundingClientRect(); const cs = getComputedStyle(el);
    if (!r.width || !r.height || cs.visibility === 'hidden' || +cs.opacity === 0) continue;
    const bg = bgOf(el); const fgRaw = parse(cs.color);
    const label = el.textContent.trim().slice(0, 30);
    if (!bg || !fgRaw) { unknown.push(label); continue; }
    const fg = blend(fgRaw, bg);
    const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + 0.05) / (Math.min(L1, L2) + 0.05);
    const px = parseFloat(cs.fontSize), bold = +cs.fontWeight >= 700;
    const need = (px >= 24 || (px >= 18.66 && bold)) ? 3 : 4.5;
    checked++;
    if (ratio < need) fails.push({ text: label, ratio: +ratio.toFixed(2), need });
  }
  const small = [];
  // Targets: real controls, plus anything styled as tappable (cursor: pointer), such as a div row with a click handler.
  // Pointer is inherited, so only the outermost pointer element counts, and nothing inside a real control.
  const CONTROL = 'a,button,input,select,textarea,[role=button],[role=link],[role=tab],[role=checkbox],[role=switch],[tabindex]:not([tabindex="-1"])';
  // Inside a real control means inside a link, button or input; a focusable container (tabindex) doesn't hide its rows.
  const INSIDE = 'a,button,input,select,textarea,[role=button],[role=link],[role=tab],[role=checkbox],[role=switch]';
  const ptr = (e) => e && e.nodeType === 1 && e !== document.body && e !== document.documentElement && getComputedStyle(e).cursor === 'pointer';
  const shown = (e) => { const cs = getComputedStyle(e); return cs.visibility === 'visible' && +cs.opacity !== 0; };
  const targets = new Set([...document.querySelectorAll(CONTROL)].filter(shown));
  for (const el of document.querySelectorAll('body *')) if (ptr(el) && !ptr(el.parentElement) && !el.closest(INSIDE) && shown(el)) targets.add(el);
  let tapTargets = 0;
  if (MIN) for (const el of targets) {
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    tapTargets++;
    if ((el.tagName === 'A' || !el.matches(CONTROL)) && getComputedStyle(el).display === 'inline' && el.closest('p,li')) continue; // inline text links are exempt (WCAG 2.5.8)
    if (Math.min(r.width, r.height) < MIN) small.push({ el: (el.innerText || el.getAttribute('aria-label') || el.tagName || '').trim().slice(0, 30), w: Math.round(r.width), h: Math.round(r.height) });
  }
  // Taste warnings, first screen only. Wrapped so a failure here can never change pass/fail.
  let taste;
  try {
  const H = innerHeight, inView = (r) => r.bottom > 0 && r.top < H && r.width && r.height;
  const visible = (el, r) => { const cs = getComputedStyle(el); return inView(r) && cs.visibility !== 'hidden' && +cs.opacity !== 0; };
  const families = new Set(); let caps = 0; const serif = []; let filled = 0;
  const pageBg = parse(getComputedStyle(document.body).backgroundColor) || { r: 255, g: 255, b: 255, a: 0 };
  for (const el of document.querySelectorAll('body *')) {
    if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
    const r = el.getBoundingClientRect(); if (!visible(el, r)) continue;
    const cs = getComputedStyle(el);
    const stack = cs.fontFamily.toLowerCase();
    families.add(stack.split(',')[0].replace(/["']/g, '').trim());
    const ls = parseFloat(cs.letterSpacing) || 0;
    if (cs.textTransform === 'uppercase' && ls >= 0.05 * parseFloat(cs.fontSize)) caps++;
    const big = /^H[1-3]$/.test(el.tagName) || parseFloat(cs.fontSize) >= 28;
    if (big && /(^|,)\\s*serif\\s*$/.test(stack)) serif.push(el.textContent.trim().slice(0, 30));
  }
  for (const el of document.querySelectorAll('a,button,[role=button]')) {
    const r = el.getBoundingClientRect(); if (!visible(el, r) || !(el.innerText || el.textContent || '').trim()) continue;
    const c = parse(getComputedStyle(el).backgroundColor);
    if (c && c.a > 0.5 && Math.abs(lum(c) - lum(pageBg.a ? pageBg : { r: 255, g: 255, b: 255 })) > 0.05) filled++;
  }
  const notes = [];
  if (families.size > 2) notes.push('type: ' + families.size + ' font families on the first screen');
  if (filled > 2) notes.push('calm: ' + filled + ' filled buttons on the first screen; one clear next step reads calmer');
  if (serif.length) notes.push('serif: serif display headings (' + serif.length + '); check they suit the job');
  if (caps >= 3) notes.push('chrome: ' + caps + ' letter-spaced ALL-CAPS labels (template chrome)');
  taste = { font_families: [...families], filled_actions_first_screen: filled, serif_headings: serif, caps_labels: caps, notes };
  } catch (e) { taste = { error: String(e).slice(0, 120), notes: [] }; }
  return JSON.stringify({ taste, checked, contrast_fails: fails, contrast_unknown: unknown.length, small_targets: small, min_target: MIN || null, targets_checked: MIN ? tapTargets : null,
    target_warning: MIN && !tapTargets ? 'no tap targets found: build tappable rows and cards as buttons or links (or cursor: pointer) so their size can be checked' : null, overflow_x: Math.max(document.documentElement.scrollWidth, document.body ? document.body.scrollWidth : 0) > W, page_width: document.documentElement.scrollWidth });
})()`;
const res = await send('Runtime.evaluate', { expression: probe, returnByValue: true }, sessionId);
const out = JSON.parse(res.result.result.value);
if (shot) {
  const { result: m } = await send('Page.getLayoutMetrics', {}, sessionId);
  const size = m.cssContentSize || m.contentSize;
  const h = Math.min(Math.ceil(size.height), 6000);
  const { result: img } = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true, clip: { x: 0, y: 0, width: VP[0], height: h, scale: 1 } }, sessionId);
  writeFileSync(shot, Buffer.from(img.data, 'base64'));
  out.shot = shot;
}
ws.close(); chrome.kill();
const pass = !out.contrast_fails.length && !out.small_targets.length && !out.overflow_x;
console.log(JSON.stringify({ target, mode, pass, ...out }, null, 2));
process.exit(pass ? 0 : 1);
