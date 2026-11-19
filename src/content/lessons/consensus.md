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
      <li>Immutability is economic and social, not absolute. In 2016, after the DAO hack, the Ethereum community changed history with a hard fork because a majority agreed (see T8 and L6).</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><p>When is a payment “final” in law? The EU Settlement Finality Directive defines legal finality for payment systems. Technical finality on a blockchain and legal finality are separate questions.</p></div>

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
