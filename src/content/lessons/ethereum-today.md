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
      <tr><td>Glamsterdam</td><td>Live on Sepolia since 6 Oct 2026. The Hoodi testnet fork was postponed on 22 Oct 2026: audits found that the gas-repricing changes (EIP-8037, EIP-8038) could break assumptions in some deployed contracts. Developers discussed the audit results on 19 Nov 2026 without a decision. No mainnet date; reports say it could slip from early 2027 to May 2027 (as of 20 Nov 2026).</td><td>ePBS (block building inside the protocol), block-level access lists (parallel validation), gas repricing.</td></tr>
      <tr><td>Post-quantum work</td><td>Target around 2029</td><td>Replace quantum-vulnerable cryptography (<a href="/lessons/quantum/">13.2 Quantum</a>).</td></tr>
    </table></div>
    <p class="note">Ethereum now aims for about two hard forks a year, and dates often move. Check ethereum.org before you rely on a date.</p>
    <div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Deploy the Escrow on an L2 testnet and compare fees with Sepolia.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Low L2 fees make micro-payments and process automation economic.</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A rollup has an operator and a bridge. Who is responsible if a bridge fails? Users trust more parties than on L1.</li></ul></div>
    </div>

<!-- deep:start -->
### In depth

<p>Ethereum chose to scale through <b>rollups</b> instead of making the base layer itself much bigger. A rollup executes transactions on its own fast chain, bundles thousands of them, and posts the data and a summary of the new state to Ethereum. Because the data is on Ethereum, anyone can rebuild the rollup’s state and challenge or check it. Users pay much lower fees because the cost of posting to Ethereum is shared.</p>
<p>There are two kinds. <b>Optimistic rollups</b> (Arbitrum, Optimism, Base) assume batches are correct and allow anyone to submit a fraud proof during a challenge window of about seven days; withdrawals to Ethereum wait for that window. <b>ZK rollups</b> (zkSync, Starknet, Scroll, Linea) post a validity proof with each batch; Ethereum checks the proof, so no challenge window is needed.</p>
<!-- diagram:rollup -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 270" role="img" aria-label="How a rollup posts to Ethereum" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-howarolluppoststoeth-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-howarolluppoststoeth-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-howarolluppoststoeth-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-howarolluppoststoeth-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-zone" x="10" y="10" width="330" height="250" rx="16"/><rect class="k-zone-b" x="380" y="10" width="330" height="250" rx="16"/><text class="th" x="175" y="34" text-anchor="middle" font-size="14">Layer 2 (rollup)</text><text class="th" x="545" y="34" text-anchor="middle" font-size="14">Ethereum (Layer 1)</text><rect class="k-law" x="30" y="54" width="120" height="52" rx="12"/><text class="tb" x="90.0" y="75.5" text-anchor="middle" font-size="13">Users</text><text class="t" x="90.0" y="93.5" text-anchor="middle" font-size="13">cheap, fast txs</text><rect class="k-bi" x="190" y="54" width="130" height="52" rx="12"/><text class="tb" x="255.0" y="75.5" text-anchor="middle" font-size="13">Sequencer</text><text class="t" x="255.0" y="93.5" text-anchor="middle" font-size="13">orders, executes</text><line class="k-a" x1="150" y1="80" x2="188" y2="80" marker-end="url(#ah-howarolluppoststoeth-a)"/><rect class="k-n" x="110" y="150" width="200" height="56" rx="12"/><text class="tb" x="210.0" y="173.5" text-anchor="middle" font-size="13.5">Batch</text><text class="t" x="210.0" y="192.0" text-anchor="middle" font-size="13.5">thousands of txs</text><line class="k-a" x1="255" y1="106" x2="230" y2="148" marker-end="url(#ah-howarolluppoststoeth-a)"/><rect class="k-cs" x="400" y="54" width="290" height="52" rx="12"/><text class="tb" x="545.0" y="75.5" text-anchor="middle" font-size="13">Blob data</text><text class="t" x="545.0" y="93.5" text-anchor="middle" font-size="13">anyone can rebuild the L2 state</text><rect class="k-brand" x="400" y="124" width="290" height="52" rx="12"/><text class="tb" x="545.0" y="145.6" text-anchor="middle" font-size="13">Rollup contract</text><text class="t" x="545.0" y="163.6" text-anchor="middle" font-size="13">new state root</text><rect class="k-warn" x="400" y="194" width="140" height="54" rx="12"/><text class="tb" x="470.0" y="216.6" text-anchor="middle" font-size="12.5">Optimistic</text><text class="t" x="470.0" y="234.1" text-anchor="middle" font-size="12.5">≈ 7-day challenge</text><rect class="k-cs" x="550" y="194" width="140" height="54" rx="12"/><text class="tb" x="620.0" y="216.6" text-anchor="middle" font-size="12.5">ZK rollup</text><text class="t" x="620.0" y="234.1" text-anchor="middle" font-size="12.5">validity proof</text><line class="k-a" x1="310" y1="172" x2="398" y2="80" marker-end="url(#ah-howarolluppoststoeth-a)"/><line class="k-a" x1="310" y1="180" x2="398" y2="150" marker-end="url(#ah-howarolluppoststoeth-a)"/></svg></div><figcaption><b>Execute on L2, settle on L1.</b> The rollup runs transactions cheaply and posts their data and a new state root to Ethereum. Correctness is enforced by a challenge window (optimistic) or a proof (ZK).</figcaption></figure>
<p>Upgrades made this cheaper. Dencun (March 2024) added <b>blobs</b>, temporary data space priced separately for rollups. Fusaka (December 2025) added PeerDAS, which lets nodes check blob data by sampling small pieces, so Ethereum can carry many more blobs. Not all rollups are equally decentralised yet. L2BEAT rates them in <b>stages</b>: Stage 0 still relies heavily on its operators, Stage 2 lets users exit and challenge without trusting anyone special.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> the same Escrow deposit on Ethereum and on a rollup.</p>
<div class="tw"><table>
  <tr><th></th><th>Ethereum mainnet</th><th>Optimistic rollup</th></tr>
  <tr><td>Fee for the deposit</td><td>About €1 (lesson 3.1 example)</td><td>A few cents</td></tr>
  <tr><td>Confirmation shown in the app</td><td>About 12 seconds</td><td>Under 1 second (from the sequencer)</td></tr>
  <tr><td>Final on Ethereum</td><td>About 13 minutes</td><td>When the batch is posted and finalised; withdrawal to L1 after about 7 days</td></tr>
  <tr><td>Extra trust</td><td>Ethereum validators</td><td>Plus the rollup’s sequencer and upgrade keys (check its L2BEAT stage)</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“L2s are separate blockchains.” Good rollups inherit Ethereum’s security for data and settlement; sidechains do not.</li>
  <li>“All rollups are equally safe.” Read the L2BEAT stage and who can upgrade the contracts.</li>
</ul>
<!-- deep:end -->

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
