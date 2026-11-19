---
title: "Quantum computing and blockchain security"
module: 13
order: 2
kind: "lesson"
minutes: "45 min"
legacy: "F4"
problem: "A quantum computer could one day derive private keys from public ones. Which records are at risk, and how long does a migration take?"
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> A quantum computer could one day derive private keys from public ones. Which records are at risk, and how long does a migration take?</div></div>

## Concept

<div class="goal"><b>Goal:</b> you can say which parts of a blockchain a quantum computer could break, and how Ethereum prepares.</div>
    <h4>What is at risk</h4>
    <ul>
      <li><b>Shor’s algorithm</b> on a large quantum computer can calculate a private key from a public key. This breaks <b>ECDSA</b> (account signatures, <a href="/lessons/keys-and-signatures/">1.3 Keys and signatures</a>) and other elliptic-curve systems.</li>
      <li>In February 2026, Vitalik Buterin listed four vulnerable areas of Ethereum: BLS signatures (validators), KZG commitments (blobs), ECDSA signatures (accounts) and some ZK proofs (Groth16).</li>
      <li><b>Hash functions</b> (Keccak-256) stay mostly safe. Grover’s algorithm only reduces their strength, and a 256-bit hash keeps a large margin.</li>
      <li>Your address is a hash of your public key. The public key becomes visible after your first transaction, so accounts that have sent transactions are more exposed.</li>
      <li>No quantum computer today can break Ethereum’s cryptography. The risk is in the future, but migration takes years.</li>
    </ul>
    <h4>The response</h4>
    <ul>
      <li>NIST published post-quantum standards in 2024: ML-KEM (FIPS 203), ML-DSA (FIPS 204) and SLH-DSA (FIPS 205). NIST IR 8547, finalised on 27 October 2026, deprecates quantum-vulnerable signatures such as ECDSA after 2030 and disallows them after 2035.</li>
      <li>The Ethereum Foundation formed a Post-Quantum team in January 2026 (pq.ethereum.org). The target for full Layer 1 protection is around 2029.</li>
      <li>Post-quantum signatures are much larger. This costs block space and gas.</li>
    </ul>
    <div class="callout law"><h5>Law and business lens</h5><ul>
      <li>Long-lived records (land registers, notarised documents, <a href="/lessons/lab-document-registry/">4.5 Document registry</a>, <a href="/lessons/lab-attestations/">9.4 Attestations</a>) must stay valid for decades. Should a contract require <b>crypto-agility</b>, the ability to change algorithms?</li>
      <li>If a quantum attacker takes funds from an old account, is that theft? Who is liable?</li>
      <li>Business: plan the migration cost like any other technology risk.</li>
    </ul></div>

<!-- deep:start -->
### In depth

<p>Quantum computers threaten two kinds of cryptography differently. <b>Shor’s algorithm</b> can compute a private key from a public key for elliptic-curve and RSA schemes, given a large enough, error-corrected quantum computer. That would break ECDSA account signatures, BLS validator signatures and KZG commitments. <b>Grover’s algorithm</b> only speeds up brute-force search, which roughly halves the security of hash functions: Keccak-256 keeps about 128 bits of security, which is still considered enough.</p>
<p>An important detail: an Ethereum address is a <i>hash</i> of the public key. As long as an account has never sent a transaction, its public key is not visible, and a quantum attacker sees only the hash. Once an account signs, its public key can be recovered from the signature. Accounts that have transacted are therefore exposed first, and any migration plan must move funds before an attacker can act.</p>
<p>The response is <b>crypto-agility</b>: making the signature scheme replaceable. Post-quantum signatures standardised by NIST (ML-DSA, SLH-DSA) are larger and more expensive to verify than ECDSA. Ethereum’s path includes account abstraction (so each account can choose its signature scheme), hash-based signatures for validators, and new proof systems. The practical question for long-lived records, such as land registers or certificates, is whether they will still be trustworthy in 20 years.</p>

### Worked example

<div class="worked">
<p><b>Case:</b> a notary office registers document hashes from one EOA and wants them to stay credible until 2045.</p>
<ol>
  <li>Risk: once quantum attacks are practical, someone could forge new signatures from that EOA and register false documents with a backdated story.</li>
  <li>Existing registrations stay valid as records: the hash and the block timestamp do not depend on ECDSA.</li>
  <li>Mitigation now: move registration to a smart account whose verifier can be replaced (crypto-agility), and publish the policy.</li>
  <li>Later: switch the verifier to a post-quantum scheme by governance, and retire the old key in a public transaction.</li>
</ol>
</div>

### Common mistakes

<ul>
  <li>“Quantum computers break all of blockchain.” Hashes survive; signatures and some proofs need replacing.</li>
  <li>“It is decades away, so ignore it.” Migrations take years; records made today must last.</li>
</ul>
<!-- deep:end -->

### Watch and read

<div class="vids">
      <a class="vid" href="https://www.youtube.com/watch?v=lvTqbM5Dq4Q" target="_blank" rel="noopener"><span class="play"></span><span><b>How quantum computers break encryption: Shor’s algorithm</b><small>minutephysics, 17 min</small></span></a>
      <a class="vid read" href="https://ethereum.org/roadmap/security/quantum-resistance/" target="_blank" rel="noopener"><span class="play"></span><span><b>Post-quantum cryptography on Ethereum</b><small>ethereum.org roadmap page</small></span></a>
    </div>

## Try it

<p>On Etherscan, open any address that has sent a transaction and any address that has only received funds. Which one has revealed its public key? Write down why that matters for quantum risk.</p>

## Apply

<div class="aud"><div class="cs"><h5>Technology lens</h5><ul><li>Design a contract whose signature check can be replaced later.</li></ul></div><div class="bi"><h5>Business lens</h5><ul><li>Put the migration cost in a risk register.</li></ul></div><div class="lw"><h5>Law lens</h5><ul><li>Is taking funds from an old account with a quantum computer theft?</li></ul></div></div>

## Ship

<p>Write three sentences in your lab log: the main idea, one example for each lens (technology, business, law), and one open question. Then take the quiz below.</p>
