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
      <li><b>Shor’s algorithm</b> on a large quantum computer can calculate a private key from a public key. This breaks <b>ECDSA</b> (account signatures, T3) and other elliptic-curve systems.</li>
      <li>In February 2026, Vitalik Buterin listed four vulnerable areas of Ethereum: BLS signatures (validators), KZG commitments (blobs), ECDSA signatures (accounts) and some ZK proofs (Groth16).</li>
      <li><b>Hash functions</b> (Keccak-256) stay mostly safe. Grover’s algorithm only reduces their strength, and a 256-bit hash keeps a large margin.</li>
      <li>Your address is a hash of your public key. The public key becomes visible after your first transaction, so accounts that have sent transactions are more exposed.</li>
      <li>No quantum computer today can break Ethereum’s cryptography. The risk is in the future, but migration takes years.</li>
    </ul>
    <h4>The response</h4>
    <ul>
      <li>NIST published post-quantum standards in 2024: ML-KEM (FIPS 203), ML-DSA (FIPS 204) and SLH-DSA (FIPS 205). NIST plans to deprecate ECDSA by 2030 and disallow it by 2035.</li>
      <li>The Ethereum Foundation formed a Post-Quantum team in January 2026 (pq.ethereum.org). The target for full Layer 1 protection is around 2029.</li>
      <li>Post-quantum signatures are much larger. This costs block space and gas.</li>
    </ul>
    <div class="callout law"><h5>Law and business lens</h5><ul>
      <li>Long-lived records (land registers, notarised documents, L4, G5) must stay valid for decades. Should a contract require <b>crypto-agility</b>, the ability to change algorithms?</li>
      <li>If a quantum attacker takes funds from an old account, is that theft? Who is liable?</li>
      <li>Business: plan the migration cost like any other technology risk.</li>
    </ul></div>

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
