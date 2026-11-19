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

<!-- deep:start -->
### In depth

<p>Before rollups, two other scaling ideas appeared, and both are still used. A <b>payment channel</b> locks funds in a contract between two parties. They then exchange signed balance updates off chain, as many as they like, for free and instantly. Only the opening and the final balance go on chain. The Bitcoin Lightning Network links channels into a network. Channels work well for repeated payments between the same parties, but funds are locked and both sides must stay online to watch for cheating.</p>
<p>A <b>sidechain</b> is an independent blockchain with its own validators that is connected to Ethereum by a bridge, for example Gnosis Chain or Polygon PoS. It is cheap and fast, but its security is its own: if its validators collude, Ethereum cannot help.</p>
<p>A <b>bridge</b> moves value between chains. The common design is <b>lock and mint</b>: lock the original tokens in a contract on chain A, and mint the same number of wrapped tokens on chain B. To return, burn on B and unlock on A. The bridge contract on A then holds everyone’s locked funds, and whoever controls the minting on B, often a small group of signers, controls their value. That is why bridges have suffered some of the largest hacks: Ronin (2022, about $600 million) and Wormhole (2022, about $320 million).</p>
<!-- diagram:bridge -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 250" role="img" aria-label="Lock-and-mint bridge" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-lockandmintbridge-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-lockandmintbridge-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-lockandmintbridge-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-lockandmintbridge-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-zone" x="10" y="10" width="300" height="230" rx="16"/><rect class="k-zone" x="410" y="10" width="300" height="230" rx="16"/><text class="th" x="160" y="34" text-anchor="middle" font-size="14">Chain A (Ethereum)</text><text class="th" x="560" y="34" text-anchor="middle" font-size="14">Chain B</text><rect class="k-cs" x="40" y="60" width="240" height="64" rx="12"/><text class="tb" x="160.0" y="87.5" text-anchor="middle" font-size="13.5">Bridge vault</text><text class="t" x="160.0" y="106.0" text-anchor="middle" font-size="13.5">locked: 100 USDC</text><rect class="k-brand" x="440" y="60" width="240" height="64" rx="12"/><text class="tb" x="560.0" y="87.5" text-anchor="middle" font-size="13.5">Wrapped token</text><text class="t" x="560.0" y="106.0" text-anchor="middle" font-size="13.5">minted: 100 bUSDC</text><rect class="k-warn" x="260" y="160" width="200" height="64" rx="12"/><text class="tb" x="360.0" y="187.5" text-anchor="middle" font-size="13.5">Signers</text><text class="t" x="360.0" y="206.0" text-anchor="middle" font-size="13.5">3 of 5 must approve</text><line class="k-a" x1="280" y1="82" x2="438" y2="82" marker-end="url(#ah-lockandmintbridge-a)"/><text class="tl" x="359.0" y="72.0" text-anchor="middle" font-size="12.5">1 lock → 2 mint</text><line class="k-am" x1="438" y1="108" x2="282" y2="108" marker-end="url(#ah-lockandmintbridge-am)"/><text class="tl" x="360.0" y="126.0" text-anchor="middle" font-size="12.5">burn → unlock</text><line class="k-am" x1="360" y1="160" x2="360" y2="126" marker-end="url(#ah-lockandmintbridge-am)"/></svg></div><figcaption><b>A wrapped token is a claim on a vault.</b> The bridge locks the original on chain A and mints a copy on chain B. Whoever controls the signers controls the vault; if it is drained, the copies are worth nothing.</figcaption></figure>

### Worked example

<div class="worked">
<p><b>Case:</b> 100 USDC goes from Ethereum to a sidechain and the bridge is hacked.</p>
<ol>
  <li>Alice locks 100 USDC in the bridge on Ethereum. The bridge mints 100 “bridged USDC” to Alice on the sidechain.</li>
  <li>The bridge is controlled by 5 signers with a 3-of-5 threshold. Attackers steal 3 keys.</li>
  <li>They sign a fake message that releases all locked USDC on Ethereum to themselves.</li>
  <li>Alice still holds 100 bridged USDC on the sidechain, but nothing backs it any more. Its market price collapses.</li>
</ol>
<p><b>Lesson:</b> a wrapped token is a claim on someone else’s vault. Ask who guards the vault and how many keys it takes.</p>
</div>

### Common mistakes

<ul>
  <li>“Bridged tokens are the same asset.” They are IOUs from the bridge.</li>
  <li>“A sidechain is a Layer 2.” It does not inherit Ethereum’s security.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
<a class="vid read" href="https://ethereum.org/developers/docs/bridges/" target="_blank" rel="noopener"><span class="play"></span><span><b>Bridges</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/scaling/state-channels/" target="_blank" rel="noopener"><span class="play"></span><span><b>State channels</b><small>ethereum.org</small></span></a>
<a class="vid read" href="https://ethereum.org/developers/docs/scaling/sidechains/" target="_blank" rel="noopener"><span class="play"></span><span><b>Sidechains</b><small>ethereum.org</small></span></a>
</div>

## Try it

<p>On <a href="https://l2beat.com" target="_blank" rel="noopener">L2BEAT</a>, open the bridges section. Pick two bridges and compare how each one validates messages and who can upgrade it.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why does a channel need a dispute window?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>A payments company must choose a chain for micro-payments. Channel, sidechain or rollup?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Who is the issuer of a bridged token under MiCA?</li></ul></div></div>

## Ship

<ul class="outc"><li>You can compare channels, sidechains, Validium and rollups by whom you trust.</li><li>You can explain lock-and-mint and why bridges are targets.</li></ul>
