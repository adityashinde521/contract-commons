import re, json, os, sys
sys.path.insert(0, 'tools')
from curriculum import MODULES, OLD
from authored_bits import TRY, APPLY
SRC = '/tmp/claude-0/-home-claude/715e66db-0a89-52e0-ab39-75c5c92ddc76/scratchpad/course/'
html = ''.join(open(SRC+f, encoding='utf-8').read() for f in ['p2.html','p3.html','p4.html','p5.html'])
srcs = open(SRC+'p6_src.html', encoding='utf-8').read()
CODE = {m.group(1): m.group(2) for m in re.finditer(r'<script type="text/plain" id="([^"]+)">(.*?)</script>', srcs, re.S)}
arts = {}
for m in re.finditer(r'<article class="lesson[^"]*" data-id="([^"]+)"([^>]*)>(.*?)</article>', html, re.S):
    aid, attrs, body = m.groups()
    a = dict(re.findall(r'data-([a-z]+)="([^"]*)"', attrs))
    tabs = re.findall(r'<section data-tab="([^"]+)">(.*?)</section>', body, re.S)
    arts[aid] = (a, tabs)

def fix(h):
    # code blocks: inline the source
    h = re.sub(r'<div class="pre-wrap"><pre data-src="([^"]+)"></pre><button class="copy" type="button">Copy</button></div>',
               lambda m: '<div class="pre-wrap"><pre><code>'+CODE[m.group(1)].replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')+'</code></pre><button class="copy" type="button">Copy</button></div>', h)
    # internal links #id -> lesson slugs
    def lk(m):
        i = m.group(1)
        if i in OLD: return f'href="../{OLD[i][0]}/"'
        return {'s2':'href="../../setup/"','s3':'href="../../teamwork/"','i1':'href="../../instructors/"','home':'href="../../"'}.get(i, m.group(0))
    h = re.sub(r'href="#([a-z0-9]+)"', lk, h)
    return h.strip()

STEP = {'Overview':'concept','Notes':'concept','Can law students build?':'concept','Tool map':'concept','Safety':'concept','Limits':'concept','Trends':'concept','Candidates':'concept',
        'Steps':'build','Mini-lab':'build','Troubleshoot':'trouble','Checklist':'build',
        'Discuss':'apply','Extend':'extend','Outcomes':'ship',
        'Watch':'watch','Read':'watch','Reading list':'watch','Also worth knowing':'watch','Where to follow':'watch'}

os.makedirs('src/content/lessons', exist_ok=True)
QUIZ = json.loads(re.search(r'var QUIZ = (\{.*?\n\});', open(SRC+'p7.html',encoding='utf-8').read(), re.S).group(1)
    .replace('\n',' '), strict=False) if False else None
lessonmod = {}
for M in MODULES:
    for i, s in enumerate(M['lessons']): lessonmod[s] = (M['n'], i+1)
made = []
for aid, (slug, kind, problem) in OLD.items():
    if aid not in arts: print('missing', aid); continue
    a, tabs = arts[aid]
    parts = {k: [] for k in ['concept','watch','build','trouble','apply','extend','ship']}
    for name, body in tabs:
        st = STEP.get(name, 'concept')
        b = fix(body)
        if st == 'concept' and len([t for t in tabs if STEP.get(t[0],'concept')=='concept'])>1 and name not in ('Overview','Notes'):
            b = f'<h3>{name}</h3>\n' + b
        parts[st].append(b)
    if not parts['build'] and aid in TRY: parts['build'].append(TRY[aid])
    if not parts['apply'] and aid in APPLY: parts['apply'].append(APPLY[aid])
    mod, order = lessonmod.get(slug, (0, 0))
    fm = {'title': a.get('title'), 'module': mod, 'order': order, 'kind': kind, 'minutes': a.get('time'), 'legacy': aid.upper(), 'problem': problem}
    out = ['---'] + [f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in fm.items()] + ['---', '']
    out += ['## Problem', '', f'<div class="cc-callout cc-callout--problem"><div><b>The question.</b> {problem}</div></div>', '']
    out += ['## Concept', ''] + parts['concept']
    if parts['watch']: out += ['', '### Watch and read', ''] + parts['watch']
    if parts['build']:
        out += ['', '## Build' if kind.startswith('lab') else '## Try it', ''] + parts['build']
        if parts['trouble']: out += ['', '### If something goes wrong', ''] + parts['trouble']
    if parts['apply'] or parts['extend']:
        out += ['', '## Apply', ''] + parts['apply']
        if parts['extend']: out += ['', '### Go further', ''] + parts['extend']
    out += ['', '## Ship', '']
    out += parts['ship'] if parts['ship'] else ['<p>Write three sentences in your lab log: the main idea, one example from your discipline, and one open question. Then take the quiz below.</p>']
    open(f'src/content/lessons/{slug}.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
    made.append(slug)
print(len(made), 'lessons converted')
# non-lesson pages
os.makedirs('src/content/pages', exist_ok=True)
PAGES = {'s1':'about','s2':'setup','s3':'teamwork','p1':'capstone','p2':'team-formats','p3':'thesis-topics','i1':'instructor-plan','i2':'instructor-sessions','i3':'instructor-rubric','i4':'instructor-about'}
for aid, slug in PAGES.items():
    a, tabs = arts[aid]
    out = ['---', f'title: {json.dumps(a["title"])}', f'minutes: {json.dumps(a.get("time",""))}', '---', '']
    for name, body in tabs:
        out += [f'## {name}', '', fix(body), '']
    open(f'src/content/pages/{slug}.md','w',encoding='utf-8').write('\n'.join(out))
print('pages', len(PAGES))
