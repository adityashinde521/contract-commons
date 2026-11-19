---
title: "Zero-knowledge proofs and privacy"
module: 10
order: 3
kind: "lesson"
minutes: "35 min"
legacy: "F2"
problem: "A public blockchain shows everything to everyone. How can someone prove they are over 18, or solvent, without revealing the data?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A public blockchain shows everything to everyone. How can someone prove they are over 18, or solvent, without revealing the data?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can explain how a blockchain can be public and still protect private data.</div>
    <ul>
      <li>A <b>zero-knowledge proof (ZKP)</b> proves that a statement is true and reveals nothing else.</li>
      <li>Example: prove “I am over 18” without showing your birth date.</li>
      <li><b>SNARKs</b>: small proofs, fast to verify; many need a trusted setup. <b>STARKs</b>: larger proofs, no trusted setup, based on hashes (considered quantum-resistant).</li>
      <li>Uses on Ethereum: ZK rollups (scaling), private payments, private voting, verifiable credentials.</li>
      <li>The EU Digital Identity Wallet (eIDAS 2.0) uses <b>selective disclosure</b>: a citizen shows only the attributes that a service needs.</li>
    </ul>
    <div class="callout law"><h5>Law lens</h5><ul>
      <li>GDPR data minimisation: a ZKP can prove compliance with less personal data. Is the proof itself personal data?</li>
      <li>Anti-money-laundering rules need traceability. How do privacy and AML fit together?</li>
    </ul></div>

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=fOGdb1CTu5c" target="_blank" rel="noopener"><span class="play"></span><span><b>Zero-knowledge proofs in 5 levels of difficulty</b><small>WIRED with Amit Sahai, 23 min. Very good first watch.</small></span></a>
    </div>

## Try it

<p>Watch the WIRED video below. Then explain in three sentences, in your own words, how you could prove “I am over 18” to a website without revealing your birth date.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>SNARK or STARK: which would you choose for a quantum-safe system?</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Design a KYC check that stores no personal data.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is a zero-knowledge proof itself personal data?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
