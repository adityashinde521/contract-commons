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

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/oracles/" target="_blank" rel="noopener"><span class="play"></span><span><b>Oracles</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://docs.chain.link/data-feeds" target="_blank" rel="noopener"><span class="play"></span><span><b>Chainlink data feeds</b><small>Chainlink documentation</small></span></a>
<a class="vid read" href="https://docs.chain.link/vrf" target="_blank" rel="noopener"><span class="play"></span><span><b>Chainlink VRF</b><small>Verifiable randomness</small></span></a>
</div>

## Try it

<p>Open <a href="https://data.chain.link" target="_blank" rel="noopener">data.chain.link</a> (read only). Open the ETH/USD feed on Ethereum. Note how many oracle nodes report, the deviation threshold and the heartbeat. Explain in two sentences when the price on chain can be out of date.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Add an oracle to the Escrow: who may call <code>confirmDelivery</code> now?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Which data source would you trust for a delivery confirmation: the courier, the buyer or a sensor?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Draft a clause that allocates the risk of a wrong oracle report.</li></ul></div></div>

## Ship

<ul class="outc"><li>You can explain the oracle problem and four oracle designs.</li><li>You can explain why on-chain randomness needs a VRF.</li></ul>
