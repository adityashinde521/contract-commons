import { getCollection, type CollectionEntry } from 'astro:content';
import modulesData from '../data/modules.json';

export type Module = { n: number; slug: string; title: string; tint: string; summary: string; sources: string; lessons: string[] };
export const MODULES = modulesData as Module[];

export const KIND_LABEL: Record<string, string> = { lesson: 'Lesson', 'lab-remix': 'Code lab', 'lab-gui': 'Tool lab', reading: 'Reading' };
export const KIND_CHIP: Record<string, string> = { lesson: 'cc-chip--brand', 'lab-remix': 'cc-chip--cs', 'lab-gui': 'cc-chip--law', reading: '' };
export const TINT: Record<string, string> = { core: 't-core', cs: 't-cs', bi: 't-bi', law: 't-law' };

export const PATHS = [
  { id: 'developer', title: 'Smart contract developer', tint: 'cs', modules: [1,2,3,4,5,6,7,8,9,10,11,12,13],
    text: 'Solidity, testing, security and deployment, ending with a tested capstone on a testnet.', tools: 'Remix, Foundry, Tenderly, Phalcon' },
  { id: 'legal', title: 'Legal-tech analyst', tint: 'law', modules: [1,2,3,4,9,11,12,13],
    text: 'Read and question contracts without writing them: smart legal contracts, MiCA, GDPR, liability.', tools: 'EAS, Safe, Aragon, Accord Project' },
  { id: 'product', title: 'Blockchain product analyst', tint: 'bi', modules: [1,2,3,4,5,9,10,11,12],
    text: 'Process design, cost of trust, token models and on-chain data, ending with a business case.', tools: 'thirdweb, Aragon, Dune, L2BEAT' },
];

export function code(m: number, order: number) { return `${m}.${order}`; }

export async function orderedLessons() {
  const all = await getCollection('lessons');
  const bySlug = new Map(all.map((e) => [e.id, e]));
  const out: { entry: CollectionEntry<'lessons'>; mod: Module; order: number; code: string }[] = [];
  for (const m of MODULES) {
    m.lessons.forEach((slug, i) => {
      const entry = bySlug.get(slug);
      if (entry) out.push({ entry, mod: m, order: i + 1, code: code(m.n, i + 1) });
    });
  }
  return out;
}

/** Split a lesson body ("## Heading" lines + HTML) into steps. */
export function splitSteps(body: string) {
  const steps: { id: string; title: string; html: string }[] = [];
  let cur: { id: string; title: string; lines: string[] } | null = null;
  for (const line of body.split('\n')) {
    const m = /^## (.+)$/.exec(line);
    if (m) {
      if (cur) steps.push({ id: cur.id, title: cur.title, html: cur.lines.join('\n') });
      const title = m[1].trim();
      cur = { id: title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''), title, lines: [] };
      continue;
    }
    const h3 = /^### (.+)$/.exec(line);
    const l = h3 ? `<h3>${h3[1]}</h3>` : line;
    if (cur) cur.lines.push(l);
  }
  if (cur) steps.push({ id: cur.id, title: cur.title, html: cur.lines.join('\n') });
  return steps;
}

export const url = (p: string) => (import.meta.env.BASE_URL.replace(/\/$/, '') + p);
