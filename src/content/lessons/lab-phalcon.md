---
title: "Phalcon: trace a real hack visually"
module: 7
order: 5
kind: "lab-gui"
minutes: "60 min"
legacy: "G9"
problem: "On 9 July 2025 about $42 million left GMX V1 in one attack. What actually happened, call by call?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> On 9 July 2025 about $42 million left GMX V1 in one attack. What actually happened, call by call?</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Analyse a real 2025 reentrancy attack with flow graphs and connect it to lab L6.</div>
      <div><b>Tool</b><a href="https://blocksec.com/explorer" target="_blank" rel="noopener">Phalcon Explorer</a> by BlockSec, a security firm. It shows invocation flow, fund flow, balance changes, state changes and a gas profiler. It supports Sepolia and many main networks.</div>
      <div><b>You need</b>A browser. Read only: you never connect a wallet here.</div>
    </div>
    <h4>The case: GMX V1, July 2025</h4>
    <p>On 9 July 2025, an attacker took about $42 million from GMX V1 on Arbitrum. GMX had a reentrancy guard on one contract, but the attacker re-entered a <i>different</i> contract (the Vault) during a callback and manipulated a price in the middle of the transaction. It is the same idea as L6, one level more complex: cross-contract reentrancy.</p>

## Build

<h4>A. Warm-up with your own transaction</h4>
    <ol class="steps">
      <li>Open <a href="https://blocksec.com/explorer" target="_blank" rel="noopener">blocksec.com/explorer</a>. Choose Sepolia and paste the hash of your L7 <code>confirmDelivery</code>.</li>
      <li>Open the <span class="ui">Invocation Flow</span>.<span class="exp">One call into Escrow and one internal call that sends ETH to the seller.</span></li>
      <li>Open <span class="ui">Fund Flow</span> and <span class="ui">Balance Changes</span>.<span class="exp">A graph: Escrow → seller, 0.001 ETH.</span></li>
    </ol>
    <h4>B. The real attack</h4>
    <ol class="steps">
      <li>Open BlockSec’s <a href="https://blocksec.com/blog/top-10-awesome-security-incidents-in-2025" target="_blank" rel="noopener">Top 10 security incidents of 2025</a>. Find GMX V1 and follow the link to its entry in the security incident library to get the attack transaction hash.</li>
      <li>In Phalcon Explorer, choose <b>Arbitrum</b> and paste the hash.<span class="exp">A very long invocation flow with many nested calls.</span></li>
      <li>Collapse the tree and find where control passes back to the attacker’s contract (a callback), and the calls into the Vault that follow inside it.<span class="why">This is the re-entry. Compare with the Attacker’s <code>receive</code> in L6.</span></li>
      <li>Open the fund flow graph. Follow where the value goes: which contracts lose, which address gains.</li>
      <li>Read BlockSec’s root-cause write-up linked from the incident entry. Check each claim against what you saw.</li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>CS</h5><ul><li>Which defence from T8 would have stopped this? Why is “protocol maturity” no protection?</li></ul></div>
      <div class="bi"><h5>BI</h5><ul><li>Write the incident cost: direct loss, reputation, recovery. Part of the funds was later returned under a bounty deal. How should that be booked?</li></ul></div>
      <div class="lw"><h5>Law</h5><ul><li>The attacker returned most of the funds in exchange for a “bounty”. Is that a lawful settlement, or does criminal liability remain? Compare with the DAO case (T8).</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can read an invocation flow and a fund flow graph.</li>
      <li>You can explain cross-contract reentrancy and why a single guard was not enough.</li>
      <li>You can check a security write-up against on-chain evidence.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Screenshots of the callback in the invocation flow and of the fund flow, and a five-sentence incident summary.</p></div>
