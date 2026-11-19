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

<!-- deep:start -->
### In depth

<p>A zero-knowledge proof (ZKP) lets a <b>prover</b> convince a <b>verifier</b> that a statement is true without revealing why. The classic picture is a cave with a magic door: Peggy shows Victor that she knows the password by coming out of whichever side he names, many times in a row, without ever saying the password. Modern ZKPs are mathematical: the statement is written as a circuit, the prover computes a short proof, and anyone can check the proof quickly.</p>
<p>A good proof system has three properties. <b>Completeness</b>: an honest prover with a true statement convinces the verifier. <b>Soundness</b>: a cheating prover with a false statement almost never succeeds. <b>Zero knowledge</b>: the verifier learns nothing except that the statement is true. Two families are common. <b>SNARKs</b> (for example Groth16, PLONK) produce tiny proofs that are cheap to verify on chain; some need a trusted setup. <b>STARKs</b> produce larger proofs but need no trusted setup and are considered safer against quantum computers.</p>
<p>ZKPs have two big uses. <b>Scaling</b>: a ZK rollup proves that thousands of transactions were executed correctly, so Ethereum checks one proof instead of re-running them. <b>Privacy</b>: a person proves “I am over 18”, “I am an EU resident” or “my balance is above X” without disclosing the underlying data. This fits the GDPR principle of data minimisation and the selective disclosure of the EU Digital Identity Wallet.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a wine shop must check that a buyer is over 18.</p>
<div class="tw"><table>
  <tr><th></th><th>Today (show ID card)</th><th>With a ZK credential</th></tr>
  <tr><td>What the shop sees</td><td>Name, date of birth, address, ID number, photo</td><td>“Age ≥ 18: true”, signed by a trusted issuer</td></tr>
  <tr><td>What the shop could leak</td><td>All of it</td><td>Almost nothing</td></tr>
  <tr><td>What the verifier checks</td><td>The card looks real</td><td>The proof is valid and the issuer’s key is on a trusted list</td></tr>
</table></div>
<p><b>Open question for the law lens:</b> is a proof that cannot be linked to a person still personal data? It depends on whether the shop or someone else can link it.</p>
</div>

### Common mistakes

<ul>
  <li>“ZK means encrypted.” The data is not sent at all; only a proof about it is.</li>
  <li>“ZK rollups are private.” Most publish all transaction data; ZK is used for correctness there, not secrecy.</li>
</ul>
<!-- deep:end -->

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
