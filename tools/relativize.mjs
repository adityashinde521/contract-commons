// Post-build: make every internal link relative and point directory links at index.html,
// so the site works from any host, any sub-path, and when opened straight from disk (file://).
import { readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { join, relative, dirname, sep } from 'node:path';
const DIST = 'dist';
const walk = (d) => readdirSync(d).flatMap((f) => { const p = join(d, f); return statSync(p).isDirectory() ? walk(p) : [p]; });
const files = walk(DIST);
const fixTarget = (t) => {
  const i = t.indexOf('#'); const hash = i >= 0 ? t.slice(i) : ''; let path = i >= 0 ? t.slice(0, i) : t;
  if (path === '' ) return t;
  if (path.endsWith('/')) path += 'index.html';
  return path + hash;
};
let n = 0;
for (const f of files.filter((x) => x.endsWith('.html'))) {
  const depth = relative(DIST, dirname(f)).split(sep).filter(Boolean).length;
  const root = depth ? Array(depth).fill('..').join('/') : '.';
  let s = readFileSync(f, 'utf8');
  s = s.replace(/(href|src)="\/(?!\/)([^"]*)"/g, (_, a, p) => { n++; return `${a}="${fixTarget(root + '/' + p)}"`; });
  s = s.replace(/href="((?:\.\.?\/)[^"]*?\/)(#[^"]*)?"/g, (_, p, h) => `href="${p}index.html${h || ''}"`);
  s = s.replace(/data-base="[^"]*"/, `data-base="${root}"`);
  writeFileSync(f, s);
}
for (const f of files.filter((x) => x.endsWith('.css'))) {
  const s = readFileSync(f, 'utf8').replace(/url\(\/assets\//g, 'url(./');
  writeFileSync(f, s);
}
console.log(`relativize: ${n} links rewritten`);
