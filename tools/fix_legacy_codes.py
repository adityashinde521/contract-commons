"""Replace references to the old course codes (L0-L7, G0-G12, T1-T10, F1-F7, S1-S2)
with the current lesson numbers, linked to the lesson. Run once from the repo root.

"L1"/"L2" also mean layer 1 / layer 2 in the scaling lessons; those phrases are protected first.
"""
import json, re, glob, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MODS = json.loads((ROOT / 'src/data/modules.json').read_text())
NUM = {slug: f"{m['n']}.{i + 1}" for m in MODS for i, slug in enumerate(m['lessons'])}

OLD = {
 'L0': 'lab-remix-tour', 'L1': 'lab-simple-storage', 'L2': 'lab-escrow', 'L3': 'lab-rental-deposit',
 'L4': 'lab-document-registry', 'L5': 'lab-course-token', 'L6': 'lab-reentrancy', 'L7': 'lab-sepolia',
 'G0': 'gui-tools-overview', 'G1': 'lab-openzeppelin-wizard', 'G2': 'lab-thirdweb', 'G3': 'lab-safe', 'G4': 'lab-aragon',
 'G5': 'lab-attestations', 'G6': 'lab-accord', 'G7': 'lab-quickdapp', 'G8': 'lab-tenderly', 'G9': 'lab-phalcon',
 'G10': 'lab-see-inside', 'G11': 'lab-dashboards', 'G12': 'tools-to-evaluate',
 'T1': 'trust-and-ledgers', 'T2': 'hash-functions', 'T3': 'keys-and-signatures', 'T4': 'consensus',
 'T5': 'ethereum-evm-gas', 'T6': 'what-smart-contracts-are', 'T7': 'solidity-for-programmers', 'T8': 'security-basics',
 'T9': 'token-standards', 'T10': 'law-and-business',
 'F1': 'ethereum-today', 'F2': 'zero-knowledge', 'F3': 'ai-agents', 'F4': 'quantum', 'F5': 'security-in-practice',
 'F6': 'regulation', 'F7': 'research',
}
SHORT = {
 'lab-remix-tour': 'Remix tour', 'lab-simple-storage': 'SimpleStorage', 'lab-escrow': 'Escrow',
 'lab-rental-deposit': 'Rental deposit', 'lab-document-registry': 'Document registry', 'lab-course-token': 'Course token',
 'lab-reentrancy': 'Reentrancy', 'lab-sepolia': 'Sepolia deployment', 'gui-tools-overview': 'Tools overview',
 'lab-openzeppelin-wizard': 'OpenZeppelin Wizard', 'lab-thirdweb': 'thirdweb', 'lab-safe': 'Safe', 'lab-aragon': 'Aragon DAO',
 'lab-attestations': 'Attestations', 'lab-accord': 'Accord Project', 'lab-quickdapp': 'QuickDApp', 'lab-tenderly': 'Tenderly',
 'lab-phalcon': 'Phalcon', 'lab-see-inside': 'See inside', 'lab-dashboards': 'Dashboards', 'tools-to-evaluate': 'Tools to evaluate',
 'trust-and-ledgers': 'Trust and ledgers', 'hash-functions': 'Hash functions', 'keys-and-signatures': 'Keys and signatures',
 'consensus': 'Consensus', 'ethereum-evm-gas': 'Ethereum, EVM and gas', 'what-smart-contracts-are': 'What smart contracts are',
 'solidity-for-programmers': 'Solidity', 'security-basics': 'Security basics', 'token-standards': 'Token standards',
 'law-and-business': 'Law and business', 'ethereum-today': 'Ethereum today', 'zero-knowledge': 'Zero knowledge',
 'ai-agents': 'AI agents', 'quantum': 'Quantum', 'security-in-practice': 'Security in practice',
 'regulation': 'Regulation', 'research': 'Research',
}

def label(slug):
    n = NUM.get(slug)
    return f"{n} {SHORT[slug]}" if n else SHORT[slug]

def link(slug):
    return f'<a href="/lessons/{slug}/">{label(slug)}</a>'

# Hand-written replacements for ranges and the places where a plain sentence reads better.
MANUAL = [
 ('<td>L1–L6</td><td>L7, G1–G8</td>', '<td>Most code labs (Remix VM)</td><td>Sepolia deployment and most tool labs</td>'),
 ('Best single video for T1–T4.', 'Best single video for lessons 1.1 to 2.1.'),
 ('(labs L0–L7)', '(the code labs)'),
 ('Labs L7, G1–G5 and G7–G8 sign tra', 'The Sepolia deployment and most tool labs sign tra'),
 ('<td>T1–T4, G10 ETH.BUILD</td><td>T5–T6, L0–L1, G1 Wizard</td>', '<td>Modules 1–2, 1.6 ETH.BUILD</td><td>Module 3, 4.1, 5.3 Wizard</td>'),
 ('<td>F1–F4, caps', '<td>Module 10 and 13.1–13.2, caps'),
 ('Dates in F1 and S2 change often', 'Dates in 10.1 Ethereum today and in Setup change often'),
 ('the five rules (S2)', 'the five safety rules (Setup)'),
 ('Use only the course MetaMask wallet (S2).', 'Use only the course MetaMask wallet (see Setup).'),
 ('<div><b>Before</b>S2 setup. T5 recommended.</div>', '<div><b>Before</b>Setup and safety. Lesson 3.1 recommended.</div>'),
 ('<div><b>Before</b>S2 done.', '<div><b>Before</b>Setup done.'),
 ('semester course (S1, “Weekly plan”)', 'semester course (About, “Weekly plan”)'),
 ('Deploy L2 Escrow on an L2 testnet', 'Deploy the Escrow on an L2 testnet'),
 ('In the Remix debugger during the L6 attack', 'In the Remix debugger during the 7.4 reentrancy attack'),
 ('the key legal discussion question for F3.', 'the key legal discussion question for 13.1 AI agents.'),
]
# Layer-1 / layer-2 phrases that must not be touched.
PROTECT = ['an L2 testnet', 'L2 testnet', 'L2 fees', 'on L1', 'L1 and L2', 'on an L2', 'L2BEAT', 'L2, rollups', 'L2 scaling',
           'L2 sequencer', 'which L2', 'on L2 first', 'L2 transactions', 'final on L1', 'Layer 2', 'L2s', 'on L1,', 'than on L1']

CODE = re.compile(r'(?<![\w/.-])(T10|G1[0-2]|[LG][0-9]|T[1-9]|F[1-7])(?![\w-])')

def fix(text, in_quiz=False):
    for a, b in MANUAL:
        text = text.replace(a, b)
    keep = {}
    for i, p in enumerate(PROTECT):
        tok = f'\x00{i}\x00'
        if p in text:
            text = text.replace(p, tok); keep[tok] = p
    out, pos = [], 0
    for m in CODE.finditer(text):
        code = m.group(1); slug = OLD.get(code)
        if not slug: continue
        before = text[:m.start()]
        # Skip frontmatter lines such as legacy: "L2".
        line_start = before.rfind('\n') + 1
        if text[line_start:m.start()].lstrip().startswith('legacy:'): continue
        open_a, close_a = before.rfind('<a '), before.rfind('</a>')
        inside_link = open_a > close_a
        in_cell = before.endswith('<td>') and text[m.end():].startswith('</td>')
        if in_quiz or inside_link:
            rep = NUM.get(slug, SHORT[slug]) if inside_link else label(slug)
        elif in_cell:
            rep = f'<a href="/lessons/{slug}/">{NUM.get(slug, SHORT[slug])}</a>'
        else:
            rep = link(slug)
        out.append(text[pos:m.start()]); out.append(rep); pos = m.end()
    out.append(text[pos:])
    text = ''.join(out)
    for tok, p in keep.items():
        text = text.replace(tok, p)
    return text

def main():
    changed = 0
    files = glob.glob(str(ROOT / 'src/content/lessons/*.md')) + glob.glob(str(ROOT / 'src/content/pages/*.md'))
    for f in files:
        s = open(f, encoding='utf-8').read(); t = fix(s)
        if t != s: open(f, 'w', encoding='utf-8').write(t); changed += 1
    qp = ROOT / 'src/data/quizzes.json'
    s = qp.read_text(encoding='utf-8'); t = fix(s, in_quiz=True)
    if t != s: qp.write_text(t, encoding='utf-8'); changed += 1
    print('files changed', changed)

if __name__ == '__main__':
    main()
