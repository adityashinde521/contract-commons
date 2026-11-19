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

<!-- deep:start -->
### In depth

<p>“Blockchain” covers very different systems. The main question is <b>who may write and who may validate</b>. On a <b>public, permissionless</b> chain such as Ethereum, anyone can send transactions, read all data and, with enough stake, become a validator. On a <b>permissioned</b> chain, an operator or a group decides who joins. When one organisation controls it, it is a <b>private</b> chain; when several known organisations share control, it is a <b>consortium</b> chain (for example Hyperledger Fabric networks in trade finance).</p>
<p>Each choice moves the trade-off between openness and control. Public chains give strong neutrality and censorship resistance, but data is visible to everyone and fees vary. Permissioned chains are faster and can keep data confidential, but users must trust the operators, who can change the rules or the history if they agree. A private chain run by one company gives few advantages over a normal database with audit logs.</p>
<p>Today many projects mix models. Rollups (Module 10) run their own fast chain but post data and proofs to Ethereum for security. Banks issue tokenised bonds on public chains but restrict who may hold them with allow-lists in the token contract. The useful question is not “which chain is best?” but “who must be able to do what, and whom are users willing to trust?”.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> three scenarios, three answers.</p>
<div class="tw"><table>
  <tr><th>Scenario</th><th>Analysis</th><th>Choice</th></tr>
  <tr><td>A university issues diplomas that employers worldwide must verify.</td><td>One writer (the university), many readers who should not need an account.</td><td>Public chain with only hashes or attestations; the data stays at the university.</td></tr>
  <tr><td>Five shipping companies share container status updates.</td><td>Several known writers who compete and do not want one of them in control; data is commercially sensitive.</td><td>Consortium chain, or a public chain with encrypted data.</td></tr>
  <tr><td>A shop wants an internal log of price changes.</td><td>One writer, one organisation, no outside verifier.</td><td>Normal database with an audit log. No blockchain.</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“Private chains are blockchains with privacy.” They are blockchains with an owner. Privacy can also be built on public chains.</li>
  <li>“Permissioned means more secure.” It means fewer, known validators: more trust in them, not more security by default.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/networks/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum networks</b><small>ethereum.org developer docs</small></span></a>
<a class="vid read" href="https://ethereum.org/enterprise/" target="_blank" rel="noopener"><span class="play"></span><span><b>Ethereum for enterprise</b><small>ethereum.org, public versus private chains</small></span></a>
</div>

## Try it

<p>Apply the decision path to three cases and write one line of reasoning for each: a university diploma register, a supply chain for organic coffee, and a shared calendar for a law firm.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>What does an EVM-compatible chain have to implement to run your Solidity code unchanged?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>A consortium chain needs a governance agreement. Who pays for the nodes?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>On a consortium chain the members are known. Does that make them jointly controllers under the GDPR?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can tell public, consortium and private chains apart.</li><li>You can apply the four-question decision path.</li><li>You can say why this course uses Ethereum.</li></ul>
