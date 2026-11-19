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
