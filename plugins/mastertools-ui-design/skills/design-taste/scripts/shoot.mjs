// Screenshot pages with headless Chrome over the DevTools protocol (no packages).
// usage: node shoot.mjs <outdir> <date> <width>x<height> <id>=<url> [<id>=<url> ...]
import { spawn } from 'node:child_process';
import { writeFileSync, mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
const [outdir, day, vp, ...jobs] = process.argv.slice(2);
const [W, H] = vp.split('x').map(Number);
const mobile = W < 600;
const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  ['--headless=new', '--remote-debugging-port=9333', `--user-data-dir=${mkdtempSync(tmpdir() + '/cdp-')}`, '--hide-scrollbars', 'about:blank'], { stdio: 'ignore' });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
let info;
for (let i = 0; i < 40 && !info; i++) { await sleep(250); try { info = await (await fetch('http://127.0.0.1:9333/json/version')).json(); } catch {} }
const ws = new WebSocket(info.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const pending = new Map();
ws.onmessage = (m) => { const d = JSON.parse(m.data); if (d.id && pending.has(d.id)) { pending.get(d.id)(d); pending.delete(d.id); } };
const send = (method, params = {}, sessionId) => new Promise(r => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
for (const job of jobs) {
  const eq = job.indexOf('='); const name = job.slice(0, eq), url = job.slice(eq + 1);
  const { result: { targetId } } = await send('Target.createTarget', { url: 'about:blank' });
  const { result: { sessionId } } = await send('Target.attachToTarget', { targetId, flatten: true });
  await send('Emulation.setDeviceMetricsOverride', { width: W, height: H, deviceScaleFactor: 1, mobile }, sessionId);
  if (mobile) await send('Emulation.setUserAgentOverride', { userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1' }, sessionId);
  await send('Page.enable', {}, sessionId);
  await send('Page.navigate', { url }, sessionId);
  await sleep(7000);
  await send('Runtime.evaluate', { expression: 'window.scrollTo(0, 40); setTimeout(()=>window.scrollTo(0,0), 300)' }, sessionId);
  await sleep(2500);
  const shot = await send('Page.captureScreenshot', { format: 'png' }, sessionId);
  if (shot.result) { writeFileSync(`${outdir}/${name}_${day}.png`, Buffer.from(shot.result.data, 'base64')); console.log('ok', name); }
  else console.log('fail', name, JSON.stringify(shot.error));
  await send('Target.closeTarget', { targetId });
}
ws.close(); chrome.kill();
