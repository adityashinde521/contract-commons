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

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>How many hashes does a Merkle proof need for a block with 1,024 transactions?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Which model would you choose for a loyalty-point system, and why?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Can a coin be “clean” again after passing through many outputs? Who decides?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can name what a block header commits to.</li><li>You can explain a Merkle proof in one sentence.</li><li>You can compare UTXO and account models with an example.</li></ul>
