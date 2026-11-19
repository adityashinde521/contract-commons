---
title: "Blocks, chain and consensus"
module: 2
order: 1
kind: "lesson"
minutes: "45 min"
legacy: "T4"
problem: "Alice sends the same 10 coins to Bob and to Carol one second apart. Thousands of computers must agree which payment came first, with no one in charge."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Alice sends the same 10 coins to Bob and to Carol one second apart. Thousands of computers must agree which payment came first, with no one in charge.</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain how many computers agree on one ledger, and compare Proof of Work with Proof of Stake.</div>
    <ul>
      <li>A <b>block</b> contains transactions, a timestamp and the hash of the previous block.</li>
      <li><b>Nodes</b> store a copy of the chain and check every new block against the rules.</li>
      <li><b>Consensus</b> is the rule set that decides which new block all nodes accept.</li>
    </ul>
    <div class="tw"><table>
      <tr><th></th><th>Proof of Work (Bitcoin)</th><th>Proof of Stake (Ethereum since 2022)</th></tr>
      <tr><td>Who adds blocks</td><td>Miners, with computing power</td><td>Validators, who lock 32 ETH as a deposit</td></tr>
      <tr><td>Why honest</td><td>Cheating wastes the electricity spent</td><td>Cheaters lose part of the deposit (<b>slashing</b>)</td></tr>
      <tr><td>Energy</td><td>Very high</td><td>About 99.9% lower</td></tr>
      <tr><td>Block time</td><td>About 10 minutes</td><td>12 seconds</td></tr>
    </table></div>
    <ul>
      <li><b>Finality:</b> the point after which a block cannot change. On Ethereum, about two epochs (approximately 13 minutes).</li>
      <li>Immutability is economic and social, not absolute. In 2016, after the DAO hack, the Ethereum community changed history with a hard fork because a majority agreed (see <a href="/lessons/security-basics/">7.1 Security basics</a> and <a href="/lessons/lab-reentrancy/">7.4 Reentrancy</a>).</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><p>When is a payment “final” in law? The EU Settlement Finality Directive defines legal finality for payment systems. Technical finality on a blockchain and legal finality are separate questions.</p></div>

<!-- deep:start -->
### In depth

<p>Consensus answers one question: when thousands of nodes receive transactions in different orders, how do they all end up with the same history? A protocol must pick who proposes the next block and make cheating more expensive than honesty.</p>
<p><b>Proof of Work</b> (Bitcoin) lets anyone propose a block if they find a number (nonce) that makes the block hash smaller than a target. Finding it costs electricity; checking it is instant. Nodes follow the chain with the most accumulated work. To rewrite history, an attacker would need more computing power than the rest of the network together (a “51% attack”).</p>
<p><b>Proof of Stake</b> (Ethereum since September 2022) replaces electricity with deposited ETH. Validators lock 32 ETH (or more since Pectra). Time is divided into <b>slots</b> of 12 seconds and <b>epochs</b> of 32 slots. In each slot one validator is chosen at random to propose a block; committees of other validators <b>attest</b> that it is correct. When two thirds of the stake has attested to a checkpoint over two epochs, the block is <b>finalised</b>, after about 13 minutes. Reversing a finalised block would require validators with at least one third of all stake to break the rules, and they would lose that stake through <b>slashing</b>.</p>
<!-- diagram:pos-finality -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 230" role="img" aria-label="Proof of Stake slots, epochs and finality" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-proofofstakeslotsepo-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-proofofstakeslotsepo-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-proofofstakeslotsepo-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-proofofstakeslotsepo-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-zone" x="20" y="40" width="220" height="70" rx="12"/><text class="tl" x="130" y="30" text-anchor="middle" font-size="12.5">Epoch N · 32 slots · 6.4 min</text><rect class="k-slot-m" x="32.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="57.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="83.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="108.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="134.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="159.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="185.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="210.5" y="58" width="20" height="34" rx="4"/><rect class="k-zone" x="250" y="40" width="220" height="70" rx="12"/><text class="tl" x="360" y="30" text-anchor="middle" font-size="12.5">Epoch N+1 · 32 slots · 6.4 min</text><rect class="k-slot-m" x="262.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="287.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="313.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="338.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="364.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="389.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="415.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="440.5" y="58" width="20" height="34" rx="4"/><rect class="k-zone" x="480" y="40" width="220" height="70" rx="12"/><text class="tl" x="590" y="30" text-anchor="middle" font-size="12.5">Epoch N+2 · 32 slots · 6.4 min</text><rect class="k-slot-m" x="492.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="517.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="543.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="568.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="594.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="619.5" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="645.0" y="58" width="20" height="34" rx="4"/><rect class="k-slot" x="670.5" y="58" width="20" height="34" rx="4"/><text class="tl" x="20" y="134" text-anchor="start" font-size="12.5">▲ checkpoint (first slot of each epoch)</text><rect class="k-warn" x="20" y="150" width="220" height="60" rx="12"/><text class="tb" x="130.0" y="175.6" text-anchor="middle" font-size="13">Epoch N checkpoint</text><text class="t" x="130.0" y="193.6" text-anchor="middle" font-size="13">2/3 of stake attests</text><rect class="k-brand" x="250" y="150" width="220" height="60" rx="12"/><text class="tb" x="360.0" y="175.6" text-anchor="middle" font-size="13">After epoch N+1</text><text class="t" x="360.0" y="193.6" text-anchor="middle" font-size="13">N is justified, then final</text><rect class="k-cs" x="480" y="150" width="220" height="60" rx="12"/><text class="tb" x="590.0" y="175.6" text-anchor="middle" font-size="13">≈ 12.8 minutes</text><text class="t" x="590.0" y="193.6" text-anchor="middle" font-size="13">reversal = slashing ≥ 1/3 stake</text><line class="k-a" x1="240" y1="180" x2="248" y2="180" marker-end="url(#ah-proofofstakeslotsepo-a)"/><line class="k-a" x1="470" y1="180" x2="478" y2="180" marker-end="url(#ah-proofofstakeslotsepo-a)"/></svg></div><figcaption><b>Two levels of “done”.</b> A block is proposed every 12-second slot. Once two thirds of all stake attests to checkpoints over two epochs, the block is final. Undoing it would cost attackers at least a third of all staked ETH.</figcaption></figure>
<p>This leads to two levels of “done”. A transaction in a new block is <i>included</i> after about 12 seconds; it is <i>final</i> after about 13 minutes. Exchanges and bridges wait for finality before they treat large deposits as safe.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> how expensive is it to attack Ethereum’s finality?</p>
<ol>
  <li>Assume about 34 million ETH is staked (check the current number on beaconcha.in).</li>
  <li>To finalise two conflicting blocks, attackers must control at least one third: more than 11 million ETH.</li>
  <li>When they do, the protocol detects the double votes and slashes them. The attack costs the attackers a large part of that stake.</li>
  <li>Compare with Proof of Work: an attacker who rents enough computing power can stop after the attack and keep the hardware. Proof of Stake punishes the attacker’s capital directly.</li>
</ol>
<p><b>Takeaway for law and business:</b> “final” on Ethereum is economic finality. It is extremely expensive, not mathematically impossible, to reverse.</p>
</div>

### Common mistakes

<ul>
  <li>“Miners still create Ethereum blocks.” Since the Merge there is no mining on Ethereum; validators propose and attest.</li>
  <li>“51% of nodes decide.” Votes are weighted by stake, not by number of computers.</li>
  <li>“A transaction in a block is final.” It is final only after the checkpoint is finalised.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/blockchain-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Blockchain</b><small>ETH.BUILD, 23 min</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/understanding-consensus-mechanisms/" target="_blank" rel="noopener"><span class="play"></span><span><b>Understanding consensus mechanisms</b><small>10 min</small></span></a>
      <a class="vid" href="https://ethereum.org/videos/proof-of-work-explained/" target="_blank" rel="noopener"><span class="play"></span><span><b>What is proof of work?</b><small>6 min</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open <a href="https://etherscan.io/blocks" target="_blank" rel="noopener">etherscan.io/blocks</a> (read only).<span class="exp">A new block about every 12 seconds.</span></li><li>Open one block. Find the slot, the proposer (fee recipient), the number of transactions and the gas used.</li><li>Open <a href="https://beaconcha.in" target="_blank" rel="noopener">beaconcha.in</a> and find the latest finalised epoch.<span class="exp">Finalised epochs trail the current one by about two epochs (around 13 minutes).</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why is Proof of Work hard to do and easy to check?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Validators earn rewards. Who pays for the security of the network?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Legal finality versus technical finality: when is a payment final for a court?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
