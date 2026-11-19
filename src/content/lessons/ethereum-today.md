---
title: "Ethereum today: scaling and the roadmap"
module: 10
order: 1
kind: "lesson"
minutes: "40 min"
legacy: "F1"
problem: "Fees on Ethereum were once tens of dollars. Today most activity costs cents. What changed, and what new risks came with it?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Fees on Ethereum were once tens of dollars. Today most activity costs cents. What changed, and what new risks came with it?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can describe how Ethereum works today, not only in 2022.</div>
    <h4>Layer 2 rollups</h4>
    <ul>
      <li>Most user activity now happens on <b>Layer 2 rollups</b> (for example Arbitrum, Optimism, Base). A rollup executes transactions off the main chain and posts compressed data and proofs to Ethereum (Layer 1).</li>
      <li><b>Optimistic rollups</b> assume batches are correct and allow a challenge period with fraud proofs.</li>
      <li><b>ZK rollups</b> post a validity proof with each batch. Ethereum checks the proof, not every transaction.</li>
      <li>Layer 1 is now mainly a <b>settlement and data layer</b> for rollups.</li>
    </ul>
    <h4>Upgrade timeline</h4>
    <div class="tw"><table>
      <tr><th>Upgrade</th><th>When</th><th>What it changed</th></tr>
      <tr><td>The Merge</td><td>Sept 2022</td><td>Proof of Work to Proof of Stake.</td></tr>
      <tr><td>Dencun</td><td>March 2024</td><td>“Blobs” (EIP-4844): cheap temporary data space for rollups.</td></tr>
      <tr><td>Pectra</td><td>May 2025</td><td>EIP-7702: a normal account can act as a smart account (batch calls, spending rules, sponsored gas).</td></tr>
      <tr><td>Fusaka</td><td>3 Dec 2025</td><td>PeerDAS: nodes check data by sampling small parts. Much more blob capacity, lower rollup fees.</td></tr>
      <tr><td>Glamsterdam</td><td>Live on Sepolia since 6 Oct 2026. The Hoodi testnet fork was postponed on 22 Oct 2026 over a gas-repricing change (EIP-8037). No mainnet date set as of mid-November 2026.</td><td>ePBS (block building inside the protocol), block-level access lists (parallel validation), gas repricing.</td></tr>
      <tr><td>Post-quantum work</td><td>Target around 2029</td><td>Replace quantum-vulnerable cryptography (<a href="/lessons/quantum/">13.2 Quantum</a>).</td></tr>
    </table></div>
    <p class="note">Ethereum now aims for about two hard forks a year, and dates often move. Check ethereum.org before you rely on a date.</p>
    <div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Deploy the Escrow on an L2 testnet and compare fees with Sepolia.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Low L2 fees make micro-payments and process automation economic.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A rollup has an operator and a bridge. Who is responsible if a bridge fails? Users trust more parties than on L1.</li></ul></div>
    </div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/rollups-scaling-strategy/" target="_blank" rel="noopener"><span class="play"></span><span><b>Rollups: the ultimate Ethereum scaling strategy?</b><small>Finematics, with transcript</small></span></a>
      <a class="vid read" href="https://ethereum.org/developers/docs/scaling/zk-rollups/" target="_blank" rel="noopener"><span class="play"></span><span><b>Zero-knowledge rollups</b><small>ethereum.org developer docs</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open <a href="https://l2beat.com" target="_blank" rel="noopener">l2beat.com</a> and note the three largest rollups by value secured.</li><li>Open one and find its stage and who can upgrade it.<span class="exp">A risk summary with upgrade and exit-window details.</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Deploy the Escrow on an L2 testnet and compare fees.</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>What do low L2 fees make possible?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Who is responsible if a rollup bridge fails?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
