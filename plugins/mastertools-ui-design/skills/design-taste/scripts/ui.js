// Inject once per page: defines window.__ui(). Returns design values plus UI facts (headings, primary actions, fields, sticky bars) for what is in the viewport.
window.__ui = () => {
  const vw = innerWidth, vh = innerHeight;
  const vis = (el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && r.bottom > 0 && r.top < vh && r.right > 0 && r.left < vw && cs.visibility !== 'hidden' && +cs.opacity > 0; };
  const fam = {}, size = {}, weight = {}, radius = {}, color = {};
  const bump = (o, k) => { o[k] = (o[k] || 0) + 1; };
  for (const el of document.querySelectorAll('body *')) {
    if (!vis(el)) continue;
    const cs = getComputedStyle(el);
    if ([...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim().length > 1)) { bump(fam, cs.fontFamily.split(',')[0].replace(/["']/g, '').trim()); bump(size, parseFloat(cs.fontSize)); bump(weight, cs.fontWeight); bump(color, cs.color); }
    if (cs.borderTopLeftRadius !== '0px') bump(radius, cs.borderTopLeftRadius);
  }
  const top = (o, n) => Object.entries(o).sort((a, b) => b[1] - a[1]).slice(0, n).map(([k, v]) => `${k}×${v}`).join(', ');
  const btn = [...document.querySelectorAll('button,a,[role=button],input[type=submit]')].filter(vis).map(b => {
    const r = b.getBoundingClientRect(), cs = getComputedStyle(b);
    return { t: (b.innerText || b.value || b.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 32), w: Math.round(r.width), h: Math.round(r.height), bg: cs.backgroundColor, r: cs.borderRadius, fs: cs.fontSize, fw: cs.fontWeight };
  });
  const filled = btn.filter(b => b.bg !== 'rgba(0, 0, 0, 0)' && b.t && b.w * b.h > 1200).sort((a, b) => b.w * b.h - a.w * a.h).slice(0, 4);
  const fields = [...document.querySelectorAll('input:not([type=hidden]),select,textarea')].filter(vis).map(i => { const r = i.getBoundingClientRect(); return `${i.type || i.tagName}:${(i.labels && i.labels[0] ? i.labels[0].innerText : i.placeholder || i.getAttribute('aria-label') || '').trim().slice(0, 24)}(${Math.round(r.height)}h)`; });
  const sticky = [...document.querySelectorAll('body *')].filter(el => { const p = getComputedStyle(el).position; return (p === 'fixed' || p === 'sticky') && vis(el) && el.getBoundingClientRect().width > vw * 0.5; }).map(el => { const r = el.getBoundingClientRect(); return `${r.top < vh / 2 ? 'top' : 'bottom'}:${Math.round(r.height)}h`; });
  const heads = [...document.querySelectorAll('h1,h2,h3')].filter(vis).slice(0, 6).map(h => `${h.tagName}:${h.innerText.trim().slice(0, 40)}(${getComputedStyle(h).fontSize})`);
  const small = btn.filter(b => Math.min(b.w, b.h) < 44).length;
  return JSON.stringify({ url: location.href.slice(0, 100), vp: `${vw}x${vh}`, at: new Date().toISOString().slice(0, 16), fonts: top(fam, 3), sizes: Object.keys(size).map(Number).sort((a, b) => a - b).join(' '), weights: top(weight, 4), radii: top(radius, 5), colors: top(color, 4), heads, primary: filled, fields, sticky: [...new Set(sticky)], controls: btn.length, under44: small });
};
