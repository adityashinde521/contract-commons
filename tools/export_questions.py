"""Export the whole question bank to docs/question-bank.csv for expert review.
One row per question, with empty Reviewer status / Comment columns. Run after tools/quiz_types.py."""
import csv, json, pathlib, re, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
Q = json.loads((ROOT / 'src/data/quizzes.json').read_text())
MODS = json.loads((ROOT / 'src/data/modules.json').read_text())
TYPE = {'mc': 'Concept', 'fill': 'Fill the missing logic', 'fix': 'Fix the wrong line', 'order': 'Put steps in order'}
plain = lambda s: html.unescape(re.sub(r'<[^>]+>', '', s))
rows = []
for m in MODS:
    for i, slug in enumerate(m['lessons'], 1):
        for n, q in enumerate(Q.get(slug, []), 1):
            t = q.get('t', 'mc')
            code = '\n'.join(f'{k + 1}: {l}' for k, l in enumerate(q['code'])) if t == 'fix' else q.get('code', '')
            if t == 'order':
                opts, ans = '', '\n'.join(f'{k + 1}. {plain(x)}' for k, x in enumerate(q['steps']))
            else:
                opts = '\n'.join(f'{"ABCDEF"[k]}) {plain(o)}' for k, o in enumerate(q['o']))
                ans = f'{"ABCDEF"[q["a"]]}) {plain(q["o"][q["a"]])}'
                if t == 'fix': ans = f'Wrong line {q["bad"] + 1}; fix: {ans}'
            rows.append([f'{m["n"]}.{i}', slug, f'{slug}-{n}', TYPE[t], plain(q['q']), code, opts, ans, plain(q['e']), '', ''])
out = ROOT / 'docs/question-bank.csv'
with out.open('w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['Unit', 'Lesson', 'ID', 'Type', 'Question', 'Code / lines', 'Options', 'Correct answer', 'Explanation', 'Reviewer status (OK / Fix / Drop)', 'Reviewer comment'])
    w.writerows(rows)
print('exported', len(rows), 'questions to', out.relative_to(ROOT))
