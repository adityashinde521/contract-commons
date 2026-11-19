"""Inline SVG diagrams for the lessons. Each <!-- diagram:name --> marker in a lesson is
replaced by <figure class="dg">…</figure>. Safe to run again (old figures are replaced).
Colours come from CSS classes in site.css (.dg .k-*), so diagrams follow the design tokens.
"""
import pathlib, re, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
W = 720

def esc(s): return html.escape(s, quote=False)

class S:
    def __init__(self, h, title):
        self.h, self.title, self.parts = h, title, []
        self.id = re.sub(r'\W+', '', title.lower())[:20]
    def box(self, x, y, w, h, lines, k='n', bold_first=True, r=12, size=13.5):
        self.parts.append(f'<rect class="k-{k}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/>')
        n = len(lines); lh = size + 5; y0 = y + h / 2 - (n - 1) * lh / 2 + size * 0.35
        for i, t in enumerate(lines):
            cls = 'tb' if (i == 0 and bold_first) else 't'
            self.parts.append(f'<text class="{cls}" x="{x + w / 2}" y="{y0 + i * lh:.1f}" text-anchor="middle" font-size="{size}">{esc(t)}</text>')
    def text(self, x, y, t, cls='t', size=13, anchor='middle'):
        self.parts.append(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}">{esc(t)}</text>')
    def arrow(self, x1, y1, x2, y2, label=None, k='a', dx=0, dy=-7, dash=False, size=12.5, anchor='middle'):
        d = ' stroke-dasharray="5 4"' if dash else ''
        self.parts.append(f'<line class="k-{k}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" marker-end="url(#ah-{self.id}-{k})"{d}/>')
        if label: self.text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, label, 'tl', size, anchor)
    def path(self, d, k='a', arrow=True, dash=False):
        m = f' marker-end="url(#ah-{self.id}-{k})"' if arrow else ''
        da = ' stroke-dasharray="5 4"' if dash else ''
        self.parts.append(f'<path class="k-{k}" d="{d}" fill="none"{m}{da}/>')
    def raw(self, s): self.parts.append(s)
    def svg(self):
        defs = ''.join(f'<marker id="ah-{self.id}-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-{k}" d="M0 0L10 5L0 10z"/></marker>' for k in ('a', 'ar', 'ag', 'am'))
        return (f'<svg viewBox="0 0 {W} {self.h}" role="img" aria-label="{esc(self.title)}" xmlns="http://www.w3.org/2000/svg">'
                f'<defs>{defs}</defs>{"".join(self.parts)}</svg>')

def fig(s, caption):
    return f'<figure class="dg"><div class="sv">{s.svg()}</div><figcaption>{caption}</figcaption></figure>'

D = {}

# 1 Hash chain and tampering
s = S(300, 'Hash-linked blocks and what tampering does')
s.text(20, 24, 'Honest chain', 'th', 14, 'start')
for i, (prev, data, h) in enumerate([('0000…', 'Rent 900 EUR', '3f9a…'), ('3f9a…', 'Alice → Bob 1', 'b21c…'), ('b21c…', 'Bob → Eve 0.5', '7d04…')]):
    x = 20 + i * 240
    s.box(x, 36, 200, 92, [f'Block {i + 1}', f'prev: {prev}', f'data: {data}', f'hash: {h}'], 'cs', size=13)
    if i: s.arrow(x - 40, 82, x - 2, 82)
s.text(20, 168, 'Someone edits block 1', 'th', 14, 'start')
rows = [('0000…', 'Rent 990 EUR', 'c8e1…', 'danger'), ('3f9a… ≠ c8e1…', 'Alice → Bob 1', 'b21c…', 'danger'), ('b21c…', 'Bob → Eve 0.5', '7d04…', 'warn')]
for i, (prev, data, h, k) in enumerate(rows):
    x = 20 + i * 240
    s.box(x, 180, 200, 92, [f'Block {i + 1}', f'prev: {prev}', f'data: {data}', f'hash: {h}'], k, size=13)
    if i: s.arrow(x - 40, 226, x - 2, 226, k='ar')
D['hash-chain'] = fig(s, '<b>Tamper-evident, not tamper-proof.</b> Changing block 1 changes its hash, so block 2’s “prev” no longer matches. To hide the edit, every later block would have to be rebuilt and accepted by the network again.')

# 2 Sign and verify
s = S(250, 'Signing in the wallet and verifying on a node')
s.raw('<rect class="k-zone" x="10" y="10" width="330" height="230" rx="16"/><rect class="k-zone" x="380" y="10" width="330" height="230" rx="16"/>')
s.text(175, 34, 'In the wallet (private)', 'th', 14); s.text(545, 34, 'On every node (public)', 'th', 14)
s.box(30, 52, 130, 56, ['Transaction', 'to, value, nonce'], 'n')
s.box(30, 160, 130, 56, ['Private key', 'never leaves'], 'law')
s.box(200, 106, 120, 56, ['Sign', 'ECDSA'], 'brand')
s.arrow(160, 80, 198, 120); s.arrow(160, 188, 198, 150)
s.box(400, 52, 140, 56, ['Tx + signature', 'r, s, v'], 'n')
s.box(400, 160, 140, 56, ['Recover', 'public key → address'], 'cs')
s.box(570, 106, 125, 56, ['Matches sender?', 'yes: valid'], 'brand')
s.arrow(320, 134, 398, 84, 'broadcast', dy=-10)
s.arrow(470, 108, 470, 158); s.arrow(540, 188, 568, 150)
D['sign-verify'] = fig(s, '<b>The key signs; the network only checks.</b> Nodes recover the signer’s address from the signature. Change one byte of the transaction and a different, random address comes out, so the transaction is rejected.')

# 3 Merkle tree with proof path
s = S(300, 'Merkle tree and the proof for transaction C')
leaves = ['Tx A', 'Tx B', 'Tx C', 'Tx D']
for i, t in enumerate(leaves):
    x = 40 + i * 170
    s.box(x, 236, 120, 44, [t], 'brand' if t == 'Tx C' else 'n')
    k = 'brand' if t == 'Tx C' else ('warn' if t == 'Tx D' else 'n')
    s.box(x, 160, 120, 44, [f'H({t[-1]})'], k)
    s.arrow(x + 60, 236, x + 60, 206)
s.box(125, 84, 120, 44, ['H(AB)'], 'warn'); s.box(465, 84, 120, 44, ['H(CD)'], 'brand')
for x in (100, 270): s.arrow(x, 160, 185 + (x - 185) * 0.25, 130)
for x in (440, 610): s.arrow(x, 160, 525 + (x - 525) * 0.25, 130)
s.box(285, 14, 150, 44, ['Merkle root', 'in block header'], 'cs')
s.arrow(185, 84, 330, 60); s.arrow(525, 84, 390, 60)
s.raw('<rect class="k-legend-b" x="560" y="20" width="14" height="14" rx="3"/><rect class="k-legend-w" x="560" y="44" width="14" height="14" rx="3"/>')
s.text(582, 32, 'path you compute', 'tl', 12, 'start'); s.text(582, 56, 'proof you receive', 'tl', 12, 'start')
D['merkle'] = fig(s, '<b>Proving inclusion with two hashes.</b> To prove Tx C is in the block, you need only H(D) and H(AB). Hash C, combine up the tree, and compare with the root in the header. With 1,000 transactions, about 10 hashes are enough.')

# 4 PoS slots, epochs, finality
s = S(230, 'Proof of Stake slots, epochs and finality')
for e in range(3):
    x0 = 20 + e * 230
    s.raw(f'<rect class="k-zone" x="{x0}" y="40" width="220" height="70" rx="12"/>')
    s.text(x0 + 110, 30, f'Epoch N{"" if e == 0 else "+" + str(e)} · 32 slots · 6.4 min', 'tl', 12.5)
    for j in range(8):
        k = 'k-slot-m' if j == 0 else 'k-slot'
        s.raw(f'<rect class="{k}" x="{x0 + 12 + j * 25.5}" y="58" width="20" height="34" rx="4"/>')
s.text(20, 134, '▲ checkpoint (first slot of each epoch)', 'tl', 12.5, 'start')
s.box(20, 150, 220, 60, ['Epoch N checkpoint', '2/3 of stake attests'], 'warn', size=13)
s.box(250, 150, 220, 60, ['After epoch N+1', 'N is justified, then final'], 'brand', size=13)
s.box(480, 150, 220, 60, ['≈ 12.8 minutes', 'reversal = slashing ≥ 1/3 stake'], 'cs', size=13)
s.arrow(240, 180, 248, 180); s.arrow(470, 180, 478, 180)
D['pos-finality'] = fig(s, '<b>Two levels of “done”.</b> A block is proposed every 12-second slot. Once two thirds of all stake attests to checkpoints over two epochs, the block is final. Undoing it would cost attackers at least a third of all staked ETH.')

# 5 Soft fork vs hard fork
s = S(250, 'Soft fork and hard fork')
s.text(20, 24, 'Soft fork: stricter rules, one chain', 'th', 14, 'start')
for i in range(6):
    x = 20 + i * 115
    s.box(x, 36, 90, 40, ['old' if i < 3 else 'new rules'], 'n' if i < 3 else 'brand', bold_first=False)
    if i: s.arrow(x - 25, 56, x - 2, 56)
s.text(20, 104, 'Old nodes still accept the new blocks.', 'tl', 12.5, 'start')
s.text(20, 140, 'Hard fork: changed rules; nodes that do not upgrade split off', 'th', 14, 'start')
for i in range(3):
    x = 20 + i * 115
    s.box(x, 172, 90, 40, ['old'], 'n', bold_first=False)
    if i: s.arrow(x - 25, 192, x - 2, 192)
for i in range(3):
    x = 365 + i * 115
    s.box(x, 152, 90, 36, ['new rules'], 'brand', bold_first=False)
    s.box(x, 204, 90, 36, ['old rules'], 'warn', bold_first=False)
    if i: s.arrow(x - 25, 170, x - 2, 170); s.arrow(x - 25, 222, x - 2, 222, k='am')
s.path('M 340 192 C 352 192 350 170 363 170'); s.path('M 340 192 C 352 192 350 222 363 222', k='am')
D['forks'] = fig(s, '<b>Upgrades and splits.</b> A soft fork narrows the rules, so old software keeps working. A hard fork changes them; if a group keeps the old rules, two chains continue, as Ethereum and Ethereum Classic did in 2016.')

# 6 Transaction lifecycle
s = S(190, 'Life of an Ethereum transaction')
steps = [('Wallet', 'signs', 'law'), ('Mempool', 'waits', 'n'), ('Proposer', 'orders', 'bi'), ('EVM', 'runs, gas', 'cs'), ('Included', '≈ 12 s', 'brand'), ('Final', '≈ 13 min', 'brand')]
for i, (a, b, k) in enumerate(steps):
    x = 10 + i * 118
    s.box(x, 40, 100, 66, [a, b], k, size=13.5)
    if i: s.arrow(x - 18, 73, x - 2, 73)
s.text(360, 140, 'Revert in the EVM: state changes are undone, gas used is still paid.', 'tl', 13)
s.text(360, 165, 'Fee = gas used × (base fee, burned + priority fee, to validator)', 'tl', 13)
D['tx-lifecycle'] = fig(s, '<b>From click to finality.</b> The wallet signs locally, the transaction waits in the mempool, a validator includes it, every node runs it in the EVM, and after about 13 minutes it is final.')

# 7 Escrow state machine
s = S(276, 'Escrow state machine')
s.box(20, 100, 170, 64, ['AwaitingPayment', 'after deploy'], 'n')
s.box(275, 100, 170, 64, ['AwaitingDelivery', '1 ETH held'], 'warn')
s.box(530, 30, 170, 64, ['Complete', 'seller paid'], 'brand')
s.box(530, 172, 170, 64, ['Refunded', 'buyer paid back'], 'law')
s.arrow(190, 132, 273, 132)
s.text(232, 86, 'deposit()', 'tb', 12.5); s.text(232, 102, 'buyer, exact price', 'tl', 12)
s.arrow(445, 116, 528, 62)
s.text(400, 30, 'confirmDelivery()', 'tb', 12.5); s.text(400, 46, 'buyer or arbiter', 'tl', 12)
s.arrow(445, 150, 528, 204)
s.text(400, 214, 'refund()', 'tb', 12.5); s.text(400, 230, 'arbiter only', 'tl', 12)
s.text(360, 262, 'Any other call in a state → revert, nothing changes', 'tl', 13)
D['escrow-states'] = fig(s, '<b>A contract is a state machine.</b> Each arrow is a function with a condition on <i>who</i> may call it and <i>in which state</i>. Everything not drawn here is forbidden by the code.')

# 8 approve / transferFrom
s = S(280, 'ERC-20 approve and transferFrom')
for x, t, k in ((90, 'Alice', 'law'), (360, 'Token contract', 'cs'), (630, 'Shop contract', 'bi')):
    s.box(x - 80, 12, 160, 40, [t], k); s.raw(f'<line class="k-life" x1="{x}" y1="52" x2="{x}" y2="270"/>')
s.arrow(90, 90, 358, 90, '1  approve(Shop, 50)'); s.text(372, 108, 'allowance[Alice][Shop] = 50', 'tl', 12, 'start')
s.arrow(90, 150, 628, 150, '2  buy(item)', dx=150)
s.arrow(630, 200, 362, 200, '3  transferFrom(Alice, Shop, 50)', dy=-8)
s.text(372, 230, 'balance Alice −50 · Shop +50', 'tl', 12, 'start'); s.text(372, 250, 'allowance back to 0', 'tl', 12, 'start')
D['approve-flow'] = fig(s, '<b>Two transactions, one pull.</b> Alice first allows the shop to take up to 50 tokens. The shop then pulls them itself. If step 1 is missing, step 3 reverts.')

# 9 Reentrancy sequence
s = S(320, 'Reentrancy attack sequence')
for x, t, k in ((120, 'Attacker contract', 'danger'), (470, 'VulnerableBank', 'cs')):
    s.box(x - 100, 12, 200, 40, [t], k); s.raw(f'<line class="k-life" x1="{x}" y1="52" x2="{x}" y2="310"/>')
s.arrow(120, 80, 468, 80, 'withdraw()')
s.text(485, 104, 'balance = 1 ✓', 'tl', 12.5, 'start')
s.arrow(470, 124, 122, 124, 'send 1 ETH', k='ar')
s.text(135, 150, 'receive() runs …', 'tl', 12.5, 'start')
s.arrow(120, 170, 468, 170, 'withdraw() again')
s.text(485, 194, 'balance still 1 ✓', 'tl', 12.5, 'start')
s.arrow(470, 214, 122, 214, 'send 1 ETH', k='ar')
s.text(295, 250, '… repeats until the bank is empty', 'tl', 13)
s.text(485, 286, 'balance = 0  (too late)', 'tl', 12.5, 'start')
s.text(485, 304, 'fix: set to 0 before sending', 'tlg', 12.5, 'start')
D['reentrancy'] = fig(s, '<b>The bank pays before it updates its books.</b> Sending ETH runs the attacker’s code, which calls <code>withdraw()</code> again while the balance is still 1. Checks-effects-interactions closes the loop.')

# 10 Proxy pattern
s = S(260, 'Upgradeable proxy pattern')
s.box(20, 100, 120, 56, ['User'], 'law')
s.box(200, 86, 180, 84, ['Proxy', 'fixed address', 'holds storage & ETH'], 'cs')
s.box(470, 20, 220, 70, ['Implementation v1', 'logic only'], 'n')
s.box(470, 166, 220, 70, ['Implementation v2', 'fixed logic'], 'brand')
s.arrow(140, 128, 198, 128, 'call')
s.arrow(380, 110, 468, 60); s.text(470, 112, 'delegatecall', 'tl', 12.5, 'start')
s.arrow(380, 150, 468, 196, dash=True, k='ag'); s.text(470, 150, 'after upgrade', 'tlg', 12.5, 'start')
s.box(200, 200, 180, 50, ['Admin', 'multisig + timelock'], 'warn', size=13)
s.arrow(290, 200, 290, 172, k='am')
D['proxy'] = fig(s, '<b>Same address, new logic.</b> The proxy keeps the data and borrows the code of the current implementation. An upgrade only changes which implementation it points to, so whoever controls the admin controls the contract.')

# 11 dApp stack
s = S(270, 'Layers of a dApp')
s.raw('<rect class="k-zone-b" x="470" y="10" width="240" height="250" rx="16"/>')
s.text(590, 34, 'On chain (decentralised)', 'th', 13.5)
s.box(20, 30, 180, 60, ['Front end', 'website, can be changed'], 'n')
s.box(20, 180, 180, 60, ['Wallet', 'holds keys, signs'], 'law')
s.box(270, 30, 150, 60, ['Indexer', 'collects events'], 'n')
s.box(270, 180, 150, 60, ['RPC node', 'provider'], 'bi')
s.box(490, 105, 200, 60, ['Smart contracts', 'rules and money'], 'brand')
s.arrow(110, 90, 110, 178); s.text(122, 140, 'asks to sign', 'tl', 12, 'start')
s.arrow(200, 210, 268, 210); s.text(234, 200, 'signed tx', 'tl', 12)
s.arrow(420, 200, 488, 150)
s.arrow(488, 120, 422, 70, k='am'); s.text(470, 84, 'events', 'tl', 12, 'end')
s.arrow(268, 60, 202, 60, k='am'); s.text(234, 50, 'history', 'tl', 12)
D['dapp-stack'] = fig(s, '<b>Only the contracts are decentralised.</b> The website, the RPC provider and the indexer are normal services that can fail or be attacked. The wallet is the last check before anything is signed.')

# 12 Oracle
s = S(260, 'Oracle designs')
for i, t in enumerate(['Exchange A', 'Exchange B', 'Data firm C']):
    s.box(20, 20 + i * 62, 130, 46, [t], 'n', bold_first=False, size=13)
for i in range(3):
    s.box(200, 20 + i * 62, 120, 46, [f'Oracle node {i + 1}'], 'bi', bold_first=False, size=13)
    s.arrow(150, 43 + i * 62, 198, 43 + i * 62)
s.box(370, 70, 120, 56, ['Aggregate', 'median'], 'cs')
for i in range(3): s.arrow(320, 43 + i * 62, 368, 98)
s.box(540, 70, 160, 56, ['Your contract', 'reads price + age'], 'brand')
s.arrow(490, 98, 538, 98)
s.box(370, 196, 160, 50, ['One DEX pool', 'spot price'], 'danger', size=13)
s.arrow(530, 220, 600, 128, 'manipulable', k='ar', dx=38, dy=18)
D['oracle'] = fig(s, '<b>Many sources versus one.</b> A decentralised feed takes the median of independent reporters, so a few bad values cannot move it. A single on-chain pool can be pushed in one transaction with a flash loan.')

# 13 Rollup
s = S(270, 'How a rollup posts to Ethereum')
s.raw('<rect class="k-zone" x="10" y="10" width="330" height="250" rx="16"/><rect class="k-zone-b" x="380" y="10" width="330" height="250" rx="16"/>')
s.text(175, 34, 'Layer 2 (rollup)', 'th', 14); s.text(545, 34, 'Ethereum (Layer 1)', 'th', 14)
s.box(30, 54, 120, 52, ['Users', 'cheap, fast txs'], 'law', size=13)
s.box(190, 54, 130, 52, ['Sequencer', 'orders, executes'], 'bi', size=13)
s.arrow(150, 80, 188, 80)
s.box(110, 150, 200, 56, ['Batch', 'thousands of txs'], 'n')
s.arrow(255, 106, 230, 148)
s.box(400, 54, 290, 52, ['Blob data', 'anyone can rebuild the L2 state'], 'cs', size=13)
s.box(400, 124, 290, 52, ['Rollup contract', 'new state root'], 'brand', size=13)
s.box(400, 194, 140, 54, ['Optimistic', '≈ 7-day challenge'], 'warn', size=12.5)
s.box(550, 194, 140, 54, ['ZK rollup', 'validity proof'], 'cs', size=12.5)
s.arrow(310, 172, 398, 80); s.arrow(310, 180, 398, 150)
D['rollup'] = fig(s, '<b>Execute on L2, settle on L1.</b> The rollup runs transactions cheaply and posts their data and a new state root to Ethereum. Correctness is enforced by a challenge window (optimistic) or a proof (ZK).')

# 14 Bridge
s = S(250, 'Lock-and-mint bridge')
s.raw('<rect class="k-zone" x="10" y="10" width="300" height="230" rx="16"/><rect class="k-zone" x="410" y="10" width="300" height="230" rx="16"/>')
s.text(160, 34, 'Chain A (Ethereum)', 'th', 14); s.text(560, 34, 'Chain B', 'th', 14)
s.box(40, 60, 240, 64, ['Bridge vault', 'locked: 100 USDC'], 'cs')
s.box(440, 60, 240, 64, ['Wrapped token', 'minted: 100 bUSDC'], 'brand')
s.box(260, 160, 200, 64, ['Signers', '3 of 5 must approve'], 'warn')
s.arrow(280, 82, 438, 82, '1 lock → 2 mint', dy=-10)
s.arrow(438, 108, 282, 108, 'burn → unlock', dy=18, k='am')
s.arrow(360, 160, 360, 126, k='am')
D['bridge'] = fig(s, '<b>A wrapped token is a claim on a vault.</b> The bridge locks the original on chain A and mints a copy on chain B. Whoever controls the signers controls the vault; if it is drained, the copies are worth nothing.')

# 15 AMM curve
s = S(300, 'Constant-product AMM curve')
ox, oy, sx, sy = 70, 260, 4.2, 0.00055
s.raw(f'<line class="k-axis" x1="{ox}" y1="{oy}" x2="{W - 30}" y2="{oy}"/><line class="k-axis" x1="{ox}" y1="{oy}" x2="{ox}" y2="20"/>')
pts = ' '.join(f'{ox + (x - 60) * sx:.1f},{oy - (30_000_000 / x - 150_000) * sy:.1f}' for x in range(62, 200, 2))
s.raw(f'<polyline class="k-curve" points="{pts}"/>')
def pt(x): return ox + (x - 60) * sx, oy - (30_000_000 / x - 150_000) * sy
ax, ay = pt(100); bx, by = pt(110)
s.raw(f'<circle class="k-dot" cx="{ax:.1f}" cy="{ay:.1f}" r="6"/><circle class="k-dot2" cx="{bx:.1f}" cy="{by:.1f}" r="6"/>')
s.text(ax + 12, ay - 10, 'A: 100 ETH · 300,000 USDC', 'tl', 12.5, 'start')
s.text(bx + 14, by + 34, 'B: 110 ETH · 272,727 USDC', 'tl', 12.5, 'start')
s.text(W - 30, oy + 26, 'ETH in pool →', 'tl', 12.5, 'end'); s.text(ox - 8, 34, 'USDC', 'tl', 12.5, 'end')
s.text(500, 70, 'x × y = k = 30,000,000', 'th', 14)
s.text(500, 94, 'Sell 10 ETH → get 27,273 USDC', 'tl', 12.5)
D['amm'] = fig(s, '<b>Price is the slope of the curve.</b> A trade moves the pool from A to B along x × y = k. The bigger the trade compared with the pool, the worse the average price (slippage).')

# 16 DAO lifecycle
s = S(220, 'DAO proposal lifecycle')
st = [('Propose', 'actions + snapshot', 'n'), ('Vote', '3 days', 'bi'), ('Timelock', '2 days, can exit', 'warn'), ('Execute', 'contract acts', 'brand')]
for i, (a, b, k) in enumerate(st):
    x = 15 + i * 178
    s.box(x, 40, 150, 66, [a, b], k, size=13)
    if i: s.arrow(x - 26, 73, x - 2, 73)
s.text(270, 30, 'quorum + majority?', 'tl', 12.5)
s.box(193, 150, 150, 50, ['Defeated', 'nothing happens'], 'danger', size=13)
s.arrow(268, 106, 268, 148, 'no', dx=14, dy=4, k='ar')
D['dao-lifecycle'] = fig(s, '<b>Code executes what members decide.</b> The snapshot fixes voting power before the vote, so borrowed tokens do not count. The timelock gives members time to react before money moves.')

# 17 Smart legal contract spectrum
s = S(210, 'Three forms of smart legal contracts')
for i, (a, b, c, k) in enumerate([('Natural language', 'text is the contract', 'code performs parts', 'law'), ('Hybrid', 'some terms in text,', 'some in code', 'bi'), ('Code only', 'the code is', 'the agreement', 'cs')]):
    x = 20 + i * 235
    s.box(x, 30, 210, 90, [a, b, c], k)
s.arrow(40, 150, 680, 150, 'more of the agreement lives in code →', dy=-8)
s.text(360, 190, 'Always answer in writing: which version prevails, and who can pause or end the code?', 'tl', 13)
D['slc-spectrum'] = fig(s, '<b>From text to code.</b> The UK Law Commission (2021) describes three forms. The further right, the harder it is for people to read, prove and challenge what they agreed.')

def main():
    n = 0
    for p in (ROOT / 'src/content/lessons').glob('*.md'):
        s = p.read_text(encoding='utf-8')
        s2 = re.sub(r'<figure class="dg">.*?</figure>\n?(<!-- /diagram -->)?', '', s, flags=re.S)
        def rep(m):
            name = m.group(1)
            return f'<!-- diagram:{name} -->\n{D[name]}\n'
        s2 = re.sub(r'<!-- diagram:([a-z-]+) -->\n?', rep, s2)
        if s2 != s:
            p.write_text(s2, encoding='utf-8'); n += 1
    print('lessons with diagrams:', n, 'diagrams defined:', len(D))

main()
