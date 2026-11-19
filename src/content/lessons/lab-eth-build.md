---
title: "ETH.BUILD: hashes, keys and transactions as blocks"
module: 1
order: 6
kind: "lab-gui"
minutes: "30 min"
problem: "Hashes and signatures are abstract until you see them change. ETH.BUILD lets you wire them together like building blocks."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Hashes and signatures are abstract until you see them change. ETH.BUILD lets you wire them together like building blocks.</div></div>

## Concept

<div class="ov"><div><b>You will</b>Build a hash, a key pair and a signature check from drag-and-drop modules.</div><div><b>Tool</b><a href="https://eth.build" target="_blank" rel="noopener">ETH.BUILD</a>, an open-source visual sandbox listed on ethereum.org.</div><div><b>You need</b>A desktop browser. No wallet, no account.</div></div>
<p>Each module (box) has inputs on the left and outputs on the right. You connect an output to an input by dragging a line. The values flow live, so every change is visible at once.</p>

## Build

<ol class="steps">
<li>Open <a href="https://eth.build" target="_blank" rel="noopener">eth.build</a>. Close the intro or watch it (about 3 minutes).</li>
<li>Right-click or use the menu to add an <b>Input → Text</b> module and a <b>Crypto → Hash</b> module. Connect the text output to the hash input.</li>
<li>Type <code>Lease Kiel: rent 900 EUR</code>.<span class="exp">A 0x… hash appears and changes completely with every key press.</span></li>
<li>Add a <b>Crypto → Key Pair</b> module. Note the private key, the public key and the address it shows.</li>
<li>Add <b>Crypto → Sign</b>: connect the private key and the text. Then add <b>Crypto → Recover</b> (or Verify): connect the signature and the text.<span class="exp">The recovered address equals the key pair’s address.</span></li>
<li>Change one character of the text after signing.<span class="exp">The recovered address changes: the signature no longer matches the message.</span></li>
</ol>
<div class="cc-callout cc-callout--warn"><div><b>Safety.</b> These keys are for play only. Never paste a real private key or recovery phrase into any website.</div></div>

## Apply

<div class="aud"><div class="cs"><h5>Computer science</h5><ul><li>Which module would you add to build a simple block that links to a previous hash?</li></ul></div><div class="bi"><h5>Business informatics</h5><ul><li>Use the model to explain to a manager why a signed invoice cannot be altered unnoticed.</li></ul></div><div class="lw"><h5>Law</h5><ul><li>The signature proves control of a key, not identity. What else is needed for an electronic signature under eIDAS?</li></ul></div></div>

## Ship

<ul class="outc"><li>You built a hash and a signature check yourself.</li><li>You can show why a changed message breaks a signature.</li></ul>
<div class="callout lab"><h5>Lab log</h5><p>A screenshot of your wiring with the recovered address, and one sentence on what you saw when you changed the text.</p></div>
