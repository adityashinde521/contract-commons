"""Merge the fill / fix / order questions into src/data/quizzes.json.

Run from the repo root: python3 tools/quiz_types.py
It is safe to run again: items with a type are replaced, concept items are kept.
For list-style "fix" items (statements, not code), the lines are shuffled with a
fixed seed so the wrong line is not always last.
"""
import json, random, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from quiz_types_a import ITEMS as A
from quiz_types_b import ITEMS as B
from quiz_types_c import ITEMS as C
from quiz_more_a import ITEMS as MA
from quiz_more_b import ITEMS as MB
from quiz_more_c import ITEMS as MC
from quiz_more_d import ITEMS as MD

ROOT = pathlib.Path(__file__).resolve().parent.parent
QP = ROOT / 'src/data/quizzes.json'
MODS = json.loads((ROOT / 'src/data/modules.json').read_text())

def is_list(lines):
    return not any(l[:1].isspace() or any(c in l for c in '{};$') or '-->' in l for l in lines)

def main():
    items = {}
    for src in (A, B, C, MA, MB, MC, MD):
        for k, v in src.items():
            items.setdefault(k, []).extend(v)
    lessons = [l for m in MODS for l in m['lessons']]
    missing = [l for l in lessons if l not in items]
    assert not missing, f'no new items for {missing}'
    Q = json.loads(QP.read_text())
    rnd = random.Random(42)
    for slug, new in items.items():
        assert slug in lessons, slug
        for it in new:
            if it['t'] == 'fix':
                assert 0 <= it['bad'] < len(it['code']), slug
                if is_list(it['code']) and not re.search(r'order|wrong place', it['q'], re.I):
                    order = list(range(len(it['code'])))
                    rnd.shuffle(order)
                    it['code'] = [it['code'][k] for k in order]
                    it['bad'] = order.index(it['bad'])
            if 'o' in it:
                assert 0 <= it['a'] < len(it['o']), slug
        old = [q for q in Q.get(slug, []) if q.get('t', 'mc') == 'mc']
        Q[slug] = old + new
    QP.write_text(json.dumps(Q, ensure_ascii=False, indent=1) + '\n')
    n = {t: sum(1 for v in Q.values() for q in v if q.get('t', 'mc') == t) for t in ('mc', 'fill', 'fix', 'order')}
    print(len(Q), 'sets', n)

main()
