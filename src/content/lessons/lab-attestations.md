---
title: "Attestations: notarise a document on Sepolia"
module: 9
order: 4
kind: "lab-gui"
minutes: "45 min"
legacy: "G5"
problem: "Two parties want a neutral, permanent record that they both had the same version of a contract on a given day."
---

## Problem

<div class="cc-callout cc-callout--problem"><div><b>The question.</b> Two parties want a neutral, permanent record that they both had the same version of a contract on a given day.</div></div>

## Concept

<div class="ov">
      <div><b>You will</b>Design a record format (schema) and make a real, signed on-chain statement about a document.</div>
      <div><b>Tool</b><a href="https://sepolia.easscan.org" target="_blank" rel="noopener">sepolia.easscan.org</a>, the explorer and app of the Ethereum Attestation Service (EAS).</div>
      <div><b>You need</b>MetaMask on Sepolia, about 0.01 SepoliaETH, and a document hash.</div>
    </div>
    <p>An attestation is a signed statement by one address about something: a person, a document, an event. EAS stores the attester, the time, the data and, if allowed, a later revocation. Anyone can verify it. It is used for certificates, notarisation, credentials and audit evidence.</p>
    <div class="callout tip"><h5>Get a document hash</h5><p>In Remix, deploy <code>DocumentRegistry</code> from L4 on the Remix VM and call <span class="ui">hashText</span> with your document text. It is free and gives a 0x… value with 64 hex characters.</p></div>

## Build

<h4>A. Create a schema (the form)</h4>
    <ol class="steps">
      <li>Open <a href="https://sepolia.easscan.org" target="_blank" rel="noopener">sepolia.easscan.org</a>. Click <span class="ui">Connect wallet</span>, choose MetaMask, approve.<span class="exp">Your address appears at the top right. Network: Sepolia.</span></li>
      <li>Go to <span class="ui">Schemas</span> and click <span class="ui">Create schema</span>.</li>
      <li>Add four fields: <code>bytes32 documentHash</code>, <code>string documentType</code>, <code>string jurisdiction</code>, <code>string team</code>.<span class="why">No names, no personal data: only the fingerprint and neutral metadata. The team field makes the schema unique.</span></li>
      <li>Keep <span class="ui">Revocable</span> on. Leave the resolver empty. Create and confirm in MetaMask.<span class="exp">A schema page with a <b>Schema UID</b> (0x…).</span></li>
    </ol>
    <h4>B. Make an attestation</h4>
    <ol class="steps">
      <li>On your schema page, click <span class="ui">Attest with schema</span>.</li>
      <li>Recipient: a teammate’s address (the counterparty). Fields: <code>documentHash</code> = your hash, <code>documentType</code> = “Lease agreement”, <code>jurisdiction</code> = “DE”, <code>team</code> = your team.</li>
      <li>Choose <span class="ui">Onchain</span>. Click <span class="ui">Make attestation</span> and confirm.<span class="exp">An attestation page: UID, attester (you), recipient, time, decoded data.</span></li>
      <li>Open the transaction on Etherscan from the link on the page.<span class="exp">A call to the EAS contract with an <code>Attested</code> event.</span></li>
    </ol>
    <h4>C. Verify and revoke</h4>
    <ol class="steps">
      <li>Your teammate searches the attestation UID on easscan, hashes the same document text in Remix and compares.<span class="exp">Same hash: the document is the one you attested.</span></li>
      <li>Make a second attestation, then revoke it with <span class="ui">Revoke</span>.<span class="exp">“Revoked” with a time. The original data stays visible: revocation adds a fact, it does not delete.</span></li>
      <li>Optional: make an <span class="ui">Offchain</span> attestation. It is signed but not stored on chain, and costs no gas.</li>
    </ol>

## Apply

<div class="aud">
      <div class="cs"><h5>Technology lens</h5><ul><li>A resolver contract can check rules before an attestation is accepted. Design one: “only the university may attest degrees”.</li></ul></div>
      <div class="bi"><h5>Business lens</h5><ul><li>Which business processes produce statements others must trust: supplier certificates, audit results, delivery proofs?</li></ul></div>
      <div class="lw"><h5>Law lens</h5><ul><li>Is an attestation an electronic signature under eIDAS? Simple, advanced or qualified? What is its value as evidence?</li><li>“Revoked” but still visible: does this satisfy a GDPR erasure request if the data was personal?</li></ul></div>
    </div>

## Ship

<ul class="outc">
      <li>You designed a data schema that avoids personal data.</li>
      <li>You made, verified and revoked a real on-chain attestation.</li>
      <li>You can explain on-chain versus off-chain attestations.</li>
    </ul>
    <div class="callout lab"><h5>Lab log</h5><p>Schema UID, attestation UID, Etherscan link, screenshot of the revoked attestation.</p></div>
