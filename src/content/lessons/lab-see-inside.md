---
title: "See inside: Remix debugger, contract diagrams, ETH.BUILD"
module: 8
order: 4
kind: "lab-gui"
minutes: "45 min"
legacy: "G10"
problem: "Code is hard to read for most people. Can you see a contract’s structure and its execution instead?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Code is hard to read for most people. Can you see a contract’s structure and its execution instead?</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Visualise how code runs, how a contract is structured and how blockchain basics fit together.</div>
      <div><b>Tools</b>Remix debugger (built in), <a href="https://github.com/naddison36/sol2uml" target="_blank" rel="noopener">sol2uml</a> (open source, listed on ethereum.org), <a href="https://eth.build" target="_blank" rel="noopener">ETH.BUILD</a> (drag-and-drop sandbox).</div>
      <div><b>You need</b>A browser. sol2uml needs Node.js; one team member runs it, everyone reads the diagram.</div>
    </div>

## Build

<h4>A. ETH.BUILD: blockchain basics as blocks (everyone)</h4>
    <ol class="steps">
      <li>Open <a href="https://eth.build" target="_blank" rel="noopener">eth.build</a>. Watch the short intro video on the start page.</li>
      <li>Add a text input and a hash module, and connect them. Type a clause.<span class="exp">The hash changes completely with every key press.</span></li>
      <li>Add a key-pair module and a sign module. Sign your text, then change one character.<span class="exp">The signature no longer verifies.</span></li>
    </ol>
    <h4>B. Remix debugger: the L6 attack step by step</h4>
    <ol class="steps">
      <li>Repeat the L6 attack on the Remix VM. In the terminal, click <span class="ui">Debug</span> next to the <code>attack</code> transaction.</li>
      <li>Use the slider and <span class="ui">Step into</span>. Watch the call stack grow as <code>withdraw</code> is entered again and again.<span class="exp">The balance variable is still 1 ether on every re-entry until the end.</span></li>
    </ol>
    <h4>C. sol2uml: a class diagram of your contract (one runs it, the team reads)</h4>
    <ol class="steps">
      <li>Install once: <code>npm install -g sol2uml</code>. Get a free Etherscan API key.</li>
      <li>Run <code>sol2uml class &lt;your verified Escrow address&gt; -n sepolia -k &lt;API key&gt;</code>.<span class="exp">An SVG file: the Escrow as a box with its state variables, functions, events and the State enum.</span></li>
      <li>Run the same for the G1 certificate contract.<span class="exp">A larger diagram showing everything it inherits from OpenZeppelin.</span></li>
      <li>Everyone annotates the diagram: who may call each function?</li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>Inheritance makes the certificate contract much bigger than its code file. Is that good or bad for audits?</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Would a diagram like this help a business owner approve a contract? What would you add?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>Draft an annex to a contract that uses the diagram to describe each party’s powers.</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You can explain hashes and signatures with a live visual model.</li>
      <li>You can follow a reentrancy attack in a debugger.</li>
      <li>You can read a contract’s structure from a diagram, without reading code.</li>
    </ul>
