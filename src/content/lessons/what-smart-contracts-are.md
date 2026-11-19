---
title: "Smart contracts: what they are and are not"
module: 4
order: 1
kind: "lesson"
minutes: "40 min"
legacy: "T6"
problem: "A vendor promises that its “smart contract” makes lawyers unnecessary. What can code really enforce, and what can it not?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A vendor promises that its “smart contract” makes lawyers unnecessary. What can code really enforce, and what can it not?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can define a smart contract and name its five most important limits.</div>
    <ul>
      <li>A <b>smart contract</b> is a program on a blockchain. It holds state, can hold and send funds, and runs when called.</li>
      <li>Nick Szabo used the term in the 1990s. His example: a vending machine. Input + rule = fixed result, with no shop assistant.</li>
      <li>Properties: automatic, deterministic, transparent, tamper-resistant.</li>
      <li>A smart contract is best understood as a <b>state machine</b>: it is always in one state (for example “waiting for payment”), and each function moves it to the next state only if its conditions hold.</li>
    </ul>
    <h4>Five limits</h4>
    <ol>
      <li><b>Not automatically a legal contract.</b> The code performs; the law decides if a binding agreement exists.</li>
      <li><b>Immutable code.</b> You cannot fix a bug after deployment. Upgrade patterns exist but add trust in an admin.</li>
      <li><b>Oracle problem.</b> The chain does not know real-world facts. An oracle brings them in, and you must trust it.</li>
      <li><b>Public data.</b> <code>private</code> only blocks other contracts, not human readers.</li>
      <li><b>No flexibility.</b> Code cannot judge good faith, reasonableness or unforeseen events (force majeure).</li>
    </ol>
    <div class="callout gui"><h5>See it with real tools</h5><p>Open a real contract transaction in <a href="../lab-tenderly/">Tenderly (8.3)</a> or <a href="../lab-phalcon/">Phalcon (7.5)</a> and watch each state change and payment.</p></div>

<!-- deep:start -->
### In depth

<p>Nick Szabo coined the term “smart contract” in the 1990s with the example of a vending machine: put in a coin, the machine releases a drink, and nobody needs to trust the shop owner. On Ethereum, a smart contract is a program stored at an address. It holds its own balance and storage, and anyone can call its public functions. It runs exactly as written, and on most contracts nobody can change the code afterwards.</p>
<p>The best way to think about a contract is as a <b>state machine</b>. It is always in one state (for the Escrow: awaiting payment, awaiting delivery, complete, refunded). Each function is a possible <b>transition</b> with conditions: who may call it, in which state, with how much money. If a condition fails, the function <b>reverts</b> and nothing changes. Writing a contract therefore means answering three questions for every action: who, when, and what happens to the money.</p>
<!-- diagram:escrow-states -->
<figure class="dg"><div class="sv"><svg viewBox="0 0 720 276" role="img" aria-label="Escrow state machine" xmlns="http://www.w3.org/2000/svg"><defs><marker id="ah-escrowstatemachine-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-a" d="M0 0L10 5L0 10z"/></marker><marker id="ah-escrowstatemachine-ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ar" d="M0 0L10 5L0 10z"/></marker><marker id="ah-escrowstatemachine-ag" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-ag" d="M0 0L10 5L0 10z"/></marker><marker id="ah-escrowstatemachine-am" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path class="m-am" d="M0 0L10 5L0 10z"/></marker></defs><rect class="k-n" x="20" y="100" width="170" height="64" rx="12"/><text class="tb" x="105.0" y="127.5" text-anchor="middle" font-size="13.5">AwaitingPayment</text><text class="t" x="105.0" y="146.0" text-anchor="middle" font-size="13.5">after deploy</text><rect class="k-warn" x="275" y="100" width="170" height="64" rx="12"/><text class="tb" x="360.0" y="127.5" text-anchor="middle" font-size="13.5">AwaitingDelivery</text><text class="t" x="360.0" y="146.0" text-anchor="middle" font-size="13.5">1 ETH held</text><rect class="k-brand" x="530" y="30" width="170" height="64" rx="12"/><text class="tb" x="615.0" y="57.5" text-anchor="middle" font-size="13.5">Complete</text><text class="t" x="615.0" y="76.0" text-anchor="middle" font-size="13.5">seller paid</text><rect class="k-law" x="530" y="172" width="170" height="64" rx="12"/><text class="tb" x="615.0" y="199.5" text-anchor="middle" font-size="13.5">Refunded</text><text class="t" x="615.0" y="218.0" text-anchor="middle" font-size="13.5">buyer paid back</text><line class="k-a" x1="190" y1="132" x2="273" y2="132" marker-end="url(#ah-escrowstatemachine-a)"/><text class="tb" x="232" y="86" text-anchor="middle" font-size="12.5">deposit()</text><text class="tl" x="232" y="102" text-anchor="middle" font-size="12">buyer, exact price</text><line class="k-a" x1="445" y1="116" x2="528" y2="62" marker-end="url(#ah-escrowstatemachine-a)"/><text class="tb" x="400" y="30" text-anchor="middle" font-size="12.5">confirmDelivery()</text><text class="tl" x="400" y="46" text-anchor="middle" font-size="12">buyer or arbiter</text><line class="k-a" x1="445" y1="150" x2="528" y2="204" marker-end="url(#ah-escrowstatemachine-a)"/><text class="tb" x="400" y="214" text-anchor="middle" font-size="12.5">refund()</text><text class="tl" x="400" y="230" text-anchor="middle" font-size="12">arbiter only</text><text class="tl" x="360" y="262" text-anchor="middle" font-size="13">Any other call in a state → revert, nothing changes</text></svg></div><figcaption><b>A contract is a state machine.</b> Each arrow is a function with a condition on <i>who</i> may call it and <i>in which state</i>. Everything not drawn here is forbidden by the code.</figcaption></figure>
<p>What a contract can enforce is limited to what it can see on chain: addresses, amounts, time, and the state of other contracts. Whether a laptop arrived, whether it is “of acceptable quality”, or whether a party is a minor are outside facts. A contract needs an oracle or an arbiter to bring them in, and the law still decides what happens when the code and the agreement differ.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> turn the laptop sale into rules.</p>
<div class="tw"><table>
  <tr><th>Clause</th><th>Who</th><th>When (state)</th><th>Effect</th></tr>
  <tr><td>§2 The buyer pays the price into escrow</td><td>Buyer only</td><td>AwaitingPayment</td><td>Exactly 1 ETH held; state → AwaitingDelivery</td></tr>
  <tr><td>§4 Payment is released on confirmed delivery</td><td>Buyer or arbiter</td><td>AwaitingDelivery</td><td>1 ETH to seller; state → Complete</td></tr>
  <tr><td>§5 Refund if the goods do not arrive</td><td>Arbiter only</td><td>AwaitingDelivery</td><td>1 ETH back to buyer; state → Refunded</td></tr>
  <tr><td>§6 Partly defective goods: price reduction</td><td colspan="3">Not in code: needs a human decision or a richer contract (lab 4.3, Apply)</td></tr>
</table></div>
</div>

### Common mistakes

<ul>
  <li>“A smart contract is a legal contract.” It may perform part of one. Formation, capacity, mistake and consumer law still apply.</li>
  <li>“The contract runs by itself.” Nothing happens until someone sends a transaction. There are no timers.</li>
  <li>“Code is law.” The code decides what happens on chain; a court can still order the parties to undo it off chain.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=pWGLtjG-F5c" target="_blank" rel="noopener"><span class="play"></span><span><b>Code is law? Smart contracts explained</b><small>Finematics, 15 min</small></span></a>
      <a class="vid read" href="https://ethereum.org/videos/smart-contracts-code-is-law/" target="_blank" rel="noopener"><span class="play"></span><span><b>Transcript of the Finematics video</b><small>ethereum.org</small></span></a>
      <a class="vid" href="https://simplyexplained.com/videos/smart-contracts/" target="_blank" rel="noopener"><span class="play"></span><span><b>Smart contracts</b><small>Simply Explained</small></span></a>
    </div>

## Try it

<p>Read the Escrow contract in <a href="../lab-escrow/">lab 4.3</a> without running it. Mark each line as “enforces a rule”, “moves money” or “records a fact”. Then list two things the buyer and seller agreed that the code cannot check.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Which of the five limits can a better design reduce, and which never?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which processes have rules clear enough to automate fully?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>When does a smart contract become a legally binding contract?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
