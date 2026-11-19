import type { APIRoute } from 'astro';
import { orderedLessons, KIND_LABEL, MODULES } from '../lib/course';
import glossary from '../data/glossary.json';
export const GET: APIRoute = async () => {
  const lessons = await orderedLessons();
  const items = [
    ...lessons.map((l) => ({ t: `${l.code} ${l.entry.data.title}`, s: `${KIND_LABEL[l.entry.data.kind]} · Module ${l.mod.n}: ${l.mod.title}`, k: `${l.entry.data.problem} ${(l.entry.body || '').replace(/<[^>]+>/g, ' ').slice(0, 1500)}`, u: `/lessons/${l.entry.id}/` })),
    ...MODULES.map((m) => ({ t: `Module ${m.n}: ${m.title}`, s: 'Module', k: m.summary, u: `/modules/${m.slug}/` })),
    ...glossary.map((g) => ({ t: g.t, s: 'Glossary', k: g.d, u: `/glossary/#${g.t.toLowerCase().replace(/[^a-z0-9]+/g, '-')}` })),
    { t: 'Setup and safety', s: 'Page', k: 'MetaMask Sepolia faucet wallet recovery phrase', u: '/setup/' },
    { t: 'Capstone: the agentic escrow', s: 'Project', k: 'capstone project team', u: '/capstone/' },
  ];
  return new Response(JSON.stringify(items), { headers: { 'Content-Type': 'application/json' } });
};
