---
title: "Channels, sidechains and bridges"
module: 10
order: 2
kind: "lesson"
minutes: "30 min"
problem: "Bridges have been behind some of the largest hacks in crypto. Why is moving tokens between chains so risky?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Bridges have been behind some of the largest hacks in crypto. Why is moving tokens between chains so risky?</div></div>

## Concept

<div class="tw"><table>
<tr><th>Approach</th><th>How it works</th><th>Who you trust</th></tr>
<tr><td><b>Payment and state channels</b></td><td>Two parties lock funds on chain, then exchange signed updates off chain, and settle at the end (Bitcoin’s Lightning Network)</td><td>Only the other party, with an on-chain dispute window</td></tr>
<tr><td><b>Sidechain</b></td><td>A separate chain with its own validators, connected by a bridge (Polygon PoS, Gnosis Chain)</td><td>The sidechain’s validators</td></tr>
<tr><td><b>Plasma, Validium</b></td><td>Off-chain execution; data kept off chain, proofs or exits on chain</td><td>Data availability committee or operator</td></tr>
<tr><td><b>Rollup</b></td><td>Execution off chain, data and proofs on Ethereum (lesson 10.1)</td><td>Ethereum, plus the rollup’s upgrade keys</td></tr>
</table></div>
<h3>Bridges</h3>
<ul>
<li>A token cannot really move between chains. A bridge <b>locks</b> it on chain A and <b>mints</b> a representation on chain B, or burns and releases on the way back.</li>
<li>The locked funds sit in one contract, often guarded by a small set of signers. That makes bridges a large target: the Ronin bridge (2022, about $600 million) and Wormhole (2022, about $320 million) were drained this way.</li>
<li>Safer designs use proofs that chain B can verify about chain A, such as a rollup’s native bridge or light-client bridges.</li>
</ul>
<div class="cc-callout cc-callout--law"><div><b>Law lens.</b> A bridged token is a claim on locked funds held by someone else. Is it the same asset? If the bridge is drained, against whom does the holder have a claim?</div></div>

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/bridges/" target="_blank" rel="noopener"><span class="play"></span><span><b>Bridges</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/scaling/state-channels/" target="_blank" rel="noopener"><span class="play"></span><span><b>State channels</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/scaling/sidechains/" target="_blank" rel="noopener"><span class="play"></span><span><b>Sidechains</b><small>ethereum.org</small></span></a>
</div>

## Try it

<p>On <a href="https://l2beat.com" target="_blank" rel="noopener">L2BEAT</a>, open the bridges section. Pick two bridges and compare how each one validates messages and who can upgrade it.</p>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Why does a channel need a dispute window?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>A payments company must choose a chain for micro-payments. Channel, sidechain or rollup?</li></ul></div><div class="lw"><h5>Law</h5><ul><li>Who is the issuer of a bridged token under MiCA?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can compare channels, sidechains, Validium and rollups by whom you trust.</li><li>You can explain lock-and-mint and why bridges are targets.</li></ul>
