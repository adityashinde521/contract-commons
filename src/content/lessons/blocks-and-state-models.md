---
title: "Blocks, Merkle trees and state models"
module: 1
order: 4
kind: "lesson"
minutes: "35 min"
problem: "Bitcoin and Ethereum both keep balances, but in completely different ways. Why does the choice of data model change what a smart contract can do?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Bitcoin and Ethereum both keep balances, but in completely different ways. Why does the choice of data model change what a smart contract can do?</div></div>

## Concept

<h3>What is inside a block</h3>
<ul>
<li>A <b>header</b>: the hash of the previous block, a timestamp, and a single hash that summarises every transaction in the block (the <b>Merkle root</b>).</li>
<li>A <b>body</b>: the list of transactions.</li>
<li>On Ethereum the header also commits to the full <b>state</b> after the block (the state root) and to the receipts and logs (events).</li>
</ul>
<h3>Merkle trees</h3>
<p>Transactions are hashed in pairs, then the hashes are hashed in pairs again, until one hash remains: the Merkle root. A light client can check that one transaction is in a block with only a handful of hashes (a <b>Merkle proof</b>), without downloading the whole block.</p>
<h3>Two ways to keep balances</h3>
<div class="tw"><table>
<tr><th></th><th>UTXO model (Bitcoin, Cardano)</th><th>Account model (Ethereum, most EVM chains)</th></tr>
<tr><td>What is stored</td><td>Unspent transaction outputs, like individual banknotes</td><td>A balance and storage per account, like a bank account</td></tr>
<tr><td>A payment</td><td>Spends whole outputs and creates new ones, with change back to you</td><td>Subtracts from one balance and adds to another</td></tr>
<tr><td>Strengths</td><td>Easy to verify in parallel; good privacy habits (new address per payment)</td><td>Simple to program; contracts keep their own state</td></tr>
<tr><td>For smart contracts</td><td>Limited scripting (Bitcoin Script)</td><td>Full programs in the EVM</td></tr>
</table></div>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> In the UTXO model a coin has a traceable history from output to output. This is why “tainted” coins after a hack are easier to follow, and why the question of good-faith acquisition of crypto-assets is debated.</div></div>

<!-- deep:start -->
### In depth

<p>A block has two parts: a small <b>header</b> and a list of <b>transactions</b>. The header contains the hash of the previous header (the link), a timestamp, and several roots: one hash that summarises all transactions, one for the receipts (results and logs), and one for the whole <b>state</b> after the block. Light clients can download only headers and still check that a transaction is included.</p>
<p>The summary works with a <b>Merkle tree</b>. Hash each transaction. Then hash the hashes in pairs, then the results in pairs, until one hash remains: the root. To prove that transaction C is in a block of 1,000 transactions, you need only about 10 hashes (the “Merkle proof”), not all 1,000 transactions. Change any transaction and the root changes. Ethereum uses a variant called a Merkle Patricia trie, which also works as a key-value store for account balances.</p>
<!-- diagram:merkle -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 300" role="img" aria-label="Merkle tree and the proof for transaction C" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-merkletreeandtheproo-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-merkletreeandtheproo-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-merkletreeandtheproo-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-merkletreeandtheproo-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-n" x="40" y="236" width="120" height="44" rx="12"/><text class="tb" x="100.0" y="262.7" text-anchor="middle" font-size="13.5">Tx A</text><rect class="k-n" x="40" y="160" width="120" height="44" rx="12"/><text class="tb" x="100.0" y="186.7" text-anchor="middle" font-size="13.5">H(A)</text><line class="k-a" x1="100" y1="236" x2="100" y2="206" marker-end="url(#ah-merkletreeandtheproo-a)"/><rect class="k-n" x="210" y="236" width="120" height="44" rx="12"/><text class="tb" x="270.0" y="262.7" text-anchor="middle" font-size="13.5">Tx B</text><rect class="k-n" x="210" y="160" width="120" height="44" rx="12"/><text class="tb" x="270.0" y="186.7" text-anchor="middle" font-size="13.5">H(B)</text><line class="k-a" x1="270" y1="236" x2="270" y2="206" marker-end="url(#ah-merkletreeandtheproo-a)"/><rect class="k-brand" x="380" y="236" width="120" height="44" rx="12"/><text class="tb" x="440.0" y="262.7" text-anchor="middle" font-size="13.5">Tx C</text><rect class="k-brand" x="380" y="160" width="120" height="44" rx="12"/><text class="tb" x="440.0" y="186.7" text-anchor="middle" font-size="13.5">H(C)</text><line class="k-a" x1="440" y1="236" x2="440" y2="206" marker-end="url(#ah-merkletreeandtheproo-a)"/><rect class="k-n" x="550" y="236" width="120" height="44" rx="12"/><text class="tb" x="610.0" y="262.7" text-anchor="middle" font-size="13.5">Tx D</text><rect class="k-warn" x="550" y="160" width="120" height="44" rx="12"/><text class="tb" x="610.0" y="186.7" text-anchor="middle" font-size="13.5">H(D)</text><line class="k-a" x1="610" y1="236" x2="610" y2="206" marker-end="url(#ah-merkletreeandtheproo-a)"/><rect class="k-warn" x="125" y="84" width="120" height="44" rx="12"/><text class="tb" x="185.0" y="110.7" text-anchor="middle" font-size="13.5">H(AB)</text><rect class="k-brand" x="465" y="84" width="120" height="44" rx="12"/><text class="tb" x="525.0" y="110.7" text-anchor="middle" font-size="13.5">H(CD)</text><line class="k-a" x1="100" y1="160" x2="163.75" y2="130" marker-end="url(#ah-merkletreeandtheproo-a)"/><line class="k-a" x1="270" y1="160" x2="206.25" y2="130" marker-end="url(#ah-merkletreeandtheproo-a)"/><line class="k-a" x1="440" y1="160" x2="503.75" y2="130" marker-end="url(#ah-merkletreeandtheproo-a)"/><line class="k-a" x1="610" y1="160" x2="546.25" y2="130" marker-end="url(#ah-merkletreeandtheproo-a)"/><rect class="k-cs" x="285" y="14" width="150" height="44" rx="12"/><text class="tb" x="360.0" y="31.5" text-anchor="middle" font-size="13.5">Merkle root</text><text class="t" x="360.0" y="50.0" text-anchor="middle" font-size="13.5">in block header</text><line class="k-a" x1="185" y1="84" x2="330" y2="60" marker-end="url(#ah-merkletreeandtheproo-a)"/><line class="k-a" x1="525" y1="84" x2="390" y2="60" marker-end="url(#ah-merkletreeandtheproo-a)"/><rect class="k-legend-b" x="560" y="20" width="14" height="14" rx="3"/><rect class="k-legend-w" x="560" y="44" width="14" height="14" rx="3"/><text class="tl" x="582" y="32" text-anchor="start" font-size="12">path you compute</text><text class="tl" x="582" y="56" text-anchor="start" font-size="12">proof you receive</text></svg></div><figcaption><b>Proving inclusion with two hashes.</b> To prove Tx C is in the block, you need only H(D) and H(AB). Hash C, combine up the tree, and compare with the root in the header. With 1,000 transactions, about 10 hashes are enough.</figcaption></figure>
<p>Blockchains also differ in how they keep <b>state</b>. Bitcoin uses the <b>UTXO</b> model: there are no balances, only unspent outputs, like banknotes in a wallet. A payment consumes whole outputs and creates new ones, including change back to the sender. Ethereum uses the <b>account</b> model: a global table of accounts with balances, nonces and, for contracts, code and storage, like bank accounts. Smart contracts are much easier to write in the account model, because a contract can simply update a balance in its storage.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> Alice owns 0.7 BTC as two outputs (0.5 and 0.2) and pays Bob 0.6. Then the same payment on Ethereum.</p>
<div class="tw"><table>
  <tr><th></th><th>UTXO (Bitcoin)</th><th>Account (Ethereum)</th></tr>
  <tr><td>Before</td><td>Outputs: 0.5 (Alice), 0.2 (Alice)</td><td>balance[Alice] = 0.7</td></tr>
  <tr><td>Transaction</td><td>Inputs: both outputs. Outputs: 0.6 to Bob, 0.099 change to Alice. Fee: 0.001</td><td>to = Bob, value = 0.6, nonce = 3</td></tr>
  <tr><td>After</td><td>Outputs: 0.6 (Bob), 0.099 (Alice). Old outputs are spent forever.</td><td>balance[Alice] = 0.7 − 0.6 − fee; balance[Bob] += 0.6; nonce[Alice] = 4</td></tr>
  <tr><td>Double-spend protection</td><td>An output can be spent once</td><td>The nonce must be the next number</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“The block stores all balances.” It stores the transactions and a state root; nodes keep the state itself.</li>
  <li>“A Merkle proof shows the transaction is valid.” It shows only that the transaction is included in that block.</li>
  <li>“The block timestamp is exact.” Validators set it within narrow rules; use it for days, not seconds.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/blocks/" target="_blank" rel="noopener"><span class="play"></span><span><b>Blocks</b><small>ethereum.org developer docs</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/accounts/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum accounts</b><small>ethereum.org developer docs</small></span></a>
<a class="vid" href="https://www.youtube.com/watch?v=bBC-nXj3Ng4" target="_blank" rel="noopener"><span class="play"></span><span><b>But how does bitcoin actually work?</b><small>3Blue1Brown, 25 min (UTXO view)</small></span></a>
</div>

## Try it

<ol class="steps">
<li>Open any recent block on <a href="https://etherscan.io/blocks" target="_blank" rel="noopener">Etherscan</a> (read only). Click “More details”.<span class="exp">You see the parent hash, the state root and the transactions root.</span></li>
<li>Open a Bitcoin transaction on <a href="https://mempool.space" target="_blank" rel="noopener">mempool.space</a>.<span class="exp">Inputs on the left, outputs on the right, usually one output as change back to the sender.</span></li>
</ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>How many hashes does a Merkle proof need for a block with 1,024 transactions?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which model would you choose for a loyalty-point system, and why?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Can a coin be “clean” again after passing through many outputs? Who decides?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name what a block header commits to.</li><li>You can explain a Merkle proof in one sentence.</li><li>You can compare UTXO and account models with an example.</li></ul>
