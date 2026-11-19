---
title: "Oracles: getting outside facts on chain"
module: 9
order: 2
kind: "lesson"
minutes: "30 min"
problem: "A crop-insurance contract should pay farmers if it does not rain for 30 days. The blockchain has no idea what the weather is."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A crop-insurance contract should pay farmers if it does not rain for 30 days. The blockchain has no idea what the weather is.</div></div>

## Concept

<ul>
<li>An <b>oracle</b> brings outside data (prices, weather, delivery status, sports results) into a smart contract by writing it in a transaction.</li>
<li>The contract can check who sent the data, but not whether it is true. Trust moves from the code to the oracle.</li>
</ul>
<div class="tw"><table>
<tr><th>Oracle design</th><th>How it works</th><th>Risk</th></tr>
<tr><td>Single source</td><td>One company or server posts the data</td><td>One point of failure or manipulation</td></tr>
<tr><td>Decentralised oracle network</td><td>Many independent nodes report; the contract uses an aggregate (Chainlink price feeds work this way)</td><td>Collusion, feed lag in fast markets</td></tr>
<tr><td>On-chain price (DEX)</td><td>Read the price from an exchange contract</td><td>Flash-loan manipulation within one transaction</td></tr>
<tr><td>Human or optimistic oracle</td><td>Someone posts an answer; others can dispute it with a bond</td><td>Slow; depends on dispute incentives</td></tr>
</table></div>
<h3>Randomness</h3>
<p>A blockchain is deterministic, so “random” values from block data can be predicted or influenced. Contracts that need fair randomness (lotteries, NFT reveals) use verifiable random functions (VRF), which return a random number with a proof.</p>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> The oracle is often the real decision-maker. Who is liable if a delivery oracle reports “delivered” by mistake? Is an oracle a party, an agent or a third-party service provider?</div></div>

<!-- deep:start -->
### In depth

<p>Contracts cannot see the outside world, because every node must compute the same result and the internet gives different answers at different times. An <b>oracle</b> is any mechanism that writes outside facts onto the chain: prices, weather, delivery status, sports results, or the result of a computation. The <b>oracle problem</b> is that the contract is only as reliable as that input: perfect code acting on a wrong fact still produces a wrong result.</p>
<p>Oracles differ in how much trust they need. A <b>single reporter</b> (one company or one person signing a value) is simple but can lie or be hacked. A <b>decentralised oracle network</b> such as Chainlink collects the same value from many independent nodes and sources, takes the median, and publishes it, so a few bad reporters cannot move it. <b>On-chain prices</b> from a DEX pool are free but can be manipulated within one transaction; time-weighted averages (TWAP) make that more expensive. <b>Optimistic oracles</b> (for example UMA) accept an answer unless someone disputes it within a time window and puts up a bond.</p>
<!-- diagram:oracle -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 260" role="img" aria-label="Oracle designs" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-oracledesigns-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-oracledesigns-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-oracledesigns-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-oracledesigns-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-n" x="20" y="20" width="130" height="46" rx="12"/><text class="t" x="85.0" y="47.5" text-anchor="middle" font-size="13">Exchange A</text><rect class="k-n" x="20" y="82" width="130" height="46" rx="12"/><text class="t" x="85.0" y="109.5" text-anchor="middle" font-size="13">Exchange B</text><rect class="k-n" x="20" y="144" width="130" height="46" rx="12"/><text class="t" x="85.0" y="171.6" text-anchor="middle" font-size="13">Data firm C</text><rect class="k-bi" x="200" y="20" width="120" height="46" rx="12"/><text class="t" x="260.0" y="47.5" text-anchor="middle" font-size="13">Oracle node 1</text><line class="k-a" x1="150" y1="43" x2="198" y2="43" marker-end="url(#ah-oracledesigns-a)"/><rect class="k-bi" x="200" y="82" width="120" height="46" rx="12"/><text class="t" x="260.0" y="109.5" text-anchor="middle" font-size="13">Oracle node 2</text><line class="k-a" x1="150" y1="105" x2="198" y2="105" marker-end="url(#ah-oracledesigns-a)"/><rect class="k-bi" x="200" y="144" width="120" height="46" rx="12"/><text class="t" x="260.0" y="171.6" text-anchor="middle" font-size="13">Oracle node 3</text><line class="k-a" x1="150" y1="167" x2="198" y2="167" marker-end="url(#ah-oracledesigns-a)"/><rect class="k-cs" x="370" y="70" width="120" height="56" rx="12"/><text class="tb" x="430.0" y="93.5" text-anchor="middle" font-size="13.5">Aggregate</text><text class="t" x="430.0" y="112.0" text-anchor="middle" font-size="13.5">median</text><line class="k-a" x1="320" y1="43" x2="368" y2="98" marker-end="url(#ah-oracledesigns-a)"/><line class="k-a" x1="320" y1="105" x2="368" y2="98" marker-end="url(#ah-oracledesigns-a)"/><line class="k-a" x1="320" y1="167" x2="368" y2="98" marker-end="url(#ah-oracledesigns-a)"/><rect class="k-brand" x="540" y="70" width="160" height="56" rx="12"/><text class="tb" x="620.0" y="93.5" text-anchor="middle" font-size="13.5">Your contract</text><text class="t" x="620.0" y="112.0" text-anchor="middle" font-size="13.5">reads price + age</text><line class="k-a" x1="490" y1="98" x2="538" y2="98" marker-end="url(#ah-oracledesigns-a)"/><rect class="k-danger" x="370" y="196" width="160" height="50" rx="12"/><text class="tb" x="450.0" y="216.6" text-anchor="middle" font-size="13">One DEX pool</text><text class="t" x="450.0" y="234.6" text-anchor="middle" font-size="13">spot price</text><line class="k-ar" x1="530" y1="220" x2="600" y2="128" marker-end="url(#ah-oracledesigns-ar)"/><text class="tl" x="603.0" y="192.0" text-anchor="middle" font-size="12.5">manipulable</text></svg></div><figcaption><b>Many sources versus one.</b> A decentralised feed takes the median of independent reporters, so a few bad values cannot move it. A single on-chain pool can be pushed in one transaction with a flash loan.</figcaption></figure>
<p>For contracts with legal meaning, the oracle often is a person or institution: an arbiter, a notary, a logistics company. The legal questions follow: who is liable if the oracle is wrong, and was the party who chose it bound by that choice?</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a lending protocol and a manipulated price.</p>
<ol>
  <li>Protocol A lets users borrow against token X. It reads X’s price from one small DEX pool.</li>
  <li>An attacker takes a flash loan of 5 million USDC and buys X in that pool. The pool price of X triples within the transaction.</li>
  <li>In the same transaction the attacker deposits X into Protocol A, which now values it at three times its real price, and borrows the maximum.</li>
  <li>The attacker sells X back, repays the flash loan and keeps the borrowed funds. Protocol A is left with overvalued collateral.</li>
  <li><b>Defence:</b> use a decentralised price feed, reject prices that move too far or are too old, and cap borrowing per block.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Chainlink makes the data true.” It makes it hard to manipulate; the sources can still be wrong.</li>
  <li>Forgetting to check how old a price is. A feed that stopped updating is a silent risk.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/oracles/" target="_blank" rel="noopener"><span class="play"></span><span><b>Oracles</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://docs.chain.link/data-feeds" target="_blank" rel="noopener"><span class="play"></span><span><b>Chainlink data feeds</b><small>Chainlink documentation</small></span></a>
<a class="vid read" href="https://docs.chain.link/vrf" target="_blank" rel="noopener"><span class="play"></span><span><b>Chainlink VRF</b><small>Verifiable randomness</small></span></a>
</div>

## Try it

<p>Open <a href="https://data.chain.link" target="_blank" rel="noopener">data.chain.link</a> (read only). Open the ETH/USD feed on Ethereum. Note how many oracle nodes report, the deviation threshold and the heartbeat. Explain in two sentences when the price on chain can be out of date.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Add an oracle to the Escrow: who may call <code>confirmDelivery</code> now?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which data source would you trust for a delivery confirmation: the courier, the buyer or a sensor?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Draft a clause that allocates the risk of a wrong oracle report.</li></ul></div></div>

## Ship

<ul class="outc"><li>You can explain the oracle problem and four oracle designs.</li><li>You can explain why on-chain randomness needs a VRF.</li></ul>
