"""Insert the deeper sections (tools/deepen_a/b/c.py) into each lesson's Concept step,
just before "### Watch and read". Safe to run again: an earlier insert is replaced.
Diagram markers <!-- diagram:x --> are filled by tools/diagrams.py.
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from deepen_a import D as A
from deepen_b import D as B
from deepen_c import D as C

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = '<!-- deep:start -->', '<!-- deep:end -->'

def main():
    for slug, block in {**A, **B, **C}.items():
        p = ROOT / 'src/content/lessons' / f'{slug}.md'
        s = p.read_text(encoding='utf-8')
        s = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n*', '', s, flags=re.S)
        ins = f'{START}\n{block.strip()}\n{END}\n\n'
        if '### Watch and read' in s:
            s = s.replace('### Watch and read', ins + '### Watch and read', 1)
        else:
            s = s.replace('\n## Try it', '\n' + ins + '## Try it', 1)
        p.write_text(s, encoding='utf-8')
    print('lessons deepened:', len({**A, **B, **C}))

main()
