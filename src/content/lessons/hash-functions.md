---
title: "Hash functions"
module: 1
order: 2
kind: "lesson"
minutes: "30 min"
legacy: "T2"
problem: "A landlord says the lease you signed said 990 EUR, not 900. How could anyone prove which text existed, without trusting either of you?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A landlord says the lease you signed said 990 EUR, not 900. How could anyone prove which text existed, without trusting either of you?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can list the properties of a hash and say why each is important for a blockchain.</div>
    <ul>
      <li>A <b>hash function</b> turns any input (a word, a contract, a film) into a fixed-length output, a “fingerprint” of the input.</li>
      <li>Bitcoin uses SHA-256. Ethereum uses <b>Keccak-256</b>. In Solidity, call <code>keccak256(...)</code>. Both give 256 bits, written as 64 hexadecimal characters.</li>
    </ul>
    <div class="tw"><table>
      <tr><th>Property</th><th>Meaning</th><th>Why it matters</th></tr>
      <tr><td>Deterministic</td><td>Same input, same hash, every time.</td><td>Anyone can recompute and check.</td></tr>
      <tr><td>Avalanche effect</td><td>One changed character gives a completely different hash.</td><td>Small edits cannot hide.</td></tr>
      <tr><td>One-way</td><td>You cannot calculate the input from the hash.</td><td>You can publish the hash of a confidential document.</td></tr>
      <tr><td>Collision-resistant</td><td>It is not practical to find two inputs with the same hash.</td><td>A hash identifies one document.</td></tr>
    </table></div>
    <ul>
      <li>Each block contains the hash of the previous block. If someone changes an old block, its hash changes and all later links break. ETH.BUILD (<a href="/lessons/lab-eth-build/">1.6</a>) shows this visually.</li>
      <li>Law use: store only the hash of a document on chain to prove it existed at a time (labs <a href="/lessons/lab-document-registry/">4.5 Document registry</a> and <a href="/lessons/lab-attestations/">9.4 Attestations</a>).</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><p>A hash proves integrity (“this exact text”) and, with a block timestamp, existence at a time. It does not prove who wrote the text or that anyone agreed to it. A hash of personal data may still be personal data under the GDPR if the data can be guessed and re-hashed.</p></div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://ethereum.org/videos/hash-function-eth-build/" target="_blank" rel="noopener"><span class="play"></span><span><b>Hash function</b><small>ETH.BUILD, 5 min</small></span></a>
      <a class="vid tool" href="https://andersbrownworth.com/blockchain/hash" target="_blank" rel="noopener"><span class="play"></span><span><b>Try it: live hash and blockchain demo</b><small>Anders Brownworth. Type text, watch the hash, tamper with a block</small></span></a>
    </div>

## Try it

<ol class="steps"><li>Open the <a href="https://andersbrownworth.com/blockchain/hash" target="_blank" rel="noopener">live hash demo</a>. Type <code>Lease Kiel: rent 900 EUR</code>.<span class="exp">A 64-character SHA-256 hash.</span></li><li>Change 900 to 990.<span class="exp">A completely different hash (avalanche effect).</span></li><li>Type the first text again exactly.<span class="exp">The original hash returns (deterministic).</span></li></ol>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Why is a 256-bit hash still safe if computers get much faster?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Which business documents need proof that they were not changed?</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is a hash of personal data still personal data under the GDPR?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
