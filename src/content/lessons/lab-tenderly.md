---
title: "Tenderly: debug and simulate your own transactions"
module: 8
order: 3
kind: "lab-gui"
minutes: "60 min"
legacy: "G8"
problem: "Etherscan shows that your transaction happened. You need to see how, and to test what would happen if someone else called it."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Etherscan shows that your transaction happened. You need to see how, and to test what would happen if someone else called it.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Open your own Escrow transactions in a visual debugger, then simulate calls as other parties without signing or spending anything.</div>
      <div><b>Tool</b><a href="https://dashboard.tenderly.co" target="_blank" rel="noopener">Tenderly</a>, a professional platform for debugging, simulating and monitoring transactions. The free account includes the explorer, debugger and single-transaction simulator.</div>
      <div><b>You need</b>A verified Escrow on Sepolia and its transaction hashes (<a href="/lessons/lab-sepolia/">8.2 Sepolia deployment</a>, part D), a free Tenderly account.</div>
    </div>
    <p>Etherscan tells you <i>that</i> a transaction happened. Tenderly shows you <i>how</i>: every internal call, each line of source code that ran, the values of variables, and which storage changed. The simulator answers “what would happen if…?” with no signature and no gas.</p>

## Build

<div class="checked"><b>Checked on 20 November 2026</b> against the tool’s official documentation. Tools change their screens often. If a button has a different name, look for the closest one and note the difference in your lab log.</div>

<h4>A. Debug a real transaction</h4>
    <ol class="steps">
      <li>Sign up at <a href="https://dashboard.tenderly.co" target="_blank" rel="noopener">dashboard.tenderly.co</a> (free). Skip any paid trial.<span class="exp">An empty Tenderly dashboard with a project. No payment details asked. (The free plan’s features change; if the debugger is limited, use the Remix debugger for part B.)</span></li>
      <li>Paste the hash of your <code>confirmDelivery</code> transaction from <a href="/lessons/lab-sepolia/">8.2 Sepolia deployment</a> into the search bar. Choose Sepolia if asked.<span class="exp">A transaction overview: status, from, to, gas, events and state changes.</span></li>
      <li>Look at the state changes.<span class="exp"><code>state</code> changed from 1 to 2, and the contract’s ETH balance went to 0.</span></li>
      <li>Click <span class="ui">Debugger</span>.<span class="exp">The execution trace on the left, the Escrow source code on the right with the current line highlighted.</span></li>
      <li>Step through with <span class="ui">Next</span>. Stop at <code>state = State.Complete;</code> and then at the line that sends ETH.<span class="why">You see checks-effects-interactions in order: the state changes before the money moves.</span><span class="exp">The line state = State.Complete; is highlighted; the state panel shows state changing from 1 to 2.</span></li>
      <li>Use <span class="ui">Evaluate</span> to read <code>msg.sender</code> and <code>price</code> at that point.<span class="exp">msg.sender shows the buyer’s address; price shows 1000000000000000 (0.001 ether).</span></li>
    </ol>
    <h4>B. Simulate “what if”</h4>
    <ol class="steps">
      <li>Deploy a fresh Escrow on Sepolia and deposit (<a href="/lessons/lab-sepolia/">8.2 Sepolia deployment</a>, part D, without confirming). Verify it.<span class="exp">A verified Escrow on Sepolia in state AwaitingDelivery (state() returns 1).</span></li>
      <li>In Tenderly, open the <span class="ui">Simulator</span>. Network Sepolia, contract = the new Escrow, function = <code>refund</code>.<span class="exp">The simulator form with From, To (your Escrow), function refund and no value.</span></li>
      <li>Set <b>From</b> to the seller’s address (impersonation; no key needed). Click <span class="ui">Simulate</span>.<span class="exp">Simulated revert: “Only arbiter”. Nothing happened on the real chain.</span></li>
      <li>Change <b>From</b> to the arbiter’s address and simulate again.<span class="exp">Success, with the balance change: the buyer receives the price.</span></li>
      <li>Simulate <code>confirmDelivery</code> from a stranger’s address.<span class="exp">Revert “Only buyer or arbiter”.</span></li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Use the simulator to test every <code>require</code> in Escrow. Is this a replacement for unit tests?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Companies simulate every treasury payment before signing. What would that have changed in the Bybit case (<a href="/lessons/security-in-practice/">7.2 Security in practice</a>)?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>A simulation shows what a contract would do for a given party. Could a lawyer use it as evidence of the contract’s terms or of foreseeability?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can read an execution trace and match it to source code.</li>
      <li>You can test a contract’s rules for any party with a simulation, at no cost.</li>
      <li>You can explain why simulation before signing is a security control.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Screenshot of the debugger at <code>state = State.Complete</code>, and a table of your three simulations: from, function, expected, result.</p></div>
