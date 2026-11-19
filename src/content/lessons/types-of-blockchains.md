---
title: "Types of blockchains"
module: 1
order: 5
kind: "lesson"
minutes: "30 min"
problem: "A logistics consortium asks for “a blockchain”. Should it use Ethereum, a private network or a shared database?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A logistics consortium asks for “a blockchain”. Should it use Ethereum, a private network or a shared database?</div></div>

## Concept

<div class="tw"><table>
<tr><th>Type</th><th>Who can read</th><th>Who can write and validate</th><th>Examples</th></tr>
<tr><td><b>Public, permissionless</b></td><td>Anyone</td><td>Anyone who follows the protocol (stake or work)</td><td>Ethereum, Bitcoin, Solana</td></tr>
<tr><td><b>Consortium</b></td><td>Members, sometimes the public</td><td>A fixed group of known organisations</td><td>Hyperledger Besu networks, bank or trade-finance consortia</td></tr>
<tr><td><b>Private, permissioned</b></td><td>One organisation decides</td><td>One organisation’s nodes</td><td>Internal audit ledgers</td></tr>
</table></div>
<ul>
<li><b>Layer 1</b> chains settle transactions themselves (Ethereum). <b>Layer 2</b> networks execute transactions elsewhere and settle on a Layer 1 (Module 10).</li>
<li><b>EVM-compatible</b> chains (Polygon PoS, BNB Chain, Avalanche C-Chain, Arbitrum, Base) run the same contracts as Ethereum. Others use different machines: Solana (Rust programs), TON (TVM), Cardano (UTXO-based Plutus), Polkadot (Substrate).</li>
<li>This course uses Ethereum because it has the largest smart contract ecosystem and its tools work on most other EVM chains.</li>
</ul>
<h3>A decision path</h3>
<ol>
<li>Do several parties that do not trust each other need to write to the same record? If not, use a database.</li>
<li>Is one trusted operator acceptable to all? If yes, use a database with audit logs.</li>
<li>Must the public be able to verify it, or must anyone be able to join? If yes, a public chain. If only known members, a consortium chain.</li>
<li>Does the data contain personal or confidential information? Then keep it off chain and store only hashes or proofs.</li>
</ol>

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/networks/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum networks</b><small>ethereum.org developer docs</small></span></a>
<a class="vid read" href="https://ethereum.org/enterprise/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum for enterprise</b><small>ethereum.org, public versus private chains</small></span></a>
</div>

## Try it

<p>Apply the decision path to three cases and write one line of reasoning for each: a university diploma register, a supply chain for organic coffee, and a shared calendar for a law firm.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>What does an EVM-compatible chain have to implement to run your Solidity code unchanged?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>A consortium chain needs a governance agreement. Who pays for the nodes?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>On a consortium chain the members are known. Does that make them jointly controllers under the GDPR?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can tell public, consortium and private chains apart.</li><li>You can apply the four-question decision path.</li><li>You can say why this course uses Ethereum.</li></ul>
